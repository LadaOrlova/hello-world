---
name: linkedin-post
description: Create a viral LinkedIn post following LinkedIn Growth Sprint methodology. Guides the author through questions, generates theses with counterarguments, writes the post, and generates a New Yorker-style editorial illustration via OpenRouter API.
user-invocable: true
---

# Skill: LinkedIn Post Creator

This skill guides the author through creating a high-engagement LinkedIn post using the LinkedIn Growth Sprint methodology. It collects context, generates theses with counterarguments, writes the post, and creates an editorial illustration.

**Language: ALWAYS English.** All posts are written in English for the US market.

---

## KNOWLEDGE BASE: Target Segments and Their Jobs

Use these segments and jobs when crafting posts. The author's audience consists of:

### Segment 1: Corporate Product People — "Earn trust from leadership"

**Who:** PM, Product Marketing Managers, Heads of Digital, Innovation Managers at large companies (banking, retail, insurance, telecom, health). They have a boss above them they need to convince. Often work in matrix structures.

**Core Jobs:**
- WHEN decisions in my org are made "by gut feeling" → I WANT a clear decision-making logic with strong arguments and show great execution → SO THAT my manager trusts every word I say
- WHEN launching a new initiative inside a bank/retail/telecom → I WANT a strong, evidence-based strategy → SO THAT I can offer an alternative to stakeholder gut instinct

**Big Job:** Become the person everyone listens to as a product and strategy expert, to influence decisions and advance my career.

### Segment 2: Product-Lead of a Stagnating Product

**Who:** Senior PM, Group PM, Head of Product at startups and scale-ups (20-500 employees). Own MRR/GMV/retention, talk to founders and investors. US/Canada, remote/hybrid. In 2025-2026 their biggest pain is decision-making and ambitions crushed by founder mode.

**Core Jobs:**
- WHEN my SaaS/app hits a plateau → I WANT to find new growth levers (segments, value, monetization) → SO THAT I break through stagnation and show results
- WHEN I need to create a strategy and roadmap, show execution to founder → I WANT to build strategy on facts and arguments, not gut feeling → SO THAT the founder trusts my process
- WHEN I work in a company but think about my own product → I WANT a strong methodological foundation → SO THAT I have competitive advantage when I go independent

**Big Job:** "Unfreeze" the product and prove I can find growth, to strengthen my leader position and move toward VP Product/CPTO.

### Segment 3: Founder 0→1 with Failed Startups Behind

**Who:** Founders and co-founders at pre-seed/seed, indie hackers. Already launched 1-3 products and lost money/time. Feel "too much chaos." First-time founders who understand they might make a mistake. SF, NYC, Austin, and online communities.

**Core Jobs:**
- WHEN I have a new idea and 1-2 failed launches behind me → I WANT a clear algorithm of actions → SO THAT I launch MVP without wasting a year on a bad idea
- WHEN I have a new idea and previous experience → I WANT to separate relevant from irrelevant experience → SO THAT I don't repeat mistakes
- WHEN investing my own or investor money → I WANT to calculate unit economics and risks upfront → SO THAT I don't burn the budget in a year
- WHEN the product reaches first users → I WANT to quickly read signals from metrics and interviews → SO THAT I can change course before money runs out

**Big Job:** Build a repeatable "launch machine" so that from a series of digital products I grow a sustainable business and don't go in circles of the same mistakes. Don't waste a year of my life on a bad idea during the AI gold rush.

### Segment 4: VC Funds and Angel Investors

**Who:** VC representatives, angel investors. Constantly review pitches and metrics. Looking for ways to calibrate team quality, founder adequacy. Evaluate "idea viability," spot red flags.

**Core Jobs:**
- WHEN looking at a new startup to invest in → I WANT a structured way to assess team quality → SO THAT I minimize risks and don't miss red flags
- WHEN conducting due diligence → I WANT to understand the team's product competency level → SO THAT I can assess the probability of successful scaling
- WHEN analyzing the business model and PMF → I WANT a framework for evaluating idea viability → SO THAT I can distinguish promising projects from doomed ones

**Big Job:** Improve the quality of investment decisions and help portfolio companies grow faster through a unified methodological framework.

---

## KNOWLEDGE BASE: LinkedIn Growth Sprint Rules

These rules MUST be followed when writing posts:

### Post Structure (mandatory)
1. **Hook (first 2 lines)** — the ONLY thing visible before "See more". No long intros, straight to the point.
2. **Scannable body** — people scan first, then read. Wall of text = 0 reach, even if expert-level.
3. **Paragraphs mandatory** — LinkedIn evaluates structure in initial post scoring.
4. **Address reader as "you"** — creates emotional connection.
5. **CTA at the end** — always specify what you want from people.

### Hook Rules
- Hook = first 2 lines (before "See more"). No exceptions.
- No universal templates — hooks go stale fast.
- All "top 10 LinkedIn hooks" lists from the internet are already dead.
- Numeric hooks work consistently: "3 mistakes that cost me $20K", "7 ways to cut marketing spend"
- Generate 5+ variants, pick the best. Edit the hook in the first hour if the post isn't performing.

### Formatting Rules
- **Paragraphs mandatory** — LinkedIn scores structure.
- **Scannability** — bullets, lists, short blocks.
- **Numbered headings work**: "3 mistakes...", "7 ways...", "5 prompts..."
- **Wall of text = post death** — even a super-expert post won't get reach.
- Each thought = separate paragraph.
- Short paragraphs: 1-3 sentences max (as seen in viral posts by Justin Welsh, Lenny Rachitsky).

### Content Formats (ranked by effectiveness)
1. **Text + photo** — MOST effective. "If you don't know what to use — text + photo."
2. **Carousels** (PDF/infographic) — 9 slides optimal. Canva. Numbered headings.
3. **Video** — vertical, subtitles mandatory, under 1 min, text explanation required.
4. **Pure text** — LinkedIn "likes it less" formally, but works in practice. Better than text + cringe AI image.

### Four Viral Topics
1. **Professional journey** — career timeline, key milestones, achievements.
2. **Money, earnings, numbers** — "Everyone loves reading about money."
3. **Advice to myself X years ago** — "What I wish I knew before..."
4. **Before/After** — photo collage, powerful visual emotion.

### Two Content Types
1. **Useful content** — reader thinks "wow, that's useful" (saves/reposts).
2. **Positive content** — triggers positive emotions, energizes. "Positive emotions from content = positive emotions toward product."

### Product Integration Levels
1. **Post-script after virality** — publish WITHOUT link. If it goes viral → edit after 1-2 hours, add CTA with link.
2. **Links in profile only** — "Visit my website" button, Description, Featured, About all lead to product.
3. **Native story integration (best conversion)** — personal story where product is organically woven into narrative. Converts **5-10x better** than post-script.
4. **No integration** — pure value/brand building post.

### What NOT to Do
- Don't get into politics or flame wars.
- Don't write content about your product directly — write what's interesting to TA, integrate product natively.
- Don't use AI-generated images — worse than stock photos, cringe.
- Don't use photos unrelated to text — cognitive dissonance.
- Don't do bare reposts — kills reach instantly.

---

## KNOWLEDGE BASE: Viral Post Patterns (from live LinkedIn research, Feb 2026)

### Pattern 1: Numbered Takeaway List (Lenny Rachitsky — 2,825 reactions)
```
Hook: "My biggest takeaways from [Expert Name] ([Role]):"
Body: Numbered list (1-8 items). Each item: bold claim + 2-3 sentences + direct quote.
CTA: Question to audience or link to full interview.
```
**Why it works:** Curated expert knowledge, easy to scan, high save/repost rate.

### Pattern 2: Emotional Hook + Short Paragraphs (Justin Welsh — 1,263 reactions)
```
Hook: "I think you already know the best thing you can do for your business. You know how I know it?"
Body: 1-2 sentence paragraphs. Emotional resonance → bullet list of examples → challenge → wisdom.
CTA: Free resource + link.
```
**Why it works:** Direct "you" address, vulnerability, relatable examples, soft CTA after full value.

### Pattern 3: Bold Provocative Statement (Justin Welsh — high engagement)
```
Hook: "One person with a laptop is about to outcompete companies with 50 employees."
Body: Acknowledge skepticism → evidence → anaphora ("AI builds... AI writes... AI designs...") →
      key insight → contrast (they vs you) → urgency → CTA.
```
**Why it works:** Bold claim triggers curiosity, anaphora creates rhythm, contrast empowers reader.

### Pattern 4: Identity Recognition Hook (Nina Churchill — 609 reactions)
```
Hook: "[Role] is such a weird job"
Body: List of contradictions and relatable situations the role faces.
CTA: "What would you add?"
```
**Why it works:** Role-identity validation triggers emotional response and comments.

### Pattern 5: Lessons Learned List (arrow bullets)
```
Hook: "If you're building a company, here's what I've learned after X years in the game:"
Body: Arrow-bulleted lessons (→), each one punchy and quotable.
CTA: "What lesson took you the longest to learn?"
```
**Why it works:** Authority through experience, scannable, comment-triggering question.

---

## WORKFLOW: Step-by-Step Post Creation

### INITIAL ROUND — All Questions At Once

Collect ALL input from the author in ONE round. No "are you ready?" or "shall I write?" — go straight to collecting information.

This round has 2 parts that happen back-to-back with NO processing between them.

#### Part A: Structured Questions (AskUserQuestion, 4 questions)

Ask these 4 questions in a SINGLE AskUserQuestion call:

**Question 1 — Target Audience:**
"Who is the primary audience for this post?"
Options:
- Founders & indie hackers
- Product managers & product leaders
- Marketers & growth people
- Engineers & technical leaders

**Question 2 — Content Type:**
"What type of value should the post deliver?"
Options:
- Useful (reader learns something new) (Recommended)
- Positive (energizes, inspires)
- Both useful and positive

**Question 3 — Product Integration:**
"How should the product/service be integrated?"
Options:
- Native story (product woven into narrative — best conversion)
- Post-script at the bottom (add CTA if post goes viral)
- Links in profile only (no mention in post)
- No integration (pure brand/value post)

**Question 4 — Content Format:**
"What format should the post be?"
Options:
- Text + photo (Recommended)
- Carousel (PDF slides)
- Pure text
- Text + video reference

#### Part B: Raw Content + Reference (AskUserQuestion, 3 questions)

IMMEDIATELY after Part A (no processing), ask these 3 questions:

**Question 1 — Raw Content:**
"What is the post about? Dump your raw stream of consciousness — a story, insight, observation, case study, numbers, lesson learned. The more detail, the better."
Options:
- Story / personal journey
- Framework / methodology / insight
- Numbers / results / case study
- Lesson learned / advice

NOTE: The author will likely select "Other" and type their full raw thoughts. The options are just conversation starters. If the author picks an option without detail, ask ONE follow-up to get more substance.

**Question 2 — Reference Post:**
"Do you have a reference LinkedIn post that inspired you? Paste it or describe it."
Options:
- No reference, skip
- I'll paste it (use text field)

**Question 3 — Business Goals (multiSelect: true):**
"What business goals should this post achieve? (select all that apply)"
Options:
- Maximum reach (likes, comments, reposts)
- Warm up audience for future product
- Give massive value to subscribers
- Product/service sales or signups

After Part B, Claude has ALL the input needed. Proceed directly to thesis extraction.

**Viral topic angle** is NOT asked — Claude infers the best angle (professional journey / money & numbers / advice to past self / before-after) from the raw content. If ambiguous, Claude picks the strongest match.

---

### THESIS STAGE — Extract, Enrich, and Challenge Ideas (Deep Research)

This stage uses **gpt-5.2-pro (Deep Research)** to enrich theses with expert opinions, counterarguments, first principles analysis, and similar theses from the web. Two parallel tracks: DR web research + Claude analysis.

#### Step 1: Extract raw theses (Claude)

For each idea in the author's stream of consciousness:
- Extract it as a 2-5 sentence thesis statement (DETAILED, not compressed)
- Extract ALL explicit and implicit ideas
- Keep the author's voice and energy
- Note any examples, numbers, or references mentioned

Display extracted theses to the author and save to temp file.

#### Step 2: Create temp directory and save raw theses

```bash
mkdir -p .claude/temp/linkedin-{slug}/
```

Save extracted theses to: `temp-dir/01-raw-theses.md`

#### Step 3: Generate DR prompt and launch Deep Research (BACKGROUND)

Build a prompt for Deep Research based on the template below. Save to `temp-dir/dr-prompt.md`.

Launch via Bash with `run_in_background=true`:
```bash
python3 8-Prompts-and-Scripts/scripts/deep-research-call.py \
  "{temp-dir}/dr-prompt.md" \
  "{temp-dir}/agent-deep-research.md" \
  --model gpt-5.2-pro \
  --effort high
```

⚠️ Deep Research may take 3-10 minutes. While it runs, proceed to Step 4.

---

##### DR PROMPT TEMPLATE FOR LINKEDIN POST

```
# Deep Research: Thesis enrichment for LinkedIn post

## ROLE

You are a world-class content strategist at the intersection of technology, product management, and business strategy. Your level: Ben Thompson (Stratechery) + Lenny Rachitsky + Paul Graham + Shreyas Doshi.

## CONTEXT

The author is writing a LinkedIn post for product managers, product leaders, founders, and engineers. The post should deliver sharp, useful insights that make readers stop scrolling.

**Target audience:** {selected audience}
**Topic angle:** {inferred viral topic angle}
**Content type:** {useful / positive / both}

## AUTHOR'S RAW THESES

{ALL extracted theses from Step 1, numbered, each 2-5 sentences}

## YOUR TASKS

### TASK 1: Expert opinions and similar theses

For EACH author thesis:
1. Find 2-3 FRESH expert opinions (2024-2026) that SUPPORT or EXTEND the thesis — with real URLs
2. Find similar theses from thought leaders — who said something similar and how?
3. Note how the thesis connects to broader industry trends

Priority experts: Lenny Rachitsky, Shreyas Doshi, Paul Graham, Marty Cagan, April Dunford, Brian Chesky, a16z, Reforge, First Round Review, Y Combinator, Ben Thompson.

### TASK 2: Counterarguments

For EACH author thesis:
1. Find 1-2 STRONG counterarguments — who disagrees and why? With real URLs.
2. These counterarguments should be useful: they help the author anticipate reader objections and strengthen the post.

### TASK 3: First Principles Analysis

Analyze the post's core topic from first principles:
1. **Identify axioms** — what has become free or near-free that makes this thesis true?
   (e.g., code writing ≈ $0, research ≈ $0, prototyping ≈ $0, distribution via agents ≈ $0)
2. **Build logical chains:** If X is free → what follows? → what follows from that? → NON-OBVIOUS conclusion
3. **Derive 2-3 NEW theses** that the author didn't mention but logically follow from the same axioms

### TASK 4: New theses suggestions

Based on Tasks 1-3, suggest 3-5 NEW theses that:
- The author didn't mention but should consider for the post
- Are NON-OBVIOUS (not the first thing you'd think of)
- Pass the relevance test: "Would removing this weaken the post?"
- Are specific enough for a LinkedIn post (not abstract philosophy)

For each new thesis: name, 2-3 sentences, source expert/URL, why the author might have missed it.

## OUTPUT FORMAT

### Part A: Enriched Author Theses

For EACH author thesis:
---
### Author Thesis {N}: "{name}"

**Expert support:**
- [Expert] (Tier, Year): "[opinion]" — URL
- [Expert] (Tier, Year): "[opinion]" — URL

**Similar theses from thought leaders:**
- [Who] said: "[what]" — URL

**Counterarguments:**
- [Source]: "[counterargument]" — URL

**First Principles deepening:**
Axiom: [what's free] → [chain] → [non-obvious conclusion]

---

### Part B: New Thesis Suggestions

For EACH new thesis:
---
### 🆕 New Thesis: "{name}"
**Idea:** [2-3 sentences]
**Source:** [expert/research] — URL
**Why author may have missed it:** [explanation]
**Connects to author thesis:** [which one and how]

---

### Part C: Key Debates
Where experts DISAGREE on the topic — useful for making the post more nuanced.

## QUALITY RULES
- Every source MUST have a real URL (don't invent!)
- Priority: 2025-2026 sources > 2024 > older
- Language: ENGLISH (the post is for the US market)
- Focus: depth > breadth. Better 3 deep insights than 10 shallow ones.
```

#### Step 4: Claude's own analysis (PARALLEL with DR)

While DR is running, Claude analyzes the theses:
1. Generate counterarguments for each thesis (sharp, 1-2 sentences)
2. Identify which theses are strongest/weakest for LinkedIn engagement
3. Suggest thesis ordering for maximum impact

#### Step 5: Wait for DR results and synthesize

1. Read `temp-dir/agent-deep-research.md` when DR completes
2. Merge DR insights with Claude's analysis
3. For each thesis, compile: thesis + expert opinions + counterarguments + first principles deepening

#### Step 6: Display enriched theses to author

Format:
```
## Enriched Theses

### T1: [thesis statement]
   👥 Experts: [who agrees, 1-line summary]
   ⚡ Counterargument: [strongest counter, 1 line]
   🔬 First Principles: [axiom → chain → non-obvious conclusion]

### T2: [thesis statement]
   👥 Experts: [who agrees]
   ⚡ Counterargument: [strongest counter]
   🔬 First Principles: [deepening]

...

### 🆕 New thesis suggestions from research:
N1: [new thesis from DR]
N2: [new thesis from DR]
...
```

#### Step 7: Ask the author which theses to keep

Use AskUserQuestion:
"Which theses should make it into the post? Type the numbers to keep (e.g., 'T1, T3, N2'). Or 'all' to keep everything."

---

### HOOK GENERATION STAGE

Based on selected theses + all context from the initial round + viral post patterns from knowledge base:

**Generate 5 hooks** (each exactly 2 lines, as visible before "See more"):
- Hook 1: Numeric/list-based ("X things I learned...")
- Hook 2: Bold provocative statement
- Hook 3: Direct "you" address + intrigue question
- Hook 4: Identity/role recognition
- Hook 5: Story opener or counterintuitive fact

Display all 5 hooks and ask the author to pick one using AskUserQuestion:
"Which hook grabs you the most?"
Options: The 5 hooks (truncated to fit).

---

### POST WRITING STAGE (gpt-5.2-pro)

The post is written by **gpt-5.2-pro** via OpenAI API for maximum quality. Claude builds the prompt, GPT writes the post.

#### Step 1: Build post-writing prompt

Save the prompt to `temp-dir/post-prompt.md`:

```
# Write a LinkedIn Post

You are a world-class LinkedIn content writer. Your posts consistently get 1000+ reactions because they combine sharp insights with perfect formatting.

## POST PARAMETERS
- Hook (MUST be first 2 lines, exactly as given): {selected hook}
- Target audience: {audience}
- Content type: {useful / positive / both}
- Product integration: {level}
- Topic angle: {angle}

## THESES TO WEAVE INTO THE POST
{Selected theses with their enrichments — expert opinions, counterarguments, first principles}

## CRITICAL: ONE COHESIVE POST
You are writing ONE single LinkedIn post — NOT a blog article with sections.
- Do NOT create separate sections with headings (## or ###) for each thesis
- Do NOT use --- separators to split the post into parts
- Do NOT treat each thesis as a standalone mini-post
- Instead: weave ALL theses into ONE continuous narrative flow where each idea naturally leads to the next
- The post should read like ONE person sharing ONE insight that has multiple facets — not like a listicle or a multi-chapter article
- Think of it as a single conversation, not a structured report

## LINKEDIN FORMATTING RULES (MANDATORY)
1. Hook = first 2 lines (before "See more"). Use the hook provided above EXACTLY.
2. Short paragraphs: 1-3 sentences MAX per paragraph.
3. **Information-dense sentences** — each sentence carries a complete, specific thought with enough context to stand on its own. Avoid ultra-short choppy fragments. A sentence like "Agents search for structured specifications: API docs, MCP integration schemas, machine-readable contracts and policies" is better than splitting into 4 separate lines.
4. Bullet points or arrow lists (→) where appropriate — but use them sparingly, ONE list max per post.
5. Address reader as "you" throughout.
6. CTA at the end — question that invites comments.
7. NO wall of text — mandatory paragraph breaks.
8. Conversational, confident tone — NOT academic.
9. NO section headings inside the post — it's a LinkedIn post, not a blog article.

## COUNTERARGUMENTS TO ADDRESS
Where useful, acknowledge counterarguments to strengthen credibility. Don't strawman — show you understand the nuance.

## REFERENCE STYLE
{If author provided reference post, include it here}

## LENGTH
Target: 200-350 words. This is a LinkedIn post, not a blog article. Every sentence must earn its place. If a thesis doesn't fit naturally into the flow, it's better to drop it than to bloat the post. Longer posts (up to 500 words) are acceptable ONLY if every extra word adds value and the post remains scannable.

## WRITE THE POST
Output ONLY the post text, ready to copy-paste into LinkedIn. No commentary, no meta-text, no "Here's your post:" prefix.
```

#### Step 2: Call gpt-5.2-pro via OpenAI API

```bash
python3 << 'PYEOF'
import json, os, sys

# Read prompt
with open("{temp-dir}/post-prompt.md", "r") as f:
    prompt = f.read()

# Read API key from .env
api_key = None
for env_path in [".env", os.path.expanduser("~/.env")]:
    if os.path.exists(env_path):
        break
with open(env_path, "r") as f:
    for line in f:
        if line.startswith("OPENAI_API_KEY="):
            api_key = line.strip().split("=", 1)[1].strip('"').strip("'")

if not api_key:
    print("ERROR: No OPENAI_API_KEY in .env")
    sys.exit(1)

import subprocess
result = subprocess.run(
    ["curl", "-s", "https://api.openai.com/v1/responses",
     "-H", f"Authorization: Bearer {api_key}",
     "-H", "Content-Type: application/json",
     "-d", json.dumps({
         "model": "gpt-5.2-pro",
         "input": [{"role": "user", "content": [{"type": "input_text", "text": prompt}]}],
         "reasoning": {"effort": "high"}
     })],
    capture_output=True, text=True, timeout=300
)

resp = json.loads(result.stdout)

# Extract text
text_parts = []
for item in resp.get("output", []):
    if item.get("type") == "message":
        for c in item.get("content", []):
            if c.get("type") == "output_text":
                text_parts.append(c.get("text", ""))

post_text = "\n".join(text_parts)

with open("{temp-dir}/post-text.md", "w") as f:
    f.write(post_text)

print(post_text)
PYEOF
```

#### Step 3: Display and save

Display the generated post in a markdown code block so the author can copy-paste. Then immediately save the post file (see SAVE POST TEXT stage below).

---

### SAVE POST TEXT (immediately after writing)

**IMPORTANT:** Save the post file to disk RIGHT AFTER the post text is written and shown to the author — BEFORE image generation begins. This ensures the text is preserved even if image generation is interrupted.

Generate a short title slug from the post content (3-4 words, kebab-case, English).

Save the post file as: `3-Marketing/1-SMM/Linkedin-posts/{YYYY-MM-DD}-{slug}.md`

The file should contain the frontmatter, the post text, and a placeholder for image metadata (to be filled in after image generation).

```markdown
---
date: {YYYY-MM-DD}
audience: {selected audience}
goals: {selected goals}
format: {selected format}
topic_angle: {selected viral topic}
content_type: {selected content type}
product_integration: {selected integration level}
---

# {title}

{the full post text, ready to copy-paste into LinkedIn}
```

After image generation is complete, UPDATE the same file to add image metadata (chosen_metaphor, final_image, prompts table).

---

### IMAGE GENERATION STAGE (New Yorker Classic Style)

Generate 10 different visual metaphors, ALL in New Yorker Classic style. Author picks the best one as the final image.

---

**Step 1: Read the post and brainstorm 10 visual metaphors**

Read the finished post carefully. Think about what makes this post UNIQUE — not generic "person at laptop" scenes, but specific, inventive visual metaphors that capture the post's core insight.

Generate 10 DIFFERENT visual metaphors. Each one is a concrete scene description (2-3 sentences).

Guidelines for metaphors:
- Each metaphor must be a SPECIFIC visual idea tied to THIS post's message — not generic business imagery
- Think in terms of: What is the TRANSFORMATION in this post? What is the TENSION? What is the AHA moment?
- Use metaphor types: analogy (X is like Y), contrast (before/after in one frame), scale shift (tiny/huge), unexpected juxtaposition, role reversal, physical manifestation of an abstract concept
- Vary the approaches: some literal, some abstract, some close-up, some wide, some with characters, some symbolic
- EVERY scene must be framed as optimistic, empowering, joyful
- NO generic business scenes: no "person at laptop", no "team in meeting room", no "handshake", no "graph going up"

**Step 2: Display metaphors and generate all 10 in New Yorker Classic style**

Display the list to the author:

```
## 10 Visual Metaphors (New Yorker Classic style)

1. {metaphor description in 10-15 words}
2. {metaphor description}
3. {metaphor description}
...
10. {metaphor description}

Generating all 10 in New Yorker Classic style...
```

For each metaphor, build the full prompt:

```
Editorial illustration in the style of classic New Yorker magazine covers by artists like Sempé and Steinberg. Precise ink pen lines with selective cross-hatching for shadow and depth. Subtle watercolor washes in a refined palette — slate blue, warm grey, ivory, with one pop of coral or golden yellow. Sophisticated composition with generous white space and one strong focal point. Witty visual metaphor that rewards a second look. Characters are elegantly simplified — expressive through posture and gesture, not detail. The humor is gentle and warm, never cynical. A sense of quiet confidence and intellectual charm.
MOOD IS CRITICAL: The overall feeling must be deeply POSITIVE — hopeful, joyful, light, uplifting, high-frequency energy. Characters should look happy, confident, and energized — never tired, stressed, or overwhelmed. The scene should radiate warmth and possibility. Bright open spaces, clean air, sunshine or warm light. No dark skies, no smoke, no dystopian imagery, no industrial gloom.
No text, no captions, no speech bubbles, no words.
[SCENE: {metaphor scene description}]
```

**Step 3: Generate 10 images via OpenRouter API (parallel)**

```bash
# Generate images in parallel batches
# Batch 1: images 1-5
for i in 1 2 3 4 5; do
  curl -s https://openrouter.ai/api/v1/chat/completions \
    -H "Authorization: Bearer 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" \
    -H "Content-Type: application/json" \
    -d "{
      \"model\": \"google/gemini-3.1-flash-image-preview\",
      \"messages\": [{\"role\": \"user\", \"content\": \"Generate an image: {full_prompt_for_metaphor_$i}\"}]
    }" > /tmp/openrouter_pass1_${i}.json &
done
wait

# Batch 2: images 6-10
for i in 6 7 8 9 10; do
  curl -s https://openrouter.ai/api/v1/chat/completions \
    -H "Authorization: Bearer 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" \
    -H "Content-Type: application/json" \
    -d "{
      \"model\": \"google/gemini-3.1-flash-image-preview\",
      \"messages\": [{\"role\": \"user\", \"content\": \"Generate an image: {full_prompt_for_metaphor_$i}\"}]
    }" > /tmp/openrouter_pass1_${i}.json &
done
wait
```

**Step 4: Save images to subfolder**

```bash
python3 << 'PYEOF'
import json, base64, os

images_dir = '3-Marketing/1-SMM/Linkedin-posts/images/{date}-{slug}'
metaphors_dir = os.path.join(images_dir, 'metaphors')
os.makedirs(metaphors_dir, exist_ok=True)

results = []
for i in range(1, 11):
    resp_file = f'/tmp/openrouter_pass1_{i}.json'
    out_file = os.path.join(metaphors_dir, f'{i:02d}-metaphor.png')

    try:
        with open(resp_file, 'r') as f:
            resp = json.load(f)
        msg = resp['choices'][0]['message']
        images = msg.get('images', [])
        if images:
            img_data_url = images[0]['image_url']['url']
            b64_data = img_data_url.split(',', 1)[1]
            raw = base64.b64decode(b64_data)
            with open(out_file, 'wb') as f:
                f.write(raw)
            results.append(f'  [{i:02d}] OK — {len(raw)} bytes')
        else:
            results.append(f'  [{i:02d}] FAILED — no images in response')
    except Exception as e:
        results.append(f'  [{i:02d}] ERROR — {e}')

print('Image generation results:')
print('\n'.join(results))
PYEOF
```

**Step 5: Ask the author to choose a metaphor**

Tell the author:
```
10 metaphor variants saved to: images/{date}-{slug}/metaphors/
Files: 01-metaphor.png through 10-metaphor.png

Please look at the images and tell me which metaphor number you like best (1-10).
You can also describe what you like about it or suggest tweaks.
```

Use AskUserQuestion with a free-text question:
"Which metaphor number (1-10) do you want to use? You can also describe any tweaks."

---

#### SAVE OUTPUTS (update post file with image metadata)

The post file was already saved during the POST WRITING STAGE as `3-Marketing/1-SMM/LinkedIn-posts/{YYYY-MM-DD}-{slug}.md`.

Now UPDATE the same file to add image metadata to the frontmatter and append the Metadata section.

Directory structure for images:
```
3-Marketing/1-SMM/LinkedIn-posts/
  {YYYY-MM-DD}-{slug}.md          ← post file (already saved, now updated)
  images/{YYYY-MM-DD}-{slug}/
    metaphors/                     ← 10 metaphor variants (New Yorker Classic style)
      01-metaphor.png ... 10-metaphor.png
    final.png                      ← copy of the chosen metaphor image
```

Copy the author's chosen metaphor image to `final.png` in the post's image folder.

Update the post file frontmatter to add:
```yaml
image_folder: images/{YYYY-MM-DD}-{slug}/
chosen_metaphor: {metaphor number}
style: new-yorker-classic
final_image: images/{YYYY-MM-DD}-{slug}/final.png
```

Append the Metadata section after the post text:
```markdown
---

## Metadata

**Theses used:**
{list of selected theses}

**Hook chosen:** {which hook pattern}

**Chosen metaphor (#{N}):**
{the full scene description}

**Style:** New Yorker Classic

**All 10 metaphor prompts:**

| # | Metaphor Scene Description | Full Prompt |
|---|---------------------------|-------------|
| 01 | {scene} | {full prompt} |
| ... | ... | ... |
| 10 | {scene} | {full prompt} |
```

After saving, tell the author:
- Final image copied to `images/{YYYY-MM-DD}-{slug}/final.png` — ready to upload to LinkedIn
- All 10 metaphor variants are in `metaphors/` for future reference
- All prompts are logged in the post metadata

---

## Error Handling

- If OpenRouter API fails for some images: retry failed ones once. If still fails, show the failed prompts to the author for manual generation. Partial success (e.g., 7 out of 10 images) is fine — report which succeeded and which failed.
- If the author gives very short raw thoughts: ask a follow-up question to get more detail before proceeding.
- If the author wants to change something after seeing the post: ask what to change and regenerate only the affected part.

---

## Quality Checklist

Before delivering the final post, verify:

- [ ] Hook is exactly 2 lines (what's visible before "See more")
- [ ] No paragraph longer than 3 sentences
- [ ] Reader is addressed as "you"
- [ ] Post is scannable (would you read it while scrolling?)
- [ ] CTA is present at the end
- [ ] Product integration matches the selected level
- [ ] Content type matches (useful / positive / both)
- [ ] Post length is 200-350 words (up to 500 only if justified)
- [ ] ONE cohesive post — no section headings, no --- separators splitting it into parts
- [ ] No wall of text anywhere
- [ ] Tone is conversational and confident (not academic)
- [ ] 10 distinct visual metaphors generated (no generic business imagery)
- [ ] All 10 metaphors in New Yorker Classic style
- [ ] Author chose their preferred metaphor
- [ ] All images have positive, high-frequency mood
- [ ] All prompts saved in post metadata
- [ ] Final image copied to final.png
- [ ] Files saved to correct directory structure
