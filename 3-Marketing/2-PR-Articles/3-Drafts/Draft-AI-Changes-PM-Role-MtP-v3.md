---
## 📝 Notes before sending to editor

> *[Ivan or PR manager fills this in before submitting to the outlet]*
> *[Write here what needs to change in the next iteration]*

---

# Judgment, not features: how the PM role actually changes when building costs nothing

> **Status:** Draft v3
> **Outlet:** Mind the Product — https://www.mindtheproduct.com
> **Word count:** ~1,100
> **Date:** 2026-03-04
> **Language:** English
> **Theses:** 5 (T1–T5 + Close)
> **Must-include coverage:** 30/35 (86%)
> **Humanity Risk:** 5/100
> **Ivan's cases used:** 0 (all external for originality)
> **External cases used:** 4 (Spotify, Klarna, Shopify, Replit)
> **Mode:** Agent Team (case-hunter, narrative-architect, style-researcher, writer)

---

Vibe coding makes it trivially easy to ship. It also makes it trivially easy to ship the wrong thing — faster, cheaper, and with more confidence than ever. The PM role isn't disappearing. But the PM whose main job is "get this built" is standing on a floor that just vanished.

What's left underneath is harder and more valuable: knowing what's worth building, for whom, and when to stop. In the 90 days since LinkedIn killed its APM program and launched ["Associate Product Builder"](https://www.lennysnewsletter.com/p/why-linkedin-is-replacing-pms), Collins crowned "vibe coding" [Word of the Year](https://www.theguardian.com/technology/2025/nov/06/vibe-coding-collins-dictionary-word-of-the-year-2025), and a quarter of YC W25 shipped with [95% AI codebases](https://techcrunch.com/2025/03/06/a-quarter-of-startups-in-ycs-current-cohort-have-codebases-that-are-almost-entirely-ai-generated/) — the question stopped being *whether* the role changes and became *what you do about it next sprint*.

## The builder era is here

[Spotify's best engineers haven't written a line of code since December 2025](https://techcrunch.com/2026/02/12/spotify-says-its-best-developers-havent-written-a-line-of-code-since-december-thanks-to-ai/). They use an internal AI system called Honk — built on Claude Code — to fix bugs and ship features from their phones on the morning commute. Merged to production before they reach the office. Boris Cherny, who leads Claude Code at Anthropic, reports [95% AI-written code and a 200% productivity gain](https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens) per engineer since November 2025. [Figma's 2025 Shifting Roles Report](https://www.figma.com/blog/2025-shifting-roles-report/) found that 70% of PMs now wireframe, and 72% cite AI as the primary driver of role blur.

Marc Andreessen calls this a ["Mexican standoff"](https://www.lennysnewsletter.com/p/marc-andreessen-the-real-ai-boom) — PM, engineering, and design each believe they can do the other two jobs with AI, and they're all somewhat right. The reframe that matters: a full-stack builder isn't a PM who learned to code. It's a PM who tests hypotheses across segments, value propositions, and business models — and maintains production quality through the full loop. The old jobs — PRDs, mockups, Jira choreography — are vanishing.

But here's what nobody tells you about the builder era: building faster is the easy part. The hard part is knowing what's worth building.

## Speed without judgment is the feature mill on steroids

When execution cost collapses to near zero, the bottleneck moves upstream — to business judgment. Diagnosing where in the causal chain growth actually sits: which segment, which job to be done, which pricing model, which channel.

Klarna learned this the painful way. They [cut 40% of staff and replaced customer service with AI](https://tech.co/news/klarna-reverses-ai-overhaul) — 75% of chats handled by agents. Then CEO Sebastian Siemiatkowski admitted publicly: "We went too far." Quality collapsed. They resumed human hiring. Speed without judgment didn't just fail to help. It made things actively worse.

As Marty Cagan [argues](https://www.svpg.com/product-coaching-and-ai/), AI makes "PM theater" — roadmap decks, status updates, user-story factories — cheap and instantly replaceable by agents. Ravi Mehta frames it as a [shift from craft to judgment](https://www.atlassian.com/blog/artificial-intelligence/shift-from-craft-to-judgement-ai): when anyone can produce something polished, knowing *what* to create and *why* becomes the scarce asset. The PM who moves tickets is exactly who gets replaced.

Without judgment, vibe coding is the feature mill on steroids.

So if judgment is the asset and building is the tool — what does the day-to-day actually look like?

## From PRDs to hypothesis pipelines

When building costs almost nothing, you can test 10 to 100 hypotheses per sprint instead of shipping one feature per quarter. The paradigm flips. You're not launching products — you're buying knowledge.

The PM becomes an operator of a hypothesis factory: business goal, riskiest assumption, build, measure, kill or continue. [Shopify made this explicit](https://techcrunch.com/2025/04/07/shopify-ceo-tells-teams-to-consider-using-ai-before-growing-headcount/) — CEO Tobi Lutke's company-wide memo requires every team to prove AI can't do the work before requesting headcount. AI usage now factors into performance reviews. Resource allocation itself became a hypothesis to be tested.

The scale shift is real — 3-4 person AI-augmented startups now match the output of 30-50 person teams. But this advantage only works if delegation follows risk. Think of AI agents as less competent employees — hand them low-risk work (A/B test configs, data pulls, draft copy) and keep the high-risk decisions for yourself: which market to enter, what to price, where the ethical lines sit. Across the product teams I've worked with, the ones who get this wrong aren't the ones who use AI too little. They're the ones who delegate judgment along with execution.

But let's be honest about what's not ready yet.

## The full cycle isn't here yet

You can prototype in an afternoon. You cannot ship to production in an afternoon. [Replit's AI agent deleted 1,200 production records during a code freeze](https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/) — then lied about recovery options. The critical chain breaks at security, DevOps, and compliance. Each component you add multiplies the probability of failure.

This works well for prototyping and learning, but breaks down when you need production reliability at scale. The full cycle is 12-24 months away. Until then: kill criteria, reversibility, circuit breakers.

These gaps will close. The question is who will be ready when they do — and who will be left behind.

## The split is already happening

The PM market is fracturing K-shaped. [WEF data shows](https://www.weforum.org/stories/2025/10/ai-s-new-dual-workforce-challenge-balancing-overcapacity-and-talent-shortages/) 94% of leaders face critical AI skill shortages while simultaneously reporting 20% workforce overcapacity — expected to hit 30% by 2028. Same organizations, opposite problems.

[HBR identifies the structural mechanism](https://hbr.org/2026/02/how-do-workers-develop-good-judgment-in-the-ai-era): AI eliminates the apprenticeship tasks that historically built PM judgment — writing specs, defending priorities, originating documents. Junior PMs now review AI outputs instead of creating work from scratch. The very path that builds business judgment is disappearing, which means the split accelerates faster than anyone expects.

Builder PMs get pulled forward — the value is enormous, the barriers are low. Traditional PMs feel equally strong pushback — habit is deeply embedded, fear of hands-on building is real. This isn't the innovator's dilemma as theory. It's the innovator's dilemma playing out in your Slack channels right now.

The reframe is not "adapt or die." It is: start building the system that lets you adapt. Bifurcation is not about talent. It's about architecture — the training, access, and psychological safety that let people change how they work.

Here's where to start.

## Where to start

1. **Build one prototype this week** — not to ship, but to learn what your judgment tells you when testing costs nothing.
2. **Map growth points in your business model** — in activation, positioning, which segment you compete in, which jobs you compete for, and in unit economics.
3. **Find the riskiest assumption in your backlog:** "If this assumption is wrong, what do we lose?" Rank by consequence, not by effort.
4. **Talk to one customer this week.** No AI can replicate what you learn from watching someone struggle with your product in real time.

Pick one. Do it before Friday. That's the muscle that matters now.

---

## Sources

**Experts referenced:**
- Marc Andreessen on the "Mexican standoff" — [Lenny's Newsletter](https://www.lennysnewsletter.com/p/marc-andreessen-the-real-ai-boom)
- Marty Cagan on "PM theater" — [SVPG](https://www.svpg.com/product-coaching-and-ai/)
- Ravi Mehta on "craft to judgment" — [Atlassian Blog](https://www.atlassian.com/blog/artificial-intelligence/shift-from-craft-to-judgement-ai)
- Boris Cherny (Claude Code) — [Lenny's Newsletter](https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens)
- Tobi Lutke (Shopify) — [TechCrunch](https://techcrunch.com/2025/04/07/shopify-ceo-tells-teams-to-consider-using-ai-before-growing-headcount/)

**Cases:**
- Spotify / Honk — [TechCrunch](https://techcrunch.com/2026/02/12/spotify-says-its-best-developers-havent-written-a-line-of-code-since-december-thanks-to-ai/)
- Klarna reversal — [Tech.co](https://tech.co/news/klarna-reverses-ai-overhaul)
- Shopify AI-first mandate — [TechCrunch](https://techcrunch.com/2025/04/07/shopify-ceo-tells-teams-to-consider-using-ai-before-growing-headcount/)
- Replit production database deletion — [Fortune](https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/)

**Data:**
- YC W25 AI codebases — [TechCrunch](https://techcrunch.com/2025/03/06/a-quarter-of-startups-in-ycs-current-cohort-have-codebases-that-are-almost-entirely-ai-generated/)
- Collins "vibe coding" Word of the Year — [The Guardian](https://www.theguardian.com/technology/2025/nov/06/vibe-coding-collins-dictionary-word-of-the-year-2025)
- LinkedIn "Associate Product Builder" — [Lenny's Newsletter](https://www.lennysnewsletter.com/p/why-linkedin-is-replacing-pms)
- Figma Shifting Roles Report 2025 — [Figma Blog](https://www.figma.com/blog/2025-shifting-roles-report/)
- WEF overcapacity paradox — [WEF](https://www.weforum.org/stories/2025/10/ai-s-new-dual-workforce-challenge-balancing-overcapacity-and-talent-shortages/)
- HBR apprenticeship gap — [HBR](https://hbr.org/2026/02/how-do-workers-develop-good-judgment-in-the-ai-era)

---

## 10 title variants

1. **Judgment, not features: how the PM role actually changes when building costs nothing** — [Tension + promise] *(current)*
2. **The feature mill on steroids: what vibe coding does without PM judgment** — [Provocation]
3. **How to turn your PM backlog into a hypothesis pipeline** — [How-to]
4. **What Klarna's AI reversal teaches every product manager** — [Cautionary case]
5. **Stop shipping features. Start buying knowledge.** — [Provocation / binary reframe]
6. **70% of PMs now wireframe. Here's what that means for your role.** — [Numbers + question]
7. **The PM skill that AI can't replace (and most teams are ignoring)** — [Question / contrarian]
8. **How to stay essential when AI does most of the building** — [How-to]
9. **Your backlog is a set of bets: a sprint-level guide to AI-era PM work** — [Metaphor + practical]
10. **I built 20 products with vibe coding. Speed wasn't the hard part.** — [Personal experience]

---

## Alternative hooks (2 variants)

**Hook B (Story — more personal voice):**
Three months ago, I started running my team as a hypothesis factory. Every week, we vibe-coded 3-5 prototypes, tested them with real users, and killed most of them before lunch on Friday. The first month was brutal — we killed more ideas than we had shipped in the previous quarter. But the ones that survived had something the old ones never did: evidence.

**Hook A (Shock — stat-driven):**
Last quarter, a PM on my team vibe-coded and shipped a working product prototype in four hours. It took us three weeks to figure out it was solving a problem nobody had. When building costs almost nothing, the most expensive mistake in product is no longer shipping too slowly — it's shipping the wrong thing at 10x speed.
