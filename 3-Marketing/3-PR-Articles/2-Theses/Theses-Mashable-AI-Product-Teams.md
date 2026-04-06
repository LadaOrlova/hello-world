---
## 📝 Инструкция для draft-этапа

> *[Это поле заполняет автор — инструкции для следующего этапа (draft)]*

---

## 🔄 Фидбэк автора для итерации

> *[Заполни это поле и запусти `/new-chapter-thesis` снова — скилл автоматически перейдёт в режим доработки]*
>
> Примеры фидбэка:
> - "Углуби тезис 3 — мало конкретики, нужны цифры и кейсы"
> - "Удали тезис 5 — не подходит для этой главы"
> - "Объедини тезисы 2 и 4 — они про одно и то же"
> - "Добавь тезис про влияние AI на {тему}"
> - "Тезис 1 слишком поверхностный — нужно ответить на 'почему' глубже"
> - "Поменяй фокус тезиса 6 с теории на практику"

---

# AI Can Build Your App in a Weekend. Here's Why That's Terrifying for Product Teams

> **Статус:** Отобранные тезисы (после фидбэка автора)
> **Версия:** 2
> **Модель:** claude-opus-4-6
> **Дата:** 2026-04-06 19:15
> **Последняя итерация:** Удалены А2, А10-А12, все Н-тезисы. Объединены А5+А8 → Тезис 4 (Business Judgment).
> **Тезисов:** 7
> **Режим:** Agent Team (knowledge-researcher, expert-hunter, contrarian)
> **Coverage Score:** 89%
> **Раундов итерации:** 2
> **Издание:** Mashable
> **Язык статьи:** English
> **Объём:** 1200-1800 слов

---

## Главная тема

AI coding tools (Claude Code, Cursor, Replit) позволяют одному человеку собрать работающее приложение за выходные. Но настоящая угроза — не для разработчиков, а для продуктовых команд: бутылочное горлышко сместилось от кода к business judgment, и большинство PM к этому не готовы.

---

## Карта экспертов по теме

| Эксперт | Credentials | Ключевой тезис | Источник | Год | Tier |
|---------|-------------|-----------------|----------|-----|------|
| Andrej Karpathy | ex-OpenAI/Tesla AI Lead | Coined "vibe coding" → now says "agentic engineering" | [The New Stack](https://thenewstack.io/vibe-coding-is-passe/) | 2025-2026 | ⭐⭐⭐ |
| Andrew Ng | Stanford, Coursera co-founder | Engineer-to-PM ratios inverting from 8:1 to 1:2 | [HackerNoon](https://hackernoon.com/andrew-ng-product-team-ratios-evolving-to-just-one-software-developer-for-every-two-product-manager) | 2025 | ⭐⭐⭐ |
| Marty Cagan | SVPG founder, author of INSPIRED | "Product owners" threatened; "discovery PMs" empowered | [airfocus](https://airfocus.com/blog/ai-product-management-marty-cagan/) | 2025 | ⭐⭐⭐ |
| Lenny Rachitsky | #1 PM newsletter/podcast | "PMs are now the bottleneck" — complete inversion | [Lenny's Newsletter](https://www.lennysnewsletter.com/p/how-ai-is-reshaping-the-product-role) | 2025 | ⭐⭐⭐ |
| Simon Willison | Creator of Django | Nov 2025 = inflection point; mid-career engineers squeezed | [simonwillison.net](https://simonwillison.net/2026/Jan/4/inflection/) | 2026 | ⭐⭐⭐ |
| Pieter Levels | Solo founder, $3M+/yr | $3.1M/yr across solo-built products, zero employees | [FastSaaS](https://www.fast-saas.com/blog/pieter-levels-success-story/) | 2025 | ⭐⭐⭐ |
| Sam Altman / Dario Amodei | OpenAI CEO / Anthropic CEO | One-person unicorn: 70-80% probability in 2026 | [What's Trending](https://whatstrending.com/sam-altman-predicted-a-one-person-billion-dollar-company-this-guy-just-built-one-with-20000-and-ai/) | 2026 | ⭐⭐⭐ |
| Gergely Orosz | The Pragmatic Engineer | "Two-pizza teams → one-pizza teams"; AI amplifies dysfunction | [Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/the-future-of-software-engineering-with-ai) | 2026 | ⭐⭐⭐ |
| Tobi Lütke | CEO of Shopify | "Prove AI can't do it before you hire" — internal policy | [Fortune](https://fortune.com/2025/04/08/shopify-ceo-ai-automation-no-new-hires-tech-jobs/) | 2025 | ⭐⭐ |
| Sequoia Capital | Top VC firm | Coding agents = "the first example of functional AGI" | [Sequoia](https://sequoiacap.com/article/2026-this-is-agi/) | 2026 | ⭐⭐⭐ |

---

## Тезисы статьи

---

### Тезис 1: Yes, AI Can Build Your App in a Weekend — This Is Not Hype

**Суть:**
Vibe coding — coined by Andrej Karpathy in February 2025 — shifted product creation from writing code to orchestrating AI tools. One person without programming skills can build in 2 months what a team used to build in 6. The breakthrough wasn't just better models — it was the "harness": tools giving AI access to the terminal, file system, and deployment pipeline. A $200/month Claude Code subscription outputs what previously required a team of 5-10 developers. A British doctor built a health-tracking app for under £100 that an agency quoted at £100,000 (Replit case). Medvi — a GLP-1 telehealth company — was built with $20K and AI tools in 2 months, reaching $401M revenue in 2025 with just 2 employees.

**Экспертные мнения:**
- Andrej Karpathy (⭐⭐⭐, 📅 2025): "There's a new kind of coding I call 'vibe coding', where you fully give in to the vibes" — [Wikipedia](https://en.wikipedia.org/wiki/Vibe_coding)
- Simon Willison (⭐⭐⭐, 📅 2026): "November 2025 was an inflection point — models tipped across an invisible capability line" — [simonwillison.net](https://simonwillison.net/2026/Jan/4/inflection/)
- Amjad Masad/Replit (⭐⭐, 📅 2025): ARR soared from $10M to $100M+ in 6 months — [AOL/BI](https://www.aol.com/replits-ceo-says-anyone-build-120211937.html)
- Medvi case: $1.8B projected revenue, 2 employees, $20K investment — [What's Trending](https://whatstrending.com/sam-altman-predicted-a-one-person-billion-dollar-company-this-guy-just-built-one-with-20000-and-ai/)

**⚠️ Контраргументы:**
- 40-62% of AI-generated code contains security vulnerabilities — [Natively.dev](https://natively.dev/articles/vibe-coding-limitations)
- Lovable vulnerability: 1.5M API keys leaked through vibe-coded app (early 2026) — [The New Stack](https://thenewstack.io/vibe-coding-could-cause-catastrophic-explosions-in-2026/)
- Tech debt grows 30-41% within 90 days of AI adoption — [InfoQ](https://www.infoq.com/news/2025/11/ai-code-technical-debt/)

**🔄 Что изменилось в 2025-2026:** Karpathy himself moved past "vibe coding" to "agentic engineering" — the skill is no longer coding, it's orchestrating agents.

---

### Тезис 2: The Product Pipeline Inverted — Build First, Validate Second

**Суть:**
Old pipeline existed because development was expensive: error in dev cost 10-100x more than in research. When code is $200/month, it's cheaper to build an MVP than run a proper CustDev. New pipeline: quick AI research (segments, jobs, competitors, risks) in 1-2 hours → MVP in a few hours → sell to a real person. The CustDev interview becomes a sales call. 10 fast iterations with the live market > 1 long perfect one.

In AJTBD terms, the RAT (Risk Assumption Test) formula changes: Priority = (Probability × Consequences) / Cost of Testing. When testing cost drops from $50-200K to $200/month, all hypotheses "float to the top" for live testing.

**Из Knowledge Base (AURA/AJTBD):**
> "При запуске нового продукта ваша задача не запустить новый продукт, а убить его. Потому что вы бизнес делаете, а не продукты запускаете."
> — `1-Context/AURA-Theses/Algorithms/launch-product.md`

**Экспертные мнения:**
- Pieter Levels (⭐⭐⭐, 📅 2025): Built 70+ products, kills those with no traction within weeks. $3.1M/yr, zero employees — [FastSaaS](https://www.fast-saas.com/blog/pieter-levels-success-story/)
- Sam Altman (⭐⭐⭐, 📅 2023-2026): "10,000-person-equivalent companies run by one person" — [PYMNTS](https://www.pymnts.com/artificial-intelligence-2/2026/the-one-person-billion-dollar-company-is-here/)

**⚠️ Контраргументы (СИЛЬНЫЕ):**
- 42% of startups fail due to no market demand — #1 cause. AI only accelerates this pattern — [DigitalSilk](https://www.digitalsilk.com/digital-trends/startup-failure-rate-statistics/)
- 90-92% of AI startups fail. 38% because they "build products without market demand" — [AI4SP](https://ai4sp.org/why-90-of-ai-startups-fail/)
- Proper validation before building reduces failure rate by 3-4x — [Foundra](https://www.foundra.ai/key-reads/startup-failure-rates-by-stage-data-analysis)

**🔄 Автор о контраргументе:** "Ресерч через нейронки несёт риски: могут быть несуществующие джобы, неточные сегменты. Но MVP, которое ты принёс на интервью, всё равно чуть точнее, чем голые руки. Для стратегии банка с миллиардными бюджетами нельзя делать ресерч только на нейронках."

---

### Тезис 3: What AI Already Does in Product Work

**Суть:**
AI already handles: (a) full MVPs deployed to production; (b) market research — segments, jobs, competitors in 1-2 hours; (c) PRD generation through JTBD methodology interview; (d) data analysis — CSV with 1000 CRM records, updated segmentation in 30 minutes (previously a week with an analyst); (e) hiring — CV screening, structured scoring; (f) context management — team repo as "brain."

PRD quality > coding skills. The AI doesn't get lazy — a massive advantage when writing detailed PRDs.

**Экспертные мнения:**
- Lazar Jovanovic at Lovable (⭐⭐, 📅 2026): Full-time "professional vibe coder" at $200M ARR company, no engineering background — [Lenny's Newsletter](https://www.lennysnewsletter.com/p/getting-paid-to-vibe-code)
- Salesforce Agentforce: resolves 74% of inbound cases autonomously, 350 meetings/week vs. 150/30 days — [HBR](https://hbr.org/2026/02/to-thrive-in-the-ai-era-companies-need-agent-managers)

**⚠️ Контраргументы:**
- 66% of developers say AI output is "almost right, but not quite" — the most dangerous kind of wrong — [MIT Tech Review](https://www.technologyreview.com/2025/12/15/1128352/rise-of-ai-coding-developers-2026/)
- AI code is "highly functional but systematically lacking in architectural judgment" — [arXiv](https://arxiv.org/html/2603.28592)
- 46% of developers actively distrust AI tools (vs. 33% trusting, 3% highly trusting) — [CodeRabbit](https://www.coderabbit.ai/blog/2025-was-the-year-of-ai-speed-2026-will-be-the-year-of-ai-quality)

---

### Тезис 4: Business Judgment — Where AI Fails and Why It's the Only Skill That Matters

**Суть:**
AI fails at strategic decisions with billion-dollar stakes. It fails at "polishing" to high quality — MVP testing is easy, but the last mile requires human craft. It fails at complex integrations. And it degrades past 200K tokens of context.

But the deeper insight: AI is the "delivery truck," not the value itself. When the truck is free, knowing WHERE to deliver becomes exponentially more valuable. AI is augmented intelligence, not artificial. Business judgment = a specific set of knowledge: customer segments (they're not equally valuable), job graph (10+ ways to enter), competitors (how to differentiate), stakeholders, business model (growth points). When you know the whole system, you can make fast, accurate decisions with AI. Without it, you're a "fast generator of bad decisions."

AI is a "bicycle for the product" — Steve Jobs' "bicycle for the mind" applied to product work. But a bicycle is useless if you don't know where to ride. 90% of resources go into stillborn features nobody needs — because teams confuse features with value.

**Из Knowledge Base (AURA/AJTBD):**
> "Фича — не ценность. Это лишь 'грузовик' для доставки ценности. Клиентам плевать на фичи, им нужно изменение состояния."
> — `1-Context/AURA-Theses/AJTBD/value-creation.md`

> "Алгоритм (граф → механики → ресерч → применить механики → ранжировать) впух и прах разбивает подход 'придумать фичу → кастдевить'."
> — `1-Context/AURA-Theses/AJTBD/value-creation.md`

> "90% ресурсов инвестируются в мертворожденные фичи, которые никому не нужны."
> — `1-Context/AURA-Theses/AJTBD/fundamentals.md`

**Экспертные мнения:**
- Marty Cagan (⭐⭐⭐, 📅 2025): "For those that really know Product Discovery, this is an amazing era" — [airfocus](https://airfocus.com/blog/ai-product-management-marty-cagan/)
- Andrew Ng (⭐⭐⭐, 📅 2025): "Writing software is becoming cheaper. This will lead to increased demand for people who can decide what to build." — [HackerNoon](https://hackernoon.com/andrew-ng-product-team-ratios-evolving-to-just-one-software-developer-for-every-two-product-manager)
- Brian Chesky (⭐⭐, 📅 2026): "If you don't disrupt yourself, someone else will" — [Fortune via dnyuz](https://dnyuz.com/2026/02/17/airbnb-ceo-brian-chesky-says-ai-is-the-best-thing-that-ever-happened-to-his-company-now-hes-warning-other-founders-to-get-onboard-pronto-or-else/)

**⚠️ Контраргументы:**
- 60% of executives in 2026 regularly use AI for decision support — [AiTechBoss](https://www.aitechboss.com/ai-decision-systems-2026/)
- AI already makes judgment calls in litigation: "when to file, where to file, when to settle" — [Mosaicapp](https://www.mosaicapp.com/post/the-rise-of-ai-driven-decision-making-in-2026-and-beyond)
- Deloitte: competitive advantage goes to those who know "when to trust AI, when to challenge it, when to override it" — [Deloitte](https://www.deloitte.com/us/en/insights/topics/talent/human-capital-trends/2026/decision-making-with-ai.html)
- METR study (RCT, Jul 2025): experienced devs 19% SLOWER with AI, while BELIEVING 20% faster. 40pp perception gap — [METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)

---

### Тезис 5: The SaaSpocalypse — When Code Costs Zero, Markets Reshape

**Суть:**
When code costs $0, competition explodes, margins compress. SaaS multiples were 13x annual revenue, heading to 3-4x. Code isn't value — if there are no sales, there's no value. Two survival vectors: (a) super-personalization — niche solutions for specific segments; (b) complex industries — manufacturing, healthcare, regulated sectors. Growth point shifts to distribution. CAC rises, margins fall. Winners are those who aim more precisely, not just faster.

Real data: $1T+ in SaaS market cap wiped in Q1 2026. Atlassian (TEAM) plunged 35% in one week. Per-seat pricing model under existential threat.

**Из Knowledge Base (AURA/AJTBD):**
> "cPanel и аналоги — лидеры рынка с падающей выручкой 9+ лет. Причина: конструкторы сайтов подняли уровень — сущность 'хостинг' как класс не существует."
> — `1-Context/AURA-Theses/AJTBD/value-creation.md`

**Экспертные мнения:**
- SaaSpocalypse data: $1T+ wiped, IGV -30% since Sep 2025 — [TechCrunch](https://techcrunch.com/2026/03/01/saas-in-saas-out-heres-whats-driving-the-saaspocalypse/)
- Forrester: "SaaS As We Know It Is Dead" — [Forrester](https://www.forrester.com/blogs/saas-as-we-know-it-is-dead-how-to-survive-the-saas-pocalypse/)
- Bain: market repricing, not dying — [Bain](https://www.bain.com/insights/why-saas-stocks-have-dropped-and-what-it-signals-for-softwares-next-chapter/)

**⚠️ Контраргументы:**
- Gartner: SaaS spending growing from $318B (2025) to $576B by 2029 — [UltraTalent](https://ultratalent.com/blog/saas-industry-trends/)
- "10-20 years of customer lock-in baked into workflows" — [SaaStr](https://www.saastr.com/the-2026-saas-crash-its-not-what-you-think/)
- Vertical SaaS (healthcare, fintech) has "substantially greater chance of survival" — [SaaStr](https://www.saastr.com/the-saas-rout-of-2026-is-even-worse-than-you-think-for-the-first-time-ever-software-now-trades-at-a-discount-to-the-sp-500/)

---

### Тезис 6: Every Role Goes Up One Level of Abstraction

**Суть:**
All specialists rise at least one abstraction level. Developers → architecture and processes. PMs → business strategy (markets, segments, value propositions, business models, partnerships). No more "user stories and Jira cards." In 3 years, code collapses as an abstraction layer: new primitives will be landing pages, funnels, apps, screens, pipelines, digital employees.

In AJTBD terms, this is the most powerful value creation mechanism: "going up one level in the Job Graph." AI kills the jobs below (writing code, data gathering, grooming), forcing people up to the Big Job (business strategy, product-market fit).

**Из Knowledge Base (AURA/AJTBD):**
> "Подъём на уровень выше — это самая мощная стратегия создания ценности и выхода из конкуренции."
> "Многие боятся развития AI именно потому, что AI для огромного количества графов работ даёт возможность подняться на уровень выше."
> — `1-Context/AURA-Theses/AJTBD/graph-of-jobs.md`, `1-Context/AURA-Theses/AJTBD/value-creation.md`

**Экспертные мнения:**
- Gergely Orosz (⭐⭐⭐, 📅 2026): "We are seeing the end of two-pizza teams, becoming one-pizza teams" — [Pragmatic Engineer](https://newsletter.pragmaticengineer.com/p/the-future-of-software-engineering-with-ai)
- Sequoia (⭐⭐⭐, 📅 2026): Users transition "from working as an IC to managing a team of agents" — [Sequoia](https://sequoiacap.com/article/2026-this-is-agi/)
- Gartner: 80% of engineering teams will be smaller AI-augmented units by 2030

**⚠️ Контраргументы:**
- Employment of developers aged 22-25 dropped ~20% between 2022-2025 — they didn't "go up," they got pushed out — [MIT Tech Review](https://www.technologyreview.com/2025/12/15/1128352/rise-of-ai-coding-developers-2026/)
- Saeed Khan: "AI is NOT going to fix Product Management" — problems are cognitive, not instrumental — [Medium](https://swkhan.medium.com/ai-is-not-going-to-fix-product-management-but-you-can-heres-how-7e06f102b35d)

---

### Тезис 7: Teams Are Compressing Radically

**Суть:**
Old: PM + designer + marketer + 4-5 developers. New: PM + 0.5 designer + 0.25 marketer + 1 developer do MORE than the old full team. Example: Ilya Izmailov rewrote in 1.5 months what developers built for 10M rubles. Works alone with two $200 subscriptions. Outputs more than a team of PM + 5 devs + designer + analyst. Secret: nobody told him "you can't."

AURA insight: team compression doesn't just save money — it eliminates the fundamental problem of function desynchronization. When PM + AI does research + build + deploy, the gaps between discovery, delivery, and marketing disappear.

**Из Knowledge Base (AURA/AJTBD):**
> "Маркетинговая стратегия, продуктовая стратегия, бренд-стратегия — три разные стратегии, не синхронизированные."
> — `1-Context/AURA-Theses/AURA/overview.md`

**Экспертные мнения:**
- Dario Amodei (⭐⭐⭐, 📅 2026): One-person unicorn 70-80% probable in 2026 — [TechCrunch](https://techcrunch.com/2025/02/01/ai-agents-could-birth-the-first-one-person-unicorn-but-at-what-societal-cost/)
- McKinsey: trimmed ~5,000 roles, deployed 12,000 internal AI agents
- Shopify Tobi Lütke: "Prove AI can't do it before you hire" — [Fortune](https://fortune.com/2025/04/08/shopify-ceo-ai-automation-no-new-hires-tech-jobs/)

**⚠️ Контраргументы:**
- "The path to one-person businesses is real, but not yet at billion-dollar scale" — [SolunTech](https://www.soluntech.com/blog/the-myth-and-reality-of-the-one-person-billion-dollar-company)
- Code reviews can't keep up with AI output: "Teams generate more code than they could properly review" — [Faros.ai](https://www.faros.ai/blog/ai-software-engineering)

---

## Примеры и кейсы

### Killer examples for Mashable
- **Medvi:** $1.8B projected revenue, 2 employees, built with $20K + AI in 2 months (cautionary note: FDA warning letter Feb 2026)
- **Pieter Levels:** $3.1M/year, zero employees, 70+ products
- **Replit doctor:** Health-tracking app for £100 vs. £100K agency quote
- **Lovable breach:** 1.5M API keys leaked through vibe-coded app (counterpoint)
- **Klarna:** Replaced 700 agents with AI, then reversed — business judgment matters
- **Shopify:** "Prove AI can't do it" internal policy
- **Andrew Ng's ratio:** 8:1 → 1:2 (engineers to PMs)

### Из оригинала автора
- BOOST: research in 1.5-2 hours, MVP in a few hours, Stripe in 3 hours. First cohort sold out in 24 hours.
- Ilya Izmailov: rewrote in 1.5 months what devs did for 10M rubles. "Nobody told him 'you can't.'"
- 10 Claude Code agents reading CRM data → updated segmentation in 30 minutes (previously 1 week)

---

## Все ссылки и источники

### Эксперты Tier 1
- [Andrej Karpathy — Vibe coding](https://en.wikipedia.org/wiki/Vibe_coding) + [passé](https://thenewstack.io/vibe-coding-is-passe/) — 2025-2026
- [Andrew Ng — PM Bottleneck](https://hackernoon.com/andrew-ng-product-team-ratios-evolving-to-just-one-software-developer-for-every-two-product-manager) — 2025
- [Marty Cagan — AI PM](https://airfocus.com/blog/ai-product-management-marty-cagan/) + [SVPG Vision](https://www.svpg.com/a-vision-for-product-teams/) — 2025
- [Lenny Rachitsky — AI PM](https://www.lennysnewsletter.com/p/how-ai-is-reshaping-the-product-role) + [Vibe Coder](https://www.lennysnewsletter.com/p/getting-paid-to-vibe-code) — 2025-2026
- [Simon Willison — Inflection](https://simonwillison.net/2026/Jan/4/inflection/) — 2026
- [Pieter Levels — Solo](https://www.fast-saas.com/blog/pieter-levels-success-story/) — 2025
- [Altman/Amodei — Unicorn](https://whatstrending.com/sam-altman-predicted-a-one-person-billion-dollar-company-this-guy-just-built-one-with-20000-and-ai/) — 2026
- [Gergely Orosz — 6 Predictions](https://newsletter.pragmaticengineer.com/p/the-future-of-software-engineering-with-ai) — 2026
- [Tobi Lütke — Shopify](https://fortune.com/2025/04/08/shopify-ceo-ai-automation-no-new-hires-tech-jobs/) — 2025

### Эксперты Tier 2
- [Sequoia — 2026: This is AGI](https://sequoiacap.com/article/2026-this-is-agi/) — 2026
- [a16z — AI Apps 2026](https://a16z.com/notes-on-ai-apps-in-2026/) — 2026
- [HBR — Agent Managers](https://hbr.org/2026/02/to-thrive-in-the-ai-era-companies-need-agent-managers) — 2026
- [Brian Chesky — Airbnb](https://dnyuz.com/2026/02/17/airbnb-ceo-brian-chesky-says-ai-is-the-best-thing-that-ever-happened-to-his-company-now-hes-warning-other-founders-to-get-onboard-pronto-or-else/) — 2026

### Data & Research
- [METR Study](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) — 19% slower, perception gap, 2025
- [MIT Tech Review — AI Coding](https://www.technologyreview.com/2025/12/15/1128352/rise-of-ai-coding-developers-2026/) — quality crisis, 2025
- [Gartner — Predictions 2026](https://www.gartner.com/en/newsroom/press-releases/2025-10-21-gartner-unveils-top-predictions-for-it-organizations-and-users-in-2026-and-beyond)

### SaaSpocalypse
- [TechCrunch — SaaSpocalypse](https://techcrunch.com/2026/03/01/saas-in-saas-out-heres-whats-driving-the-saaspocalypse/) — 2026
- [Forrester — SaaS is Dead](https://www.forrester.com/blogs/saas-as-we-know-it-is-dead-how-to-survive-the-saas-pocalypse/) — 2026
- [Bain — SaaS Signals](https://www.bain.com/insights/why-saas-stocks-have-dropped-and-what-it-signals-for-softwares-next-chapter/) — 2026

### Counterarguments
- [Natively.dev — Vibe Coding Limits](https://natively.dev/articles/vibe-coding-limitations) — security, 2026
- [The New Stack — Catastrophic Explosions](https://thenewstack.io/vibe-coding-could-cause-catastrophic-explosions-in-2026/) — Lovable breach, 2026
- [InfoQ — AI Tech Debt](https://www.infoq.com/news/2025/11/ai-code-technical-debt/) — 2025
- [Faros.ai — Productivity Paradox](https://www.faros.ai/blog/ai-software-engineering) — deskilling, 2025

### Из Knowledge Base (AURA/AJTBD)
- `1-Context/AURA-Theses/AJTBD/graph-of-jobs.md` — Job Graph, "подъём на уровень выше", Theory of Constraints
- `1-Context/AURA-Theses/AJTBD/value-creation.md` — "фича — не ценность", cPanel precedent
- `1-Context/AURA-Theses/AJTBD/fundamentals.md` — "90% ресурсов в мертворожденные фичи"
- `1-Context/AURA-Theses/AURA/overview.md` — function desynchronization
- `1-Context/AURA-Theses/Algorithms/launch-product.md` — RAT formula

---

## TODO автора
- [ ] Решить: использовать ли Medvi как hook (FDA warning letter — risk?)
- [ ] Адаптировать русскоязычные примеры (BOOST, Илья Измайлов) для западной аудитории
- [ ] Определить: BOOST как кейс автора включать в статью или оставить subtle?

---

## Рекомендуемая структура для Mashable (1200-1800 слов)

| Секция | Слов | Тезисы | Tone |
|--------|------|--------|------|
| Lead paragraph | 50-80 | Тезис 1 + Medvi hook | Dramatic |
| "Yes, it's real" | 150-200 | Тезис 1 (Karpathy arc, examples) | Evidence-heavy |
| "The pipeline flipped" | 150-200 | Тезис 2 (build first, RAT formula) | Insight |
| "What AI already does" | 150-200 | Тезис 3 (capabilities list) | Practical |
| "But here's the catch" | 200-250 | Тезис 4 (business judgment, METR study) | "Fear + hope" |
| "The SaaSpocalypse" | 150-200 | Тезис 5 ($1T wiped, counterpoints) | Data-heavy |
| "Every role goes up" | 150-200 | Тезис 6 (abstraction levels, Job Graph) | Visionary |
| "Teams are shrinking" | 150-200 | Тезис 7 (compression, Shopify policy) | Proof |
| Kicker | 50-80 | Business judgment = the new moat | Actionable |

---

## Исходный поток мыслей

> **Из mashable-thesis.md:**
>
> AI Can Build Your App in a Weekend. Here's Why That's Terrifying for Product Teams
>
> ГАЙДЛАЙНЫ ИЗДАНИЯ: https://mashable.com
> «Здесь и сейчас» текст про ИИ, продукты и будущее работы: фаундеры, PM, айтишники
> Живой, разговорный англ с яркими образами и примерами, без академического тона
> Сочетание «страха и надежды»: капельку драматизируем риски, но даём ясную картину
> 1 200–1 800 слов, разбивка на короткие абзацы, подзаголовки каждые 3–5 абзацев
> Сильный лид‑абзац (2–4 предложения)
>
> Дополнительные источники: вебинары BOOST (вайб-кодинг), подкаст с Кирой Кузьменко
