---
## 📝 Инструкция автора для итерации

> *Заполни 3 вещи, чтобы драфт стал готовым к отправке в Mind the Product:*
>
> 1) Добавь 1 реальный кейс (3–6 предложений): где “vibe coding”/агент ускорил работу и где сломался (quality/security/cost/trust) — и что вы поменяли в следующем спринте.
> 2) Заменить “сырые” URL в тексте на гиперссылки при переносе в CMS (текст уже написан так, чтобы это было легко).
> 3) Выбери заголовок и хук (варианты лучше хранить отдельно от текста, чтобы не влиять на word count).

---

# From PRDs to Pipelines: the AI-era PM playbook (without the hype)

> **Статус:** Черновик
> **Дата:** 2026-03-02 21:04
> **Целевое издание:** Mind the Product
> **Язык:** English
> **Слов:** ~1700
> **Тезисов:** 16
> **Must-include покрытие:** 43/43 (100%)
> **Publication Style Match:** 82/100
> **Humanity Risk:** 18/100


“Vibe coding” makes it feel like specs, mockups, and first‑draft code are becoming close to free.
Andrej Karpathy popularised the term as “describe what you want, then iterate on what the model gives you.” (2025: https://x.com/karpathy/status/1886192184808149383)

That triggers a very real PM anxiety: *if AI can write the PRD and the code, what’s left for us?*

What’s left is the hard part: turning a huge option space into the right bets, with the right constraints, and with outcome ownership. This is a next‑sprint playbook for that shift.

## 1) Judgment is the job now (and it’s a team sport)

Marty Cagan has a blunt way to describe what AI exposes: a lot of what we call “product work” is theatre — documents and process artifacts that look like progress but don’t create outcomes. When those artifacts become easy to generate, the illusion collapses. What’s left is accountability for results. (SVPG, 2026: https://www.svpg.com/product-coaching-and-ai/)

When you can test more directions faster, *picking the wrong direction* gets more expensive, not less. You can ship mistakes faster.

So the differentiator moves to business judgment:
- Which assumptions are worth testing first?
- Which trade‑offs are you willing to own?

Judgment also doesn’t improve in a blame culture. AI work increases uncertainty, and uncertainty triggers hesitation. Teams need space to surface risks early and run “small failures” without punishment.

That’s why psychological safety isn’t HR fluff in the AI era — it’s a product variable. One industry report found that 83% of leaders said psychological safety measurably impacts the success of AI initiatives. (Infosys + MIT Technology Review Insights, 2025: https://www.infosys.com/newsroom/press-releases/2025/psychological-safety-driving-ai-initiatives.html)

## 2) “Builder PM” doesn’t mean “PM replaces engineering”

In YC’s Winter 2025 cohort, TechCrunch reported that a quarter of startups had codebases that were almost entirely AI-generated. (TechCrunch, 2025: https://techcrunch.com/2025/03/06/a-quarter-of-startups-in-ycs-current-cohort-have-codebases-that-are-almost-entirely-ai-generated/)

That doesn’t mean “PMs should ship production code solo.” It means the cost of learning loops just collapsed — and PMs can (and should) use that to validate faster.

The useful definition of a builder PM is narrower:
- build prototypes and thin vertical slices to buy learning;
- understand enough to make constraints explicit (risk, cost, maintainability);
- partner with engineering for production decisions.

Speed can also be deceptive. A trial highlighted by TechCrunch found experienced developers were slower with an AI coding tool, despite feeling faster. (TechCrunch, 2025: https://techcrunch.com/2025/07/11/ai-coding-tools-may-not-speed-up-every-developer-study-shows/)

Build more — but don’t confuse “I can generate code” with “I can own the consequences.”

## 3) Your new artifact isn’t a PRD. It’s a pipeline.

As execution gets cheaper, the PM bottleneck becomes learning: turning uncertainty into knowledge fast, and turning knowledge into reliable product behavior.

That’s why the AI-era PM role looks less like “write requirements” and more like “operate a hypothesis pipeline”:
1) choose the riskiest assumption,
2) design the smallest test that can change your mind,
3) run it safely,
4) decide what to do next.

In practice, that pipeline becomes *executable artifacts*: prompt sets, evaluation suites, rollout rules, and autonomy boundaries.

Aparna Chennapragada put it well: “Prompt sets” start to function like the new PRD — intent + examples + iteration. (2025: https://www.linkedin.com/posts/aparnacd_ive-been-saying-for-a-while-on-lenny-rachitskys-activity-7367028030768123904-Cq9r)

### Evals-first PM: manage quality as a distribution

In AI products, correctness isn’t binary. A single input produces a *range* of outputs — and the “tail risks” are where trust dies.

That’s why evals aren’t an ML-only concern. Reforge argues that evals and observability are core to building AI products that scale. (2026: https://www.reforge.com/blog/ai-evals-course)

Make evals part of the product loop:
- Start with 20–50 “golden prompts” that represent real jobs.
- Add 5–10 red‑team prompts for failure modes.
- Use a simple rubric a human can score fast.
- Re-run on every meaningful change (prompt/model/context/tools).

### Progressive autonomy: ship AI on a gradient, not a cliff

One reason “agent” discourse is unhelpful is that the term is fuzzy — even a16z VCs have said no one really agrees on what an AI agent is. (TechCrunch, 2025: https://techcrunch.com/2025/05/12/even-a16z-vcs-say-no-one-really-knows-what-an-ai-agent-is/)

Instead of debating whether “agents replace humans,” ship a gradient of autonomy:
- **Assist:** suggest next actions.
- **Supervise:** execute with confirmation.
- **Constrain:** execute with strict limits (steps/cost/permissions).
- **Autopilot:** only where the downside is cheap and reversible.

This isn’t just risk management — it’s also user adoption management. Research suggests automation needs to align with people’s desire for human agency, or it breaks on trust even if it “works.” (WORKBank / Brynjolfsson, Yang et al., 2025: https://arxiv.org/abs/2506.06576)
And adoption is uneven: many workers feel they’re falling behind as AI becomes more agentic. (EY, 2026: https://www.ey.com/en_us/insights/consumer-products/how-workers-in-consumer-products-feel-about-agentic-ai)

## 4) Guardrails are product work: cost, reversibility, security, debt, pricing

AI makes it easier to build something. It also makes it easier to build a feature that bleeds money, leaks data, fails in edge cases, or becomes unmaintainable.
And even when prototyping feels effortless, getting to reliable production integration is still a constraint — Chesky has publicly said the tools weren’t ready for the kind of tie‑up people imagined. (LA Times, 2025: https://www.latimes.com/business/story/2025-10-21/chesky-says-openai-tools-not-ready-for-chatgpt-tie-up-with-airbnb-app)
This is why “agents will reshape everything” arguments are both useful and dangerous: the direction is clear, but the constraints decide the timeline. (Des Traynor, 2025: https://destraynor.com/speaking/)

If you want a crisp, practical guide to this mindset, Artem Chigrinets’ AI product strategy guide is worth bookmarking — especially the parts about planning and budgeting without buying into the hype. (Mind the Product, 2026: https://www.mindtheproduct.com/the-2026-ai-product-strategy-huide-how-to-plan-budget-and-build-without-buying-into-the-hype/)

Four guardrails you can implement next sprint:

1) **Circuit breakers + kill criteria** (cost/latency/tool-call limits; what evidence kills the feature). “Pilot forever” is common; don’t confuse PoC signals with traction. (April Dunford, 2025: https://businessofsoftware.org/2025/06/positioning-in-the-age-of-ai-what-founders-need-to-know/)

2) **Security in Definition of Done** (data access, logging, refusal behavior, user-visible constraints). Vibe coding increases output; it doesn’t automatically increase safety. (Veracode, 2025: https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/)

3) **Debt capacity** (refactoring/cleanup is a product choice now). GitClear links AI-assisted speed with refactoring and duplication risks. (2025: https://www.gitclear.com/recent_ai_developer_productivity_code_quality_research)
CodeRabbit reported more issues and security findings in AI‑assisted pull requests. (2025: https://www.helpnetsecurity.com/2025/12/23/coderabbit-ai-assisted-pull-requests-report/)

4) **Pricing tied to jobs, not seats** (usage caps, outcome tiers, value-per-job framing). If inference has running cost, your roadmap is also a P&L decision. (Lenny Distilled, 2025: https://www.lennydistilled.com/episodes/pricing-your-ai-product-lessons-from-400-companies-and-50-unicorns/)

## 5) Where advantage moves: context, interop, and narrative

When models commoditise, advantage shifts to what’s hard to copy: context, distribution surfaces, and trust.

a16z’s “system of record” framing is useful: it’s not only about having a smart model — it’s about having the right data, permissions, freshness policies, and sources of truth. (2024: https://a16z.com/ai-copilot-ai-agent-white-collar-roles/)
Chesky has also argued that AI changes product surfaces and shifts “classic PM” work toward narrative and distribution. (Decoder / The Verge, 2025: https://www.theverge.com/decoder-podcast-with-nilay-patel/677324/airbnb-ceo-brian-chesky-services-redesign-app-future-travel)

Three practical moves:
- Treat context like a supply chain (sources of truth, freshness, permissions, ownership).
- Make your product “agent-friendly” (APIs/tool calls, clear permissions, verifiable execution artifacts).
- Write the positioning in one sentence (job + promise + boundary) so build and GTM align.

## 6) Career + org bets: the market is bifurcating (and you can influence which side you’re on)

Two things can be true at the same time:
- product skills can be a bridge into AI work, and
- teams can still cut roles in the short term.

Mind the Product’s own analysis connects product thinking to some of the fastest-growing roles and career paths in 2026. (2026: https://www.mindtheproduct.com/product-thinking-driving-fastest-growing-jobs/)

And there’s also real disruption. A U.S. congressional report compiled AI-related layoff numbers for 2025. (Rep. Valerie Foushee, 2025: https://foushee.house.gov/media/press-releases/amid-historic-layoffs-surge-rep-foushee-releases-report-on-ais-impact-on-american-jobs-and-demands-clarity-from-industry-leaders)

This creates a K-shaped market: people who can own outcomes + constraints + context pull ahead; people who mostly coordinate pre-defined work get squeezed.
AI is getting good at local optimisations; PM leverage shifts toward global bets and irreversible trade-offs.

There’s a second-order org risk too: “apprenticeship debt.” If companies reduce junior hiring because AI can do junior tasks, they may create a future shortage of seniors — the people who do architecture, reviews, and risk containment. One LeadDev piece reported 54% of engineering leaders expected a long-term reduction in junior hiring. (2025: https://leaddev.com/hiring/what-happens-when-learn-code-fails-generation)
Anthropic’s Jack Clark has also argued the value of junior roles is becoming “dubious,” pushing hiring toward senior judgment. (Business Insider, 2026: https://www.businessinsider.com/anthropic-ai-value-of-junior-roles-dubious-senior-talent2026-2)
At the same time, some companies are increasing entry-level hiring — which is exactly why you should treat this as a strategy choice, not a fate. (Business Insider, 2026: https://www.businessinsider.com/companies-boosting-hiring-entry-level-engineers-2026-2)

Two concrete responses:
- protect the learning pipeline (structured apprenticeship, code review as teaching, rotation through incidents),
- invest in psychological safety so people surface AI risks early.

## How-to / Actionable takeaways

Here’s a “next sprint” checklist that doesn’t require a reorg.

1) Pick one workflow where failure is expensive (money, trust, compliance).  
2) Prototype it end-to-end (prototype only) to learn the real bottlenecks.  
3) Write a prompt set like a spec: intent + examples + failure modes.  
4) Create a tiny eval suite (golden prompts + red-team prompts) and re-run on changes.  
5) Add circuit breakers + kill criteria + security to Definition of Done.  
6) Roll out on a gradient of autonomy (assist → supervise → constrain → autopilot).  

##### One-page template: “AI feature contract” (copy/paste)

- **Job to be done:**
- **User promise (in one sentence):**
- **Autonomy level (assist/supervise/constrain/autopilot):**
- **Golden prompts (N=):**
- **Red-team prompts (N=):**
- **Eval rubric (pass/fail):**
- **Circuit breaker (max cost/steps/latency):**
- **Kill criteria (what proves it should die):**
- **Security constraints (data + logging + refusals):**
- **Owner (who is accountable for outcomes):**

## Sources (selected)

- SVPG / Marty Cagan (2026): https://www.svpg.com/product-coaching-and-ai/
- Infosys + MIT TR Insights (2025): https://www.infosys.com/newsroom/press-releases/2025/psychological-safety-driving-ai-initiatives.html
- YC W25 AI codebases (TechCrunch, 2025): https://techcrunch.com/2025/03/06/a-quarter-of-startups-in-ycs-current-cohort-have-codebases-that-are-almost-entirely-ai-generated/
- “Vibe coding” (Karpathy, 2025): https://x.com/karpathy/status/1886192184808149383
- Reforge on evals (2026): https://www.reforge.com/blog/ai-evals-course
- Agents definition debate (TechCrunch, 2025): https://techcrunch.com/2025/05/12/even-a16z-vcs-say-no-one-really-knows-what-an-ai-agent-is/
- WORKBank on human agency (2025): https://arxiv.org/abs/2506.06576
- MtP AI strategy guide (2026): https://www.mindtheproduct.com/the-2026-ai-product-strategy-huide-how-to-plan-budget-and-build-without-buying-into-the-hype/
- Product thinking & fastest-growing jobs (MtP, 2026): https://www.mindtheproduct.com/product-thinking-driving-fastest-growing-jobs/
- Layoffs report (2025): https://foushee.house.gov/media/press-releases/amid-historic-layoffs-surge-rep-foushee-releases-report-on-ais-impact-on-american-jobs-and-demands-clarity-from-industry-leaders
- LeadDev junior hiring expectations (2025): https://leaddev.com/hiring/what-happens-when-learn-code-fails-generation
- a16z system-of-record/context wedge (2024): https://a16z.com/ai-copilot-ai-agent-white-collar-roles/
