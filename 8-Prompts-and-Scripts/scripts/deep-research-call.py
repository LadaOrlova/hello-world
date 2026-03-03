#!/usr/bin/env python3
"""
Deep Research caller via OpenAI Responses API.

Architecture: Background Mode + Polling (recommended by OpenAI for long-running requests).
1. Submit request with background=true → get response ID immediately
2. Poll GET /v1/responses/{id} every 30s until completed
3. Auto-resume: saves response ID to .state file, so re-running resumes from polling

Features:
- Background mode: no TCP idle timeout issues
- Auto-resume from crash/restart via .state file
- Retry with exponential backoff on transient errors
- Verbose logging to stdout AND .log file
- Heartbeat every 30s during polling
- Detailed response analysis

Usage:
    python3 deep-research-call.py <prompt-file> <output-file> [--model MODEL] [--effort EFFORT]
    python3 deep-research-call.py <prompt-file> <output-file> --resume  # resume from saved state

Examples:
    python3 deep-research-call.py prompt.md result.md
    python3 deep-research-call.py prompt.md result.md --model gpt-5.2-pro --effort xhigh
    python3 deep-research-call.py prompt.md result.md --resume  # resume after crash
"""

import sys
import json
import time
import os
import signal

# --- Configuration ---
DEFAULT_MODEL = "gpt-5.2-pro"
DEFAULT_EFFORT = "xhigh"
POLL_INTERVAL = 30       # seconds between polling
SUBMIT_TIMEOUT = 120     # seconds for initial submit request
POLL_TIMEOUT = 30        # seconds for each poll request
MAX_RETRIES = 3          # retries for transient errors
MAX_POLL_TIME = 7200     # max total polling time (2 hours)


# --- Logger ---
class Logger:
    """Writes to both stdout and a log file with timestamps."""

    def __init__(self, log_path: str):
        self.log_path = log_path
        self.start_time = time.time()
        self._file = open(log_path, 'a', encoding='utf-8')  # append mode for resume
        self.log("=" * 60, tag="INIT")
        self.log("Logger initialized", tag="INIT")

    def log(self, msg: str, tag: str = "DR"):
        elapsed = time.time() - self.start_time
        ts = time.strftime("%Y-%m-%d %H:%M:%S")
        line = f"[{ts}] [{tag:>8s}] +{elapsed:7.1f}s | {msg}"
        print(line, flush=True)
        try:
            self._file.write(line + "\n")
            self._file.flush()
        except Exception:
            pass  # don't crash on log write failure

    def close(self):
        self.log("Logger closed", tag="INIT")
        try:
            self._file.close()
        except Exception:
            pass


# --- API Key ---
def get_api_key(logger: Logger) -> str:
    # 1. Environment variable
    key = os.environ.get("OPENAI_API_KEY")
    if key:
        logger.log(f"API key: env var OPENAI_API_KEY (len={len(key)}, ends=...{key[-4:]})", tag="AUTH")
        return key
    # 2. .env files
    env_paths = [
        os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '.env'),
        os.path.expanduser('~/.env'),
    ]
    for env_path in env_paths:
        abs_path = os.path.abspath(env_path)
        try:
            with open(abs_path, 'r') as f:
                for line in f:
                    if line.startswith('OPENAI_API_KEY='):
                        value = line.strip().split('=', 1)[1]
                        value = value.split('#')[0].strip()
                        value = value.strip('"').strip("'")
                        if value:
                            logger.log(f"API key: {abs_path} (len={len(value)}, ends=...{value[-4:]})", tag="AUTH")
                            return value
        except FileNotFoundError:
            continue
    logger.log("ERROR: No API key found anywhere", tag="AUTH")
    return None


def ensure_requests():
    """Import requests, installing if needed."""
    try:
        import requests
        return requests
    except ImportError:
        import subprocess
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests', '-q'])
        import requests
        return requests


# --- State Management (for resume) ---
def state_path(output_file: str) -> str:
    """Path to .state file for resume capability."""
    return output_file.rsplit('.', 1)[0] + '.state'


def save_state(output_file: str, response_id: str, model: str, logger: Logger):
    """Save response ID to disk for resume."""
    sp = state_path(output_file)
    state = {"response_id": response_id, "model": model, "saved_at": time.strftime("%Y-%m-%d %H:%M:%S")}
    with open(sp, 'w') as f:
        json.dump(state, f)
    logger.log(f"State saved: {sp} (response_id={response_id})", tag="STATE")


def load_state(output_file: str, logger: Logger) -> dict:
    """Load saved state if exists."""
    sp = state_path(output_file)
    if os.path.exists(sp):
        with open(sp, 'r') as f:
            state = json.load(f)
        logger.log(f"State loaded: {sp} (response_id={state.get('response_id')}, saved={state.get('saved_at')})", tag="STATE")
        return state
    logger.log(f"No saved state at {sp}", tag="STATE")
    return None


def clear_state(output_file: str, logger: Logger):
    """Remove state file after successful completion."""
    sp = state_path(output_file)
    if os.path.exists(sp):
        os.remove(sp)
        logger.log(f"State cleared: {sp}", tag="STATE")


# --- Pre-flight ---
def preflight_check(api_key: str, logger: Logger) -> bool:
    """Validate API key with a lightweight call."""
    requests = ensure_requests()
    logger.log("Pre-flight: validating API key...", tag="PRE")
    try:
        resp = requests.get(
            "https://api.openai.com/v1/models",
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=15
        )
        if resp.status_code == 200:
            models = resp.json().get("data", [])
            logger.log(f"Pre-flight OK: {len(models)} models available", tag="PRE")
            return True
        else:
            logger.log(f"Pre-flight FAILED: HTTP {resp.status_code} — {resp.text[:200]}", tag="PRE")
            return False
    except Exception as e:
        logger.log(f"Pre-flight ERROR: {e}", tag="PRE")
        return False


def prompt_stats(prompt: str, logger: Logger):
    """Log prompt statistics."""
    chars = len(prompt)
    words = len(prompt.split())
    lines = prompt.count('\n') + 1
    # Russian text: ~2 tokens per word; English: ~1.3
    est_tokens_en = int(words * 1.3)
    est_tokens_ru = int(words * 2.0)
    logger.log(f"Prompt: {chars:,} chars, {words:,} words, {lines:,} lines", tag="PROMPT")
    logger.log(f"Est. tokens: ~{est_tokens_en:,} (EN) / ~{est_tokens_ru:,} (RU)", tag="PROMPT")


# --- HTTP helpers with retry ---
def request_with_retry(method: str, url: str, headers: dict, logger: Logger,
                       json_body: dict = None, timeout: int = 30,
                       max_retries: int = MAX_RETRIES) -> 'requests.Response':
    """Make HTTP request with exponential backoff retry on transient errors."""
    requests = ensure_requests()

    for attempt in range(1, max_retries + 1):
        try:
            logger.log(f"HTTP {method} {url} (attempt {attempt}/{max_retries}, timeout={timeout}s)", tag="HTTP")

            if method == "POST":
                resp = requests.post(url, headers=headers, json=json_body, timeout=timeout)
            else:
                resp = requests.get(url, headers=headers, timeout=timeout)

            # Retry on server errors (5xx) and rate limits (429)
            if resp.status_code in (429, 500, 502, 503, 504):
                retry_after = int(resp.headers.get('retry-after', 0))
                wait = max(retry_after, 2 ** attempt * 5)  # exponential backoff, min from retry-after
                logger.log(f"HTTP {resp.status_code} — retrying in {wait}s (attempt {attempt}/{max_retries})", tag="RETRY")
                if attempt < max_retries:
                    time.sleep(wait)
                    continue
                else:
                    logger.log(f"All {max_retries} retries exhausted", tag="RETRY")

            return resp

        except requests.exceptions.Timeout:
            wait = 2 ** attempt * 5
            logger.log(f"TIMEOUT — retrying in {wait}s (attempt {attempt}/{max_retries})", tag="RETRY")
            if attempt < max_retries:
                time.sleep(wait)
            else:
                raise

        except requests.exceptions.ConnectionError as e:
            wait = 2 ** attempt * 5
            logger.log(f"CONNECTION ERROR: {e} — retrying in {wait}s (attempt {attempt}/{max_retries})", tag="RETRY")
            if attempt < max_retries:
                time.sleep(wait)
            else:
                raise

    # Should not reach here, but just in case
    raise Exception(f"All {max_retries} retries exhausted")


# --- Core: Submit + Poll ---
def submit_background_request(prompt: str, model: str, effort: str,
                              api_key: str, logger: Logger) -> str:
    """Submit Deep Research request in background mode. Returns response ID."""
    payload = {
        "model": model,
        "input": [
            {
                "role": "user",
                "content": [{"type": "input_text", "text": prompt}]
            }
        ],
        "tools": [{"type": "web_search_preview"}],
        "reasoning": {"effort": effort},
        "background": True  # KEY: async mode, returns immediately
    }

    logger.log(f"Submitting background request: model={model}, effort={effort}", tag="SUBMIT")
    logger.log(f"Payload size: {len(json.dumps(payload)):,} bytes", tag="SUBMIT")

    resp = request_with_retry(
        "POST",
        "https://api.openai.com/v1/responses",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json_body=payload,
        timeout=SUBMIT_TIMEOUT,
        logger=logger
    )

    logger.log(f"Submit response: HTTP {resp.status_code}", tag="SUBMIT")

    if resp.status_code not in (200, 201, 202):
        logger.log(f"Submit ERROR: {resp.text[:500]}", tag="ERR")
        raise Exception(f"Submit failed: HTTP {resp.status_code} — {resp.text[:500]}")

    result = resp.json()
    response_id = result.get("id")
    status = result.get("status")

    logger.log(f"Response ID: {response_id}", tag="SUBMIT")
    logger.log(f"Initial status: {status}", tag="SUBMIT")

    # Log response headers
    for h in ['x-request-id', 'openai-processing-ms', 'openai-model']:
        val = resp.headers.get(h)
        if val:
            logger.log(f"Header {h}: {val}", tag="SUBMIT")

    if not response_id:
        logger.log(f"ERROR: No response ID in result. Full response: {json.dumps(result)[:500]}", tag="ERR")
        raise Exception("No response ID returned from API")

    return response_id


def poll_for_completion(response_id: str, api_key: str, logger: Logger) -> dict:
    """Poll until response is completed. Returns full response object."""
    url = f"https://api.openai.com/v1/responses/{response_id}"
    headers = {"Authorization": f"Bearer {api_key}"}

    poll_start = time.time()
    tick = 0

    logger.log(f"Starting polling for {response_id} (interval={POLL_INTERVAL}s, max={MAX_POLL_TIME}s)", tag="POLL")

    while True:
        tick += 1
        elapsed = time.time() - poll_start

        if elapsed > MAX_POLL_TIME:
            logger.log(f"POLL TIMEOUT: {elapsed:.0f}s > {MAX_POLL_TIME}s max", tag="ERR")
            raise Exception(f"Polling exceeded max time ({MAX_POLL_TIME}s)")

        try:
            resp = request_with_retry("GET", url, headers=headers, timeout=POLL_TIMEOUT, logger=logger)
        except Exception as e:
            logger.log(f"Poll request failed: {e}. Will retry next tick.", tag="POLL")
            time.sleep(POLL_INTERVAL)
            continue

        if resp.status_code != 200:
            logger.log(f"Poll HTTP {resp.status_code}: {resp.text[:200]}. Will retry.", tag="POLL")
            time.sleep(POLL_INTERVAL)
            continue

        result = resp.json()
        status = result.get("status", "unknown")
        mins = elapsed / 60

        # Count output items for progress
        output = result.get("output", [])
        web_searches = sum(1 for o in output if o.get("type") == "web_search_call")
        messages = sum(1 for o in output if o.get("type") == "message")

        logger.log(
            f"Poll #{tick}: status={status}, {mins:.1f} min elapsed, "
            f"{web_searches} web searches, {messages} messages, "
            f"{len(output)} total output items",
            tag="POLL"
        )

        # Log web search queries for progress visibility
        if tick <= 3 or tick % 5 == 0:  # first 3 polls + every 5th
            for o in output:
                if o.get("type") == "web_search_call":
                    query = "?"
                    action = o.get("action")
                    if isinstance(action, dict):
                        query = action.get("query", "?")
                    o_status = o.get("status", "?")
                    logger.log(f"  Web search [{o_status}]: {query[:80]}", tag="SEARCH")

        # Check terminal states
        if status == "completed":
            logger.log(f"COMPLETED after {mins:.1f} min ({tick} polls)", tag="POLL")
            return result

        if status == "failed":
            error = result.get("error", {})
            logger.log(f"FAILED after {mins:.1f} min: {json.dumps(error)[:500]}", tag="ERR")
            raise Exception(f"Deep Research failed: {json.dumps(error)[:500]}")

        if status == "incomplete":
            reason = result.get("incomplete_details", {}).get("reason", "unknown")
            logger.log(f"INCOMPLETE after {mins:.1f} min: {reason}", tag="ERR")
            # Still try to extract whatever we got
            return result

        if status == "cancelled":
            logger.log(f"CANCELLED after {mins:.1f} min", tag="ERR")
            raise Exception("Deep Research was cancelled")

        # Still in progress — wait and poll again
        time.sleep(POLL_INTERVAL)


# --- Response analysis ---
def analyze_response(result: dict, logger: Logger):
    """Log detailed analysis of the API response."""
    logger.log(f"Response keys: {list(result.keys())}", tag="ANALYSIS")
    logger.log(f"Response ID: {result.get('id', 'N/A')}", tag="ANALYSIS")
    logger.log(f"Model: {result.get('model', 'N/A')}", tag="ANALYSIS")
    logger.log(f"Status: {result.get('status', 'N/A')}", tag="ANALYSIS")

    output = result.get("output", [])
    logger.log(f"Output items: {len(output)}", tag="ANALYSIS")

    web_searches = 0
    messages = 0
    reasoning_items = 0

    for i, item in enumerate(output):
        item_type = item.get("type", "unknown")
        if item_type == "web_search_call":
            web_searches += 1
            query = "?"
            action = item.get("action")
            if isinstance(action, dict):
                query = action.get("query", "?")
            o_status = item.get("status", "?")
            logger.log(f"  [{i}] web_search [{o_status}]: {query[:80]}", tag="ANALYSIS")
        elif item_type == "message":
            messages += 1
            content = item.get("content", [])
            total_text_len = sum(len(c.get("text", "")) for c in content if c.get("type") == "output_text")
            total_annotations = sum(len(c.get("annotations", [])) for c in content if c.get("type") == "output_text")
            logger.log(f"  [{i}] message: {total_text_len:,} chars, {total_annotations} annotations", tag="ANALYSIS")
        elif item_type == "reasoning":
            reasoning_items += 1
            logger.log(f"  [{i}] reasoning", tag="ANALYSIS")
        else:
            logger.log(f"  [{i}] {item_type}", tag="ANALYSIS")

    logger.log(f"Summary: {web_searches} web searches, {messages} messages, {reasoning_items} reasoning", tag="ANALYSIS")

    usage = result.get("usage", {})
    if usage:
        logger.log(f"Tokens: in={usage.get('input_tokens', 0):,}, out={usage.get('output_tokens', 0):,}, total={usage.get('total_tokens', 0):,}", tag="USAGE")
    else:
        logger.log("No usage data", tag="USAGE")


# --- Extract content ---
def extract_text_and_citations(result: dict, logger: Logger) -> tuple:
    """Extract text and citations from Responses API output."""
    text_parts = []
    citations = []

    if "output" not in result:
        logger.log("WARNING: No 'output' in result, dumping raw JSON", tag="EXTRACT")
        return json.dumps(result, ensure_ascii=False, indent=2), []

    for item in result["output"]:
        if item.get("type") == "message" and "content" in item:
            for content_item in item["content"]:
                if content_item.get("type") == "output_text":
                    text_parts.append(content_item.get("text", ""))
                    for ann in content_item.get("annotations", []):
                        if ann.get("type") == "url_citation":
                            title = ann.get("title", "Источник")
                            url = ann.get("url", "")
                            if url:
                                citations.append(f"- [{title}]({url})")

    total_text = "\n".join(text_parts)
    logger.log(f"Extracted: {len(total_text):,} chars, {len(citations)} citations", tag="EXTRACT")
    return total_text, citations


def extract_usage(result: dict) -> dict:
    usage = result.get("usage", {})
    return {
        "input_tokens": usage.get("input_tokens", 0),
        "output_tokens": usage.get("output_tokens", 0),
        "total_tokens": usage.get("total_tokens", 0),
    }


# --- Main ---
def main():
    import argparse
    parser = argparse.ArgumentParser(description="Call OpenAI Deep Research API (background mode + polling)")
    parser.add_argument("prompt_file", help="Path to prompt file (.md or .txt)")
    parser.add_argument("output_file", help="Path to save the result (.md)")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Model (default: {DEFAULT_MODEL})")
    parser.add_argument("--effort", default=DEFAULT_EFFORT,
                        choices=["none", "low", "medium", "high", "xhigh"],
                        help=f"Reasoning effort (default: {DEFAULT_EFFORT})")
    parser.add_argument("--resume", action="store_true",
                        help="Resume polling from saved state (skip submit)")
    args = parser.parse_args()

    # Logger
    log_file = args.output_file.rsplit('.', 1)[0] + '.log' if '.' in args.output_file else args.output_file + '.log'
    logger = Logger(log_file)

    # Graceful shutdown
    def handle_signal(signum, frame):
        logger.log(f"Signal {signum} received — exiting gracefully (state is saved, re-run with --resume)", tag="SIGNAL")
        logger.close()
        sys.exit(130)

    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)

    logger.log("=== Deep Research Call (Background Mode) ===", tag="START")
    logger.log(f"Prompt: {args.prompt_file}", tag="START")
    logger.log(f"Output: {args.output_file}", tag="START")
    logger.log(f"Log: {log_file}", tag="START")
    logger.log(f"Model: {args.model}, Effort: {args.effort}", tag="START")
    logger.log(f"Resume: {args.resume}", tag="START")
    logger.log(f"PID: {os.getpid()}, Python: {sys.version.split()[0]}", tag="START")

    # API key
    api_key = get_api_key(logger)
    if not api_key:
        logger.log("FATAL: No API key", tag="ERR")
        logger.close()
        sys.exit(1)

    # Pre-flight
    if not preflight_check(api_key, logger):
        logger.log("WARNING: Pre-flight failed, continuing anyway...", tag="PRE")

    # --- PHASE 1: Get response ID (submit or resume) ---
    response_id = None
    saved = load_state(args.output_file, logger)

    if args.resume and saved:
        response_id = saved["response_id"]
        logger.log(f"RESUMING from saved state: {response_id}", tag="RESUME")
    elif saved and not args.resume:
        logger.log(f"Found saved state ({saved['response_id']}). Use --resume to continue, or delete .state to start fresh.", tag="STATE")
        logger.log("Starting fresh (ignoring saved state)...", tag="STATE")

    if not response_id:
        # Read prompt
        logger.log(f"Reading prompt: {args.prompt_file}", tag="IO")
        with open(args.prompt_file, 'r', encoding='utf-8') as f:
            prompt = f.read()
        if not prompt.strip():
            logger.log("FATAL: Prompt file is empty", tag="ERR")
            logger.close()
            sys.exit(1)
        prompt_stats(prompt, logger)

        # Submit
        try:
            response_id = submit_background_request(prompt, args.model, args.effort, api_key, logger)
            save_state(args.output_file, response_id, args.model, logger)
        except Exception as e:
            logger.log(f"FATAL: Submit failed: {e}", tag="ERR")
            with open(args.output_file, 'w', encoding='utf-8') as f:
                f.write(f"# Deep Research ERROR\n\nSubmit failed: {e}\n")
            logger.close()
            sys.exit(1)

    # --- PHASE 2: Poll for completion ---
    try:
        result = poll_for_completion(response_id, api_key, logger)
    except Exception as e:
        logger.log(f"FATAL: Polling failed: {e}", tag="ERR")
        logger.log(f"State is saved. Re-run with --resume to continue.", tag="ERR")
        with open(args.output_file, 'w', encoding='utf-8') as f:
            f.write(f"# Deep Research ERROR\n\nPolling failed: {e}\n\nResponse ID: {response_id}\nRe-run with --resume to retry.\n")
        logger.close()
        sys.exit(1)

    # --- PHASE 3: Extract and save ---
    analyze_response(result, logger)
    text, citations = extract_text_and_citations(result, logger)
    usage = extract_usage(result)

    # Write output
    logger.log(f"Writing output: {args.output_file}", tag="IO")
    with open(args.output_file, 'w', encoding='utf-8') as f:
        f.write(text)
        if citations:
            seen = set()
            unique = [c for c in citations if c not in seen and not seen.add(c)]
            f.write("\n\n---\n\n## Автоматически извлечённые URL-источники\n\n")
            f.write("\n".join(unique))
            f.write("\n")
            logger.log(f"Citations: {len(unique)} unique / {len(citations)} total", tag="IO")

    # Save raw JSON
    raw_file = args.output_file.rsplit('.', 1)[0] + '-raw.json' if '.' in args.output_file else args.output_file + '-raw.json'
    logger.log(f"Saving raw JSON: {raw_file}", tag="IO")
    with open(raw_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    # Clear state (success!)
    clear_state(args.output_file, logger)

    # Final summary
    total_elapsed = time.time() - logger.start_time
    logger.log("=== DONE ===", tag="END")
    logger.log(f"Output: {args.output_file} ({len(text):,} chars)", tag="END")
    logger.log(f"Raw: {raw_file}", tag="END")
    logger.log(f"Log: {log_file}", tag="END")
    logger.log(f"Citations: {len(citations)}", tag="END")
    logger.log(f"Tokens: in={usage['input_tokens']:,} out={usage['output_tokens']:,} total={usage['total_tokens']:,}", tag="END")
    logger.log(f"Wall time: {total_elapsed:.0f}s ({total_elapsed/60:.1f} min)", tag="END")

    logger.close()


if __name__ == "__main__":
    main()
