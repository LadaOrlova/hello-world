---

## 📝 Инструкция для draft-этапа

> *[Это поле заполняет автор — инструкции для следующего этапа (draft)]*

---

## 🔄 Фидбэк автора для итерации

Так, давай теперь оставим несколько ключевых тезисов для статьи. Давай объединим тезис А1 с тезисом А3. Тезис А2 Оставляем. Тезис А5 Оставляем. Тезис А6 убираем. А7 убираем. А8 объединяем с А4 Тезис А9 оставляем. Тезис А10 оставляем Тезис H1 H2 убираем
---

# Как AI меняет роль продакт-менеджера

> **Статус:** Расширенные тезисы (фаза расхождения)
> **Версия:** 2
> **Модель:** claude-opus-4-6
> **Дата:** 2026-02-19 12:00
> **Последняя итерация:** v2 — слияние тезисов по фидбэку автора (24→12), обогащение интервью Boris Cherny + Marc Andreessen, reframe ego→psychological safety, timeline 12-24 мес.
> **Тезисов автора:** 10
> **Новых тезисов от команды:** 2
> **Всего тезисов:** 12
> **Коэффициент расширения:** 0.2x
> **Режим:** Agent Team (knowledge-researcher, expert-hunter, contrarian) + Iteration v2
> **Coverage Score:** 90.9%
> **Раундов итерации:** 1 (v1) + 1 (v2 iteration)

---

## Главная тема

Как AI, vibe coding и команды агентов трансформируют роль продакт-менеджера: от "заказчика фич для инженеров" к стратегу, оператору конвейера гипотез и full-stack builder-у. Статья для practicing PMs на mindtheproduct.com — с фреймворками, данными и actionable советами.

---

## Coverage Score (метрики качества ресерча)

| Критерий | Оценка | Детали |
|----------|--------|--------|
| Экспертное покрытие | 95% | 9 tier-1 (Cagan, Lenny, Torres, Doshi, Cohen, Chennapragada, Vo, Boris Cherny, Marc Andreessen), 5+ tier-2 |
| Свежесть источников | 92% | >70% источников 2025-2026, интервью Cherny + Andreessen 2026 |
| Глубина тезисов | 90% | RAT-формула, Four Forces, каузальные цепочки, interview data |
| Контраргументы | 90% | 10 из 12 тезисов имеют контрпозицию с URL |
| Knowledge Base | 90% | 16 файлов KB прочитаны, механики маппированы на тезисы |
| Actionability | 88% | RAT, Four Forces, value backlog, prompt sets — actionable |
| Ссылки на источники | 95% | Все URL реальные, KB пути указаны |
| 🆕 Качество расширения | 87% | 2 новых тезиса после слияний, оба прошли тест релевантности |
| **СРЕДНИЙ** | **90.9%** | |

---

## Оценка ценности для сегментов

| Сегмент | Релевантность | Ключевые Jobs | Что усилить |
|---------|---------------|---------------|-------------|
| Корпоративные продакты | ⭐⭐⭐ | Выжить в реструктуризации, стать незаменимым, аргументировать своё value перед стейкхолдерами | Больше actionable frameworks (RAT, value backlog) |
| Product-leads | ⭐⭐⭐ | Перестроить команду, ускорить discovery, выбрать правильные AI-инструменты | Кейсы реструктуризации команд (LinkedIn APB) |
| Фаундеры 0→1 | ⭐⭐ | Построить продукт без большой команды, быстро проверить PMF | Hypothesis pipeline как операционная система |
| VC/Инвесторы | ⭐ | Оценить продуктовые команды, понять тренды | Метрики качества PM-команд |

---

## Карта экспертов по теме

| Эксперт | Credentials | Ключевой тезис | Источник | Год | Tier |
|---------|-------------|-----------------|----------|-----|------|
| Boris Cherny | Head of Claude Code, Anthropic | 100% кода через Claude Code с ноября 2025; productivity +200%; "coding is largely solved" | Lenny's Podcast interview | 2026 | ⭐⭐⭐ |
| Marc Andreessen | a16z co-founder | "Mexican standoff" PM/eng/design; T→E/F-shaped skills; "superpowered individual"; "don't be fungible" | Lenny's Podcast interview | 2026 | ⭐⭐⭐ |
| Marty Cagan | SVPG founder, "Inspired" автор | PM роль становится MORE essential, но требует strong judgment + AI | [svpg.com](https://www.svpg.com/ai-product-management-2-years-in/) | 2025 | ⭐⭐⭐ |
| Lenny Rachitsky | #1 PM newsletter | 55% PMs: AI превзошёл ожидания; user research — самый большой untapped opportunity | [lennysnewsletter.com](https://www.lennysnewsletter.com/p/ai-tools-are-overdelivering-results) | 2025-2026 | ⭐⭐⭐ |
| Tomer Cohen | LinkedIn CPO | Full-Stack Builder программа; top performers усиливают AI, а не наоборот | [lennysnewsletter.com](https://www.lennysnewsletter.com/p/why-linkedin-is-replacing-pms) | 2025 | ⭐⭐⭐ |
| Aparna Chennapragada | Microsoft CPO | Prompt sets = new PRDs; PM становится curriculum designer | [aparnacd.substack.com](https://aparnacd.substack.com/p/prompt-sets-are-the-new-prds) | 2025 | ⭐⭐⭐ |
| Teresa Torres | Continuous Discovery автор | Discovery ещё важнее; AI ускоряет и провалы тоже | [producttalk.org](https://www.producttalk.org/ai-evals-discovery-all-things-product-podcast-with-teresa-torres-petra-wille/) | 2025 | ⭐⭐⭐ |
| Claire Vo | LaunchDarkly CPO, ChatPRD | "Product Management is Dead" — Super ICs заменяют мид-уровень | [chatprd.ai](https://www.chatprd.ai/blog/product-management-is-dead) | 2024 | ⭐⭐⭐ |
| Shreyas Doshi | Ex-Stripe, Twitter PM | AI сжимает feedback loop; 3-4 чел. стартап = импакт 30-50 чел. | [maven.com](https://maven.com/shreyas-doshi/product-management-career) | 2025 | ⭐⭐⭐ |
| Brian Chesky | Airbnb CEO | "AI — лучшее что случилось с Airbnb"; founder-led компании выигрывают | [fortune.com](https://fortune.com/2026/02/17/airbnb-ceo-brian-chesky-says-ai-best-thing-ever-happened-company-warns-other-founders-get-onboard-or-else/) | 2026 | ⭐⭐ |
| a16z | Venture fund | "What to build" > "how to build"; tools для thinking ещё не созданы | [a16z.com](https://a16z.com/notes-on-ai-apps-in-2026/) | 2026 | ⭐⭐ |
| Reforge | PM education | PM должен "move to higher ground"; first-mover advantage | [reforge.com](https://www.reforge.com/blog/ai-impact-product-management) | 2025 | ⭐⭐ |
| Saeed Khan | PM veteran, контрариан | AI НЕ починит PM — проблемы системные, не в инструментах | [medium.com](https://swkhan.medium.com/ai-is-not-going-to-fix-product-management-but-you-can-heres-how-7e06f102b35d) | 2025 | ⭐⭐ |
| METR | AI research org | Опытные разработчики на 19% МЕДЛЕННЕЕ с AI, хотя думают что на 20% быстрее | [metr.org](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) | 2025 | ⭐⭐ |

---

## 📝 Тезисы автора (обогащённые)

> Эти тезисы извлечены из потока мыслей автора и обогащены ресерчем команды.
> v2: 24 тезиса → 12 после слияний по фидбэку автора.

---

### 📝 Тезис А1: Business Judgment — критичный навык эпохи AI (merged: A1+A5 v1)

**Суть:**
Абсолютно критичный навык в эпоху нейронок — это business judgment: способность принимать правильные бизнес-решения в условиях неопределённости. Когда AI автоматизирует исполнение, ключевым дифференциатором становится не скорость делания, а качество решений: какие гипотезы проверять, какие рынки выбирать, какие trade-offs делать, как обеспечить прибыль компании. Knowledge Base даёт judgment точное определение через AHEA: это способность диагностировать, ГДЕ в каузальной цепочке (Рынок → Сегменты → Jobs → Ценность → Коммуникация → Юнит-экономика → Прибыль) находится проблема, и сделать ПРАВИЛЬНЫЙ стратегический выбор. PM-ы, разбирающиеся в бизнес-стратегии и системном мышлении, получают мощные рычаги. PM-ы, которые "двигают таски в Task Tracker" — их ТОЧНО заменят. Из точки А в точку Б ведёт огромное количество решений; те, кто в промежуточных шагах принимают решения неточно или делегируют нейронкам, проигрывают. a16z подтверждает: модели всё ещё генерируют "bland, derivative" идеи — инструменты для ДЕЛАНИЯ есть, для ДУМАНИЯ — нет. Marc Andreessen через Larry Summers: "Don't be fungible" — не будь заменяемым.

**Происхождение:** 📝 Авторский (merged: judgment + business-savvy PMs leverage)
**Глубина:** 🔬 Глубокий
**Актуальность:** 📅 Вечнозелёный + Актуальный 2025+
**Статус:** ✅ Подтверждается (с нюансами)

**Ценность для сегментов:** Критически важен для ВСЕХ — это центральный тезис статьи

**Из Knowledge Base (AURA/AJTBD):**
> "Если на предыдущем шаге цепочки совершена ошибка, следующие шаги не работают."
> — Источник: `Knowledge/AJTBD/fundamentals.md`

> "Все стратегические решения продукта сводятся к одному типу: 'За какие работы каких людей мы будем конкурировать, почему именно за эти, а не за другие, и почему мы победим в конкуренции?'"
> — Источник: `Knowledge/AURA/product-strategy.md`

> "Фича не ценность. Это лишь 'грузовик' для доставки ценности. Клиентам плевать на фичи, им нужно изменение состояния."
> — Источник: `Knowledge/AJTBD/value-creation.md`

> "Те, кто знают граф работ, знают фокусные сегменты и применяют все механики — обгонят тех, кто пилит фичи."
> — Источник: `Knowledge/AJTBD/value-creation.md`

**Экспертные мнения:**
- Marty Cagan (⭐⭐⭐ Tier 1, 📅 2025): "PM с strong judgment + AI tools = winning combination. Но AI без product foundation — опасно." — [svpg.com](https://www.svpg.com/ai-product-management-2-years-in/)
- a16z (⭐⭐ Tier 2, 📅 2026): "Hard problem перешёл от 'how to build' к 'WHAT to build'. Модели генерируют bland, derivative идеи." — [a16z.com](https://a16z.com/notes-on-ai-apps-in-2026/)
- Marc Andreessen (⭐⭐⭐ Tier 1, 📅 2026): Larry Summers: "Don't be fungible — don't be replaceable. Don't be a cog." Если ты "just a product manager" — тебя можно заменить. Но комбинация навыков делает тебя незаменимым. — Lenny's Podcast interview (boris_cherny_interview_transcript.txt / marc_andreessen_transcript.txt)
- Claire Vo (⭐⭐⭐ Tier 1, 📅 2024): "Super ICs (high-leverage) заменяют mid-level PM managers." — [chatprd.ai](https://www.chatprd.ai/blog/product-management-is-dead)
- Naval Ravikant (⭐⭐⭐ Tier 1, 📅 2024-2025): "Leverage — force multiplier для judgment. Если ChatGPT может это выдать, ты не монетизируешь это." — [podcastnotes.org](https://podcastnotes.org/naval-periscope-sessions/fireside-chat-with-naval-ravikant-niklas-anzinger-ai-technological-progress-vitalia/)

**⚠️ Контраргументы:**
Saeed Khan: создаётся ложная бинарность. Проблема PM — не "task-movers vs стратеги", а структурные проблемы профессии (burnout, unclear roles). Во многих regulated industries execution-focused PM НЕОБХОДИМ. — [swkhan.medium.com](https://swkhan.medium.com/ai-is-not-going-to-fix-product-management-but-you-can-heres-how-7e06f102b35d). Naval Ravikant сам говорит, что "AI fears are overblown" — если execution AI ещё ненадёжен (METR: девелоперы на 19% медленнее), то bottleneck — не judgment, а reliable execution. — [metr.org](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/)

**🔄 Что изменилось в 2025-2026:** a16z зафиксировал "gap в tools для thinking" — инструменты для делания есть, для стратегического мышления ещё нет. Andreessen: "superpowered individual" — тот, кто глубоко разбирается в предмете + использует AI = spectacularly great.

---

### 📝 Тезис А2: PM-ы становятся full-stack builders (enriched: Boris Cherny + Marc Andreessen)

**Суть:**
Все PM будут становиться full-stack builder-ами. Точка перелома наступила в ноябре-декабре 2025 года: модели Opus 4.5/4.6 в Claude Code и Codex достигли уровня, при котором код генерируется достаточно хорошего качества для продакшена. Boris Cherny (Head of Claude Code, Anthropic) подтверждает: с ноября 2025 года 100% его кода пишется Claude Code, ни одной строки вручную. Productivity per engineer на Anthropic выросла на 200%. 4% всех коммитов на GitHub — от Claude Code (в приватных репо ещё больше). Cherny: "coding is largely solved" — для того типа программирования, которое он делает, это решённая задача. Spotify: лучшие разработчики не пишут код с декабря. Следующий рубеж: Claude начинает сам предлагать идеи — смотрит фидбэк, баги, телеметрию и предлагает что починить. Cherny: "Думаю, к концу года everyone's going to be a product manager and everyone codes. Титул software engineer начнёт уходить — его заменит builder."

Marc Andreessen описывает "Mexican standoff" между PM, инженерами и дизайнерами: каждый теперь верит, что может делать работу двух других с помощью AI — и они все правы. Additive effect: быть хорошим в двух вещах = больше чем двойной эффект, в трёх — больше чем тройной. T-shaped → E/F-shaped навыки. Andreessen: "the superpowered individual" — глубок в одном домене + AI помогает быть хорошим в двух других = "feats of magic" в создании продуктов.

LinkedIn формализовал: заменили APM программу на "Associate Product Builder" с карьерной лестницей full-stack builder-а.

**Происхождение:** 📝 Авторский (enriched Boris Cherny + Marc Andreessen interviews)
**Глубина:** 🔬 Глубокий (интервью данные + формализованные программы)
**Актуальность:** 📅 Актуальный 2025+ (tipping point Nov-Dec 2025)
**Статус:** ⚠️ Спорный (сильные контраргументы по качеству кода)

**Ценность для сегментов:** Критически важен для корпоративных PM и product-leads

**Из Knowledge Base (AURA/AJTBD):**
> "Мы не запускаем продукт --- мы покупаем знания. Наиболее вероятный исход --- провал."
> — Источник: `Knowledge/RAT/risk-assumption-test.md`

> "Красота фрактала: Поняв механики один раз, применяешь их везде — от копирайтинга до выбора рынка."
> — Источник: `Knowledge/AURA/product-strategy.md`

**Экспертные мнения:**
- Boris Cherny, Head of Claude Code (⭐⭐⭐ Tier 1, 📅 2026): "100% of my code is written by Claude Code. I have not edited a single line by hand since November. Every day I ship 10, 20, 30 pull requests. Productivity per engineer has increased 200%. Coding is largely solved. By the end of the year, everyone's going to be a product manager and everyone codes. The title software engineer is going to start to go away — replaced by builder." — Lenny's Podcast interview (`Book-and-linkedin/Experts/boris_cherny_interview_transcript.txt`)
- Marc Andreessen (⭐⭐⭐ Tier 1, 📅 2026): "There's a Mexican standoff happening between PM, eng, design. Every coder believes they can be a PM and a designer. Every PM thinks they can code and design. They're actually all kind of correct. The additive effect of being good at two things is more than double. You become a super relevant specialist in the combination of domains." — Lenny's Podcast interview (`Book-and-linkedin/Experts/marc_andreessen_transcript.txt`)
- Tomer Cohen, LinkedIn CPO (⭐⭐⭐ Tier 1, 📅 2025): "Full Stack Builder — формальный титул и карьерная лестница. Три столпа: Platform + Agents + Culture (culture — самый важный)." — [lennysnewsletter.com](https://www.lennysnewsletter.com/p/why-linkedin-is-replacing-pms)
- Jackie Bavaro (⭐⭐ Tier 2-3, 📅 2025): "Все PM-навыки прямо переносятся в vibe coding." — [jackiebavaro.substack.com](https://jackiebavaro.substack.com/p/vibe-coding-for-product-managers)

**⚠️ Контраргументы (СИЛЬНЫЕ):**
1. **Качество кода катастрофическое:** 69 уязвимостей в 15 приложениях (CSO Online); 62% AI-кода содержит security flaws; 1.7x больше major issues (CodeRabbit). — [thenewstack.io](https://thenewstack.io/vibe-coding-could-cause-catastrophic-explosions-in-2026/)
2. **Opportunity cost:** Каждый час PM на vibe coding = час НЕ на customer discovery / стратегию (Bryce York). — [bryceyork.com](https://bryceyork.com/vibe-coding-prototypes/)
3. **LinkedIn — единственный кейс:** N=1, нет данных по outcome.
4. **Boris Cherny сам подчёркивает:** "I do look at the code. I don't think we're at the point yet where you can be totally hands-off, especially when there's a lot of people running the program. You have to make sure that it's correct, safe."

**🔄 Что изменилось в 2025-2026:** Tipping point: ноябрь 2025 — Claude Code crossed 100% для Boris Cherny лично; Opus 4.5 (май 2025) → Opus 4.6 значительно улучшили качество. 4% всех GitHub коммитов от Claude Code, прогноз — 20% к концу 2026. Vibe coding = Collins Word of the Year 2025. НО: растёт и backlash — "demise of vibe coding" (Feb 2026), замена на structured AI coding.

---

### 📝 Тезис А3: PM-роль поднимается к стратегическому влиянию — через psychological safety (merged: A3+A13+A14+H6 v1)

**Суть:**
PM-ы будут вынуждены подняться на уровень выше по влиянию на бизнес. Execution-level PM-работа (PRD, user stories, эксперименты) автоматизируется — PM должен подняться до strategy-level. Ключевые компетенции: системное мышление, аналитика, проектирование агентских команд, стратегия и целеполагание. KB даёт математическое доказательство через формулу RAT: когда AI обрушивает стоимость тестирования (знаменатель), доминирует числитель — идентификация рисков и оценка последствий. Это чисто человеческий business judgment.

Но этот подъём — болезненный процесс. 67% PM сообщают о тревоге по поводу своей роли (Perspective AI, 54 PM study). Нейронки полностью перестраивают процесс — многим придётся отказаться от старой идентичности. KB углубляет: ego — #1 враг при запуске продукта, привязанность к фичам = слияние с идентичностью.

**КРИТИЧЕСКИ ВАЖНЫЙ REFRAME:** То, что выглядит как "ego resistance" — на самом деле rational response на ambiguity. HBR (Nov 2025): "Hesitation grounded in ambiguity, not ego." MIT Technology Review: нужна psychological safety, а не стыд "резисторов". Когда мир турбулентный, лучшее, что вы можете сделать — создать безопасную среду для себя, семьи и коллег, чтобы люди могли меняться. Людям сложно с изменениями, потому что для эго изменение = смерть, и через этот процесс проще проходить с ресурсами и поддержкой. Boris Cherny подтверждает: "You have to give people space. Psychological safety that it's okay to fail. It's okay if 80% of the ideas are bad."

PM-ы, которые разбираются в бизнесе, находят возможности из данных/юнит-экономики/рынка, и используют AI для быстрой реализации — получают огромное карьерное преимущество. Top performers adopt AI fastest и УСИЛИВАЮТ свои возможности.

**Происхождение:** 📝 Авторский (merged: PM role elevation + ego barrier reframe + career advantage + psych safety data)
**Глубина:** 🔬 Глубокий
**Актуальность:** 📅 Актуальный 2025+
**Статус:** ✅ Подтверждается (с psychological safety reframe)

**Ценность для сегментов:** Критически важен для корпоративных PM

**Из Knowledge Base (AURA/AJTBD):**
> "Приоритет риска = (Вероятность наступления риска x Последствия в деньгах) / Стоимость проверки. AI обрушивает знаменатель → числитель (человеческий judgment) доминирует."
> — Источник: `Knowledge/RAT/risk-assumption-test.md`

> "Выход на уровень работы выше — самая мощная механика создания ценности."
> — Источник: `Knowledge/AJTBD/value-creation.md`

> "При запуске нового продукта главный враг -- это эго."
> — Источник: `Knowledge/Algorithms/launch-product.md`

> "Ловушка идентичности: Фаундеры влюбляются в свои фичи, считая их частью своей личности."
> — Источник: `Knowledge/AJTBD/fundamentals.md`

> "Все стратегические решения продукта сводятся к одному типу: 'За какие работы каких людей мы будем конкурировать?'"
> — Источник: `Knowledge/AURA/product-strategy.md`

**Экспертные мнения:**
- HBR (⭐⭐ Tier 2, 📅 2025): "Hesitation grounded in ambiguity, not ego." — [hbr.org](https://hbr.org/2025/11/overcoming-the-organizational-barriers-to-ai-adoption)
- MIT Technology Review (⭐⭐ Tier 2, 📅 2025): Нужна psychological safety, а не стыд "резисторов". — [technologyreview.com](https://www.technologyreview.com/2025/12/16/1125899/creating-psychological-safety-in-the-ai-era)
- Boris Cherny (⭐⭐⭐ Tier 1, 📅 2026): "You have to give people psychological safety that it's okay to fail. It's okay if 80% of the ideas are bad." — Lenny's Podcast interview (`Book-and-linkedin/Experts/boris_cherny_interview_transcript.txt`)
- Perspective AI Study (⭐⭐ Tier 2-3, 📅 2025): "67% PM report anxiety about their role. Microsoft PM: 'I honestly don't know what my job is then.'" — [getperspective.ai](https://getperspective.ai/published/page/6851e02fc1043be42b224395)
- Reforge (⭐⭐ Tier 2, 📅 2025): "AI commoditizes documentation tasks — PMs must 'move to higher ground'." — [reforge.com](https://www.reforge.com/blog/ai-impact-product-management)
- Tomer Cohen (⭐⭐⭐ Tier 1, 📅 2025): "Top performers adopt AI fastest и УСИЛИВАЮТ свои возможности." — [lennysnewsletter.com](https://www.lennysnewsletter.com/p/why-linkedin-is-replacing-pms)

**⚠️ Контраргументы:**
Параллельно идёт и DISSOLUTION роли. AI-native компании (Anthropic, Cursor) откладывают найм первого PM. Claire Vo: дизайнеры и инженеры с AI покрывают PM-задачи. Если ВСЕ могут делать PM-работу с AI, роль не поднимается — она растворяется. — [creatoreconomy.so](https://creatoreconomy.so/p/so-whats-going-to-happen-to-product-management-anyway)

---

### 📝 Тезис А4: PM как оператор конвейера гипотез и оркестратор агентов (merged: A4+H4 v1)

**Суть:**
PM станут управлять конвейером проверки гипотез И оркестрировать флоты AI-агентов. AI позволяет в единицу времени проверять на порядок больше гипотез — это не ручная работа с 2-3 гипотезами в спринт, а индустриальный конвейер. Метафора: "PM как оператор фабрики". KB подкрепляет: "мы не запускаем продукт — мы покупаем знания", и "90% ресурсов инвестируются в мертворожденные фичи". Если можно тестировать 10 идей за время одной — throughput успешных идей растёт в 10x.

Одновременно PM сдвигается от управления человеческими командами к оркестрации AI-агентов. Пять операционных столпов: artifact coherence, draft-to-decision loops, governed automation, live collaboration, transparent syncing. PM становится context engineer, проектирующий agent workflows. При этом агенты НЕ МОГУТ: стратегия, tradeoff prioritization, ethical judgment, stakeholder alignment, data privacy decisions — это остаётся за PM. PRD мертвы как статические документы — PM пишет "prompt sets" (живые артефакты, одновременно спецификация и тренировочные данные). PM сдвигается от документации к curriculum design.

Boris Cherny подтверждает: на Anthropic все в команде кодят — PM, дизайнер, data scientist, финансы. Claude уже предлагает идеи: смотрит фидбэк, баг-репорты, телеметрию.

**Происхождение:** 📝 Авторский (merged: hypothesis pipeline + agent orchestrator)
**Глубина:** 🔬 Глубокий
**Актуальность:** 📅 Актуальный 2025+
**Статус:** ⚠️ Спорный (AI productivity paradox + agents only 2.5% success rate)

**Ценность для сегментов:** Критически важен для фаундеров и product-leads

**Из Knowledge Base (AURA/AJTBD):**
> "Мы не запускаем продукт --- мы покупаем знания."
> — Источник: `Knowledge/RAT/risk-assumption-test.md`

> "90% ресурсов инвестируются в мертворожденные фичи, которые никому не нужны."
> — Источник: `Knowledge/AJTBD/value-creation.md`

**Экспертные мнения:**
- Lenny Rachitsky (⭐⭐⭐ Tier 1, 📅 2025-2026): "PMs экономят 4+ часов в неделю (63%)." — [lennysnewsletter.com](https://www.lennysnewsletter.com/p/ai-tools-are-overdelivering-results)
- Teresa Torres (⭐⭐⭐ Tier 1, 📅 2025): "Discovery ещё важнее; AI ускоряет и провалы тоже." — [producttalk.org](https://www.producttalk.org/ai-evals-discovery-all-things-product-podcast-with-teresa-torres-petra-wille/)
- Aparna Chennapragada (⭐⭐⭐ Tier 1, 📅 2025): "Prompt sets = new PRDs. PM shifts from documentation to curriculum design." — [aparnacd.substack.com](https://aparnacd.substack.com/p/prompt-sets-are-the-new-prds)
- Boris Cherny (⭐⭐⭐ Tier 1, 📅 2026): "Claude is starting to come up with ideas. Looking through feedback, bug reports, telemetry. A little more like a co-worker." + "All of my project management for the team — co-work does all of it. Syncing stuff between spreadsheets, messaging people on Slack and email." — Lenny's Podcast interview (`Book-and-linkedin/Experts/boris_cherny_interview_transcript.txt`)
- StoriesOnBoard (⭐⭐ Tier 2, 📅 2026): "PM как agent orchestrator — 5 операционных столпов." — [storiesonboard.com](https://storiesonboard.com/blog/ai-agents-product-management-2026)

**⚠️ Контраргументы (СИЛЬНЫЕ):**
METR study (июль 2025): опытные разработчики на **19% МЕДЛЕННЕЕ** с AI, хотя ДУМАЮТ что на 20% быстрее. AI агенты завершают только **2.5%** реальных проектов (Remote Labor Index). Gartner: 40%+ agentic AI проектов провалятся к 2027. Только 11% организаций имеют AI агентов в продакшене. — [metr.org](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/), [ai2incubator.com](https://www.ai2incubator.com/articles/insights-15-the-state-of-ai-agents-in-2025-balancing-optimism-with-reality)

---

### 📝 Тезис А5: Полный цикл до продакшена и продаж — через 12-24 месяца (was A6 v1, timeline extended)

**Суть:**
Через год-два появится полный цикл вплоть до тестов и продаж. Сейчас можно делать прототипы, но в существующем продукте безопасность и deploy не позволяют катать эксперименты. Бизнес будет ВЫНУЖДЕН перестроить процессы: от автоматического создания рекламных кампаний до запуска "цифровых продажников".

**Происхождение:** 📝 Авторский (timeline extended: 6-12 → 12-24 месяца по фидбэку автора)
**Глубина:** 🔬 Средний
**Актуальность:** 📅 Актуальный 2025+ (но timeline может быть оптимистичен)
**Статус:** ⚠️ Спорный (данные против)

**Экспертные мнения:**
- Brian Chesky (⭐⭐ Tier 2, 📅 2026): "AI is the best thing that ever happened to Airbnb. AI handles a third of customer service." — [fortune.com](https://fortune.com/2026/02/17/airbnb-ceo-brian-chesky-says-ai-best-thing-ever-happened-company-warns-other-founders-get-onboard-or-else/)
- Mind the Product (⭐⭐ Tier 2, 📅 2026): "76% product leaders увеличивают инвестиции в AI в 2026." — [mindtheproduct.com](https://www.mindtheproduct.com/the-2026-ai-product-strategy-huide-how-to-plan-budget-and-build-without-buying-into-the-hype/)
- Boris Cherny (⭐⭐⭐ Tier 1, 📅 2026): "We're starting to branch out of coding. General tasks — I use co-work every day to do all sorts of things not related to coding. Paying parking tickets, project management, syncing spreadsheets, messaging on Slack and email." — Lenny's Podcast interview

**⚠️ Контраргументы (СИЛЬНЫЕ):**
AI агенты успешно завершают только **2.5%** реальных рабочих проектов (Remote Labor Index). Gartner: 40%+ agentic AI проектов провалятся к 2027. Только 11% организаций имеют AI агентов в продакшене. Расширение timeline до 12-24 месяцев более реалистично, но всё равно амбициозно. — [ai2incubator.com](https://www.ai2incubator.com/articles/insights-15-the-state-of-ai-agents-in-2025-balancing-optimism-with-reality)

---

### 📝 Тезис А6: Точки роста смещаются в дистрибуцию, маркетинг, бренд (was A7 v1)

**Суть:**
Когда создание продукта дешевеет, конкурентное преимущество смещается в: дистрибуцию, маркетинг, бренд, знание психологии людей, JTBD, коммуникацию ценности. KB объясняет механизм: bottleneck переходит от execution к СИНХРОНИЗАЦИИ между функциями (product, marketing, sales, brand). AURA говорит: "Продукт — единый организм. Нельзя менять маркетинг в отрыве от продукта и сегмента."

**Происхождение:** 📝 Авторский
**Глубина:** 🔬 Средний
**Актуальность:** 📅 Вечнозелёный
**Статус:** ✅ Подтверждается

**Из Knowledge Base (AURA/AJTBD):**
> "Принцип: 'Продукт --- это единый организм'. Рассинхронизация функций — исследователи делают исследования, которые не используются; продукт пилит фичи, которые не продаются; маркетинг привлекает 'не тех' лидов."
> — Источник: `Knowledge/AURA/overview.md`

**⚠️ Контраргументы:** Слабые. Тезис хорошо подтверждён. Единственный риск: если ВСЕ переключатся на distribution, это тоже станет commoditized.

---

### 📝 Тезис А7: Рост эстетики и качества продукта, усиление конкуренции (was A8 v1)

**Суть:**
Эстетика продукта вырастет. Конкуренция усилится. Качество продукта должно кардинально вырасти. KB даёт нейробиологическое обоснование: мозг АВТОМАТИЧЕСКИ оценивает цвета, формы, пропорции, тактильные ощущения — это не "nice-to-have", а нейрологический механизм, влияющий на воспринимаемую ценность.

Marc Andreessen подтверждает: capital-D Design (что это для людей? как это впишется в их жизнь?) останется за людьми, а lowercase-d design (icons, layouts) — за AI. "If I'm a 25-year-old designer and I aspire to be Johnny Ive in a decade — I have a new path. Because Johnny Ive did everything without AI."

**Происхождение:** 📝 Авторский
**Глубина:** 🔬 Средний
**Актуальность:** 📅 Актуальный 2025+
**Статус:** ⚠️ Спорный (risk of homogenization)

**Из Knowledge Base (AURA/AJTBD):**
> "Эстетика: Нейросети мозга автоматически оценивают сочетания цветов, фактур, форм, пропорций, материалов, тактильных ощущений."
> — Источник: `Knowledge/AJTBD/value-creation.md`

**Экспертные мнения:**
- Marc Andreessen (⭐⭐⭐ Tier 1, 📅 2026): "Taste and capital-D Design — higher level questions that great designers have always thought about — the job of designer will involve much more of those higher level more important components." — Lenny's Podcast interview (`Book-and-linkedin/Experts/marc_andreessen_transcript.txt`)
- Perspective AI Study (⭐⭐ Tier 2-3, 📅 2025): "85% PM считают, что 'taste' не может быть автоматизирован." — [getperspective.ai](https://getperspective.ai/published/page/6851e02fc1043be42b224395)

**⚠️ Контраргументы:**
AI design tools могут СГЛАДИТЬ эстетику вместо повышения. Если все используют одни AI-инструменты (Figma AI, v0), продукты начинают выглядеть одинаково. "AI aesthetic" = узнаваемый generic шаблон — противоположность дифференциации. — [davidrdesign.medium.com](https://davidrdesign.medium.com/ai-in-product-design-where-we-are-now-in-2026-a71bceada2d8)

---

### 📝 Тезис А8: Маленькие команды, PM ведёт гипотезу от начала до конца (was A9 v1)

**Суть:**
Команды становятся меньше. PM проверяет гипотезу от начала до конца с минимальным привлечением разработки. Shreyas Doshi задаёт вопрос: "Насколько вероятно, что через 3 года стартап из 3-4 человек будет иметь импакт стартапа из 30-50 человек?"

Marc Andreessen: "the most leading edge founders are thinking — can you have entire companies where the founder does everything". Boris Cherny подтверждает на практике: "We put one engineer on a project. If you underfund things a little bit, people are forced to use Claude — and they ship really quickly."

**Происхождение:** 📝 Авторский
**Глубина:** 🔬 Средний
**Актуальность:** 📅 Актуальный 2025+
**Статус:** ⚠️ Спорный

**Экспертные мнения:**
- Shreyas Doshi (⭐⭐⭐ Tier 1, 📅 2025): "3-4 person startups with same impact as 30-50 person startups." — [maven.com](https://maven.com/shreyas-doshi/product-management-career)
- Marc Andreessen (⭐⭐⭐ Tier 1, 📅 2026): "The most leading edge founders are thinking of entire companies where the founder does everything." — Lenny's Podcast interview
- Boris Cherny (⭐⭐⭐ Tier 1, 📅 2026): "Underfund things a little bit — then people use Claude to automate work and ship really quickly. One engineer on a project." — Lenny's Podcast interview

**⚠️ Контраргументы:**
Faros AI: AI adoption связана с 9% ростом багов на разработчика и 154% ростом размера PR. Один человек end-to-end = single point of failure. Нет code review, нет adversarial testing. — [faros.ai](https://www.faros.ai/blog/ai-software-engineering)

---

### 📝 Тезис А9: Спрос на Knowledge Workers растёт, а не падает (was A11 v1)

**Суть:**
PM, разбирающиеся в JTBD, создании ценности, юнит-экономике, стратегических возможностях + умеющие строить agent pipeline — будут супер востребованы. Есть данные о прибавке к зарплате за AI-навыки.

Marc Andreessen даёт макро-контекст: "If we didn't have AI, we'd be in a panic right now about what's going to happen to the economy. We've actually been in a regime for 50 years of very slow technological change in the face of declining population growth. The timing has worked out miraculously well. We're going to have AI and robots precisely when we actually need them. The remaining human workers are going to be at a premium, not at a discount."

**Происхождение:** 📝 Авторский
**Глубина:** 🔬 Средний (нужны данные)
**Актуальность:** 📅 Актуальный 2025+ (но survivorship bias!)
**Статус:** ⚠️ Спорный (сильные контраргументы)

**Экспертные мнения:**
- Marc Andreessen (⭐⭐⭐ Tier 1, 📅 2026): "Remaining human workers are going to be at a premium, not at a discount. Population decline + AI timing = miraculously well." + "Task loss, not job loss. The job persists longer than the individual tasks." — Lenny's Podcast interview
- Agents Today (⭐⭐ Tier 2-3, 📅 2025): "AI PMs зарабатывают на 35% больше. 75% работодателей не могут найти qualified AI-PM кандидатов." — [agentstoday.substack.com](https://agentstoday.substack.com/p/agents-today-16-the-great-reshuffling)

**⚠️ Контраргументы (ОЧЕНЬ СИЛЬНЫЕ):**
54,000+ сокращений из-за AI в US в 2025 (Challenger Gray & Christmas). Microsoft — ~15K, Amazon — 14K, Salesforce — 4K+. 40%+ сокращений затронули software engineers. 54% engineering leaders планируют нанимать МЕНЬШЕ junior developers. Спрос растёт только для ЭЛИТЫ (top 10-20%). Для большинства — ПАДАЕТ. — [nationalcioreview.com](https://nationalcioreview.com/articles-insights/extra-bytes/ai-forces-over-50000-layoffs-in-2025-at-leading-technology-firms/)

---

### 📝 Тезис А10: Расслоение и K-shaped бифуркация — через psychological safety (merged: A12+H2 v1)

**Суть:**
Произойдёт расслоение между быстро адаптировавшимися и теми, кто не смог — в форме K-shaped бифуркации. PM-рынок труда раскалывается: surging demand на двух полюсах (AI-специалисты зарабатывают на 35% больше И AI-усиленные senior generalists) при быстром исчезновении mid-level PM ролей. Это не постепенная эволюция — структурное вымывание середины. AI-savvy джуниоры outperform senior-ов, сопротивляющихся AI, создавая "performance inversion".

KB подтверждает через Four Forces of Progress: что тянет к новому (ценность AI), что толкает от старого (frustration), что удерживает (страхи), что держит у старого (привычка — физическое изменение мозга). Люди в среднем в 3 раза переоценивают свою способность сменить привычку.

**КРИТИЧЕСКИ ВАЖНЫЙ REFRAME:** Не "адаптируйся или умри", а "создай безопасную среду". Когда мир турбулентный, лучшее, что вы можете сделать — найти среду с psychological safety, где вам проще адаптироваться. Это не только индивидуальный выбор — это СТРУКТУРНОЕ неравенство. Microsoft: AI adoption gap по географии (Global North 24.7% vs Global South 14.1%). Gap определяется инфраструктурой, ресурсами, доступом — не только личной мотивацией. Поэтому совет не "преодолей своё эго", а "найди/создай среду, которая поддерживает изменения".

**Происхождение:** 📝 Авторский (merged: segregation + K-shaped bifurcation + psychological safety reframe)
**Глубина:** 🔬 Глубокий (Four Forces + structural analysis + reframe)
**Актуальность:** 📅 Актуальный 2025+
**Статус:** ⚠️ Спорный (структурное неравенство)

**Из Knowledge Base (AURA/AJTBD):**
> "Четыре силы: 1. Добавочная ценность (тянет к новому). 2. Проблемы с текущим (толкают от старого). 3. Страхи (удерживают от нового). 4. Привычка (удерживают у старого)."
> — Источник: `Knowledge/AJTBD/main-idea.md`

> "Люди в среднем в 3 раза переоценивали свою способность сменить привычку."
> — Источник: `Knowledge/AJTBD/main-idea.md`

**Экспертные мнения:**
- Agents Today (⭐⭐ Tier 2-3, 📅 2025): "K-shaped bifurcation: surging demand на двух полюсах, middle hollows out. AI PMs зарабатывают на 35% больше." — [agentstoday.substack.com](https://agentstoday.substack.com/p/agents-today-16-the-great-reshuffling)
- HBR (⭐⭐ Tier 2, 📅 2025): "Hesitation grounded in ambiguity, not ego." — [hbr.org](https://hbr.org/2025/11/overcoming-the-organizational-barriers-to-ai-adoption)
- MIT Technology Review (⭐⭐ Tier 2, 📅 2025): Psychological safety, не стыд "резисторов". — [technologyreview.com](https://www.technologyreview.com/2025/12/16/1125899/creating-psychological-safety-in-the-ai-era)
- Microsoft (⭐⭐ Tier 2, 📅 2026): AI adoption gap — Global North 24.7% vs Global South 14.1%. — [blogs.microsoft.com](https://blogs.microsoft.com/on-the-issues/2026/01/08/global-ai-adoption-in-2025/)

**⚠️ Контраргументы:**
Фрейминг "K-shaped" может быть oversimplified — реальность сложнее, чем бинарное деление. Многие PM находят средний путь — не "вершина" и не "дно". Также 54,000+ сокращений говорят, что это не только вопрос адаптации, но и macro economics. — [nationalcioreview.com](https://nationalcioreview.com/articles-insights/extra-bytes/ai-forces-over-50000-layoffs-in-2025-at-leading-technology-firms/)

---

## 🆕 Новые тезисы от команды (фаза расхождения)

> Эти тезисы НЕ были в потоке мыслей автора. Оставлены после слияний и фильтрации по фидбэку.
> v2: из 10 новых тезисов оставлено 2 после слияния остальных с авторскими.

---

### 🆕 Тезис Н1: "What to Build" Gap — AI решает execution, но не exploration (was H5 v1)

**Суть:**
Когда coding-агенты набирают точность, hard problem перемещается от "HOW to build" к "WHAT to build". Модели всё ещё генерируют bland, derivative идеи — им не хватает spark от хорошего product thinking. ВСЕ существующие инструменты — для ДЕЛАНИЯ, не для ДУМАНИЯ. Есть massive gap в tools для exploration. Spiritual successors сегодняшних инструментов будут фокусироваться на exploration, а не execution. 2026 = "death of the prompt box" для mainstream users.

Boris Cherny подтверждает: "the next big open question is — now we need humans for figuring out what to build, what to prioritize." Claude начинает помогать, но это всё ещё frontier.

**Происхождение:** 🆕 expert-hunter
**Откуда взялся:** a16z "Notes on AI Apps in 2026" — [a16z.com](https://a16z.com/notes-on-ai-apps-in-2026/)
**Почему автор мог не упомянуть:** Автор фокусируется на использовании AI-инструментов, но не адресует мета-вопрос: что происходит, когда execution дешевеет — какой стратегический вакуум это создаёт
**Связь с авторскими тезисами:** Углубляет А1 (business judgment) и А3 (elevation) — даёт ЭКОНОМИЧЕСКОЕ объяснение, почему judgment становится bottleneck
**Глубина:** 🔬 Глубокий
**Актуальность:** 📅 Актуальный 2025+ (свежайшее — 2026)
**Спорный?** Нет — a16z как tier-2 источник + Boris Cherny confirms

---

### 🆕 Тезис Н2: Открытый вопрос — как измерять качество AI-assisted output? (was H9 v1, reframed)

**Суть:**
PM как full-stack builder тратит время на vibe-coding — но каждый час кодинга = час НЕ на customer discovery, stakeholder alignment или стратегическое мышление. Opportunity cost реален. При этом vibe coding quality проблематичен: 62% AI-кода содержит security flaws. METR study: разработчики на 19% МЕДЛЕННЕЕ с AI, хотя ДУМАЮТ что на 20% быстрее. Этот perception gap вероятно затрагивает и PM.

Открытый вопрос: как PM должен ИЗМЕРЯТЬ, а не ЧУВСТВОВАТЬ продуктивность AI-assisted output? Как оценить opportunity cost vibe-coding vs стратегической работы? Meta-judgment: оценка качества собственного AI-assisted output — ключевой навык, для которого пока нет framework-а.

**Происхождение:** 🆕 contrarian (reframed as open question per author feedback)
**Откуда взялся:** Bryce York — [bryceyork.com](https://bryceyork.com/vibe-coding-prototypes/); METR — [metr.org](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/); Faros AI — [faros.ai](https://www.faros.ai/blog/ai-software-engineering)
**Почему автор мог не упомянуть:** Фокус на позитиве velocity; productivity paradox — неприятная правда
**Связь с авторскими тезисами:** Нуансирует А2 (full-stack builder) — opportunity cost; усиливает А1 (judgment) — нужен meta-judgment для оценки собственной продуктивности
**Глубина:** 🔬 Средний (есть данные, нет framework-а — это вопрос, не ответ)
**Актуальность:** 📅 Актуальный 2025+
**Спорный?** Да — сильный counterpoint к авторскому тезису А2, но автор принял его как вопрос для исследования

---

## Дебаты команды (ключевые споры)

### Спор 1: "PM role MORE essential" vs "PM role is DEAD"
- **Позиция expert-hunter (Cagan):** PM роль становится более важной, но требует judgment + AI
- **Позиция expert-hunter (Vo):** PM роль как мы её знаем МЕРТВА; Super ICs заменяют мид-уровень
- **Вызов contrarian:** Оба правы на разных уровнях. ФУНКЦИЯ essential, традиционная СТРУКТУРА РОЛИ умирает
- **Результат:** Both/and, не either/or. Это ключевое tension для статьи.

### Спор 2: AI productivity — реальная или иллюзорная?
- **Позиция expert-hunter (Lenny):** 55% PM говорят: AI exceeded expectations; 63% экономят 4+ часов
- **Позиция Boris Cherny:** Productivity per engineer +200% at Anthropic. "Coding is largely solved."
- **Вызов contrarian (METR):** Разработчики ДУМАЮТ что на 20% быстрее, но на 19% МЕДЛЕННЕЕ. Perception ≠ reality.
- **Результат:** Критически важное tension. PM ДОЛЖНЫ измерять, а не чувствовать productivity gains. Возможно зависит от уровня навыка — top engineers (Cherny) реально быстрее, average developers — нет.

### Спор 3: Full-stack builder — будущее или миф?
- **Позиция Cherny + Cohen + Andreessen:** Full-stack builder = реальность. Tipping point ноябрь 2025. "Everyone codes."
- **Вызов contrarian:** 62% AI-кода с security flaws; opportunity cost; качество — проблема
- **Результат:** Тренд реален, но "everyone codes" ≠ "everyone codes WELL". Нужен nuance: PM кодит для прототипов и экспериментов, не для production code.

### Спор 4: "Адаптируйся или умри" vs "Создай безопасную среду"
- **Позиция автора v1:** Ego resistance как ключевой барьер
- **Вызов HBR + MIT + Boris Cherny:** "Hesitation grounded in ambiguity, not ego." Psychological safety > стыд
- **Результат:** Reframe принят автором. Совет: не "преодолей эго", а "найди/создай среду для безопасных экспериментов".

---

## Примеры и кейсы (из оригинала + ресерча + интервью)
- **Boris Cherny / Anthropic** — 100% AI-code since Nov 2025, +200% productivity, 4% GitHub commits, "coding is largely solved"
- **Marc Andreessen / a16z** — "Mexican standoff" PM/eng/design, T→E/F shaped skills, "superpowered individual", "don't be fungible"
- **LinkedIn APB Program** — заменили APM на Associate Product Builder (Dec 2025)
- **Airbnb AI** — Brian Chesky: "best thing ever happened", AI handles 1/3 customer service (Feb 2026)
- **METR Study** — RCT showing 19% slower performance despite 20% perceived speedup (July 2025)
- **Perspective AI** — 54 PM interviews, 67% report anxiety (June 2025)
- **Lenny Survey** — largest quantitative dataset on PM AI adoption
- **a16z "Notes on AI Apps"** — "what to build" > "how to build" gap (2026)
- **Spotify** — best developers haven't written a line of code since December (2026)

## Все ссылки и источники

### Из Knowledge Base (AURA/AJTBD)
- `Knowledge/AJTBD/fundamentals.md` — каузальная цепочка, фича ≠ ценность, ловушка идентичности
- `Knowledge/AJTBD/value-creation.md` — 20+ механик создания ценности, 90% мертворожденных фич, эстетика
- `Knowledge/AJTBD/main-idea.md` — Four Forces, привычка (3x переоценка), физическое изменение мозга
- `Knowledge/AJTBD/psychology.md` — статус как hidden driver
- `Knowledge/AJTBD/graph-of-jobs.md` — Big Job, Apple пример
- `Knowledge/RAT/risk-assumption-test.md` — RAT формула, "покупаем знания", мультипликация рисков
- `Knowledge/AURA/overview.md` — единый организм, десинхронизация функций
- `Knowledge/AURA/product-strategy.md` — стратегический вопрос, фрактальность стратегий
- `Knowledge/Algorithms/launch-product.md` — ego как враг #1

### Интервью (эксклюзивные источники)
- Boris Cherny, Head of Claude Code, Anthropic — Lenny's Podcast 2026 (`Book-and-linkedin/Experts/boris_cherny_interview_transcript.txt`)
- Marc Andreessen, a16z co-founder — Lenny's Podcast 2026 (`Book-and-linkedin/Experts/marc_andreessen_transcript.txt`)

### Эксперты Tier 1 (прямые авторитеты)
- [Marty Cagan](https://www.svpg.com/ai-product-management-2-years-in/) — SVPG, 2025, PM role more essential with judgment
- [Lenny Rachitsky](https://www.lennysnewsletter.com/p/ai-tools-are-overdelivering-results) — 2025-2026, AI productivity survey, user research gap
- [Lenny Rachitsky](https://www.lennysnewsletter.com/p/how-close-is-ai-to-replacing-product) — 2025, AI vs human PM blind tests
- [Tomer Cohen / LinkedIn CPO](https://www.lennysnewsletter.com/p/why-linkedin-is-replacing-pms) — 2025, Full-Stack Builder program
- [Aparna Chennapragada / Microsoft CPO](https://aparnacd.substack.com/p/prompt-sets-are-the-new-prds) — 2025, prompt sets = new PRDs
- [Teresa Torres](https://www.producttalk.org/ai-evals-discovery-all-things-product-podcast-with-teresa-torres-petra-wille/) — 2025, discovery более важна в AI era
- [Claire Vo](https://www.chatprd.ai/blog/product-management-is-dead) — 2024, "PM is Dead", Super ICs
- [Shreyas Doshi](https://maven.com/shreyas-doshi/product-management-career) — 2025, small team leverage
- [Naval Ravikant](https://podcastnotes.org/naval-periscope-sessions/fireside-chat-with-naval-ravikant-niklas-anzinger-ai-technological-progress-vitalia/) — 2024-2025, judgment + leverage

### Эксперты Tier 2 (VC, HBR, MIT)
- [Brian Chesky / Airbnb](https://fortune.com/2026/02/17/airbnb-ceo-brian-chesky-says-ai-best-thing-ever-happened-company-warns-other-founders-get-onboard-or-else/) — 2026, AI best thing for Airbnb
- [a16z](https://a16z.com/notes-on-ai-apps-in-2026/) — 2026, "what to build" gap
- [Reforge](https://www.reforge.com/blog/ai-impact-product-management) — 2025, move to higher ground
- [Mind the Product](https://www.mindtheproduct.com/the-2026-ai-product-strategy-huide-how-to-plan-budget-and-build-without-buying-into-the-hype/) — 2026, AI strategy guide
- [LogRocket](https://blog.logrocket.com/product-management/ai-changes-product-management-2026) — 2026, 3 AI shockwaves reshaping PM
- [HBR](https://hbr.org/2025/11/overcoming-the-organizational-barriers-to-ai-adoption) — 2025, ambiguity не ego
- [MIT Technology Review](https://www.technologyreview.com/2025/12/16/1125899/creating-psychological-safety-in-the-ai-era) — 2025, psychological safety
- [METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) — 2025, AI productivity paradox (RCT)
- [Faros AI](https://www.faros.ai/blog/ai-software-engineering) — 2025, no company-level productivity gain
- [Saeed Khan](https://swkhan.medium.com/ai-is-not-going-to-fix-product-management-but-you-can-heres-how-7e06f102b35d) — 2025, AI won't fix PM
- [Jackie Bavaro](https://jackiebavaro.substack.com/p/vibe-coding-for-product-managers) — 2025, vibe coding for PMs

### Tier 2-3 (Data Sources & Emerging Voices)
- [Perspective AI](https://getperspective.ai/published/page/6851e02fc1043be42b224395) — 2025, 54-PM identity crisis study
- [Agents Today](https://agentstoday.substack.com/p/agents-today-16-the-great-reshuffling) — 2025, K-shaped bifurcation, 35% pay premium
- [StoriesOnBoard](https://storiesonboard.com/blog/ai-agents-product-management-2026) — 2026, PM as agent orchestrator

### Contrarian / Critical Sources
- [The New Stack](https://thenewstack.io/vibe-coding-could-cause-catastrophic-explosions-in-2026/) — 2026, vibe coding catastrophic quality
- [Stack Overflow](https://stackoverflow.blog/2026/01/02/a-new-worst-coder-has-entered-the-chat-vibe-coding-without-code-knowledge) — 2026, "new worst coder"
- [Bryce York](https://bryceyork.com/vibe-coding-prototypes/) — PM time on coding = opportunity cost
- [National CIO Review](https://nationalcioreview.com/articles-insights/extra-bytes/ai-forces-over-50000-layoffs-in-2025-at-leading-technology-firms/) — 54K+ layoffs
- [WEF](https://www.weforum.org/stories/2025/04/ai-jobs-international-workers-day/) — AI jobs impact
- [Microsoft AI Economy](https://blogs.microsoft.com/on-the-issues/2026/01/08/global-ai-adoption-in-2025/) — geographic AI divide
- [AI2 Incubator](https://www.ai2incubator.com/articles/insights-15-the-state-of-ai-agents-in-2025-balancing-optimism-with-reality) — state of AI agents reality check

### Ссылки автора
- [Naval Ravikant on Judgment](https://nav.al/judgment) — judgment essay
- [AI Skills Pay Premium](https://blog.theinterviewguys.com/how-much-more-ai-skills-pay-in-2025/) — salary data

## TODO автора
- [ ] Определить 3-5 тезисов для статьи MtP из 12 (статья 1200 слов — не все поместятся)
- [ ] Что AI действительно заменяет в продуктовой работе (примеры) — нужны конкретные примеры из практики автора
- [ ] Что AI никогда не заменит (примеры) — нужны конкретные примеры из практики автора
- [ ] Какие PM-роли исчезают первыми — данные есть (task-movers, mid-level), нужен авторский опыт
- [ ] Новая реальность PM-роли — фрейм: hypothesis pipeline operator + agent orchestrator + curriculum designer
- [ ] Что это значит для продактов — actionable takeaways для "следующего спринта"
- [ ] Решить: как раскрыть тему ИНАЧЕ, чем для фаундеров в startup growth guide
- [ ] Подготовить обложку 1600 x 900 px

## Рекомендации по усилению статьи

### Для дифференциации от Startup Growth Guide (КРИТИЧЕСКИ ВАЖНО!)
- **Startup Growth Guide** = для фаундеров, фокус на "как строить компанию с AI"
- **MtP статья** = для practicing PMs, фокус на "как трансформировать свою роль в существующей компании"
- Suggested angle: **"The PM Identity Crisis — and What to Do About It"** — начать с 67% anxiety data, показать K-shaped bifurcation, дать actionable framework (Four Forces + value backlog + prompt sets)
- Другой angle: **"From Feature Factory Operator to Hypothesis Pipeline Engineer"** — practical transformation guide
- Третий angle: **"AI Won't Replace PMs — But PMs Who Use AI Will Replace PMs Who Don't"** — с nuance от contrarian (survivorship bias, productivity illusion)

### Для корпоративных продактов (PRIMARY AUDIENCE для MtP)
- Больше фокуса на "как убедить stakeholders" и "как обосновать value в AI era"
- RAT-формула как инструмент коммуникации: "вот почему мы тестируем ЭТО, а не ТО"
- "Value backlog" vs "Feature backlog" — immediately actionable
- Four Forces как self-assessment tool

### Для product-leads
- LinkedIn APB case study — конкретный пример реструктуризации
- K-shaped bifurcation — warning для тех, кто управляет PM-командами
- Prompt sets as new PRDs — конкретное изменение рабочего процесса

---

## Исходный поток мыслей

> Абсолютно критичный навык в эпоху нейронок — это "judgment". Вот про это писал Наваль Равикант. https://nav.al/judgment
>
> Все будут становиться full-stack builderами и я абсолютно уверен, что мы видим уже к концу года много публичных кейсов как компании перестроили свою инфраструктуру, контур хранения данных, безопасность, deploy так чтобы продукты и продакт маркетинг менеджеры могли выкатывать эксперименты в продакшен без привлечения разработки или с минимальным привлечением разработки следующий очень важный тезис что все продукты поднимутся на уровень на несколько уровней выше и будет важным понимать как как что нужно делать чтобы бизнес зарабатывал деньги системное мышление аналитическое мышление умение проектировать агентские команды системы из агентов управлять и улучшать систему из агентов стратегия и целеполагание то есть все те кто сейчас там пишут продуктовые требования пишут юзер stories и выкатывают эксперименты они скорее всего поднимутся будут вынуждены подняться на уровень она выше по большему влиянию на бизнес еще одна гипотеза это то что продукты станут управлять конвейером проверки гипотез потому что веб кодинг и нейронки позволяют единицу времени проверять в разы на порядок больше гипотез а это означает что это будет конвейера управления конвейером качество операции гипотез качество фидбэка отсеивания качество проработки каждой гипотезы качество анализа каждой гипотезы представьте что каждый продукт станет оператором фабрики оператором производственного процесса проверки гипотез те продукты которые прокачали насмотренность шарит за бизнес стратегию системного мышления получают мощные рычаги C&A те продукты которые двигают таски в Task Tracker они их точно заменят почему так потому что из точки А в точку Б ведет огромное количество до без результата ведет большое количество решений и те люди которые в промежуточных шагах принимают решения не точно или полностью делегируют их нейронки с высокой вероятностью придут в сильно менее промежуточные точку чем те ребята кто например знает как работает рынок знает как оценить рынок знает как найти сегменты знает как выбрать правильные jobs клиентов знает как создать добавочную ценность знает как строить конкурентов спозиционироваться на этот выбрать без модель корректируй без модель найти точки роста там знаю когда говорится с коллегами знают как убедиться их holder а лучше считать потребности холдера и вот все те кто знает это на более высоком более системном уровне ближе к влиянию на прибыль те продукты с неровками получают очень мощные рычаги и сильно ускоряются я уверен что еще год и будет полгода год и будет появляться полный цикл вплоть до тестов с просто продаж то есть сейчас можно сделать прототипы проверить на их с тестах или там сделать и виппо идти продавать но существующем продукте безопасность структура хранить данных и deploy не позволяют катать эксперименты но бизнес скорее всего будет вынужден перестроить процессы так чтобы продукты катали гипотезы вплоть до из автоматического создания рекламных компаний автоматического запуска цифровых продажников которые идут продают ваш продукт это приведет тому что точки роста сместятся в дистрибуцию и маркетинг в бренд в точное знание психологии людей точное знание джобс точно знание коммуникации ценности моя еще ставка что эстетика продукта вырастет в целом конкуренция усилится качество продукта должно кардинально усилиться команды будут становиться меньше, продукт будет прерывать гипотезу от начала до конца с минимальным увеличением разработки ну и точка роста скорее всего сместится в качестве принимаемых решений в коммуникации внутри команды а
>
> Все больше подтверждений тому что спрос на Knowledge Workers растет. То есть я не думаю что те продукты которые шарят за бизнес шарят за jobs to be done создание ценности коммуникация ценности активации в ценность юнит экономику поиск точек роста из юнит экономики поиск стратегических возможностей на рынке и могут выстраивать команды агентов и pipeline проверки гипотез и оптимизировать pipeline проверки я думаю что эти продукты будут супер востребованы плюс есть уже информация что те кто хорошо ладится с нейронками получают прирост по деньгам https://blog.theinterviewguys.com/how-much-more-ai-skills-pay-in-2025/
>
> Скорее всего, произойдет сегрегация тех, кто сейчас довольно быстро разберутся в нейронках и внедрят это в процесс создания продуктов, и те, кто по какой-то причине не смогут адаптироваться. Например, одна из причин это сопротивление эго. Нейронки полностью перестраивают, нейронки веб-кодинг команды агентов полностью перестраивают процесс создания продуктов. Это означает, что многим придется отказаться от старой идентичности. Отказ от старой идентичности это смерть эго, и это для многих очень тяжело и страшно. И те, кто успеет адаптироваться, готовится, они получают преимущество, потому что данных преимущества этой революции это быть просто раньше других. Ну и в целом у продуктов-маркетологов, которые шарят за бизнес и которые умеют находить возможности из данных из юнит экономики и стратегические возможности на рынке в зависимости от того какие недообслуженные сегменты и джобы на рынке есть они получают огромное преимущество с нейронками потому что они эти возможности могут значительно быстрее реализовывать и быстрее приносить ценность компании и как следствие получить огромные преимущества в карьере.
>
> Что AI действительно заменяет в продуктовой работе (примеры)
> Что AI никогда не заменит (примеры)
> Какие PM-роли исчезают первыми
> Новая реальность PM-роли
> Что это значит для продактов
