---

## 📝 Инструкция для draft-этапа

ГАЙДЛАЙНЫ ИЗДАНИЯ:

Язык: английский 
Сайт: https://www.mindtheproduct.com

1 000–1 800 слов, лучше около 1 200
Формат: практическая статья для practising product managers с чёткой структурой и actionable insights, а не общий thought leadership
Особенно для AI‑тем: материал обязан содержать практические, применимые советы и/или быть оформлен как полноценный case study, иначе не рассматривается
Короткие абзацы (3–5 предложений), подзаголовки и списки для удобства чтения
Язык: живой, понятный PM‑сообществу, с продуктовой терминологией, но без академичности и маркетингового тона
Фокус на конкретных практиках, фреймворках, примерах из реальной работы; читатель должен понять, что делать “в следующем спринте”
Нужен честный опыт автора: что пробовали, что не сработало, какие выводы сделали

Требования к визуалу:
Перед отправкой драфта нужно подготовить и прислать одно изображение 1600 x 900 px для обложки статьи
Визуал должен быть action‑able / personable / визуально цепляющим и задавать тон статье, не быть случайным стоком

ТЕЗИСЫ — СМОТРИ — оставила пока почти те же, что в статье для стартап гроус гайда, но важно чтобы тексты не были аналогичными иначе это не считается оригинальной статьей, они проверят и в бан нас отправят)
Так что идеально если ты экспертным взглядом поймешь, как раскрыть эту же тему иначе, нежели для фаундеров в стартап гроус гайде! Ну или как минимум перефразировка чтобы абзацев была, чтобы “антиплагиат” не обнаружил
Контекст: появление "vibe coding" tools и паника вокруг исчезновения PM-ролей

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

# Как AI меняет роль продакт-менеджера (condensed для статьи)

> **Статус:** Финальные тезисы для статьи (фаза схождения)
> **Версия:** 3
> **Модель:** claude-opus-4-6
> **Дата:** 2026-02-19 15:30
> **Последняя итерация:** v3 — condensed 12→6 тезисов для статьи по фидбэку автора (А1+А3, А4+А8, удалены А6, А7, H1, H2)
> **Тезисов:** 6
> **Режим:** Agent Team (knowledge-researcher, expert-hunter, contrarian) + Iteration v2 + Condensed v3
> **Coverage Score:** 90.9% (из v2)

---

## Главная тема

Как AI, vibe coding и команды агентов трансформируют роль продакт-менеджера: от "заказчика фич для инженеров" к стратегу, оператору конвейера гипотез и full-stack builder-у. Статья для practicing PMs на mindtheproduct.com — с фреймворками, данными и actionable советами.

---

## Карта экспертов по теме

| Эксперт | Credentials | Ключевой тезис | Источник | Год | Tier |
|---------|-------------|-----------------|----------|-----|------|
| Boris Cherny | Head of Claude Code, Anthropic | 100% кода через Claude Code с ноября 2025; productivity +200%; "coding is largely solved" | Lenny's Podcast interview | 2026 | ⭐⭐⭐ |
| Marc Andreessen | a16z co-founder | "Mexican standoff" PM/eng/design; T→E/F-shaped skills; "superpowered individual"; "don't be fungible" | Lenny's Podcast interview | 2026 | ⭐⭐⭐ |
| Marty Cagan | SVPG founder, "Inspired" автор | PM роль становится MORE essential, но требует strong judgment + AI | [svpg.com](https://www.svpg.com/ai-product-management-2-years-in/) | 2025 | ⭐⭐⭐ |
| Lenny Rachitsky | #1 PM newsletter | 55% PMs: AI превзошёл ожидания; user research — самый большой untapped opportunity | [lennysnewsletter.com](https://www.lennysnewsletter.com/p/ai-tools-are-overdelivering-results) | 2025-2026 | ⭐⭐⭐ |
| Tomer Cohen | LinkedIn CPO | Full-Stack Builder программа; top performers усиливают AI | [lennysnewsletter.com](https://www.lennysnewsletter.com/p/why-linkedin-is-replacing-pms) | 2025 | ⭐⭐⭐ |
| Aparna Chennapragada | Microsoft CPO | Prompt sets = new PRDs; PM становится curriculum designer | [aparnacd.substack.com](https://aparnacd.substack.com/p/prompt-sets-are-the-new-prds) | 2025 | ⭐⭐⭐ |
| Teresa Torres | Continuous Discovery автор | Discovery ещё важнее; AI ускоряет и провалы тоже | [producttalk.org](https://www.producttalk.org/ai-evals-discovery-all-things-product-podcast-with-teresa-torres-petra-wille/) | 2025 | ⭐⭐⭐ |
| Claire Vo | LaunchDarkly CPO, ChatPRD | "Product Management is Dead" — Super ICs заменяют мид-уровень | [chatprd.ai](https://www.chatprd.ai/blog/product-management-is-dead) | 2024 | ⭐⭐⭐ |
| Shreyas Doshi | Ex-Stripe, Twitter PM | AI сжимает feedback loop; 3-4 чел. стартап = импакт 30-50 чел. | [maven.com](https://maven.com/shreyas-doshi/product-management-career) | 2025 | ⭐⭐⭐ |

---

## Тезисы для статьи (6 штук)

---

### Тезис 1: Business Judgment и стратегическое влияние — через psychological safety (merged: А1+А3)

**Суть:**
Абсолютно критичный навык в эпоху нейронок — это business judgment: способность принимать правильные бизнес-решения в условиях неопределённости. Когда AI автоматизирует исполнение, ключевым дифференциатором становится не скорость делания, а качество решений: какие гипотезы проверять, какие рынки выбирать, какие trade-offs делать, как обеспечить прибыль компании. Knowledge Base даёт judgment точное определение через AHEA: это способность диагностировать, ГДЕ в каузальной цепочке (Рынок → Сегменты → Jobs → Ценность → Коммуникация → Юнит-экономика → Прибыль) находится проблема, и сделать ПРАВИЛЬНЫЙ стратегический выбор.

PM-ы будут вынуждены подняться на уровень выше по влиянию на бизнес. Execution-level PM-работа (PRD, user stories, эксперименты) автоматизируется — PM должен подняться до strategy-level. KB даёт математическое доказательство через формулу RAT: когда AI обрушивает стоимость тестирования (знаменатель), доминирует числитель — идентификация рисков и оценка последствий. PM-ы, которые "двигают таски в Task Tracker" — их ТОЧНО заменят. a16z подтверждает: модели генерируют "bland, derivative" идеи — инструменты для ДЕЛАНИЯ есть, для ДУМАНИЯ — нет. Marc Andreessen через Larry Summers: "Don't be fungible" — не будь заменяемым.

Но этот подъём — болезненный процесс. 67% PM сообщают о тревоге по поводу своей роли (Perspective AI). **КРИТИЧЕСКИ ВАЖНЫЙ REFRAME:** То, что выглядит как "ego resistance" — на самом деле rational response на ambiguity. HBR: "Hesitation grounded in ambiguity, not ego." Когда мир турбулентный, лучшее, что вы можете сделать — создать безопасную среду для себя и коллег, чтобы люди могли меняться. Boris Cherny: "You have to give people psychological safety that it's okay to fail."

PM-ы, которые разбираются в бизнесе + используют AI для быстрой реализации — получают огромное карьерное преимущество. Top performers adopt AI fastest.

**Глубина:** 🔬 Глубокий
**Актуальность:** 📅 Вечнозелёный + Актуальный 2025+

**Из Knowledge Base (AURA/AJTBD):**
> "Если на предыдущем шаге цепочки совершена ошибка, следующие шаги не работают."
> — Источник: `Knowledge/AJTBD/fundamentals.md`

> "Приоритет риска = (Вероятность x Последствия) / Стоимость проверки. AI обрушивает знаменатель → числитель (человеческий judgment) доминирует."
> — Источник: `Knowledge/RAT/risk-assumption-test.md`

> "Выход на уровень работы выше — самая мощная механика создания ценности."
> — Источник: `Knowledge/AJTBD/value-creation.md`

> "При запуске нового продукта главный враг -- это эго."
> — Источник: `Knowledge/Algorithms/launch-product.md`

**Экспертные мнения:**
- Marty Cagan (⭐⭐⭐ Tier 1, 📅 2025): "PM с strong judgment + AI tools = winning combination." — [svpg.com](https://www.svpg.com/ai-product-management-2-years-in/)
- a16z (⭐⭐ Tier 2, 📅 2026): "Hard problem перешёл от 'how to build' к 'WHAT to build'." — [a16z.com](https://a16z.com/notes-on-ai-apps-in-2026/)
- Marc Andreessen (⭐⭐⭐ Tier 1, 📅 2026): "Don't be fungible — don't be replaceable." — Lenny's Podcast interview
- HBR (⭐⭐ Tier 2, 📅 2025): "Hesitation grounded in ambiguity, not ego." — [hbr.org](https://hbr.org/2025/11/overcoming-the-organizational-barriers-to-ai-adoption)
- MIT Technology Review (⭐⭐ Tier 2, 📅 2025): Psychological safety > стыд "резисторов". — [technologyreview.com](https://www.technologyreview.com/2025/12/16/1125899/creating-psychological-safety-in-the-ai-era)
- Boris Cherny (⭐⭐⭐ Tier 1, 📅 2026): "Psychological safety that it's okay to fail. 80% of ideas are bad." — Lenny's Podcast interview
- Perspective AI (⭐⭐ Tier 2-3, 📅 2025): "67% PM report anxiety. Microsoft PM: 'I honestly don't know what my job is then.'" — [getperspective.ai](https://getperspective.ai/published/page/6851e02fc1043be42b224395)
- Claire Vo (⭐⭐⭐ Tier 1, 📅 2024): "Super ICs заменяют mid-level PM managers." — [chatprd.ai](https://www.chatprd.ai/blog/product-management-is-dead)
- Tomer Cohen (⭐⭐⭐ Tier 1, 📅 2025): "Top performers adopt AI fastest." — [lennysnewsletter.com](https://www.lennysnewsletter.com/p/why-linkedin-is-replacing-pms)

**⚠️ Контраргументы:**
- Saeed Khan: проблема PM не "task-movers vs стратеги", а структурные проблемы профессии. — [swkhan.medium.com](https://swkhan.medium.com/ai-is-not-going-to-fix-product-management-but-you-can-heres-how-7e06f102b35d)
- Claire Vo: роль не поднимается — она растворяется. AI-native компании откладывают найм PM. — [creatoreconomy.so](https://creatoreconomy.so/p/so-whats-going-to-happen-to-product-management-anyway)

---

### Тезис 2: PM-ы становятся full-stack builders (enriched: Boris Cherny + Marc Andreessen)

**Суть:**
Все PM будут становиться full-stack builder-ами. Точка перелома: ноябрь-декабрь 2025. Boris Cherny (Head of Claude Code): с ноября 2025 100% его кода пишется Claude Code, ни одной строки вручную. Productivity per engineer +200%. 4% всех GitHub коммитов от Claude Code. "Coding is largely solved." "К концу года everyone's going to be a product manager and everyone codes. Титул software engineer заменит builder."

Marc Andreessen: "Mexican standoff" между PM, инженерами и дизайнерами — каждый верит, что может делать работу двух других с AI, и они все правы. T-shaped → E/F-shaped навыки. "The superpowered individual" — глубок в одном + AI помогает быть хорошим в двух других. LinkedIn формализовал: "Associate Product Builder" как карьерная лестница.

**Глубина:** 🔬 Глубокий
**Актуальность:** 📅 Актуальный 2025+ (tipping point Nov-Dec 2025)

**Из Knowledge Base (AURA/AJTBD):**
> "Мы не запускаем продукт --- мы покупаем знания."
> — Источник: `Knowledge/RAT/risk-assumption-test.md`

**Экспертные мнения:**
- Boris Cherny (⭐⭐⭐ Tier 1, 📅 2026): "100% of my code is written by Claude Code. Not edited a single line by hand since November. Productivity per engineer increased 200%. Coding is largely solved." — Lenny's Podcast interview (`Book-and-linkedin/Experts/boris_cherny_interview_transcript.txt`)
- Marc Andreessen (⭐⭐⭐ Tier 1, 📅 2026): "Mexican standoff between PM, eng, design. They're all kind of correct. The additive effect of being good at two things is more than double." — Lenny's Podcast interview (`Book-and-linkedin/Experts/marc_andreessen_transcript.txt`)
- Tomer Cohen, LinkedIn CPO (⭐⭐⭐ Tier 1, 📅 2025): "Full Stack Builder — формальный титул. Platform + Agents + Culture." — [lennysnewsletter.com](https://www.lennysnewsletter.com/p/why-linkedin-is-replacing-pms)

**⚠️ Контраргументы (СИЛЬНЫЕ):**
1. Качество кода: 62% AI-кода содержит security flaws; 1.7x больше major issues. — [thenewstack.io](https://thenewstack.io/vibe-coding-could-cause-catastrophic-explosions-in-2026/)
2. Opportunity cost: час на vibe coding = час НЕ на стратегию. — [bryceyork.com](https://bryceyork.com/vibe-coding-prototypes/)
3. Boris Cherny сам: "I do look at the code. Not at the point where you can be totally hands-off."
4. METR study: разработчики на 19% МЕДЛЕННЕЕ с AI, хотя ДУМАЮТ что на 20% быстрее. — [metr.org](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)

---

### Тезис 3: PM как оператор конвейера гипотез, оркестратор агентов и маленьких команд (merged: А4+А8)

**Суть:**
PM станут управлять конвейером проверки гипотез И оркестрировать флоты AI-агентов в маленьких командах. AI позволяет в единицу времени проверять на порядок больше гипотез — это индустриальный конвейер, не 2-3 гипотезы в спринт. "PM как оператор фабрики." KB: "90% ресурсов инвестируются в мертворожденные фичи" — если можно тестировать 10 идей за время одной, throughput растёт 10x.

Команды становятся меньше. Shreyas Doshi: "3-4 person startups = impact of 30-50." Andreessen: "the most leading edge founders are thinking — can you have entire companies where the founder does everything." Cherny: "Underfund things a little bit — people use Claude and ship quickly. One engineer on a project."

PM сдвигается от документации к curriculum design: PRD мертвы, PM пишет "prompt sets" — живые артефакты, одновременно спецификация и тренировочные данные. Агенты НЕ МОГУТ: стратегия, tradeoff prioritization, ethical judgment — это за PM.

**Глубина:** 🔬 Глубокий
**Актуальность:** 📅 Актуальный 2025+

**Из Knowledge Base (AURA/AJTBD):**
> "Мы не запускаем продукт --- мы покупаем знания."
> — Источник: `Knowledge/RAT/risk-assumption-test.md`

> "90% ресурсов инвестируются в мертворожденные фичи."
> — Источник: `Knowledge/AJTBD/value-creation.md`

**Экспертные мнения:**
- Lenny Rachitsky (⭐⭐⭐ Tier 1, 📅 2025-2026): "PMs экономят 4+ часов в неделю (63%)." — [lennysnewsletter.com](https://www.lennysnewsletter.com/p/ai-tools-are-overdelivering-results)
- Teresa Torres (⭐⭐⭐ Tier 1, 📅 2025): "AI ускоряет и провалы тоже." — [producttalk.org](https://www.producttalk.org/ai-evals-discovery-all-things-product-podcast-with-teresa-torres-petra-wille/)
- Aparna Chennapragada (⭐⭐⭐ Tier 1, 📅 2025): "Prompt sets = new PRDs." — [aparnacd.substack.com](https://aparnacd.substack.com/p/prompt-sets-are-the-new-prds)
- Boris Cherny (⭐⭐⭐ Tier 1, 📅 2026): "Claude is starting to come up with ideas. Looking through feedback, bug reports, telemetry." — Lenny's Podcast interview
- Shreyas Doshi (⭐⭐⭐ Tier 1, 📅 2025): "3-4 person startups with same impact as 30-50." — [maven.com](https://maven.com/shreyas-doshi/product-management-career)
- Marc Andreessen (⭐⭐⭐ Tier 1, 📅 2026): "Founders thinking of entire companies where the founder does everything." — Lenny's Podcast interview

**⚠️ Контраргументы (СИЛЬНЫЕ):**
- METR: 19% МЕДЛЕННЕЕ с AI. AI агенты завершают 2.5% проектов. Gartner: 40%+ agentic AI провалятся к 2027. — [metr.org](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/), [ai2incubator.com](https://www.ai2incubator.com/articles/insights-15-the-state-of-ai-agents-in-2025-balancing-optimism-with-reality)
- Faros AI: AI adoption = 9% рост багов, 154% рост размера PR. Один человек = single point of failure. — [faros.ai](https://www.faros.ai/blog/ai-software-engineering)

---

### Тезис 4: Полный цикл до продакшена и продаж — через 12-24 месяца

**Суть:**
Через год-два появится полный цикл вплоть до тестов и продаж. Сейчас можно делать прототипы, но безопасность и deploy не позволяют катать эксперименты в существующем продукте. Бизнес будет ВЫНУЖДЕН перестроить процессы: от автоматического создания рекламных кампаний до запуска "цифровых продажников."

Boris Cherny: "We're starting to branch out of coding. I use co-work every day for things not related to coding — paying parking tickets, project management, syncing spreadsheets, messaging on Slack."

**Глубина:** 🔬 Средний
**Актуальность:** 📅 Актуальный 2025+ (timeline может быть оптимистичен)

**Экспертные мнения:**
- Brian Chesky (⭐⭐ Tier 2, 📅 2026): "AI is the best thing that ever happened to Airbnb. AI handles a third of customer service." — [fortune.com](https://fortune.com/2026/02/17/airbnb-ceo-brian-chesky-says-ai-best-thing-ever-happened-company-warns-other-founders-get-onboard-or-else/)
- Mind the Product (⭐⭐ Tier 2, 📅 2026): "76% product leaders увеличивают инвестиции в AI в 2026." — [mindtheproduct.com](https://www.mindtheproduct.com/the-2026-ai-product-strategy-huide-how-to-plan-budget-and-build-without-buying-into-the-hype/)
- Boris Cherny (⭐⭐⭐ Tier 1, 📅 2026): "Branching out of coding into general tasks." — Lenny's Podcast interview

**⚠️ Контраргументы:**
AI агенты завершают 2.5% проектов. Только 11% организаций имеют агентов в продакшене. — [ai2incubator.com](https://www.ai2incubator.com/articles/insights-15-the-state-of-ai-agents-in-2025-balancing-optimism-with-reality)

---

### Тезис 5: Спрос на Knowledge Workers растёт, а не падает

**Суть:**
PM, разбирающиеся в JTBD, создании ценности, юнит-экономике + умеющие строить agent pipeline — будут супер востребованы. AI PMs зарабатывают на 35% больше. 75% работодателей не могут найти qualified AI-PM.

Marc Andreessen: "If we didn't have AI, we'd be in a panic about the economy. 50 years of slow technological change + declining population. The timing has worked out miraculously well. Remaining human workers at a premium, not a discount." + "Task loss, not job loss. The job persists longer than the individual tasks."

**Глубина:** 🔬 Средний
**Актуальность:** 📅 Актуальный 2025+ (но survivorship bias!)

**Экспертные мнения:**
- Marc Andreessen (⭐⭐⭐ Tier 1, 📅 2026): "Remaining human workers at a premium. Task loss, not job loss." — Lenny's Podcast interview
- Agents Today (⭐⭐ Tier 2-3, 📅 2025): "AI PMs +35% зарплата. 75% работодателей не находят AI-PM." — [agentstoday.substack.com](https://agentstoday.substack.com/p/agents-today-16-the-great-reshuffling)

**⚠️ Контраргументы (ОЧЕНЬ СИЛЬНЫЕ):**
54,000+ AI-сокращений в US 2025. 40%+ затронули software engineers. 54% eng leaders нанимают МЕНЬШЕ джуниоров. Спрос растёт только для элиты (top 10-20%). — [nationalcioreview.com](https://nationalcioreview.com/articles-insights/extra-bytes/ai-forces-over-50000-layoffs-in-2025-at-leading-technology-firms/)

---

### Тезис 6: Расслоение и K-shaped бифуркация — через psychological safety

**Суть:**
PM-рынок раскалывается в форме K: surging demand на полюсах (AI-специалисты +35% и AI-усиленные senior generalists) при вымывании mid-level ролей. AI-savvy джуниоры outperform senior-ов, создавая "performance inversion".

KB через Four Forces: что тянет к новому (ценность AI), что толкает от старого (frustration), что удерживает (страхи), что держит у старого (привычка — физическое изменение мозга). Люди в 3 раза переоценивают способность сменить привычку.

**REFRAME:** Не "адаптируйся или умри", а "создай безопасную среду". Это не только индивидуальный выбор — СТРУКТУРНОЕ неравенство. Microsoft: AI adoption gap Global North 24.7% vs Global South 14.1%. Совет: не "преодолей эго", а "найди/создай среду, которая поддерживает изменения."

**Глубина:** 🔬 Глубокий
**Актуальность:** 📅 Актуальный 2025+

**Из Knowledge Base (AURA/AJTBD):**
> "Четыре силы: 1. Добавочная ценность (тянет к новому). 2. Проблемы с текущим (толкают от старого). 3. Страхи (удерживают от нового). 4. Привычка (удерживают у старого)."
> — Источник: `Knowledge/AJTBD/main-idea.md`

> "Люди в среднем в 3 раза переоценивали свою способность сменить привычку."
> — Источник: `Knowledge/AJTBD/main-idea.md`

**Экспертные мнения:**
- Agents Today (⭐⭐ Tier 2-3, 📅 2025): "K-shaped bifurcation: middle hollows out." — [agentstoday.substack.com](https://agentstoday.substack.com/p/agents-today-16-the-great-reshuffling)
- HBR (⭐⭐ Tier 2, 📅 2025): "Hesitation grounded in ambiguity, not ego." — [hbr.org](https://hbr.org/2025/11/overcoming-the-organizational-barriers-to-ai-adoption)
- Microsoft (⭐⭐ Tier 2, 📅 2026): AI adoption gap по географии. — [blogs.microsoft.com](https://blogs.microsoft.com/on-the-issues/2026/01/08/global-ai-adoption-in-2025/)

**⚠️ Контраргументы:**
K-shaped framing может быть oversimplified. 54,000+ сокращений — не только вопрос адаптации, но и macro economics. — [nationalcioreview.com](https://nationalcioreview.com/articles-insights/extra-bytes/ai-forces-over-50000-layoffs-in-2025-at-leading-technology-firms/)

---

## Дебаты команды (ключевые споры)

### Спор 1: "PM role MORE essential" vs "PM role is DEAD"
- **Cagan:** PM роль более важна с judgment + AI
- **Claire Vo:** PM роль МЕРТВА; Super ICs заменяют мид-уровень
- **Результат:** ФУНКЦИЯ essential, традиционная СТРУКТУРА РОЛИ умирает

### Спор 2: AI productivity — реальная или иллюзорная?
- **Cherny:** +200% productivity. "Coding is largely solved."
- **METR:** 19% МЕДЛЕННЕЕ, хотя ДУМАЮТ 20% быстрее
- **Результат:** Зависит от уровня навыка. Top engineers реально быстрее, average — нет.

### Спор 3: "Адаптируйся или умри" vs "Создай безопасную среду"
- **Автор v1:** Ego resistance как барьер
- **HBR + MIT + Cherny:** Psychological safety > стыд
- **Результат:** Reframe принят. "Найди/создай среду для безопасных экспериментов."

---

## Примеры и кейсы
- **Boris Cherny / Anthropic** — 100% AI-code since Nov 2025, +200% productivity, "coding is largely solved"
- **Marc Andreessen / a16z** — "Mexican standoff" PM/eng/design, "superpowered individual", "don't be fungible"
- **LinkedIn APB Program** — Associate Product Builder (Dec 2025)
- **Airbnb AI** — Brian Chesky: "best thing ever happened" (Feb 2026)
- **METR Study** — 19% slower despite 20% perceived speedup (July 2025)
- **Perspective AI** — 67% PM report anxiety (June 2025)
- **Spotify** — best developers haven't written code since December (2026)

---

## Все ссылки и источники

### Интервью (эксклюзивные источники)
- Boris Cherny — Lenny's Podcast 2026 (`Book-and-linkedin/Experts/boris_cherny_interview_transcript.txt`)
- Marc Andreessen — Lenny's Podcast 2026 (`Book-and-linkedin/Experts/marc_andreessen_transcript.txt`)

### Knowledge Base
- `Knowledge/AJTBD/fundamentals.md` — каузальная цепочка
- `Knowledge/AJTBD/value-creation.md` — механики создания ценности, эстетика
- `Knowledge/AJTBD/main-idea.md` — Four Forces, привычка
- `Knowledge/RAT/risk-assumption-test.md` — RAT формула
- `Knowledge/AURA/overview.md` — единый организм
- `Knowledge/AURA/product-strategy.md` — стратегический вопрос
- `Knowledge/Algorithms/launch-product.md` — ego как враг #1

### Эксперты Tier 1
- [Marty Cagan](https://www.svpg.com/ai-product-management-2-years-in/) — 2025
- [Lenny Rachitsky](https://www.lennysnewsletter.com/p/ai-tools-are-overdelivering-results) — 2025-2026
- [Tomer Cohen / LinkedIn](https://www.lennysnewsletter.com/p/why-linkedin-is-replacing-pms) — 2025
- [Aparna Chennapragada](https://aparnacd.substack.com/p/prompt-sets-are-the-new-prds) — 2025
- [Teresa Torres](https://www.producttalk.org/ai-evals-discovery-all-things-product-podcast-with-teresa-torres-petra-wille/) — 2025
- [Claire Vo](https://www.chatprd.ai/blog/product-management-is-dead) — 2024
- [Shreyas Doshi](https://maven.com/shreyas-doshi/product-management-career) — 2025
- [Naval Ravikant](https://podcastnotes.org/naval-periscope-sessions/fireside-chat-with-naval-ravikant-niklas-anzinger-ai-technological-progress-vitalia/) — 2024-2025

### Tier 2
- [Brian Chesky](https://fortune.com/2026/02/17/airbnb-ceo-brian-chesky-says-ai-best-thing-ever-happened-company-warns-other-founders-get-onboard-or-else/) — 2026
- [a16z](https://a16z.com/notes-on-ai-apps-in-2026/) — 2026
- [Reforge](https://www.reforge.com/blog/ai-impact-product-management) — 2025
- [HBR](https://hbr.org/2025/11/overcoming-the-organizational-barriers-to-ai-adoption) — 2025
- [MIT Technology Review](https://www.technologyreview.com/2025/12/16/1125899/creating-psychological-safety-in-the-ai-era) — 2025
- [METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) — 2025
- [Saeed Khan](https://swkhan.medium.com/ai-is-not-going-to-fix-product-management-but-you-can-heres-how-7e06f102b35d) — 2025
- [Perspective AI](https://getperspective.ai/published/page/6851e02fc1043be42b224395) — 2025
- [Agents Today](https://agentstoday.substack.com/p/agents-today-16-the-great-reshuffling) — 2025

### Contrarian Sources
- [The New Stack](https://thenewstack.io/vibe-coding-could-cause-catastrophic-explosions-in-2026/) — vibe coding quality
- [Bryce York](https://bryceyork.com/vibe-coding-prototypes/) — opportunity cost
- [National CIO Review](https://nationalcioreview.com/articles-insights/extra-bytes/ai-forces-over-50000-layoffs-in-2025-at-leading-technology-firms/) — layoffs
- [Microsoft AI Economy](https://blogs.microsoft.com/on-the-issues/2026/01/08/global-ai-adoption-in-2025/) — AI divide
- [AI2 Incubator](https://www.ai2incubator.com/articles/insights-15-the-state-of-ai-agents-in-2025-balancing-optimism-with-reality) — agents reality check
- [Faros AI](https://www.faros.ai/blog/ai-software-engineering) — no company-level productivity gain

---

## Рекомендации по усилению статьи

### Для MtP аудитории (practicing PMs)
- Suggested angle: **"The PM Identity Crisis — and What to Do About It"** — начать с 67% anxiety, K-shaped bifurcation, actionable framework
- Другой angle: **"From Feature Factory Operator to Hypothesis Pipeline Engineer"**
- Третий angle: **"AI Won't Replace PMs — But PMs Who Use AI Will Replace PMs Who Don't"**

### Actionable takeaways
- RAT-формула: "вот почему мы тестируем ЭТО, а не ТО"
- "Value backlog" vs "Feature backlog"
- Four Forces как self-assessment tool
- Prompt sets as new PRDs

---

## Исходный поток мыслей

> [Сохранён в полном файле: `Book-and-linkedin/2-Theses/Theses-AI-Changes-PM-Role.md`]
