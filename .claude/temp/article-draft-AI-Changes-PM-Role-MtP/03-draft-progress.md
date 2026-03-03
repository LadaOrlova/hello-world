# Judgment, Not Features: A PM's Guide to the Builder Era

Last November, I opened Cursor for the first time and built a working prototype in four hours -- something that would have taken my engineering team two sprints. I sat there staring at the screen, feeling two things at once: exhilaration that I could move this fast, and a quiet dread that I had just made my own job description obsolete. If I can build this without engineers, what exactly is the PM supposed to do now?

I spent the next three months finding out. This is what I learned.

## The Builder Era Is Here

I'm not alone in this. The shift from PM to builder is not a metaphor anymore -- it's happening across the industry, and it's happening fast.

[Boris Cherny](https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens), Head of Claude Code at Anthropic, hasn't edited a single line of code by hand since November 2025. One hundred percent of his code is AI-generated. Anthropic reports a 200% productivity increase per engineer. At Y Combinator, [25% of the latest batch](https://techcrunch.com/2025/03/06/a-quarter-of-startups-in-ycs-current-cohort-have-codebases-that-are-almost-entirely-ai-generated/) shipped products with 95% AI-generated codebases -- and every one of those founders was fully capable of writing the code themselves.

Marc Andreessen calls it a "[Mexican standoff](https://a16z.com/)": PMs believe they can do engineering work with AI, engineers believe they can do product work, designers believe the same -- and they're all right. The old T-shaped skillset is giving way to E-shaped and F-shaped profiles where you go deep in multiple domains. LinkedIn made it official, [killing its Associate PM program](https://www.lennysnewsletter.com/p/why-linkedin-is-replacing-pms) and replacing it with an Associate Product Builder track. [Teresa Torres documented](https://www.producttalk.org/ai-prototyping-lovable/) eleven PMs building functional prototypes with Lovable -- one created a mental health risk identification system in six hours.

But let me be precise about what "full-stack builder" means. It does not mean a PM learned to code. It means a PM learned to maintain production quality through tests, reviews, constraints, and unit economics. That distinction matters. And honesty demands a caveat: a [METR study](https://techcrunch.com/2025/07/11/ai-coding-tools-may-not-speed-up-every-developer-study-shows/) found experienced developers were actually 19% slower with AI tools on familiar codebases. The tools are powerful, not magic.

But here's what nobody tells you about the builder era: building faster is the easy part. The hard part is knowing what's worth building.

## Speed Without Judgment Is the Feature Mill on Steroids

The absolutely critical skill in the AI era is business judgment -- the ability to make the right decision under uncertainty. When AI automates execution, the differentiator is not speed of doing but quality of deciding.

I think about this through a simple formula I call the Risk Assumption Test: Priority equals Probability times Consequence divided by Cost of Verification. AI is crushing the denominator. When it costs almost nothing to test an idea, the numerator dominates -- your ability to identify which risks matter and assess what happens if you're wrong. That is judgment.

The data backs this up. A [General Assembly survey](https://generalassemb.ly/blog/ai-and-product-management-survey/) found that 98% of PMs already use AI at work, averaging eleven tool interactions per day. Yet only 39% have received job-specific AI training. Almost everyone adopted the execution layer. Almost nobody upgraded their judgment layer.

Without that upgrade, you get the feature mill on steroids. We already know that roughly 90% of resources go into features that fail to move the needle. Give a team with no strategic direction an AI that builds ten times faster, and you get ten times more waste.

[Marty Cagan](https://www.svpg.com/product-coaching-and-ai/) put it bluntly: AI makes "PM theater" -- writing PRDs, maintaining roadmaps, running ceremonies -- cheap and replaceable. The PM who moves tasks in a tracker will be replaced. The PM who owns outcomes will not. [Ravi Mehta](https://www.atlassian.com/blog/artificial-intelligence/shift-from-craft-to-judgement-ai), former CPO of Tinder, frames the same shift: historically, product work demanded both taste (knowing what to make) and craft (skill to make it). AI democratizes craft. What's scarce now is knowing what to create and why it matters.

Business judgment means diagnosing where in the causal chain the real problem sits -- not just whether to build, but which lever actually moves the outcome.

So if judgment is the asset and building is the tool -- what does the day-to-day actually look like?

## Your New Operating System

Three shifts are replacing the PRD-sprint-ship cycle.

**From PRDs to prompt sets.** [Aparna Chennapragada](https://aparnacd.substack.com/p/prompt-sets-are-the-new-prds), CPO at Microsoft, says prompt sets are the new PRDs. When her teams start a project, they deliver an interactive prototype and a collection of prompts, not a spec document. For you, that means delegating by risk level: let AI agents handle low-risk verification while you focus judgment on high-stakes decisions. [Shreyas Doshi](https://x.com/shreyas/status/1943689228313067545) projects that three-to-four-person startups will soon match the impact of teams of thirty to fifty. You don't need more people. You need better decisions.

**From launches to a hypothesis pipeline.** We are not launching products -- we are buying knowledge. Each experiment purchases information about what works. Today, AI delivers prototype-speed gains. But the full cycle -- security, compliance, deployment -- still lags twelve to twenty-four months behind. Your job: define kill criteria before you start building, design for reversibility, and install circuit breakers that stop a losing bet before it compounds.

**From inbound to full-funnel.** When production is cheap, differentiation moves to story, positioning, and distribution. [Brian Chesky restructured Airbnb](https://fortune.com/2026/02/17/airbnb-ceo-brian-chesky-says-ai-best-thing-ever-happened-company-warns-other-founders-get-onboard-or-else/) around this insight -- fewer PMs, more product marketing, merging inbound and outbound into a single function. [Des Traynor](https://websummit.com/summaries/lis25/the-death-of-saas-the-dawn-of-agents/) at Intercom rebuilt the entire product for an agent-first world and changed pricing from seats to outcomes. The PM who only builds features and hands them to marketing is leaving value on the table. Own the story from hypothesis to customer.

## Your Move

None of this requires a restructuring or a leadership mandate. You can start this week.

1. **Pick one hypothesis.** Build a working prototype -- not to ship, but to learn what your judgment tells you when testing costs nothing.
2. **Replace one PRD with a prompt set.** Write the intent, the examples, and the constraints. Hand it to an AI agent.
3. **Ask the RAT question for every backlog item:** "If this assumption is wrong, what do we lose?" Rank by consequence, not by effort.
4. **Talk to one customer this week.** No AI replaces watching someone struggle with your product in real time.
5. **Kill one feature.** Find the zombie burning compute and margin, and delete it.

The PM role is not disappearing. But the PM who only coordinates is. The builder who judges -- who knows what to build, for whom, and when to stop -- that PM has never been more essential.
