---
name: pr-article-draft
description: Write a PR article draft for a specific media outlet. Use when you have theses from the PR manager and a media brief from the outlet. Do NOT use for book chapters — that is a separate skill.
user-invocable: true
---

# Skill: Writing a PR Article Draft

This skill turns ready-made theses and a media brief into a polished article draft via an agent team. All output is in English.

## Core principles

1. **Theses are law.** They came from the PR manager and are already aligned with the editor. Do not add, remove, or reinterpret them.
2. **The media brief is the style authority.** Tone, structure, word count, banned patterns — already defined by the outlet. The style-researcher agent provides *supplementary* insights (paragraph length, data density, hook patterns) but **never overrides explicit rules from the media brief**.
3. **Thesis body = section skeleton.** The writer takes the thesis logic as a starting point and enriches it with cases. Does not generate from scratch.
4. **Ivan's voice matters.** The article must sound like Ivan — not a generic thought-leader. Extract his real voice from his book chapters and blend it with the outlet's style requirements.
5. **Cases = combo.** Ivan's cases from the repository first (first-person credibility), then fresh external ones (2025–2026) for broader context. Every case must pass the ARGUMENT TEST.
6. **No AI-sounding English.** A dedicated language review step ensures the final text reads like a sharp native writer in tech/business — not a language model.
7. **Every source needs a link.** Inline markdown links in the text body. No URL = don't mention the source. Every URL must be verified via WebFetch before inclusion.
8. **Every named source needs credentials.** When a person or organization is mentioned inline, the reader must immediately understand WHY they are an authority. Not just `[Boris Cherny](url)` but `[Boris Cherny, creator of Claude Code at Anthropic](url)`. Not just `[Bessemer](url)` but `[Bessemer Venture Partners, one of Silicon Valley's oldest VC firms](url)`. If the person is unknown to the target audience and you can't explain their credentials in ≤8 words — cite the fact without naming them, or find a higher-tier source.
9. **Source tiers determine citation style.** Every external source has a tier that dictates how it's used in the article:
   - **Tier 1 (⭐⭐⭐):** Named experts (Marty Cagan, Bob Moesta), major research orgs, top-tier VC firms, definitive studies. → Cite by NAME + credentials + quote.
   - **Tier 2 (⭐⭐):** Respected industry publications (HBR, First Round Review, a16z blog), large data reports (CB Insights, Gartner). → Cite by PUBLICATION name + key finding.
   - **Tier 3 (⭐):** Medium posts, minor blogs, secondary aggregators, unknown authors. → Use the DATA or FACT only, do NOT cite the author by name. Attribute to the original source they reference, or state the fact without attribution if it's widely known.
   
   **Rule:** Never introduce an unknown person as if the reader should recognize them. "Random blogger says X" destroys credibility. If the insight is good but the source is Tier 3 — find the original Tier 1-2 source, or state the fact without a name.

---

## Input

Ivan provides:
1. **Theses file** — from the PR manager (topic, theses, the core argument of each)
2. **Media brief** — tone, format, structure, word count, restrictions, any suggested phrases

Both are required. If either is missing — stop and ask before doing anything else.

---

## Working paths and initialisation

Compute the repo root and working directories at the very start:

```bash
ROOT="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"

DRAFT_DIR="$ROOT/3-Marketing/2-PR-Articles/3-Drafts"
BOOK_DIR="$ROOT/3-Marketing/2-Writing-Book"
KB_INDEX="$ROOT/1-Context/AURA-Theses/_index.md"

mkdir -p "$DRAFT_DIR"
```

Derive the slug and temp path:

```bash
SLUG="$(printf '%s' "{article-slug}" \
  | tr '[:upper:]' '[:lower:]' \
  | sed -E 's/[^a-z0-9]+/-/g; s/^-+|-+$//g; s/-+/-/g')"

TEMP="$ROOT/tmp/pr-draft-${SLUG}"
mkdir -p "$TEMP"
```

`{temp}` below always means `$TEMP`.

---

## CONTEXT PRESERVATION PROTOCOL (Anti-Compaction)

⚠️ Claude Code compacts context in long sessions, losing details and reducing quality. Save intermediate results to disk and re-read them before each stage.

### Temp files

| After stage | File | Contents |
|-------------|------|----------|
| Stage 0 | `00-brief.md` | Parsed theses + media brief + Ivan's voice notes + section map |
| Stage 0 | `00-must-include.md` | All must-include elements by thesis (checkboxes) |
| Agents | `agent-case-hunter.md` | Cases (Ivan's + external) |
| Agents | `agent-narrative-architect.md` | Narrative plan |
| Agents | `agent-style-researcher.md` | Style fingerprint (supplementary to brief) |
| Stage 2 | `01-section-briefs.md` | Section briefs for writer |
| Stage 3 | `02-draft.md` | Raw draft |
| Stage 4 | `03-draft-reviewed.md` | After language review + humanity pass |
| Stage 5 | `04-quality-report.md` | Verification results |
| All stages | `_spring-context.md` | Current state and next step |
| All stages | `_decision-log.md` | Every decision with rationale |

### Spring context file (_spring-context.md)

Update after every stage:

```markdown
# Spring Context — PR Draft: {article title}

## Current stage: {N} — {stage name}
## Status: {in progress / done}

## Outlet: {name}
## Word count target: {N}
## Theses count: {N}
## Total must-include elements: {N}

## Ivan's voice notes
{2–3 sentences: how he argues, what patterns, what phrases}

## Key decisions
- Hook: {type, brief description}
- Section count: {N}
- Word budget: {N} words

## Saved files
{list with status}

## Next step
{what to do next}
```

### Decision log (_decision-log.md)

Create at the very start. Log EVERY decision:

```markdown
# Decision Log — PR Draft: {article title}

## [STAGE {N}] {decision}
**Context:** {why the question arose}
**Options:** {what was on the table}
**Decision:** {what was chosen}
**Rationale:** {why}
**Trade-off:** {what we lose}
```

**Mandatory entries:**
- Stage 0.4: word budget check result
- Stage 2: every DROPPED element (one line: element + reason)
- Stage 5: every [BODY DISTORTED] and [MISSING] with action taken

---

## STAGE 0: Parse inputs, extract voice, extract must-include, check word budget (lead)

### Step 0.1: Read theses and media brief in full

From the theses file extract:
- Core idea of the article (1–2 sentences)
- Full list of theses with their body — **copy verbatim, do not summarise**
- Any cases or examples already included
- Target audience

From the media brief extract:
- Outlet name, word count
- Article structure (if prescribed)
- Tone and formality level
- Banned phrases or patterns
- Special requirements (AI detector, etc.)
- Suggested phrases for framing cases (e.g. "In my experience across multiple product teams…") — copy verbatim, these go to writer and language-reviewer

### Step 0.2: Extract Ivan's voice from book chapters

Read 2–3 recently modified chapters from:
```
{ROOT}/3-Marketing/2-Writing-Book/
```

Extract:
- **How he argues:** concrete → abstract, or "here's what I expected vs what actually happened"?
- **Signature moves:** how he opens sections, how he lands a point
- **Metaphor domains:** what areas does he draw comparisons from?
- **Rhythm:** sentence length patterns, use of short punchy statements after complex ones
- **Distinctive phrases:** 3–5 short verbatim examples that feel unmistakably Ivan

⚠️ Do NOT copy long passages. Extract patterns and short examples only.

### Step 0.3: Extract MUST-INCLUDE elements from every thesis

For EACH thesis, go through its content and extract ALL specific elements of six types. Copy VERBATIM — do not rephrase, do not shorten.

**6 types of MUST-INCLUDE elements:**

| Type | What to extract | How to copy |
|------|----------------|-------------|
| **BODY** | ⚠️ FIRST: full text of the thesis body | Verbatim, in full, no cuts. This is the SKELETON of the future section — the most important element. |
| **DATA** | Every specific number, statistic, fact | Verbatim: "4% of all GitHub commits from Claude Code" |
| **QUOTE** | Every direct expert quote | Verbatim with name and URL: Boris Cherny: "Coding is largely solved" — [URL] |
| **CONCEPT** | Every named framework, concept, term | Verbatim: "T-shaped → E/F-shaped skills", "Mexican standoff" |
| **KB** | Every Knowledge Base citation | Verbatim with file path |
| **COUNTER** | Every counterargument with source | Verbatim with URL: "METR: 19% SLOWER with AI" — [URL] |

⚠️ **BODY is the most important type.** The thesis body is already a READY argument — a logical chain that will become the section skeleton. DATA, QUOTE and the rest are elements to ENRICH the body, not replace it.

⚠️ **Extraction rule:** If an element exists in the thesis — it goes into must-include. Do NOT filter at this stage. Do NOT decide "this isn't important". Extract EVERYTHING. Filtering happens at Stage 2 (Section Briefs).

Save to `{temp}/00-must-include.md` with this format:

```markdown
# MUST-INCLUDE Elements — {article title}

## Thesis 1: {full title}

### BODY (section skeleton — COPY IN FULL):
{FULL text of the thesis body — verbatim, every sentence}

### DATA (numbers and facts):
- [ ] {element 1 — verbatim}
- [ ] {element 2 — verbatim}

### QUOTE (expert quotes):
- [ ] {Name}: "{exact quote}" — [URL]

### CONCEPT (frameworks and concepts):
- [ ] {concept — verbatim}

### KB (from Knowledge Base):
- [ ] > "{exact quote}" — Source: {file path}

### COUNTER (counterarguments):
- [ ] {Who}: "{summary}" — [URL]

### TOTAL ELEMENTS: {N}

---

## Thesis 2: {full title}
{same structure}

---

## From "Debates" section (if present):
- [ ] {debate 1}

## From "Examples and cases" section (if present):
- [ ] {case 1}

## TOTAL ELEMENTS ACROSS ALL THESES: {N}
```

**Rules:**
1. **VERBATIM** — copy element text as-is
2. **Every URL** must be copied next to the element
3. **Checkboxes `- [ ]`** — each element starts with one (will be marked `- [x]` during final verification)
4. **COUNT elements** — per thesis and grand total
5. **Do NOT merge** — each separate fact, quote, number = separate element. Guideline: 8–20 elements per thesis. If < 5 — you missed something.

### Step 0.4: Word budget compatibility check

⚠️ **Mandatory safety check.** Count the minimum budget:

| Thesis depth | Minimum words per section |
|--------------|--------------------------|
| Deep | 250 words |
| Medium | 150 words |

**Formula:**
```
Minimum = Σ(words per thesis by depth) + 120 (hook) + 140 (close)
```

**If minimum > word count from brief:**

⛔ **STOP. Tell the user:**

"The word budget ({N}) is insufficient for {M} theses (minimum needed: {K} words).
Options:
1. Increase the word limit to {K} words
2. Flag to the PR manager that some theses may get lighter coverage
3. Proceed with tight budget — some theses will get ~100 words (NOT recommended)"

Log the result in `_decision-log.md`. **Do NOT proceed without a resolution.**

### Step 0.5: Build Section Map

Each thesis = one section. If the brief prescribes a rigid structure — map theses to those slots. If structure is open — follow the logic of the theses.

### Save to `{temp}/00-brief.md`:

```markdown
# Brief — {article title}

## Outlet: {name}
## Word count: {N}

## Core idea
{1–2 sentences}

## Theses (verbatim from input file)
### Thesis 1: {title}
{full body — verbatim}

### Thesis 2: ...

## Section Map
| Section | Thesis | Words |
|---------|--------|-------|
| Hook | — | ~{N} |
| {section from brief} | Thesis {N} | ~{N} |
| ... | ... | ... |
| Close | — | ~{N} |

## Style Rules (from media brief — THESE TAKE PRIORITY)
- Tone: {description}
- Structure: {description}
- Banned: {list}
- Special requirements: {list}
- Suggested case phrases: {verbatim from brief — these must appear in the article}

## Ivan's Voice Notes
- How he argues: {pattern}
- Signature moves: {description with example}
- Metaphor domains: {examples}
- Rhythm: {notes}
- Distinctive phrases (verbatim): {3–5 examples}
```

Update `_spring-context.md`.

---

## STAGE 1: Launch agents (3 in parallel)

Launch the following 3 agents in parallel using the Agent tool (subagent_type: general-purpose). Each agent saves its output to a file in `{temp}/`.

---

### Agent 1 — "case-hunter" (subagent_type: general-purpose)

**Launch prompt:**
```
You are "case-hunter" for the article "{title}" targeting {outlet}.

Theses:
{full thesis list from 00-brief.md — verbatim}

YOUR ROLE: Find concrete cases and examples for each thesis.
PRIORITY: Ivan's cases from the repository first, then fresh external ones.

## CRITICAL RULE: ARGUMENT TEST

A case is valid ONLY if it serves as an ARGUMENT for the thesis — not just "on the same topic". Before including any case, ask yourself:

> "If I say [thesis], then say 'For example, [case]' — does this sound like PROOF of the thesis, or just RELATED INFORMATION?"

**Example of a correct case:**
- Thesis: "Prototypes can be built in a day, but production is far away — the bottleneck is security, DevOps, compliance"
- ✅ VALID: "Startup X built a prototype in 2 days but spent 6 months on SOC2 compliance and production deployment" — this PROVES the gap between prototype and production
- ❌ INVALID: "Airbnb added AI to customer service and handles a third of requests" — this is about AI in support, NOT about the prototype → production gap

**Topical proximity ≠ argumentative relevance.** A case about "AI at company X" does not argue a thesis about "limitations of vibe coding", even if both involve AI.

**PERCEPTION CHECK (run after Argument Test passes):**

> "Will this case read as proof of the thesis — or as self-promotion by the author?"

If a case features the author's own company, product, or direct success story, ask:
- Does it prove a universal principle, or does it just make Ivan look good?
- Would a skeptical reader at this outlet trust it, or dismiss it as PR?

If it risks reading as promotional → pair it with an external case that proves the same point independently, or lead with the external case and use Ivan's as a supporting "in my experience" detail.

## PART 1: Ivan's cases (from repository)

STEP 1: Read the index:
{ROOT}/1-Context/AURA-Theses/_index.md

STEP 2: For each thesis, grep the entire repository by key terms from the thesis.
Look for: concrete cases from Ivan's practice, real examples from his work with product teams, results with specific numbers.

STEP 3: Read found files. Use offset/limit ~800 lines for large files.

For each Ivan case found, note:
- What happened (specific, 2–4 sentences)
- Result or takeaway, with numbers if available
- Full file path in repository — REQUIRED
- ARGUMENT TEST: "This case proves that ___" → matches thesis? ✅/❌

## PART 2: External cases (web)

For each thesis:

STEP 1: Formulate the thesis argument in one sentence: "This thesis PROVES that ___". Use this as your search filter.

STEP 2: Run 2–3 searches:
- "{thesis argument keywords} case study 2025 2026"
- "{thesis argument keywords} real example startup product"
- "{thesis argument keywords} lessons learned"

STEP 3: For each candidate case, run ARGUMENT TEST:
1. Does it ARGUE the thesis? Can you say "[thesis]. For example, [case]" and it sounds like proof?
2. If the case is "on the same topic" but proves a DIFFERENT claim → DISCARD
3. Write: "This case proves that ___" — if it doesn't match the thesis → DISCARD

STEP 4: Verify URL via WebFetch
⚠️ MANDATORY for every external case:
1. Open URL via WebFetch
2. Does the page exist and load?
3. Does the content confirm what you want to cite?
4. If URL doesn't load or content doesn't match → DO NOT INCLUDE THE CASE.

What makes a good external case:
1. Named company or person — no anonymous "a startup"
2. Fresh (2025–2026 = top priority, 2024 = acceptable)
3. Surprising, not generic — not just "Google built AI"
4. Contains specifics: what happened, numbers, outcome
5. ARGUMENT TEST passed ✅
6. URL verified via WebFetch ✅

⚠️ NO URL = NO CASE. NO ARGUMENT TEST = NO CASE. NO WEBFETCH VERIFICATION = NO CASE.

## SOURCE TIER CLASSIFICATION (MANDATORY for every source)

For EVERY external source (expert, study, publication), classify its tier:

⭐⭐⭐ **Tier 1 — Authority sources:** Direct domain experts (Bob Moesta on JTBD, Marty Cagan on product), major VC firms whose audience recognizes them (a16z, Sequoia, Y Combinator), definitive studies (CB Insights failure report, Startup Genome). Rule: cite by NAME + short credential.

⭐⭐ **Tier 2 — Respected publications:** First Round Review, HBR, Lenny's Newsletter, Reforge, MIT Sloan. Rule: cite by PUBLICATION name + finding.

⭐ **Tier 3 — Minor sources:** Medium posts, personal blogs, unknown authors, secondary aggregators, TikTok threads. Rule: use the FACT only. Do NOT cite the author by name — the reader won't know them, and naming them weakens the article's credibility. Find the ORIGINAL source they reference, or state the fact without attribution.

**CREDENTIAL CHECK:** For each named expert, provide a ≤8 word credential that answers "why should the reader care?" Examples:
- ✅ "Rahul Vohra, CEO of Superhuman" — reader recognizes the company
- ✅ "Elena Verna, Head of Growth at Lovable" — clear role at known company
- ✅ "Bessemer Venture Partners, one of Silicon Valley's oldest VC firms" — context provided
- ❌ "Ahmad Fiaz Jan" — who? Reader has no context. Use the data, drop the name
- ❌ "According to a Medium post" — find the original research source instead

Include tier + credential in the output format for every source.

## OUTPUT FORMAT

### Thesis {N}: {title}
**This thesis proves that:** {one sentence — the argument}

**Ivan's cases:**
- Case: {what happened, outcome}
  Source: {full path to file in repository}
  Key detail: {most specific/memorable element}
  ARGUMENT TEST: "This case proves that ___" → ✅

**External cases:**
- Case: {company/person — what happened — outcome}
  URL: {real link}
  URL verified via WebFetch: ✅
  Year: {year}
  ARGUMENT TEST: "This case proves that ___" → ✅
  Why it fits: {one sentence connection to thesis}
  **Tier:** ⭐⭐⭐ / ⭐⭐ / ⭐
  **Credential for inline use:** "{Name}, {≤8 word credential}" — e.g. "Elena Verna, Head of Growth at Lovable"

**All sources used in cases (with tiers):**
| Source | Tier | Credential (≤8 words) | Can name inline? |
|--------|------|----------------------|-----------------|
| {name} | ⭐⭐⭐ | {credential} | ✅ Yes |
| {name} | ⭐ | {none — unknown author} | ❌ Use fact only |

## SAVE (REQUIRED)

Save full report to:
{temp}/agent-case-hunter.md

## ITERATIONS

Wait for follow-up requests from the lead. If asked to dig deeper — do it. Always overwrite the file with the full updated version.
```

---

### Agent 2 — "narrative-architect" (subagent_type: general-purpose)

**Launch prompt:**
```
You are "narrative-architect" for the article "{title}" targeting {outlet}.
Word count target: {N}

Theses and Section Map:
{from 00-brief.md — full}

Style Rules from media brief:
{from 00-brief.md — full}

Ivan's Voice Notes:
{from 00-brief.md — full}

YOUR ROLE: Build the narrative plan — section order, hook variants, transitions, close.

⚠️ CONSTRAINTS:
- Do NOT change the content of theses
- Do NOT merge theses or create new sections
- N theses = N sections. You decide ORDER and CONNECTIVE TISSUE only.
- If the brief prescribes a rigid structure — follow it

## TASK 0: Why Now?

Before building anything else, answer in one sentence: why does this argument matter specifically today?

What changed recently — in the industry, in technology, in how teams work — that makes this thesis urgent **now** vs. 6 months ago? Look for: a recent event, a shift in practice, a data point from the last 90 days, a trend that just became impossible to ignore.

Write the "why now" sentence. This must appear in the hook or within the first 100 words of the article.

⚠️ If you cannot find a compelling "why now" → write `[WHY NOW: NOT FOUND]` and flag it. Do not proceed silently.

## TASK 1: Narrative arc

- Conflict: what the reader believes now VS what the article will show them
- Transformation: how their thinking or behaviour changes by the end
- Emotional arc: what states they move through (e.g. recognition → doubt → insight → confidence → action)

## TASK 2: Hook — 3 variants

Write 3 opening paragraphs in English, 3–4 sentences each.
Follow the brief's hook requirements if specified.

**Variant A: Shock** — a stat or fact that surprises
**Variant B: Story** — a mini-story about a specific person or team (3–5 sentences)
**Variant C: Tension** — a contradiction ("everyone does X, but it doesn't work because...")

For each: write the actual text + explain why it works for this outlet's audience.

## TASK 3: Section order

Propose the optimal order for the thesis-sections.
Explain the logic: why this order works for this specific audience.

## TASK 4: Transitions

For each pair of adjacent sections, write a specific transition sentence in English.

## TASK 5: Close — 3 variants in English

**Rule:** The closing must NEVER summarise what was already said. It must move the reader forward — to a decision, an action, or an uncomfortable question.

**Variant A: Decision reframe** — one concrete thing the reader should do differently starting tomorrow. Specific, not generic ("stop doing X" or "try Y with your next sprint").
**Variant B: Provocation** — a question that makes them uncomfortable about their current approach. Should sting slightly. Not rhetorical — genuinely hard to answer.
**Variant C: Prediction** — where this trend goes in 12 months if the reader ignores the argument. Make it specific and falsifiable.

## TASK 7: Memorable Moment

Identify ONE element in the article that the reader will remember a week later. Not the argument — the moment.

This could be:
- A paradoxical formulation: "The faster you ship, the slower you learn" 
- An unexpected number that reframes the problem
- A specific image or scene from a case that sticks
- A one-line thesis so sharp it could be tweeted

Write it out explicitly. Mark which section it lives in. Flag it for the writer: this moment must not be diluted, buried, or softened in editing.

`MEMORABLE MOMENT: "{exact formulation}" → Section: {N}`

## TASK 6: Word budget

| Section | Thesis | Words |
|---------|--------|-------|
| Hook | — | ~{N} |
| ... | ... | ... |
| Close | — | ~{N} |
| **Total** | | ~{N} |

## SAVE (REQUIRED)

Save full report to:
{temp}/agent-narrative-architect.md
```

---

### Agent 3 — "style-researcher" (subagent_type: general-purpose)

⚠️ **Priority rule:** The media brief's explicit rules ALWAYS take priority. The style-researcher provides *supplementary* insights for areas the brief doesn't cover (paragraph rhythm, data density, hook patterns, what makes articles go viral at this outlet).

**Launch prompt:**
```
You are "style-researcher" for the article "{title}" targeting {outlet}.
Article language: English

YOUR ROLE: Find the most popular/most-read articles at the target outlet and extract stylistic patterns that make texts successful there. Your findings SUPPLEMENT (never override) the media brief.

## TASK 1: Find top articles at the outlet

WebSearch and WebFetch:
1. Search: "site:{outlet domain} most popular" / "site:{outlet domain} best articles"
2. Search: "site:{outlet domain} {article topic} 2025 2026"
3. Search: "{outlet name} most read articles"
4. Visit the outlet's homepage and find "Popular", "Trending", "Most Read" sections
5. Collect 5–8 most-read/popular articles

For each article found:
- Read via WebFetch
- Record URL, title, author, date
- Note signal type: popular_list, trending_badge, editor_pick, high_engagement_proxy

## TASK 2: Extract stylistic patterns

Analyse the 5–8 top articles and extract:

### Structural patterns:
- Average article length (words)
- Headline types (questions? statements? how-to?)
- Average paragraph length
- Use of bullet points/lists — how often?
- Subheading frequency
- Hook format (first 2–3 sentences)
- Conclusion format

### Tonal patterns:
- Formality (1–10 scale)
- First person ("I", "we") usage?
- Direct address ("you")?
- Humour/irony?
- Expert vs conversational tone?
- Personal experience usage?

### Content patterns:
- Data/statistics density per article
- Expert quote format
- Company case study format
- Actionable advice format
- Use of frameworks/models?

### Viral/citable traits:
- What type of conflict opens the best pieces?
- What headline format gets the most traction?
- What type of insight gets reshared most?
- What increases quotability? (short formulas, paradoxes, crisp thesis statements)

## TASK 3: Create supplementary Style Guide

Based on the analysis, create SPECIFIC rules:

```
### SUPPLEMENTARY STYLE GUIDE for {outlet name}
(These rules apply WHERE the media brief is silent. Media brief always takes priority.)

**Headlines:** {pattern}
**Hook:** {pattern}
**Paragraphs:** {length}
**Subheadings:** {frequency and format}
**Tone:** {description}
**Lists:** {format}
**Expert quotes:** {how to present}
**Data points:** {how to embed}
**Conclusion:** {pattern}
**AVOID:** {anti-patterns found}

### TOP-3 TECHNIQUES from the best articles:
1. {technique 1 with example from a specific article}
2. {technique 2 with example}
3. {technique 3 with example}

### VIRAL TRIGGERS to replicate:
1. {trigger with example}
2. {trigger with example}
```

## SAVE (REQUIRED)

Save full report to:
{temp}/agent-style-researcher.md
```

---

### Step 1.4: Quality check (lead)

After all 3 agents complete:
1. Re-read all 3 files from temp folder
2. Check case-hunter: cases for every thesis? ARGUMENT TEST passed? URLs verified? At least one Ivan case per thesis?
3. Check narrative-architect: three hook variants written out? Word budget complete?
4. Check style-researcher: concrete supplementary style guide? Top articles actually analysed?
5. If anything is missing — launch a follow-up agent with a specific request
6. Maximum 1 round of follow-up. Then move on.

Update `_spring-context.md`.

---

## STAGE 2: Build Section Briefs (lead)

### Load context

Re-read all files from temp folder:
1. `00-brief.md`
2. `00-must-include.md`
3. `agent-case-hunter.md`
4. `agent-narrative-architect.md`
5. `agent-style-researcher.md`

### Choose final structure

- Which hook variant (A, B, or C)?
- Section order
- Word budget per section
- Which close variant
- Which supplementary style rules to apply (where the brief is silent)

Log choices in `_decision-log.md`.

### Section Brief for each section

```markdown
## Section Brief: {section title}

**Thesis:** {N} — {title}
**Word budget:** ~{N} words

### SECTION SKELETON (thesis body — verbatim):
{FULL body text of the thesis from 00-brief.md.
Writer takes this as the starting point — polishes it, does NOT rewrite from scratch.
The argument and logic here MUST be recognisable in the final text.}

### MUST-INCLUDE ELEMENTS (from 00-must-include.md):

**DATA (mandatory numbers):**
1. {element — verbatim from 00-must-include.md}
2. {element}

**QUOTE (mandatory quotes — top 2–3):**
1. {Name}: "{quote}" — [URL]
2. {Name}: "{quote}" — [URL]

**CONCEPT (mandatory concepts):**
1. {concept}

**KB (if present):**
1. > "{quote}" — Source: {file path}

**COUNTER (best counterargument):**
1. {counterargument with URL}

### CASES (from case-hunter):

**Ivan's case (use this first):**
{case description with key detail}
Source: {full file path in repository}

**External case (supplementary):**
{case description with outcome}
URL: {link}
Year: {year}

### TRANSITIONS (from narrative-architect):
- From previous section: "{phrase}"
- To next section: "{phrase}"

### STYLE RULES for this section:
{relevant rules from media brief — PRIORITY}
{supplementary rules from style-researcher — where brief is silent}

### IVAN'S VOICE — apply here:
{1–2 specific notes from Ivan's Voice Notes most relevant to this section's argument}

### TOTAL MUST-INCLUDE items: {N}
```

Repeat for every section + Hook + Close.

### Check BODY completeness

⚠️ **Mechanical check — do NOT skip.**

For EACH Section Brief:
1. Open `00-must-include.md`, find the BODY of the corresponding thesis
2. Count SENTENCES in the original BODY
3. Count SENTENCES in the BODY in the Section Brief
4. **If Section Brief has < 80% of original sentences** → add the missing ones back

### Count coverage

Walk through `00-must-include.md` and check: which elements made it into Section Briefs, which didn't.

**Rule:** For deep theses → minimum 75% of elements in briefs. Medium theses → minimum 60%. If coverage is lower — add missing elements or increase word budget.

**DROPPED elements** — list separately with explanation WHY (word limit, duplication, weak element). Log each in `_decision-log.md`.

Save to `{temp}/01-section-briefs.md`. This is the writer's master document.

Update `_spring-context.md`.

---

## STAGE 3: Writer (sequential)

### Agent — "writer" (subagent_type: general-purpose)

**Launch prompt:**
```
You are "writer" for the article "{title}" targeting {outlet}.
Word count target: {N} words. Write entirely in English.

Read in this order before writing anything:
1. {temp}/01-section-briefs.md — MASTER DOCUMENT. Read every word.
2. {temp}/agent-narrative-architect.md — if you need more detail on the narrative
3. {temp}/agent-case-hunter.md — if you need more detail on a specific case

## HOW TO WRITE

### Pass 1: Enrich the skeleton

For each section:
1. Open its Section Brief
2. Take the SECTION SKELETON text as your starting point — this is already the argument
3. Weave in the must-include elements: DATA inline, QUOTE with attribution, CONCEPT naturally
4. Weave in the cases: Ivan's case first (first-person, credibility), then the external case (broader context)
5. Add the transitions between sections
6. The argument from the skeleton MUST be recognisable in your final text — do not replace it with your own reasoning

### ⚠️ ARGUMENT TEST FOR CASES

BEFORE including any case in a section, verify:
1. What is the thesis of this section?
2. What does this case prove?
3. Test: "[thesis]. For example, [case]" — does this sound like PROOF or just RELATED INFORMATION?
If it doesn't prove the thesis → DO NOT INCLUDE. Flag to lead.

### ⚠️ INLINE LINKS — MANDATORY

EVERY source mentioned in the text MUST be wrapped in a markdown link.

Examples:
- Expert quote: `As [Marty Cagan argues](https://url), "product teams need empowerment..."`
- Data: `According to [McKinsey's 2025 report](https://url), 47% of companies...`
- Case: `[Airbnb's pivot in 2020](https://url) showed that constraints can drive innovation.`
- Counterargument: `Critics like [Ben Thompson](https://url) point out that...`

NO "naked" source mentions without a clickable link. If there's no URL — don't mention the source by name.

### ⚠️ SOURCE CREDENTIALING — MANDATORY

When naming a person or organization inline, the reader must IMMEDIATELY understand why they matter. Apply the tier rules from the case-hunter:

**Tier 1 (⭐⭐⭐) — Name + credential inline:**
- ✅ `[Boris Cherny, creator of Claude Code at Anthropic](url)` — reader knows Anthropic + Claude Code
- ✅ `[Elena Verna, Head of Growth at Lovable](url)` — role + company in the link text
- ✅ `[Bessemer Venture Partners, one of Silicon Valley's oldest VC firms](url)` — context for those who don't know BVP

**Tier 2 (⭐⭐) — Publication name + finding:**
- ✅ `[CB Insights' startup failure report](url) found that 42%...` — reader trusts CB Insights
- ✅ `A [First Round Review analysis of 20 PMF stories](url) showed...` — publication carries weight

**Tier 3 (⭐) — Fact only, NO author name:**
- ❌ `[Ahmad Fiaz Jan warns](url) that technical debt...` — WHO? Reader loses trust
- ✅ `Technical debt from AI-generated code can [drop velocity 50-70%](url)` — fact stands on its own

**LINK-THESIS ALIGNMENT CHECK:** Before including ANY link in a section, ask: "Does the CONTENT behind this URL directly support the thesis of THIS section?" If the link is topically adjacent but argues a different point — remove it or move it to the section where it belongs. A link about "AI developer productivity" does NOT belong in a section about "choosing the right customer segment."

### ⚠️ URL VERIFICATION — MANDATORY

BEFORE including ANY URL in the text — verify it via WebFetch:
1. Open URL via WebFetch
2. Confirm the page exists and loads
3. Confirm the content SUPPORTS what you want to cite
4. If URL doesn't load or content doesn't match → DO NOT USE this URL and DO NOT MENTION this source

DO NOT invent URLs. Use only URLs from Section Briefs and agent files.

### Pass 2: Style and voice polish

Apply Style Rules from the Section Brief. Apply Ivan's voice notes.

**The goal:** the article should sound like Ivan wrote it for this outlet. Opinionated. Direct. Grounded in real experience. Not assembled by a committee. Not generated by a model.

**Ivan's voice — apply throughout:**
{paste Ivan's Voice Notes from 00-brief.md here verbatim}

**Suggested phrases from media brief — use naturally where they fit:**
{paste suggested case phrases from 00-brief.md here verbatim}
These phrases must appear in the article. Integrate them so they feel natural, not forced.

**⚠️ NATIVE CREDIBILITY RULE — no overt selling:**

The article must never sell Ivan or his work directly. Credibility is built through:
- Specificity of cases: exact numbers, named teams, real outcomes — not vague references
- Intellectual honesty: moments where the approach didn't work or needed adjustment
- The quality of the argument itself: a reader who finds value will seek out the author

**One permitted soft signal per article:** a single mention of Ivan's context (e.g. "across the 40+ product teams I've worked with") — ONLY if it strengthens the argument. Never as a standalone credential drop. Never more than once.

❌ Banned: "Ivan's methodology", "Ivan's framework", product names, company names, pricing, "book available at…", any call to hire or contact.

**⚠️ FIRST LINE TEST — run for every section:**

Read only the first sentence of each section, ignoring everything before it.
- Does it stand alone — understood without the previous section?
- Does it signal what this section is about?

If the first line depends on context from above → rewrite it to contain its own entry point.
This is critical: readers of Forbes/Inc/HBR skim and jump sections. Every section must be self-sufficient from its opening line.

**BANNED PHRASES — find and delete every instance:**
(See APPENDIX A in the skill file for the full list)
- "In today's rapidly evolving landscape"
- "It's worth noting that" / "It is important to note"
- "Delve into"
- "Leverage" (used metaphorically)
- "Game-changer" / "Paradigm shift" / "Groundbreaking"
- "Navigating the complexities of"
- "In the realm of"
- "Importantly," / "Notably," / "Crucially," as sentence starters
- Three subordinate clauses in a row
- Passive voice where active is possible
- Hedging stacks: "might potentially", "could possibly", "may perhaps"
- "It is essential to understand that"
- "This article will explore"

**WHAT GOOD SOUNDS LIKE — use as calibration:**
- "We tried this with three teams. It didn't work. Here's why."
- "Most product managers get this backwards."
- "The fix isn't complicated. It's just uncomfortable."
- "I've seen this pattern kill products that had everything else right."
- "Here's what nobody tells you."
Short. Direct. Point of view. No hedging.

### Pass 3: Humanity check

Before sending, scan the entire draft against these signals:

**Remove if found:**
- Generic openers without substance ("In today's world…", "It's important to note…")
- Uniform sentence rhythm (all sentences 8–15 words throughout)
- Abstract formulations without an actor ("a decision was made", "optimisation occurred")
- Too-smooth transitions with no conflict or trade-offs
- Paragraphs that could be swapped without losing meaning

**Add if missing:**
- Specific subject of action: who exactly decided, refused, changed approach
- Decision context: when, under what constraint, what was at stake
- Intellectual friction: where the thesis might not work
- **Self-limitation:** one moment where Ivan's own voice acknowledges the boundary of the argument — "this works when X, but breaks down when Y". Not a counterargument from an external source — Ivan himself drawing the limit. This is what separates a trusted expert from a salesperson.
- Markers of live speech: short question, contrast, self-correction

### Self-check before sending

For each section:
- [ ] Skeleton logic preserved and recognisable
- [ ] Must-include DATA/QUOTE/CONCEPT/COUNTER elements present
- [ ] Ivan's case woven in naturally (not appended at the end)
- [ ] External case woven in with verified URL
- [ ] ARGUMENT TEST passed for every case
- [ ] All sources have inline markdown links
- [ ] All URLs verified via WebFetch
- [ ] **SOURCE CREDENTIALING:** every named person has ≤8 word credential inline; no Tier-3 authors named
- [ ] **LINK-THESIS ALIGNMENT:** every URL's content directly supports this section's thesis
- [ ] Transitions in place
- [ ] No banned phrases anywhere
- [ ] Word count close to budget
- [ ] Suggested phrases from brief used where natural
- [ ] No AI-smell patterns (see humanity check above)

### After writing: Collect Sources block

After writing ALL sections, collect a FULL LIST of all mentioned sources at the end.

Walk through EACH section and extract:
1. **Experts and quotes** — each quoted expert + URL
2. **Cases and stories** — each mentioned company/story + URL
3. **Data and statistics** — each number/fact + URL
4. **Books and publications** — if mentioned

⚠️ NO URL = DON'T INCLUDE IN THE LIST.

## SAVE (REQUIRED)

Save draft to: {temp}/02-draft.md

Return a brief summary: word count, sections written, which must-include elements were hard to fit, file path.
```

---

## STAGE 4: Language Review + Humanity Pass (lead)

⚠️ Mandatory stage. Goal: the text must sound like it was written by a sharp native English speaker in the tech/business space — not a non-native speaker, not a language model.

### Step 4.1: Read the draft

Read `02-draft.md` with this lens:

**Naturalness:**
- [ ] Every sentence flows the way a native speaker would actually say it
- [ ] No stiff or over-formal constructions
- [ ] Transitions between paragraphs feel smooth and unforced

**Register — tech/business, smart but not nerdy, not corporate:**
- [ ] Vocabulary is current for 2024–2026 tech/product discourse
- [ ] No dated or overly academic phrases
- [ ] Modern expressions used where they genuinely fit — not forced:
  "ship it", "nail the brief", "move the needle", "in the weeds",
  "directionally right", "table stakes", "pressure-test", "hard no", "earn the right to"
- [ ] No MBA-speak: "synergize", "circle back" (as filler), "bandwidth" for people, "boil the ocean", "low-hanging fruit"

**Rhythm and voice:**
- [ ] Sentence length varies — not all short, not all long
- [ ] Clear point of view throughout, not just information transfer
- [ ] Ivan's voice is present — the article feels authored, not assembled
- [ ] Consistent voice throughout — no tonal shifts

**Brief compliance:**
- [ ] Suggested phrases from the brief are present and sound natural
- [ ] Word count within specified range
- [ ] All explicit brief rules followed (brief > everything else)

**Complexity Pass — Ivan's academic tendency:**
- [ ] Every sentence understood on first read by a smart non-expert (a business manager who has never worked in product)
- [ ] No sentence requires re-reading to parse meaning
- [ ] Technical terms only used if immediately explained in plain language in the same sentence
- [ ] No nested clauses with 3+ concepts in one sentence
- [ ] No academic hedging: "it can be argued that", "one might posit", "it is worth considering"
- [ ] No unexplained acronyms

If any sentence fails → rewrite it. Keep the idea, simplify the delivery. This is not dumbing down — it is precision.

**Humanity Pass** (see APPENDIX C for full checklist):
- [ ] No AI-smell patterns (generic openers, uniform rhythm, abstract actors)
- [ ] Human signals present (specific actors, decision context, intellectual friction)
- [ ] Rhythm varies — mix of short and long sentences in every section
- [ ] Source integrity — every external fact has a URL, every quote has a source

**Score Humanity Risk (0–100):**
- +20: many template AI phrases
- +20: text too uniform in rhythm
- +20: weak specificity (few names/numbers/context)
- +20: no counterarguments/limitations
- +20: claims without sources

Target: ≤ 20. If 21–40: targeted rewrite. If 41+: full humanisation pass needed.

### Step 4.2: Fix issues

**Fewer than 5 issues** — fix directly, save as `03-draft-reviewed.md`.

**Systemic issues** (whole sections feel stiff or generic) — launch language-reviewer agent:

```
You are "language-reviewer" for the article "{title}".

Read: {temp}/02-draft.md
Also read Ivan's Voice Notes from: {temp}/00-brief.md

YOUR TASK: Rewrite this article so it sounds like Ivan Zamesin wrote it for {outlet}.
Direct. Experienced. Opinionated. Grounded in real practice.
Think: the voice you hear in First Round Review, Lenny's Newsletter, or a great Hacker News post.
Smart and accessible. Not academic. Not corporate. Not AI.

RULES:
- Keep all arguments, theses, cases, and facts exactly as they are
- Keep all inline markdown links exactly as they are
- Only change the language: word choice, sentence structure, rhythm, transitions
- Apply Ivan's voice patterns from the Voice Notes
- Vary sentence length deliberately — a complex idea followed by a short punchy sentence
- Use first person ("I", "we") and direct address ("you") where the outlet allows it

BANNED — enforce strictly, find and remove every instance:
(See APPENDIX A in the skill file)

WHAT GOOD SOUNDS LIKE:
(See APPENDIX B in the skill file)

HUMANITY CHECK:
- Remove: generic openers, uniform rhythm, abstract actors, too-smooth transitions, swappable paragraphs
- Add: specific actors, decision context, intellectual friction, live speech markers

Save reviewed version to: {temp}/03-draft-reviewed.md
Return: main changes made + word count + Humanity Risk score + file path.
```

Update `_spring-context.md`.

---

## STAGE 5: Two-level verification (lead)

⚠️ **Critical step. Do NOT skip.**

### Load context

Re-read ALL THREE files:
1. `00-must-include.md` — ORIGINAL elements from theses (full set)
2. `01-section-briefs.md` — Section Briefs (filtered set)
3. `03-draft-reviewed.md` — the draft (or `02-draft.md` if no language review was needed)

### LEVEL 1: Check BODY preservation (PRIORITY #1)

For EACH thesis:

1. **Read the FULL BODY text from `00-must-include.md`** (NOT from section briefs!)
2. **Find the corresponding section** in the draft
3. **Walk through each SENTENCE of the Body** and check: is this argument/idea present in the section?
4. **Create a BODY checklist:**

```
### BODY of Thesis {N}: {title}
- [x] / [ ] Argument 1: "{first key claim from Body}"
- [x] / [ ] Argument 2: "{second}"
...
- Preserved: {X}/{Y} arguments ({%})
```

**If < 70% of Body arguments preserved** → `[BODY DISTORTED]` — section must be REWRITTEN starting from the full Body.

### LEVEL 2: Element-by-element check (DATA/QUOTE/CONCEPT/KB/COUNTER)

For EACH element in `00-must-include.md`:

1. **Element in section briefs AND in draft** → `[x] IN BRIEF + IN DRAFT`
2. **Element in section briefs but NOT in draft** → `[MISSING FROM DRAFT]`
3. **Element NOT in section briefs AND NOT in draft** → `[DROPPED AT BRIEF]`
4. **Element NOT in section briefs but IS in draft** → `[x] BONUS`

### LEVEL 3: Case relevance and URL verification

#### Step 5.1: ARGUMENT TEST for every case in the draft

For EACH case/story/example in the draft:

1. Identify the **thesis of the section**
2. Identify **what the case proves**
3. Test: "[thesis]. For example, [case]" — PROOF or RELATED INFORMATION?

```
### Case: {description}
- Section thesis: "{thesis summary}"
- Case proves: "{what it proves}"
- ARGUMENT TEST: ✅ PROVES / ❌ TOPICALLY CLOSE BUT DOESN'T ARGUE
```

**If case fails ARGUMENT TEST** → `[IRRELEVANT CASE]` — must REPLACE or REMOVE.

#### Step 5.2: Verify ALL URLs via WebFetch

For EACH URL in the draft:

1. Open via WebFetch
2. Check: page exists? Content confirms the citation/fact/case?
3. Record:

```
- [✅/❌] {URL} — {what the article claims} → {what's actually on the page}
```

**If URL doesn't load or content doesn't match** → `[BAD URL]` — REMOVE the link and source mention (or replace with a verified one).

### Step 5.3: Fix issues

**Priority 0 — `[IRRELEVANT CASE]` and `[BAD URL]`:**
Replace irrelevant cases (search via WebSearch). Remove broken/irrelevant links.

**Priority 1 — `[BODY DISTORTED]`:**
Rewrite the section, starting from the full Body text in `00-must-include.md`.

**Priority 2 — `[MISSING FROM DRAFT]`:**
If < 5 — add directly. If ≥ 5 — launch writer agent with specific list.

**Priority 3 — `[DROPPED AT BRIEF]`:**
Review whether top-3 dropped elements can be restored. If word budget allows — add them.

### LEVEL 3.5: Source quality and credentialing check

For EACH named source (person or organization) in the draft:

1. **Is the source Tier 1, 2, or 3?**
2. **If named inline — does the reader know who they are?**
   - Is there a credential in the link text or surrounding sentence? (role, company, achievement)
   - Would a smart generalist reader say "I know why this person matters" after reading the sentence?
3. **LINK-THESIS ALIGNMENT:** Does the content behind this URL directly argue the thesis of its section?

```
### Source: {name}
- Tier: ⭐⭐⭐ / ⭐⭐ / ⭐
- Credential present inline: ✅ / ❌
- Link-thesis alignment: ✅ ARGUES / ❌ TOPICALLY ADJACENT
```

**Violations:**
- `[UNCREDENTIALED SOURCE]` — named person with no context → add credential or remove name
- `[TIER 3 NAMED]` — unknown author cited by name → remove name, keep fact
- `[LINK MISALIGNED]` — URL content doesn't argue the section's thesis → remove or relocate
- `[ORPHAN CREDENTIAL]` — org mentioned without explaining what it is (e.g. "Bessemer" without "VC firm") → add context

**Fix all violations before proceeding to LEVEL 4.**

### LEVEL 4: "So what?" check

For EACH section in the draft, ask: **"So what does this mean for the reader — practically, today?"**

The answer must appear explicitly in the text of that section — not implied, not left for the reader to infer. It can be one sentence. It must be there.

```
### So What — Section: {title}
- Reader takeaway present in text: ✅ / ❌
- Where: "{exact sentence or phrase that answers So What}"
- If ❌: add a closing sentence to this section before proceeding
```

**If any section has no explicit "so what" → `[NO SO WHAT]` — add it before Stage 5.5.**

### Step 5.4: Brief compliance check

Read the entire text and verify:
- Matches the tone prescribed by the media brief?
- Word count within specified range?
- All explicit brief rules followed?
- Suggested phrases from brief used naturally?
- Style-researcher supplementary rules applied where brief was silent?

### Save verification results

Save to `{temp}/04-quality-report.md`:

```markdown
## Verification Results

### LEVEL 1: Body preservation
| Thesis | Arguments in Body | Preserved | % |
|--------|-------------------|-----------|---|
| T1     | {N}               | {M}       | {%} |
...
| TOTAL  | {N}               | {M}       | {%} |

### LEVEL 2: Element coverage
- Total elements in 00-must-include: {N}
- IN BRIEF + IN DRAFT [x]: {N}
- MISSING FROM DRAFT: {N} (fixed: {N})
- DROPPED AT BRIEF: {N}
- Coverage from ORIGINAL: {%}
- Coverage from BRIEFS: {%}

### LEVEL 3: Case relevance and URLs
- Total cases in draft: {N}
- ARGUMENT TEST passed ✅: {N}
- IRRELEVANT CASE ❌: {N} (replaced: {N})
- Total URLs in draft: {N}
- URLs verified ✅: {N}
- BAD URL ❌: {N} (removed/replaced: {N})

### LEVEL 3.5: Source quality
- Total named sources in draft: {N}
- Tier 1 (⭐⭐⭐): {N} — all credentialed inline ✅/❌
- Tier 2 (⭐⭐): {N} — publication named ✅/❌
- Tier 3 (⭐): {N} — NONE named by author ✅ / {N} violations ❌
- UNCREDENTIALED SOURCE: {N} (fixed: {N})
- TIER 3 NAMED: {N} (fixed: {N})
- LINK MISALIGNED: {N} (fixed: {N})
- ORPHAN CREDENTIAL: {N} (fixed: {N})

### Humanity Risk: {score}/100

### Brief compliance: {pass/fail with notes}
```

**Thresholds:** Body coverage ≥ 70% for EACH thesis. Brief coverage ≥ 90%. ARGUMENT TEST — 100% cases must pass. BAD URL — 0 in final draft. UNCREDENTIALED SOURCE — 0 in final draft. TIER 3 NAMED — 0 in final draft. LINK MISALIGNED — 0 in final draft. Humanity Risk ≤ 20.

Update `_spring-context.md`.

---

## STAGE 5.5: Generate 10 title variants (lead)

### Load context

Re-read `03-draft-reviewed.md` and `agent-style-researcher.md`.

### Step 5.5.1: Generate 10 titles

Based on the FINISHED draft (not theses!) and the outlet's style, generate **10 DIFFERENT titles**.

**Rules:**
- Each title is a SEPARATE angle on the topic (not variations of one phrasing!)
- Follow the outlet's headline patterns from the style-researcher
- Titles must hook the target audience

**Use DIFFERENT title types:**

| Type | Approach | Count |
|------|----------|-------|
| **Provocation / challenge** | Challenges a common belief | 2 |
| **How-to / practical** | Promises a concrete outcome | 2 |
| **Numbers / data** | Leads with a stat or number | 1–2 |
| **Question** | Asks a question the reader wants answered | 1–2 |
| **Metaphor / analogy** | Unexpected comparison | 1 |
| **Prediction / trend** | "The future of X looks like…" | 1 |
| **Personal experience** | "What I learned when…" | 1 |

### Step 5.5.2: Show author and ask to choose

Display all 10 titles as a numbered list with type labels:

```
## 10 title variants:

1. {title} — [Provocation]
2. {title} — [How-to]
...
10. {title} — [Personal experience]
```

**Ask via AskUserQuestion:**

"Which title do you prefer? You can pick a number, combine several, or suggest your own."

Options:
- "Pick from the list" — "Specify the number (or several numbers to combine) in the text field"
- "I'll suggest my own" — "Write your title or direction, and I'll refine it"
- "Generate 10 more" — "These don't work, need different options"

**Do NOT proceed without a title choice.**

---

## STAGE 6: Create final output file

### Load context

Re-read `_spring-context.md` and `03-draft-reviewed.md`.

Create the file at:
```
{DRAFT_DIR}/PR-{Outlet}-{Article-Slug}.md
```

---

## Output file format

```markdown
---
## 📝 Notes before sending to editor

> *[Ivan or PR manager fills this in before submitting to the outlet]*
> *[Write here what needs to change in the next iteration]*

---

# {Chosen article title}

> **Status:** Draft
> **Outlet:** {name}
> **Word count:** ~{N}
> **Date:** {YYYY-MM-DD HH:MM}
> **Theses:** {N}
> **Must-include coverage:** {N}/{M} ({%})
> **Humanity Risk:** {score}/100
> **Ivan's cases used:** {N}
> **External cases used:** {N}
> **Mode:** Agent Team (case-hunter, narrative-architect, style-researcher, writer)

---

{Article text with inline markdown links}

---

## Sources

### Experts and quotes
1. [{Expert name}]({URL}) — "{brief quote summary}"

### Cases and stories
1. [{Company/person — case title}]({URL}) — {year}

### Data and statistics
1. [{Data source}]({URL}) — "{which number/fact}"

### Ivan's cases (from repository)
- {file path} — {what was used}

### Books and publications
1. {Author} — "{Title}", {year}
```

---

## ITERATION MODE (I1–I3)

When the author reads the draft and provides feedback (in the "Notes before sending to editor" field or as a message):

### I1: Parse feedback

Classify each point:

- **Light:** rephrase, shorten, rearrange, tweak tone
- **Deep:** add new case, strengthen argument, check freshness, change angle for audience segment

### I2: Choose strategy

- Only **Light** → edit the draft directly
- Has **Deep** → targeted data fetch:
  - from theses/temp files
  - or via WebSearch for a specific question

Do NOT relaunch the full pipeline unless necessary.

### I3: Update draft in-place

- Update text and metadata (date, iteration number)
- Clear the "Notes before sending to editor" field back to placeholder
- Log changes in `_decision-log.md`
- Run a targeted verification on changed sections (Stage 5 logic, but only for affected sections)

---

## Full quality checklist

### Inputs and setup
- [ ] Both inputs present: theses file + media brief
- [ ] Theses not reinterpreted, not changed, not added to
- [ ] Ivan's voice extracted from book chapters and documented in `00-brief.md`
- [ ] Must-include elements extracted from ALL theses into `00-must-include.md`
- [ ] Word budget check passed (or resolution logged)
- [ ] Suggested phrases from brief copied verbatim and passed through pipeline

### Agent work
- [ ] style-researcher: supplementary style guide with concrete rules (does not override brief)
- [ ] case-hunter: cases for each thesis with URLs, ARGUMENT TEST + PERCEPTION CHECK passed, URLs verified
- [ ] narrative-architect: "why now" + memorable moment identified + 3 hook variants + transitions + 3 close variants + word budget

### Section Briefs
- [ ] Every thesis has its own section (or explicit merge with author approval)
- [ ] BODY completeness ≥ 80% for each thesis
- [ ] Element coverage ≥ 60% (medium) / ≥ 75% (deep)
- [ ] DROPPED elements listed with reasons

### Draft quality
- [ ] Writer did three-pass polish: enrich skeleton → style and voice → humanity check
- [ ] All sources have inline markdown links
- [ ] All URLs verified via WebFetch
- [ ] ARGUMENT TEST + PERCEPTION CHECK passed for every case
- [ ] NATIVE CREDIBILITY RULE followed — zero overt selling, max one soft signal
- [ ] FIRST LINE TEST passed for every section — each opens independently
- [ ] Self-limitation present — Ivan draws the boundary of his own argument in his voice
- [ ] Memorable moment present and not diluted
- [ ] Language review done — sounds like Ivan, reads as native English, no AI patterns
- [ ] COMPLEXITY PASS done — every sentence understood on first read
- [ ] Humanity Risk ≤ 20

### Verification
- [ ] LEVEL 1: Body preservation ≥ 70% for each thesis
- [ ] LEVEL 2: Brief coverage ≥ 90%
- [ ] LEVEL 3: 0 irrelevant cases, 0 bad URLs
- [ ] LEVEL 3.5: 0 uncredentialed sources, 0 Tier-3 authors named, 0 misaligned links, 0 orphan credentials
- [ ] LEVEL 4: "So what?" explicit in every section

### Brief compliance
- [ ] Matches tone from media brief
- [ ] Word count within specified range
- [ ] Suggested phrases used naturally
- [ ] All explicit brief rules followed (brief > everything else)

### Title
- [ ] 10 title variants shown to author
- [ ] Author chose a title
- [ ] Chosen title used in the final file

### Decision trail
- [ ] `_decision-log.md` has entries for budget check, dropped elements, fixes

---

## APPENDIX A: Banned Phrases

Find and delete every instance. Apply in writer prompt, language review, and final check.

- "In today's rapidly evolving landscape"
- "It's worth noting that" / "It is important to note"
- "Delve into"
- "Leverage" (used metaphorically)
- "Game-changer" / "Paradigm shift" / "Groundbreaking"
- "Navigating the complexities of"
- "In the realm of"
- "Importantly," / "Notably," / "Crucially," as sentence starters
- Three subordinate clauses in a row
- Passive voice where active is possible
- Hedging stacks: "might potentially", "could possibly", "may perhaps"
- "It is essential to understand that"
- "This article will explore"
- "In today's world" / "In an era of"
- "It cannot be overstated"
- "At the end of the day"
- "Moving forward"

---

## APPENDIX B: What Good English Sounds Like

Use as calibration for writer, language-reviewer, and final check.

- "We tried this with three teams. It didn't work. Here's why."
- "Most product managers get this backwards."
- "The fix isn't complicated. It's just uncomfortable."
- "I've seen this pattern kill products that had everything else right."
- "Here's what nobody tells you."
- "This sounds obvious. It isn't."
- "The data says one thing. The org does the opposite."
- "Every PM I've coached hits this wall around month three."

Short. Direct. Point of view. No hedging. Specific. Grounded in experience.

---

## APPENDIX C: Humanity Pass Checklist

Run after the first complete draft. Score Humanity Risk (0–100).

### 1) AI-smell patterns (remove/rewrite)

- Generic openers without substance: "In today's world", "It's important to note", "One cannot underestimate"
- Uniform rhythm: same sentence length (8–15 words) throughout the text
- Abstract formulations without an actor: "a decision was made", "optimisation occurred"
- Too-smooth transitions without conflict or trade-offs
- Paragraphs that can be swapped without losing meaning

### 2) Human signal amplifiers (add)

- Specific subject of action: who exactly decided, refused, changed approach
- Decision context: when, under what constraint, what was at stake
- Intellectual friction: where the thesis might not work
- Markers of live speech: short question, contrast, self-correction

### 3) Rhythm and readability

- Every section has a mix of short and long sentences
- No overload of nominalisations and corporate-speak
- Subheadings carry meaning, not just decorative labels

### 4) Source integrity

- Every external fact has a URL
- Every direct quote has a primary source
- No claims like "research shows" without a link

### 5) Humanity Risk scoring

- +20: many template AI phrases
- +20: text too uniform in rhythm
- +20: weak specificity (few names/numbers/context)
- +20: no counterarguments/limitations
- +20: claims without sources

Interpretation:
- 0–20: OK for publication
- 21–40: targeted rewrite needed
- 41+: full humanisation pass by section

---

## APPENDIX D: Style Fingerprint Template

Use for `agent-style-researcher.md` when documenting the outlet's style.

```markdown
## Publication Profile

- Outlet:
- Domain:
- Corpus (N articles analysed):
- Period:

## Signal Pack Summary

| # | Article | URL | Date | Popularity signal | Notes |
|---|---------|-----|------|-------------------|-------|

## Tone Of Voice

- Formality (1–10):
- Voice: (1st person / 2nd person / neutral)
- Expert vs conversational:
- Emotional range:
- Typical author stance (mentor / operator / researcher):

## Structural Patterns

- Headline types:
- Hook format:
- Average paragraph length:
- Subheading frequency:
- List usage:
- Conclusion format:

## Viral/Citable Traits

- Recurring "share triggers":
- Recurring "quotable units":
- Common conflict type in opening paragraphs:
- How insights are framed (model / rule / paradox):

## Best Practices To Reuse

1.
2.
3.
4.
5.

## Anti-Patterns To Avoid

1.
2.
3.
4.
5.

## Supplementary Style Rules For Draft

(Apply where the media brief is silent)

- Headlines:
- Hook:
- Paragraphs:
- Subheadings:
- Tone:
- Quotes:
- Data:
- Conclusion:

## Confidence & Gaps

- Confidence (0–100):
- Signals that couldn't be confirmed:
- What to check additionally in iteration:
```
