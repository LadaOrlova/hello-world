— -
## Notes before sending to editor

> *[Ivan or PR manager fills this in before submitting to Mashable]*
> *[Write here what needs to change in the next iteration]*

— -

# The Bottleneck Was Never Code — And Product Teams Aren't Ready for What Comes Next

> **Status:** Draft
> **Outlet:** Mashable
> **Word count:** ~1620
> **Date:** 2026-04-06 20:30
> **Theses:** 7
> **Must-include coverage:** 85/88 (97%)
> **Humanity Risk:** 10/100
> **Ivan's cases used:** 3 (BOOST, CRM segmentation, 12K students)
> **External cases used:** 11 (Medvi, Dr. Hussan, Pieter Levels, Klarna, METR, Salesforce, Lovable, Shopify, McKinsey, Sequoia, Atlassian)
> **Mode:** Agent Team (case-hunter, narrative-architect, style-researcher, writer)

— -

*By Ivan Zamesin*

Two things are true at the same time. First: AI can now build a functional app in a weekend for $200/month Claude Code subscription. Second: 90 percent of features built by product teams are dead on arrival —  nobody uses them. Put those together and you get an uncomfortable question: what if the bottleneck was never code?

## It's real, and it has a price tag

[Andrej Karpathy coined it "vibe coding"](https://en.wikipedia.org/wiki/Vibe_coding) in February 2025 —  building software by describing what you want to an AI agent and letting it write, debug, and deploy. By early 2026, [Boris Cherny](https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens), the creator of Claude Code at Anthropic, went further: "Coding is a solved problem." He hasn't written a single line by hand since November 2025 —  and ships 10 to 30 pull requests a day. This wasn't just better autocomplete. It was a new class of tool: AI with access to the terminal, the file system, and the deployment pipeline.

The numbers that followed are hard to dismiss. [Dr. Fahim Hussan](https://analyticsindiamag.com/ai-news-updates/doctor-with-no-coding-experience-builds-a-health-app-on-replit-in-just-4-days/), a British GP with zero coding experience, built a full health-tracking app in four days for under 175 pounds. Agencies had quoted him 100,000. A telehealth startup called Medvi went from $20,000 in AI tools to $401 million in revenue in under a year —  with two employees total.

I've built my own education product in the same way: full market research in 90 minutes, MVP in a few hours, Stripe integration takes 30 mins. The next morning I am selling. Two cohorts sold out in 24 hours each. My developer didn't know I'd done it.

Of course there are limitations. [Research shows](https://natively.dev/articles/vibe-coding-limitations) 40 to 62 percent of AI-generated code contains security vulnerabilities. [Technical debt climbs](https://www.infoq.com/news/2025/11/ai-code-technical-debt/) in AI-heavy codebases. But the trajectory is clear: the term has already evolved from "vibe coding" to "agentic engineering," and the cost of a functional prototype has collapsed from six figures to a monthly subscription.

When building gets this cheap, cost stops being the bottleneck. 

## The product validation pipeline flipped

For decades, the product validation pipeline existed because development was expensive. An error caught in coding cost 10 to 100 times more than one caught in research. So teams ran months of discovery in order to de-risk the expensive part.

When code costs $200 a month, it's cheaper to build an MVP and sell it ASAP. The rational sequence inverts: quick AI research in an hour or two, prototype in a few more, then sell to a real person. The customer interview becomes a sales call. Ten fast iterations beat one perfect plan.

[Pieter Levels](https://www.fast-saas.com/blog/pieter-levels-success-story/) has been doing this for years — 40-plus products launched, the failures killed within weeks, the winners generating $3.1 million a year with zero employees and zero investors. What used to look crazy now looks like a good strategy.

Bad news: [90% of AI startups fail](https://www.digitalsilk.com/digital-trends/startup-failure-rate-statistics/). But the old guardrail —  "development is too expensive to skip validation" —  is gone. Something else has to replace it. 

If you think this is just a startup story, check the stock market. 

## The SaaSpocalypse

When code approaches free, competition explodes, margins compress, and the market notices. Over $1 trillion in SaaS market cap was [erased in Q1 2026](https://techcrunch.com/2026/03/01/saas-in-saas-out-heres-whats-driving-the-saaspocalypse/). [SaaStr called it](https://www.saastr.com/the-saas-rout-of-2026-is-even-worse-than-you-think-for-the-first-time-ever-software-now-trades-at-a-discount-to-the-sp-500/) the worst rout in the history of the sector —  for the first time ever, software now trades at a discount to the S&P 500. Atlassian plunged 35 percent in a single week after reporting its first-ever systemic decline in enterprise seat counts. SaaS valuation multiples cratered from 13x to 3-4x revenue.

Per-seat pricing —  the business model that built an industry —  is under existential threat. If one person with AI can do the work of ten, why pay for ten seats?

## Teams are shrinking. Fast.

The old product team: a PM, a designer, a marketer, four or five developers. The new one: a PM, half a designer, a quarter of a marketer, and one developer —  producing more than the full squad did before. [Andrew Ng's data](https://hackernoon.com/andrew-ng-product-team-ratios-evolving-to-just-one-software-developer-for-every-two-product-manager) shows engineer-to-PM ratios inverting from 8:1 to as low as 1:2. His own team proposed having twice as many PMs as engineers —  for the first time ever. At [Shopify](https://fortune.com/2025/04/08/shopify-ceo-ai-automation-no-new-hires-tech-jobs/), CEO Tobi Lutke now requires teams to "demonstrate why they cannot get what they want done using AI" before any new hire is approved. McKinsey's CEO [told Yahoo Finance](https://finance.yahoo.com/news/mckinseys-ceo-breaks-down-ai-100301404.html) the firm now has 25,000 AI agents alongside 40,000 human employees —  with parity expected by year's end.

So if a PM and one developer can do the work of eight, what exactly is AI handling —  and what's left for humans?

## What AI handles right now

The list is longer than most people realize. AI builds full MVPs to production quality. It runs market research in one to two hours that used to take weeks. It generates product requirement documents. It segments tens of thousands CRM records in 30 minutes (I've done this —  few Claude Code agents reading, debating, and producing an analysis that previously took an analyst a full week).

[At Salesforce](https://hbr.org/2026/02/to-thrive-in-the-ai-era-companies-need-agent-managers), AI agents now autonomously resolve 74 percent of inbound support cases and boosted sales meetings from 150 per month to 350 per week. [Lazar Jovanovic](https://www.lennysnewsletter.com/p/getting-paid-to-vibe-code) works full-time as a "professional vibe coder" at Lovable, a $200-million-ARR company, with no engineering background.

## Business judgment is the moat

Think of a feature as a delivery truck that delivers value for the customer. When the truck was expensive to build, companies obsessed over construction: timelines, sprints, velocity. Now the truck is free. So the only question that matters is: what and whom should we deliver?

This is business judgment —  understanding which segments to serve, which jobs customers actually hire your product for, who the real competitors are, what the business model can sustain. Without it, AI just helps you build the wrong thing faster.

I've seen this pattern across 13,000 students. A person without business judgment using ChatGPT becomes a fast generator of bad decisions. The output looks polished. The reasoning is hollow. [Klarna learned this the hard way](https://www.digitalapplied.com/blog/klarna-reverses-ai-layoffs-replacing-700-workers-backfired) —  the company replaced 700 customer service agents with AI, watched satisfaction crater on complex cases, and quietly started rehiring.

[Andrew Ng argues](https://hackernoon.com/andrew-ng-product-team-ratios-evolving-to-just-one-software-developer-for-every-two-product-manager) AI will "significantly increase demand for people who can come up with clear specs for valuable things to build." [Marty Cagan](https://airfocus.com/blog/ai-product-management-marty-cagan/) puts it more bluntly: "For those that really know what Product Discovery is, this is an amazing era." The skill that was always important —  figuring out what to build and why —  is now the only skill that can't be automated away.

## Every role goes up

Developers stop writing code and start owning architecture. PMs stop managing Jira cards and start owning business strategy. Designers stop pushing pixels and start defining the judgment layer between what AI generates and what users actually need.

[Sequoia Capital](https://sequoiacap.com/article/2026-this-is-agi/) describes the shift cleanly: workers will "go from working as an IC to managing a team of agents." In JTBD terms —  the framework I use for product strategy —  this is "going up one level in the Job Graph," which has always been the most powerful value creation mechanism. When a lower-level job gets automated, whoever owns the level above captures all the value.

— -

*Ivan Zamesin is the founder of Zamesin Academy, an ed-tech company that has trained 13,000+ product professionals. He teaches AJTBD-based product strategy and runs BOOST, a vibe coding intensive for product teams.*

— -

## Sources

### Experts and quotes
- [Andrej Karpathy — "vibe coding"](https://en.wikipedia.org/wiki/Vibe_coding) — coined the term, Feb 2025
- [Boris Cherny — "Coding is solved"](https://www.lennysnewsletter.com/p/head-of-claude-code-what-happens) — creator of Claude Code, Lenny's Podcast, Feb 2026
- [Andrew Ng — PM bottleneck](https://hackernoon.com/andrew-ng-product-team-ratios-evolving-to-just-one-software-developer-for-every-two-product-manager) — ratio inversion 8:1 → 1:2
- [Marty Cagan — Product Discovery](https://airfocus.com/blog/ai-product-management-marty-cagan/) — "amazing era for those who know Product Discovery"
- [Sequoia Capital — This Is AGI](https://sequoiacap.com/article/2026-this-is-agi/) — "from IC to managing agents"
- [Tobi Lutke / Shopify — AI-first hiring](https://fortune.com/2025/04/08/shopify-ceo-ai-automation-no-new-hires-tech-jobs/) — "prove AI can't do it"

### Cases and stories
- Medvi — $20K to $401M, 2 employees, AI-built, 2025-2026
- [Dr. Fahim Hussan — health app](https://analyticsindiamag.com/ai-news-updates/doctor-with-no-coding-experience-builds-a-health-app-on-replit-in-just-4-days/) — £175 vs £100K quote, 4 days
- [Pieter Levels — $3.1M solo](https://www.fast-saas.com/blog/pieter-levels-success-story/) — 70+ products, zero employees
- [Klarna — reversed AI layoffs](https://www.digitalapplied.com/blog/klarna-reverses-ai-layoffs-replacing-700-workers-backfired) — replaced 700, then rehired
- [Lazar Jovanovic — professional vibe coder](https://www.lennysnewsletter.com/p/getting-paid-to-vibe-code) — $200M ARR company, no engineering background
- [Salesforce Agentforce](https://hbr.org/2026/02/to-thrive-in-the-ai-era-companies-need-agent-managers) — 74% autonomous resolution

### Data and statistics
- [METR study — 19% slower with AI](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) — 40pp perception gap, Jul 2025
- [SaaSpocalypse — $1T+ wiped](https://techcrunch.com/2026/03/01/saas-in-saas-out-heres-whats-driving-the-saaspocalypse/) — Q1 2026
- [SaaStr — worst rout in SaaS history](https://www.saastr.com/the-saas-rout-of-2026-is-even-worse-than-you-think-for-the-first-time-ever-software-now-trades-at-a-discount-to-the-sp-500/)
- [McKinsey CEO on AI agents — Yahoo Finance](https://finance.yahoo.com/news/mckinseys-ceo-breaks-down-ai-100301404.html)
- [Startup failure rates — 42% no demand](https://www.digitalsilk.com/digital-trends/startup-failure-rate-statistics/)
- [AI code vulnerabilities — 40-62%](https://natively.dev/articles/vibe-coding-limitations)
- [AI technical debt — +30-41%](https://www.infoq.com/news/2025/11/ai-code-technical-debt/)
- [McKinsey — 25K AI agents](https://thefinancestory.com/mckinsey-deploys-12000-ai-agents)
- [Junior dev employment -20%](https://www.technologyreview.com/2025/12/15/1128352/rise-of-ai-coding-developers-2026/)

### Ivan's cases (from repository)
- BOOST launch — idea to revenue in ~8h, two cohorts sold out in 24h
- CRM segmentation — 10 Claude Code agents, 30 min vs 1 week
- 12,000+ students — "fast generator of bad decisions" pattern
