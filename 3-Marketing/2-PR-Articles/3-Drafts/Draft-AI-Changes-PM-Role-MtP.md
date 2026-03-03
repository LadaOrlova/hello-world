—-
## Инструкция от Вани Замесина

> *[Это поле заполняет автор после прочтения черновика]*
> *[Напишите здесь, что нужно изменить на этапе редактуры]*

—-

# {ВЫБРАТЬ ЗАГОЛОВОК ИЗ 20 ВАРИАНТОВ НИЖЕ}

> **Статус:** Черновик v2
> **Модель:** claude-opus-4-6
> **Дата:** 2026-03-03
> **Целевое издание:** Mind the Product — https://www.mindtheproduct.com
> **Язык:** English
> **Слов:** ~1300
> **Тезисов:** 5 (A1, A2, A3, A4, A6)
> **Режим:** Agent Team (style-researcher, case-hunter, narrative-architect, writer)

## 20 вариантов заголовков

1. I built 20 products in 3 months. Here's what AI can't do.
2. Vibe coding won't save you. Business judgment will.
3. Your PRD is dead. Your judgment isn't.
4. Speed kills products. Judgment saves them.
5. AI made building free. Knowing what to build costs everything.
6. The PM who only coordinates is already gone
7. Stop writing PRDs. Start buying knowledge.
8. Building is solved. Deciding what to build is not.
9. The feature mill runs at AI speed now. That's the problem.
10. 20 products, $100K, and one lesson: judgment beats velocity
11. AI gave PMs superpowers. Most will use them wrong.
12. Your team of 4 is the new team of 40. Now what?
13. The fastest PM in the room is still wrong 90% of the time
14. Judgment, not features: what 20 vibe-coded products taught me
15. The builder era doesn't need more features. It needs better bets.
16. AI won't take your PM job. Another PM with AI will.
17. Vibe coding is the easy part. Here's the hard part.
18. The $100K question: what separates builder PMs from the rest
19. The PM market is splitting. Which side are you on?
20. I shipped 20 AI products. The bottleneck was never the code.

—-

Over the past three months, I built 20 products with vibe coding. They've already generated $100K in revenue. After 20 products, real traction, and integrating vibe coding and AI agents into my team's workflow — here's what I've learned about what the PM role is actually becoming.

The shift from PM to builder isn't a metaphor anymore — it's happening across the industry, and it's happening fast.

## The builder era is here

Boris Cherny, Head of Claude Code at Anthropic, hasn't edited a single line by hand since November 2025 — [100% of his code is AI-written](https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens), with +200% productivity per engineer. A quarter of Y Combinator's W25 batch ships with [95% AI-generated codebases](https://techcrunch.com/2025/03/06/a-quarter-of-startups-in-ycs-current-cohort-have-codebases-that-are-almost-entirely-ai-generated/). Collins Dictionary named "vibe coding" [Word of the Year 2025](https://www.theguardian.com/technology/2025/nov/06/vibe-coding-collins-dictionary-word-of-the-year-2025).

Marc Andreessen calls it a ["Mexican standoff" between PM, engineering, and design](https://www.lennysnewsletter.com/p/marc-andreessen-the-real-ai-boom) — each believes they can do the other two roles with AI, and "they're actually all kind of correct." LinkedIn formalized this in December 2025, scrapping its APM program and launching ["Associate Product Builder"](https://www.lennysnewsletter.com/p/why-linkedin-is-replacing-pms) — new hires learn coding, design, and PM together in cross-trained pods.

The reframe that matters: a full-stack builder isn't a PM who just learned to code. It's a PM who learned to maintain production quality through tests, reviews, and economics. The old jobs — writing PRDs, creating mockups, coding prototypes — disappear as a class. You level up from pushing tasks to owning the entire value chain.

But here's what nobody tells you about the builder era: building faster is the easy part. The hard part is knowing what's worth building.

## Speed without judgment is the feature mill on steroids

When AI crushes execution cost to near zero, the bottleneck moves upstream — to business judgment. It means diagnosing where in the causal chain the growth sits:

- Market segment
- Jobs to be done
- Strategy
- Value proposition
- Unit Economics
- Aquisition Channels

You're not just optimizing features. You're bringing growth to business. I think about priority through a simple formula: assumption risk times consequence, divided by cost of testing. AI collapses the denominator. What dominates is the numerator — your ability to identify which assumptions have major risks and what consequences they carry.

As Marty Cagan [puts it](https://www.svpg.com/product-coaching-and-ai/): AI makes "PM theater" — PRDs, roadmaps, user stories — cheap and replaceable by agents. The PM who moves tickets is exactly who gets replaced. Ravi Mehta frames it as a [shift from craft to judgment](https://www.atlassian.com/blog/artificial-intelligence/shift-from-craft-to-judgement-ai): when anyone can produce something polished, knowing what to create and why is the scarce asset.

Without judgment, vibe coding is the feature mill on steroids. Ninety percent of resources already go to features that never find a market. AI makes that 10x faster. The [General Assembly survey](https://generalassemb.ly/blog/ai-and-product-management-survey/) captures the gap: 98% of PMs use AI at work (11 interactions/day), but only 39% received job-specific training. Execution adopted, strategic framework missing.

So if judgment is the asset and building is the tool — what does the day-to-day actually look like?

## From PRDs to hypothesis pipelines

The paradigm flips: you're not launching products — you're buying knowledge. Every prototype is a bet, and AI lets you run an order of magnitude more bets per sprint. This turns the PM into an operator of an industrial hypothesis pipeline: business goal, causal graph of growth mechanics, research, risk assumption test, build. Each step can be delegated to an AI agent — and increasingly is.

Boris Cherny describes the frontier: "Claude is starting to come up with ideas. Looking through feedback, bug reports, telemetry." The agent doesn't just execute — it proposes. Shreyas Doshi frames the scale: 3-4 person startups now match the impact of 30-50 person teams. But this leverage only works if delegation follows risk. AI agents are less competent employees — hand them low-risk tasks (A/B tests, data analysis, draft copy) and keep the high-risk decisions for yourself: which segment to enter, what to price, where the ethical lines sit.

Here's the part that changes your day-to-day most: AI products are probabilistic. One prompt, many possible outputs. The classical PM loop of "write spec, build, ship" breaks. Reforge calls it the evals-first model — you manage quality distributions, not feature checklists. Your job shifts from writing documents to designing evaluation systems that catch degradation before users do.

Yet ninety percent of human decisions are unconscious — reading someone's face as they struggle with your product, sensing the unspoken need. No agent replicates that. The irreducible human core of the PM role is the empathic interview, not the PRD.

But let's be honest about what's not ready yet.

## The full cycle isn't here yet

You can prototype in an afternoon. You cannot ship to production in an afternoon. The critical chain breaks at security, DevOps, and compliance — the slowest link determines your actual speed. Brian Chesky calls AI ["the best thing that ever happened to Airbnb"](https://fortune.com/2026/02/17/airbnb-ceo-brian-chesky-says-ai-best-thing-ever-happened-company-warns-other-founders-get-onboard-or-else/) — it handles a third of customer service — but [also admitted](https://www.latimes.com/business/story/2025-10-21/chesky-says-openai-tools-not-ready-for-chatgpt-tie-up-with-airbnb-app) the tools are "not ready" for deep integration. As April Dunford [warns](https://businessofsoftware.org/2025/06/positioning-in-the-age-of-ai-what-founders-need-to-know/), PoC revenue is routinely mistaken for traction.

AI makes creation cheap, but each component you add multiplies the probability of failure. The full cycle is 12-24 months away. Until then: kill criteria, reversibility, and circuit breakers.

These gaps will close. The question is who will be ready when they do — and who will be left behind.

## The split is already happening

The PM market is fracturing K-shaped: surging demand at both poles — AI specialists earning 35% premiums and AI-augmented senior generalists — while mid-level coordination roles hollow out. Performance inversion is real: AI-savvy juniors outperform traditional seniors, upending career ladders built over decades.

The forces are structural. Builder PMs feel strong pull forward — the value is enormous, the pain of the old model obvious, barriers low. Traditional PMs feel equally strong pushback — habit is deeply embedded, fear of coding real. People overestimate their readiness to change by a factor of three. And AI diffusion itself is [uneven across countries and cohorts](https://arxiv.org/abs/2506.08945), compounding the gap.

Spotify's developers [haven't written code since December](https://techcrunch.com/2026/02/12/spotify-says-its-best-developers-havent-written-a-line-of-code-since-december-thanks-to-ai/), shipping 50+ features through their "Honk" system on Claude Code. METR found experienced developers [19% slower](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) with the same tools. Same technology, opposite results. The difference is organizational architecture, not talent.

This is the innovator's dilemma in real time. Companies get disrupted not because they work badly, but because they work well enough to resist change. AI excels at local optimization — A/B tests, UX tweaks. The PM who operates only there gets replaced. The PM who works at the global level — which market, which segment, when to pivot — becomes irreplaceable. The reframe is not "adapt or die." It is: build the environment — training, access, psychological safety — that lets people adapt. Bifurcation is not about talent. It's about architecture.

This isn't a three-year transformation plan. It starts Monday.

## Your Monday morning

1. **Build one prototype this week** — not to ship, but to learn what your judgment tells you when testing costs nothing.
2. **Replace one PRD with a prompt set.** Write the intent, the examples, and the constraints — and hand it to an AI agent.
3. **Ask the RAT question for every backlog item:** "If this assumption is wrong, what do we lose?" Rank by consequence, not by effort.
4. **Talk to one customer this week.** No AI can replicate what you learn from watching someone struggle with your product in real time.
5. **Kill one feature.** Find the zombie that's burning compute and margin and delete it.

The PM role isn't disappearing. But the PM who only coordinates is. The builder who judges — who knows what to build, for whom, and when to stop — that PM has never been more essential.
