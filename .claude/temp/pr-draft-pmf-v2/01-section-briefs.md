# Section Briefs — PMF Playbook (HackerNoon v2)

## Structural decisions

- Hook: Variant C (Tension/Paradox) — RECOMMENDED by narrative-architect
- Section order: Hook → T1 → T2 → T3 → T4 → T5 → Close
- Close: Variant A (Checklist + micro-bridge) — "Start this week. Pick your killer assumption. Test it."
- Memorable moments: "Building was free. Validation was skipped. The company died." (T3) + "PMF is not something you find. It is something you keep finding." (Close)
- Total target: 1,500-1,600 words

## NOTE: Ivan updated his draft on 2026-03-05

Key changes from his update:
- Removed "foundational cohort" nuance from T1
- Changed T2 title to "Start With the Job To Be Done", added "model unit-economics" to sequence
- Simplified T3 heavily — removed METR study, EnrichLead case, arXiv references
- **Merged old T4 (killer assumption) + T5 (hypothesis factory) into one lean section "The Hypothesis Factory"**
- T5 (PMF Treadmill) + Close remain largely intact
- Checklist still references the formula and 4-component OS → these concepts should appear in body

**v2 approach:** Preserve Ivan's simplified 5-section structure. Flesh out T3 and T4 with cases/data. Keep his transitions verbatim. Don't re-split T4.

## CRITICAL HackerNoon STYLE RULES (from style-researcher + media brief)
- First person ("I"), never corporate "we" (HackerNoon official rule)
- Max 4 sentences per paragraph (hard ceiling)
- Hook: 3-4 sentences, never opens with definition
- Subheadings: 5-7 per article, sentence case or Title Case
- Data: 3-5 specific data points embedded in flow
- Expert references: paraphrase and attribute, inline links
- Tone: slightly informal professional (6/10 formality), contractions OK
- Frameworks > anecdotes — name frameworks explicitly
- AI text tracked — avoid "delve", "leverage", "it's important to note"
- Suggested case phrases: "In my experience...", "A recurring pattern I've observed..."
- No emoji in body text

---

## Hook (~80 words)

**Variant C (Tension/Paradox) — RECOMMENDED:**

Building a product has never been cheaper. Killing a startup has never been easier. AI collapsed the cost of writing code to near zero — and the number of startups dying from untested assumptions has not gone down. It has gone up. The anti-pattern is everywhere: more code, less validation. The playbook of "find PMF, then scale" is a trap in a world where product-market fit expires every quarter. This article is the operating manual for the treadmill that never stops.

**Bridge to T1:** "The first step is admitting where you actually stand. And the honest answer is brutal."

---

## Section Brief: Your idea is already dead (T1)

**Word budget:** ~220 words

### SECTION SKELETON (from Ivan's updated draft):
90-95% fail. "Buy knowledge about what will kill your idea." "We don't launch products — we purchase validated learnings." Pivot = surgical act of changing assumptions. Notion case: V1 failed as tool "for non-coders" → Kyoto → modular workspace → $10B. Wrong assumption was about the Job and Value Proposition.

### MUST-INCLUDE:
- T1-D1: 90-95% of new products fail
- T1-C1: "Buy knowledge about what will kill your idea"
- T1-C2: "We don't launch products — we purchase validated learnings"
- T1-C3: Pivot = surgical act of changing wrong assumptions
- T1-CS1: Notion case (V1 failed, Kyoto, modular workspace, $10B)

### NEW CASES (optional supplement):
- Slack as alternative example: Glitch game failed → internal messaging tool → $27.7B (byproduct was the real product)
  URL: https://startupdevkit.com/slacks-startup-story-a-remarkable-pivot-from-failing-startup-to-unicorn/
  **Decision: KEEP Notion as primary (Ivan's choice). Don't replace.**

### TRANSITION to T2 (VERBATIM — KEEP):
"If the goal of early stage is to buy knowledge about what kills your idea, the next question is obvious: where do you start digging?"

### IVAN'S VOICE: Analytical with gut-punch data → opinionated reframe. "In my experience training 12,000+ product managers..."

---

## Section Brief: Start with the Job To Be Done (T2)

**Word budget:** ~230 words

### SECTION SKELETON:
Jobs = root cause. Correct sequence: segment → job → unit economics → value → communication. Common mistake: skip to solution, fall in love with technology. Wispr Flow case: hardware dream killed, macOS dictation, 20% conversion, #1 PH.

### MUST-INCLUDE:
- T2-C1: Correct sequence: segment → job → unit economics → value → communication
- T2-C2: "Fall in love with the technology, not the problem" = mistake
- T2-CS1: Wispr Flow case (20% conversion vs 3-4% industry)

### NEW CASES (supplement):
- Superhuman: PMF score 22% → 58% by narrowing segment to "Nicole" persona
  URL: https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/
  **Decision: OPTIONAL supplement if word budget allows. Wispr Flow is primary.**

### TRANSITION to T3 (adapted from Ivan's original, since the explicit one was removed):
"AI can accelerate hypothesis generation — spinning up segment maps and assumption lists in minutes. But there is a trap hiding in that speed."

### IVAN'S VOICE: Methodical, builds step-by-step. "The most common mistake I see?"

---

## Section Brief: AI made building free ≠ learning free (T3)

**Word budget:** ~250 words (THE VALLEY — needs room for case + data)

### SECTION SKELETON (from Ivan's updated draft — lean):
AI collapsed the build step — prototype in a weekend. "More code, less validation" anti-pattern. AI = accelerator of artifacts, not substitute for learning. Measure validated checks.

### MUST-INCLUDE:
- T3-C1: "More code, less validation" anti-pattern
- T3-C2: AI = accelerator of artifacts, not substitute for learning
- T3-C3: Measure validated checks, not features shipped

### NEW DATA (flesh out Ivan's lean version):
- METR study: AI tools slow experienced developers 19% while they feel 20% faster — 39% perception gap
  URL: https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/

### NEW CASES:
- Moltbook [NEW PRIMARY, Jan 2026]: AI social network, vibe-coded, 1.5M API keys + 35K emails exposed in 72 hours. No Row-Level Security. 770K AI agents hijackable.
  URL: https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys
  **Why: Fresher than EnrichLead (Jan 2026), verified by Wiz, larger scale, HackerNoon readers will recognize the headlines.**

### KEY PHRASE (standalone — don't bury):
"Building was free. Validation was skipped. The company died."

### TRANSITION to T4 (VERBATIM — KEEP):
"If AI gives you speed but not direction, you need a compass. Here is the formula that tells you which assumption to test first."

### IVAN'S VOICE: Dark, confrontational. Staccato. Short sentences.

---

## Section Brief: The Hypothesis Factory (T4)

**Word budget:** ~280 words (LONGEST — operational heart, merges old T4+T5)

### SECTION SKELETON (from Ivan's updated draft — very lean):
Founder = factory operator. Throughput without validation = noise. Kill criteria.

### NOTE: Ivan's checklist still references formula + 4-component OS. The v2 must flesh this section out with:
1. The killer assumption formula: (probability × consequences) / cost
2. The 4-component OS: assumption ledger, decision log, staged validation, stop criteria
3. A case showing the formula or OS in action

### MUST-INCLUDE:
- T4-C1: Killer assumption formula: (probability wrong × consequences) / cost of testing
- T4-C2: "AI tourists" inflate early metrics → set signal horizon
- T4-C3: 4-component OS: assumption ledger, decision log, staged validation, stop criteria
- T4-C4: Learning velocity > experiment velocity

### NEW CASES:
- Popsa [RESTORE from Ivan's earlier version]: changed "Fast" to "Five Minutes" in tagline → 4x conversion. Cost: one round of user interviews.
  URL: https://review.firstround.com/founder-led-growth-playbook/
- Booking.com [NEW supplement]: 25,000 experiments/year, anyone can test without permission.
  URL: https://hbr.org/2020/03/building-a-culture-of-experimentation
  **Decision: Use Popsa for the formula, Booking.com for the OS. Both compact.**

### TRANSITION to T5 (adapted):
"But even the best operating system is useless if you treat PMF as a one-time achievement. Here is the part most teams miss."

### IVAN'S VOICE: Precision. The formula as centerpiece. Then the OS as a structured list. "Here is the prioritization formula" — direct, instructional.

---

## Section Brief: The PMF treadmill (T5)

**Word budget:** ~200 words

### SECTION SKELETON (from Ivan's updated draft — intact):
Jasper AI: $120M → $35M ARR. PMF less durable in every market. Two loops: optimize + innovate. Elena Verna: "quarterly reality." "The treadmill never stops. But now you have the operating manual."

### MUST-INCLUDE:
- T5-CS1: Jasper AI case ($120M→$35M, ChatGPT disruption)
- T5-C1: Two loops: optimize current fit + continuous innovation
- T5-Q1: Elena Verna "quarterly reality"
- T5-C2: "PMF is not something you find. It is something you keep finding."

### NEW CASES (optional supplement):
- Chegg: $12B → delisting risk, 87.5% drop, CEO blamed "new realities of AI"
  URL: https://www.cnbc.com/2025/10/27/chegg-slashes-45percent-of-workforce-blames-new-realities-of-ai.html
  **Decision: ADD as second proof — different market (education), same pattern. Makes the "every market" claim concrete.**

### KEY PHRASE (standalone):
"The treadmill never stops. But now you have the operating manual."

### IVAN'S VOICE: Reflective, resolving. Zoom out. "This is not just an AI-category phenomenon."

---

## Section Brief: Close — The Operating Checklist

**Word budget:** ~150 words

### BODY (from Ivan's draft — keep all 6 items):
1. Start with jobs and segments — this is the root cause of everything else.
2. List your riskiest assumptions. Prioritize by: (probability of error × consequences) / cost of test.
3. Use AI to build artifacts fast — but measure progress in validated checks, not shipped features.
4. Run the factory with an OS: assumption ledger, decision log, staged validation, explicit stop criteria.
5. When pivoting, name exactly which assumption changed and why.
6. Accept the treadmill. Schedule the next round of re-validation before you need it.

### MICRO-BRIDGE (narrative-architect recommendation):
"Start this week. Pick your killer assumption. Test it."

### CLOSING LINE:
"PMF is not something you find. It is something you keep finding."

### IVAN'S VOICE: Action-oriented. Scannable. Screenshot-ready.

---

## Coverage check

### Elements from updated must-include: ~30/39
### DROPPED elements (with reason):
- T1-C4 (foundational cohort nuance) — Ivan removed it in his update
- T2-D1/D2 (Wispr Flow $81M raised, 20% conversion specific) — conversion kept, funding detail dropped for word budget
- T2-CT1 (arXiv over-reliance on AI) — merged into T3 thematically
- T3-D1/D2 (METR + vibe-coding arXiv) — METR restored, arXiv vibe-coding dropped
- T3-CS1 (EnrichLead) — replaced by Moltbook (fresher)
- T5-D1 (Spotify 520 experiments) — replaced by Booking.com or dropped for word budget
- T6-CS2 (Lovable) — moved to hook per Ivan's design

### NEW elements added:
- Moltbook case (T3)
- METR data restored (T3)
- Popsa case restored (T4)
- Booking.com case (T4)
- Chegg case (T5)
