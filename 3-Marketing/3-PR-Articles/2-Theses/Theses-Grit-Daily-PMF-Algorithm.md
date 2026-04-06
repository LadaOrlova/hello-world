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

# The Startup PMF Algorithm: Why Most Founders Search in All the Wrong Places

> **Статус:** Расширенные тезисы (фаза расхождения)
> **Версия:** 1
> **Модель:** claude-opus-4-6
> **Дата:** 2026-04-06 23:00
> **Тезисов автора:** 8
> **Новых тезисов от команды:** 8
> **Всего тезисов:** 16
> **Коэффициент расширения:** 1x
> **Режим:** Agent Team (knowledge-researcher, expert-hunter, contrarian)
> **Coverage Score:** 90.6%
> **Раундов итерации:** 1
> **Издание:** Grit Daily (gritdaily.com)
> **Аудитория:** англоязычные фаундеры и стартап-команды
> **Объём статьи:** 600–1200 слов, идеально 800–1000
> **Формат:** narrative/feature (история + выводы), короткие абзацы, мобильно-ориентировано
> **Тон:** живой простой английский для фаундеров, без академичности, без рекламы "нашего продукта"
> **Требования:** 1-2 мини-кейса, 1 внутренняя ссылка на Grit Daily, чёткий конфликт/проблема в начале

---

## Главная тема

Большинство фаундеров ищут PMF в коде, фичах и дизайне — то есть в *решении*. Но PMF находится в выборе правильного сегмента и правильной "работы" (job) клиента. AI сделал прототипирование дешёвым, но одновременно создал новый тип ловушки: скорость без направления = потерянность на более высокой скорости. Статья даёт пошаговый алгоритм — от выбора сегмента до валидации через продажи — основанный на опыте 12,000+ обученных фаундеров.

---

## Coverage Score (метрики качества ресерча)

| Критерий | Оценка | Детали |
|----------|--------|--------|
| Экспертное покрытие | 95% | 6 tier-1 (Moesta, Vohra, Dunford, Todd Jackson, Torres, Balfour), 4 tier-2 (Bessemer, a16z x2, First Round) |
| Свежесть источников | 85% | >60% источников 2024-2026, Bessemer 2025, a16z 2025, METR 2025 |
| Глубина тезисов | 90% | "5 почему" x2, causal chain, risk multiplication math |
| Контраргументы | 95% | Для всех 8 авторских тезисов есть контрпозиция с URL |
| Knowledge Base | 90% | 17 findings из AURA/AJTBD: RAT, Traction Map, Causal Chain, Segmentation, Value Creation, Launch Algorithm |
| Actionability | 85% | 4-step algorithm, Traction Map, validation in batches of 6, segment score formula |
| Ссылки на источники | 95% | Все с URL или путём к KB |
| 🆕 Качество расширения | 90% | 8 новых тезисов прошли тест релевантности |
| **СРЕДНИЙ** | **90.6%** | |

---

## Оценка ценности для сегментов

| Сегмент | Релевантность | Ключевые Jobs | Что усилить |
|---------|---------------|---------------|-------------|
| Фаундеры 0→1 (основная аудитория Grit Daily) | ⭐⭐⭐ | "Не потратить год на плохую идею", "Быстро выйти на первые продажи" | 30-Day Discovery Sprint, RAT formula, selling as validation |
| Post-PMF стартапы | ⭐⭐ | "Масштабироваться правильно", "Не попасть в premature scaling" | Model-Market Fit, PMF gradient, Velocity Trap |
| Корпоративные продакты | ⭐⭐ | "Запустить новый продукт внутри компании" | Causal chain, RAT, expert interviews |
| VC/Инвесторы | ⭐ | "Оценить quality of PMF search" | Assumption ledger, pivot quality metrics |

---

## Карта экспертов по теме

| Эксперт | Credentials | Ключевой тезис | Источник | Год | Tier |
|---------|-------------|-----------------|----------|-----|------|
| Bob Moesta | Co-creator JTBD, 3500+ launches | 10 интервью = 90% рынка. 4 силы переключения — реальная механика покупки | [SaaS Club podcast](https://saasclub.io/podcast/jobs-to-be-done-bob-moesta-423/) | 2024-25 | ⭐⭐⭐ |
| Rahul Vohra | CEO Superhuman, создатель PMF Engine | Пересегментация подняла PMF с 22% до 32% без изменения продукта | [First Round Review](https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/) | 2018+ | ⭐⭐⭐ |
| April Dunford | Автор "Obviously Awesome", 16+ позиционирований | PMF "не существует операционально" — нужна actionable segmentation | [One Knight in Product](https://www.oneknightinproduct.com/april-dunford/) | 2024-25 | ⭐⭐⭐ |
| Todd Jackson | Partner First Round, ex-VP Product Facebook/Twitter | PMF имеет 4 уровня: Nascent → Developing → Strong → Extreme | [Lenny's Newsletter](https://www.lennysnewsletter.com/p/a-framework-for-finding-product-market) | 2024-25 | ⭐⭐⭐ |
| Brian Balfour | CEO Reforge, ex-VP Growth HubSpot | PMF — один из 4 необходимых fit (Product-Market, Product-Channel, Channel-Model, Model-Market) | [Brian Balfour blog](https://brianbalfour.com/essays/product-market-fit-isnt-enough) | 2023+ | ⭐⭐⭐ |
| Lenny Rachitsky | Ex-Airbnb Growth, 500K+ подписчиков | Медианное время идея → PMF = ~2 года (25 B2B стартапов) | [Lenny's Newsletter](https://www.lennysnewsletter.com/p/finding-product-market-fit) | 2024-25 | ⭐⭐ |
| Bessemer VP (Taj Shorter, Lauri Moore) | Top-tier VC, Atlas research | AI PMF = "buying shoes for a growing kid." Различай experimental vs durable ARR | [BVP Atlas](https://www.bvp.com/atlas/mastering-product-market-fit-a-detailed-playbook-for-ai-founders) | 2025 | ⭐⭐⭐ |
| Peter Lauten & David Ulevitch | a16z | Product-User Fit ≠ Product-Market Fit. Фаундеры путают стадии | [a16z](https://a16z.com/product-user-fit-comes-before-product-market-fit/) | 2025 | ⭐⭐ |

---

## 📝 Тезисы автора (обогащённые)

> Эти тезисы извлечены из потока мыслей автора и вебинаров, обогащены ресерчем команды.

### 📝 Тезис А1: Фаундеры ищут PMF не там — проблема не в лени, а в направлении поиска

**Суть:**
Большинство стартапов проваливаются не потому что плохо работают, а потому что строят то, что никому не нужно. Корневая причина — неправильный выбор сегмента и "работы" (Job) клиента. AJTBD определяет строгую причинно-следственную цепочку: Рынок → Сегменты → Jobs → Ценность → Unit Economics → Привлечение → Прибыль. Ошибка на любом раннем шаге каскадирует: низкая конверсия почти всегда = проблемы с работами или сегментами. Три катастрофических ошибки сегментации: (1) продукт для несуществующих задач, (2) маленький убыточный сегмент при наличии большого рядом, (3) размывание ресурсов по всем сегментам. Rahul Vohra (Superhuman) доказал количественно: пересегментация подняла PMF score с 22% до 32% — без единого изменения продукта.

**Происхождение:** 📝 Авторский (из потока мыслей + вебинары 27.01, 12.03.2026)
**Глубина:** 🔬 Глубокий
**Актуальность:** 📅 Вечнозелёный (с обновлением 2025-2026)
**Статус:** ✅ Подтверждается

**Ценность для сегментов:** Фаундеры 0→1 (критический), Post-PMF (высокая)

**Из Knowledge Base (AURA/AJTBD):**
> "Базовая формула: Рынок с деньгами → Сегменты клиентов → Работы клиентов → Ценность → Показываем ценность → Юнит-экономика → Привлечение → Конверсия → Прибыль."
> — Источник: `1-Context/AURA-Theses/AJTBD/fundamentals.md`

> "Ошибка №1: Продукт для несуществующих работ — самая катастрофическая ошибка."
> — Источник: `1-Context/AURA-Theses/AJTBD/fundamentals.md`

> "Score = Важность работы x Частотность x Размер сегмента x (10 - Удовлетворённость текущим решением)"
> — Источник: `1-Context/AURA-Theses/Algorithms/launch-product.md`

**Экспертные мнения:**
- Rahul Vohra (⭐⭐⭐, 📅 2018+): Superhuman PMF score вырос с 22% до 32% только от пересегментации, без изменения продукта. За 3 квартала итераций — 58%. — [First Round Review](https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/)
- Tren Griffin / a16z (⭐⭐, 📅 2023+): "When a lousy team meets a great market, market wins." — [a16z](https://a16z.com/12-things-about-product-market-fit/)
- First Round Review (⭐⭐⭐, 📅 2025): David Hsu (Retool) думал его сегмент — малый бизнес, оказалось — enterprise ($400M/год на internal tools). Тот же продукт, другой сегмент = PMF. — [First Round Review](https://review.firstround.com/20-lessons-from-20-different-paths-to-product-market-fit-advice-for-founders-from-founders/)

**⚠️ Контраргументы:**
- Andy Rachleff (Wealthfront): "You cannot customer-development your way into a massive success. Non-consensus outlier wins come from a unique insight." — Сегментация без неконсенсусного инсайта = бесполезна. [Reforge](https://www.reforge.com/blog/lean-startup-methodology-problems)
- Когнитивные bias (overconfidence, planning fallacy, anchoring) заставляют фаундеров систематически недооценивать ошибки в выборе сегмента. Фреймворк может маскировать bias, давая ложное чувство "системности". [LeanFoundry](https://www.leanfoundry.com/lean-1-2-3/jul-3-2025)

**🔄 Что изменилось в 2025-2026:** Costanoa Ventures предлагает инвертировать формулу: не Product-Market Fit, а Market-Product Fit — начни с рынка, забудь о продукте. [Costanoa VC](https://costanoa.vc/product-market-fit-pmf-is-dead-for-early-stage-startups-its-market-product-fit/)

---

### 📝 Тезис А2: Классический поиск PMF сломан — интервью без структуры, фреймворки без сегментов

**Суть:**
Стандартный подход (поговори с пользователями → запусти MVP → итерируй) не работает без правильной сегментации по Jobs. Сегментация по индустриям или ролям — ложная. Lean Startup посвящает 300+ страниц тому, КАК проверять гипотезы, но только 3 страницы — КАКИЕ гипотезы и в какой очерёдности. В 2026 году ключевой сдвиг: "хорошая валидация" — это поведение (пользователь тратит время, деньги, репутацию), а не слова. Интервью (даже структурированные) — всё ещё слова, не поведение.

**Происхождение:** 📝 Авторский
**Глубина:** 🔬 Глубокий
**Актуальность:** 📅 Актуальный 2025+ (сдвиг к behavior-based validation)
**Статус:** ✅ Подтверждается

**Из Knowledge Base (AURA/AJTBD):**
> "В книге Lean Startup ответ на вопрос 'какие гипотезы, про что, в какой очерёдности и почему именно их проверять' занимает 3 страницы. Остальные 300+ — про то, КАК проверять."
> — Источник: `1-Context/AURA-Theses/RAT/risk-assumption-test.md`

> "Лучший способ провалидировать гипотезу ценности — это продажи."
> — Источник: `1-Context/AURA-Theses/HowTos/validate-value.md`

**Экспертные мнения:**
- April Dunford (⭐⭐⭐, 📅 2024-25): PMF "doesn't exist, isn't operationally useful, and is a VC pipe dream." Нужна actionable segmentation, начинающаяся с конкурентных альтернатив. — [One Knight in Product](https://www.oneknightinproduct.com/april-dunford/)
- Material Security (⭐⭐⭐, 📅 2025): Ryan Noon ПРОДАВАЛ 4 разных идеи одновременно вместо user research. Продажа показала appetite рынка быстрее любых интервью. — [First Round Review](https://review.firstround.com/20-lessons-from-20-different-paths-to-product-market-fit-advice-for-founders-from-founders/)

**⚠️ Контраргументы:**
- Один фаундер провёл 50 customer interviews за 3 месяца для VR-платформы — стал MORE confused. Проблема не только в отсутствии структуры, а в том, что люди не могут артикулировать свои Jobs. [LeanFoundry](https://www.leanfoundry.com/lean-1-2-3/jul-24-2025)
- JTBD не захватывает подсознательные cues и эмоциональные ассоциации, oversimplifies мотивацию. [Medium](https://shahmm.medium.com/exploring-the-limitations-of-the-jobs-to-be-done-framework-ebd387fd12e0)

**🔄 Что изменилось в 2025-2026:** Переход от "validation through conversation" к "validation through behavior" (Presta Validation Framework 2026). Second-order engagement (return after first use) = единственный надёжный AI-native metric PMF. [Presta](https://wearepresta.com/startup-validation-framework-2026-the-ultimate-guide-to-testing-ideas/)

---

### 📝 Тезис А3: Рабочие стратегии из опыта 12,000+ фаундеров — 3-5 ключевых механик

**Суть:**
Из ~80 продуктовых механик AURA, ключевые для ранней стадии: (1) Kill a Job — полностью убрать шаги в задаче клиента, (2) Move Up the Graph — конкурировать за Big Job вместо Core Job, (3) Execute the Next Job — сделать следующую работу в критической цепочке, (4) Satisfy Deep Needs — безопасность, статус, автономия, (5) Expert Interviews — поговорить с провалившимися конкурентами (ROI запредельный: 20 написал → 2 поговорили → 1 ценная информация). Ключевой инсайт: "Если не знаешь про механику — не найдёшь в интервью."

**Происхождение:** 📝 Авторский
**Глубина:** 🔬 Средний
**Актуальность:** 📅 Вечнозелёный
**Статус:** ✅ Подтверждается

**Из Knowledge Base (AURA/AJTBD):**
> "Если не знаешь про механику, не найдёшь в интервью."
> — Источник: `1-Context/AURA-Theses/AJTBD/value-creation.md`

> "Если 20 написали, двое поговорили и один рассказал что-то ценное — вся инвестиция окупилась."
> — Источник: `1-Context/AURA-Theses/Algorithms/launch-product.md`

**⚠️ Контраргументы:**
- "80+ механик" звучит как инфобиз-обещание (contrarian). Для Grit Daily лучше 3-5 ключевых с кейсами. Nintendo десятилетиями использует одну стратегию: "Make extraordinary games." — [Fortune](https://fortune.com/2025/12/03/video-games-can-teach-designers-deeper-lessons-than-high-score-streaks-and-gamification/)

---

### 📝 Тезис А4: AI изменил уравнение — но создал НОВЫЙ тип ловушки, а не просто "ускорил"

**Суть:**
AI/vibe-coding сделал прототипирование дешёвым (Victoria за 5.5 часов собрала прототип, который в энтерпрайзе потребовал бы 20+ человек). Но AI не просто "не заменяет валидацию" — он активно СОЗДАЁТ иллюзию прогресса. Velocity Trap: 10x скорость на старте → tech debt → velocity падает на 50-70%. METR Study (2025): разработчики с AI были на 19% МЕДЛЕННЕЕ, но считали что на 20% быстрее. 42% кода AI-assisted (Sonar 2025) = "you can build the wrong thing faster than ever." Bessemer: различай "experimental ARR" и "durable ARR" — novelty ≠ value.

**Происхождение:** 📝 Авторский (усилен contrarian + expert-hunter)
**Глубина:** 🔬 Глубокий
**Актуальность:** 📅 Актуальный 2025+ (Velocity Trap — новый феномен)
**Статус:** ✅ Подтверждается / ⚠️ Самый актуальный и спорный тезис

**Ценность для сегментов:** Все — но особенно фаундеры, использующие vibe-coding

**Из Knowledge Base (AURA/AJTBD):**
> "Мы не продукт запускаем — мы покупаем знания."
> — Источник: `1-Context/AURA-Theses/RAT/risk-assumption-test.md`

**Экспертные мнения:**
- Bessemer VP (⭐⭐⭐, 📅 2025): "Market and buyer preferences are changing at the same time founders try to find PMF. It's like buying shoes for a growing kid." — [BVP Atlas](https://www.bvp.com/atlas/mastering-product-market-fit-a-detailed-playbook-for-ai-founders)
- METR Study (⭐⭐, 📅 2025-07): AI-assisted developers 19% slower, perceived 20% faster — [TechStartups](https://techstartups.com/2025/12/11/the-vibe-coding-delusion-why-thousands-of-startups-are-now-paying-the-price-for-ai-generated-technical-debt/)
- OpenAI Product Lead (⭐⭐, 📅 2025): "In the AI world, PMF is a moving target—users' definition of 'intelligent enough' changes every month." — [The VC Corner](https://www.thevccorner.com/p/ai-product-market-fit-framework-openai)
- Sonar 2025 (⭐⭐, 📅 2025): "42% of code is AI-assisted — which means you can build the wrong thing faster than ever." — [SketchFlow](https://www.sketchflow.ai/blog/guides/how-to-validate-a-startup-idea-with-ai-prototyping/)

**⚠️ Контраргументы:**
- JP Morgan и Google Cloud: vibe coding = фундаментальный сдвиг, циклы Build-Measure-Learn стали 100x быстрее. Возможно, дешевле билдить и измерять реальное поведение, чем валидировать ДО билда. [JP Morgan](https://www.jpmorgan.com/insights/technology/artificial-intelligence/vibe-coding-a-guide-for-startups-and-founders)
- НО: 95% AI-пилотов не дают measurable revenue (MIT, 2025). 42% компаний бросили AI-инициативы в 2025. Только 11% seed дошли до Series A.

**Данные:**
| Факт | Цифра | Источник |
|------|-------|----------|
| AI-assisted код | 42% | Sonar 2025 |
| AI pilots без revenue | 95% | MIT 2025 |
| Компании бросившие AI | 42% (2x vs 2024) | TechStartups |
| METR speed perception gap | -19% actual vs +20% perceived | METR 2025 |
| Velocity drop после sprint | 50-70% | Dual Boot Partners |
| AI code failing security | 45% | Veracode 2025 |

---

### 📝 Тезис А5: PMF — градиент, не бинарное состояние (но PMF alone недостаточен)

**Суть:**
PMF — это спектр с 4 стадиями: (1) Нет PMF — полная неопределённость, нет продаж; (2) Слабый PMF — редкие немасштабируемые продажи; (3) Сильный PMF — повторяемые продажи, работающие каналы; (4) "Отрывают с руками" — спрос превышает capacity. Todd Jackson (First Round) даёт аналогичные 4 уровня с метриками: Nascent (3-5 клиентов) → Developing → Strong → Extreme. Медианное время от идеи до ощущения PMF = ~2 года (Lenny Rachitsky, 25 B2B стартапов). НО: даже PMF-gradient — устаревшая рамка. В 2026 нужны 4 fit одновременно (Balfour): Product-Market, Product-Channel, Channel-Model, Model-Market.

**Происхождение:** 📝 Авторский (из вебинара 28.02.2026)
**Глубина:** 🔬 Глубокий
**Актуальность:** 📅 Актуальный 2025+ (обновлён через 4-fit framework)
**Статус:** ✅ Подтверждается, но требует расширения до Model-Market Fit

**Из Knowledge Base (AURA/AJTBD):**
> "Product-Market Fit — это градиент, а не бинарное состояние: Не бинарное 'есть/нет': PMF — это градиент, спектр."
> — Источник: `1-Context/AURA-Theses/RAT/risk-assumption-test.md`

> "Локальный оптимум: +10-30% рост. Глобальный оптимум: x2-x10 рост. Это 2 педальки, можно нажимать одновременно."
> — Источник: `1-Context/AURA-Theses/AURA/local-vs-global-optimum.md`

**Экспертные мнения:**
- Todd Jackson (⭐⭐⭐, 📅 2024-25): 4 уровня PMF с метриками и таймлайнами. "4 P's" (Persona, Problem, Promise, Product) для диагностики "где застрял". — [Lenny's Newsletter](https://www.lennysnewsletter.com/p/a-framework-for-finding-product-market)
- Lenny Rachitsky (⭐⭐, 📅 2024-25): Медиана = ~2 года от идеи до PMF, 9-18 мес от рабочего продукта до PMF. — [Lenny's Newsletter](https://www.lennysnewsletter.com/p/finding-product-market-fit)
- Brian Balfour (⭐⭐⭐): Нужны 4 fit — Product-Market, Product-Channel, Channel-Model, Model-Market. — [Balfour blog](https://brianbalfour.com/essays/product-market-fit-isnt-enough)

**⚠️ Контраргументы:**
- Rand Fishkin: "Fit" как метафора подразумевает конечную точку и вредит мышлению. Лучше "Customer Adoption Spectrum". — [SparkToro](https://sparktoro.com/blog/product-market-fit-is-a-broken-concept-theres-a-better-way/)
- Model-Market Fit > PMF: Casper имел великолепный PMF (клиенты обожали), но модель не масштабировалась. Purple построил vertical integration и выиграл. — [RCKT](https://www.therckt.com/blog/model-market-fit)

---

### 📝 Тезис А6: "Мы не запускаем продукт — мы покупаем знания"

**Суть:**
Правильная цель ранней стадии — не "выпустить продукт", а максимально быстро и дёшево купить знание: что в текущем наборе гипотез не работает. MVP — не продукт, а зонд для проверки самого рискованного предположения. "Топим котят. Самые жизнеспособные выживут." Pivot = структурированная смена одного или нескольких рискованных предположений, а не "начинаем заново". КРИТИЧНО: "покупаем знания" работает только с чёткими kill criteria и time-boxes. Если через 24 месяца ты всё ещё "учишься" без retention — это не обучение, это прокрастинация.

**Происхождение:** 📝 Авторский (из вебинара 28.02.2026)
**Глубина:** 🔬 Глубокий
**Актуальность:** 📅 Вечнозелёный
**Статус:** ✅ Подтверждается (с guard rail: нужны kill criteria)

**Из Knowledge Base (AURA/AJTBD):**
> "Смена парадигмы: Когда мы делаем продукт с нуля, мы не запускаем продукт — мы покупаем знания."
> — Источник: `1-Context/AURA-Theses/RAT/risk-assumption-test.md`

> "MVP — не продукт. В MVP есть коварное слово 'продукт'. Его там не должно быть."
> — Источник: `1-Context/AURA-Theses/RAT/risk-assumption-test.md`

> "Цель не запустить, а убить: Ваша идея с вероятностью 90% не жизнеспособна. Вы просто ещё не знаете, почему."
> — Источник: `1-Context/AURA-Theses/Algorithms/launch-product.md`

**⚠️ Контраргументы:**
- "Мы учимся" может быть rationalization для отсутствия результатов. PMF занимает 12-24 месяцев в SaaS. "Покупаем знания" без kill criteria = бесконечный цикл. — [Mag Startup](https://www.magstartup.com/en/product-market-fit-pmf-the-founders-guide-2026/)
- 43% стартапов умирают из-за poor PMF. Самая опасная ситуация — ВЕРИТЬ, что у тебя есть PMF, когда его нет ("False PMF — the silent killer"). — [Medium/Bootcamp](https://medium.com/design-bootcamp/false-product-market-fit-the-silent-killer-of-early-stage-startups-1416ff57e446)

---

### 📝 Тезис А7: RAT — 5 базовых рисков, и математика, которая убивает стартапы

**Суть:**
Каждый продукт стоит на 5 базовых предположениях: (1) Рынок достаточно большой, (2) Нашли привлекательный сегмент, (3) Сегмент покупает продукт, (4) Unit economics сходится, (5) Можем создать и масштабировать спрос. Если ХОТЯ БЫ ОДНО не подтверждается — кина не будет. Математика: при 40% вероятности подтверждения каждого предположения (в 4 раза выше реальных 10-20%), 7 рисков = 0.6^7 = 3% шанс на успех. Вывод: лучшее, что можете сделать — УБИРАТЬ предположения из продукта, а не добавлять фичи. Формула ранжирования: Приоритет = (Вероятность × Цена ошибки) / Стоимость проверки.

**Происхождение:** 📝 Авторский
**Глубина:** 🔬 Глубокий
**Актуальность:** 📅 Вечнозелёный
**Статус:** ✅ Подтверждается

**Из Knowledge Base (AURA/AJTBD):**
> "Пять базовых рискованных предположений: Рынок, Сегмент, Ценность, Юнит-экономика, Спрос. Если хотя бы одно не подтверждается — кина не будет."
> — Источник: `1-Context/AURA-Theses/RAT/risk-assumption-test.md`

> "0.6 в 7 степени = 3%. Лучшее, что вы можете сделать для вашего продукта — избавлять его от рисков."
> — Источник: `1-Context/AURA-Theses/RAT/risk-assumption-test.md`

**Экспертные мнения:**
- Startup Genome (⭐⭐⭐): 74% стартапов умирают от premature scaling. 70% масштабируются преждевременно. Ни один premature scaler не прошёл 100K users. — [Startup Genome](https://startupgenome.com/articles/a-deep-dive-into-the-anatomy-of-premature-scaling-new-infographic)
- Immad Akhund, Mercury (⭐⭐, 📅 2025): "In the beginning, spend all your time doing the thing you're the least capable of proving." — [First Round Review](https://review.firstround.com/the-30-best-pieces-of-company-building-advice-we-heard-in-2025/)

**⚠️ Контраргументы:**
- RAT предполагает, что фаундер может правильно ранжировать риски — а overconfidence bias систематически мешает. Ранжирование рисков — скилл, который нужно развивать, не данность. — [LeanFoundry](https://www.leanfoundry.com/lean-1-2-3/jul-3-2025)

---

### 📝 Тезис А8: 30-Day Discovery Sprint — не путь к PMF, а правильный первый шаг

**Суть:**
Конкретный алгоритм на 30 дней (не обещание PMF за месяц — честно: это начало Discovery phase). Основан на Top-Down Algorithm + Traction Map из AURA:
- **Неделя 1:** Определи 3 возможных сегмента, оцени по формуле (Важность × Частотность × Размер × (10 - Удовлетворённость)). Выбери один.
- **Неделя 2:** Проведи 10-12 AJTBD-интервью. Извлеки работы и критерии успеха. (Совет: поговори с провалившимися конкурентами — ROI запредельный.)
- **Неделя 3:** Составь Assumption Ledger (список всех рискованных предположений). Ранжируй по RAT-формуле. Выбери killer assumption. Собери демо/прототип с AI.
- **Неделя 4:** Проведи итерацию из 6 решенческих интервью / пресейлов. Нет продаж → переделываем гипотезу ценности. Есть продажи → следующая итерация. (5 итераций без продаж = фундаментальная ошибка сегмента.)

**Происхождение:** 📝 Авторский (TODO из потока мыслей, конкретизирован через KB)
**Глубина:** 🔬 Средний
**Актуальность:** 📅 Вечнозелёный
**Статус:** ✅ Actionable

**Из Knowledge Base (AURA/AJTBD):**
> "Четыре этапа Top-Down: 1. Выбор рынка. 2. Поиск и выбор сегмента. 3. Валидация гипотезы ценности. 4. Тест гипотезы привлечения."
> — Источник: `1-Context/AURA-Theses/Algorithms/launch-product.md`

> "Если вы уверены, что идея взлетит: Алгоритм для таких людей: Молиться."
> — Источник: `1-Context/AURA-Theses/Algorithms/launch-product.md`

> "Делаем итерацию из 6 решенческих интервью. Нет продаж — переделываем. 5 итераций без продаж — фундаментально ошиблись сегментом."
> — Источник: `1-Context/AURA-Theses/HowTos/validate-value.md`

**⚠️ Контраргументы:**
- GFR Fund: "Scaling fast before hitting real PMF no longer works." PMF занимает 12-24 месяца. 30 дней — max начало Discovery. Переименовано в "30-Day Discovery Sprint" чтобы не создавать ложных ожиданий. — [GFR Fund](https://gfrfund.com/blog/2025-founder-lessons)

---

## 🆕 Новые тезисы от команды (фаза расхождения)

> Эти тезисы НЕ были в потоке мыслей автора. Найдены командой в процессе ресерча.
> Автор выбирает, какие из них включить в статью.

### 🆕 Тезис Н1: Пересегментация повышает PMF без изменения продукта

**Суть:**
Rahul Vohra (Superhuman) доказал количественно: простая пересегментация аудитории подняла PMF-score с 22% до 32% — без единого изменения в продукте. Изоляция "very disappointed" респондентов и фокус на их persona = instant PMF boost. Это самое мощное доказательство тезиса А1: буквально тот же продукт, другой сегмент = другой PMF.

**Происхождение:** 🆕 expert-hunter
**Откуда взялся:** Rahul Vohra / First Round Review — [URL](https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/)
**Почему автор мог не упомянуть:** Кейс 2018 года, но framework жив и используется массово
**Связь с авторскими тезисами:** Расширяет А1 + А5 — даёт конкретные цифры
**Глубина:** 🔬 Глубокий
**Актуальность:** 📅 Вечнозелёный (framework жив)
**Спорный?** Нет — количественно доказанный кейс

---

### 🆕 Тезис Н2: Product-User Fit ≠ Product-Market Fit — фаундеры путают стадии

**Суть:**
a16z (Lauten & Ulevitch) ввели различие: product-user fit = правильный продукт для правильного пользователя. Product-market fit = то же ПЛЮС gravitational market pull. Фаундеры преждевременно объявляют PMF, когда у них только product-user fit. Forcing growth на продукте без market pull "will not ultimately convert to highly retained, happy users." Добавляет ещё один слой к проблеме "ищут не там" — не только неправильный сегмент, но и путаница стадий.

**Происхождение:** 🆕 expert-hunter
**Откуда взялся:** Peter Lauten & David Ulevitch / a16z — [URL](https://a16z.com/product-user-fit-comes-before-product-market-fit/)
**Связь с авторскими тезисами:** Расширяет А1 + А2
**Глубина:** 🔬 Средний
**Актуальность:** 📅 Актуальный 2025+
**Спорный?** Нет — элегантная декомпозиция

---

### 🆕 Тезис Н3: False Pivot — фаундеры меняют продукт, когда нужно менять сегмент

**Суть:**
38% всех стартап-пивотов — customer segment pivots. Но многие — "ложные пивоты": фаундер выбрасывает продукт, когда нужна тактическая корректировка (GTM, messaging, целевой сегмент). Признаки false pivot: сильные leading indicators (meetings, demos) но слабые lagging (revenue). Это = проблема targeting, не продукта. Стартапы с 1-2 пивотами привлекают 2.5x больше фандинга и достигают 3.6x лучший user growth.

**Происхождение:** 🆕 expert-hunter
**Откуда взялся:** M Accelerator + Vanderbuild — [URL](https://maccelerator.la/en/blog/entrepreneurship/false-pivot-why-founders-change-products-need-tactical-adjustment/)
**Связь с авторскими тезисами:** Расширяет А6 + А7 (pivot = смена assumptions, не restart)
**Глубина:** 🔬 Средний
**Актуальность:** 📅 Актуальный 2025+
**Спорный?** Нет — подтверждено данными

---

### 🆕 Тезис Н4: AI Novelty Trap — experimentation spikes ≠ adoption

**Суть:**
Bessemer VP (2025): AI-продукты создают НОВУЮ ловушку — experimentation spikes выглядят как adoption, но это novelty, не value. "Fast-growing wedge products aren't nearly as sticky as SaaS." Ключевая метрика: различай "experimental ARR" vs "durable ARR". AI прототипы дают ложные сигналы PMF: (a) novelty effect, (b) second-order engagement = нулевой.

**Происхождение:** 🆕 expert-hunter
**Откуда взялся:** Bessemer Venture Partners — [URL](https://www.bvp.com/atlas/mastering-product-market-fit-a-detailed-playbook-for-ai-founders)
**Связь с авторскими тезисами:** Расширяет А4 — конкретный новый failure mode
**Глубина:** 🔬 Глубокий
**Актуальность:** 📅 Актуальный 2025+ (новый феномен)
**Спорный?** Да — vibe-coding апологеты не согласятся

---

### 🆕 Тезис Н5: Velocity Trap — AI создаёт новый тип ложного PMF

**Суть:**
Формулировка "AI не заменяет валидацию" слишком мягкая. Реальность: AI активно МЕШАЕТ валидации, создавая иллюзию прогресса. Velocity Trap = начальный 10x speed → tech debt → velocity drop 50-70%. METR: разработчики ДУМАЮТ они на 20% быстрее, а реально на 19% медленнее. 95% AI pilots не дают measurable revenue. Это не "не заменяет" — это "создаёт новый fail mode".

**Происхождение:** 🆕 contrarian
**Откуда взялся:** METR Study + Dual Boot Partners + TechStartups — [URL](https://techstartups.com/2025/12/11/the-vibe-coding-delusion-why-thousands-of-startups-are-now-paying-the-price-for-ai-generated-technical-debt/), [URL](https://www.dualbootpartners.com/insights/the-velocity-trap/)
**Связь с авторскими тезисами:** Переворачивает А4 — из "не заменяет" в "активно мешает"
**Глубина:** 🔬 Глубокий
**Актуальность:** 📅 Актуальный 2025+
**Спорный?** Да — самый спорный и актуальный тезис

---

### 🆕 Тезис Н6: Model-Market Fit — PMF необходим, но недостаточен

**Суть:**
В 2026 разговор ушёл дальше PMF. Даже идеальный PMF не гарантирует выживания бизнеса (Casper vs Purple). Brian Balfour: нужны 4 fit одновременно — Product-Market, Product-Channel, Channel-Model, Model-Market. "More startups fail AFTER traction than before it — not because demand disappears, but because the business model can't support growth."

**Происхождение:** 🆕 contrarian
**Откуда взялся:** RCKT + Balfour — [URL](https://www.therckt.com/blog/model-market-fit), [URL](https://brianbalfour.com/essays/product-market-fit-isnt-enough)
**Связь с авторскими тезисами:** Расширяет А5 — из "gradient" в "один из четырёх fit"
**Глубина:** 🔬 Средний
**Актуальность:** 📅 Актуальный 2025+ (Model-Market Fit = тренд 2026)
**Спорный?** Нет — признанная эволюция концепции

---

### 🆕 Тезис Н7: Cognitive Bias Paradox — фреймворки не лечат когнитивные искажения

**Суть:**
Фаундеры выбирают неправильный сегмент не из-за отсутствия фреймворка — из-за 6 когнитивных bias (overconfidence, planning fallacy, anchoring, availability, representativeness, optimism). JTBD/AURA могут МАСКИРОВАТЬ bias, давая фаундеру ложное чувство "я действую системно". Пример: кофейня оптимизировала меню по данным участников rewards program (любителей specialty) — проигнорировав большинство (быстрый простой кофе). Результат — падение продаж.

**Происхождение:** 🆕 contrarian
**Откуда взялся:** LeanFoundry + HubSpot + Reforge — [URL](https://www.leanfoundry.com/lean-1-2-3/jul-3-2025), [URL](https://blog.hubspot.com/sales/survivorship-bias), [URL](https://www.reforge.com/blog/lean-startup-methodology-problems)
**Связь с авторскими тезисами:** Углубляет А1 — объясняет КОРЕНЬ проблемы
**Глубина:** 🔬 Глубокий
**Актуальность:** 📅 Вечнозелёный (когнитивные bias не меняются)
**Спорный?** Нет — документированный эффект

---

### 🆕 Тезис Н8: Selling beats surveying — продажа как инструмент валидации

**Суть:**
Material Security (Ryan Noon) продавал 4 разных идеи одновременно вместо user research. Обнаружил market appetite быстрее любых интервью. Logan Randolph (Sierra) требует от design partners финансовый commitment (10-20% контракта) + дедлайн (2-6 мес). Бесплатные пилоты = ложная валидация. Gong: 12 design partners → 11 конвертировались (92%). Искали "innovators", а не "plug-and-play".

**Происхождение:** 🆕 expert-hunter
**Откуда взялся:** First Round Review — [URL](https://review.firstround.com/20-lessons-from-20-different-paths-to-product-market-fit-advice-for-founders-from-founders/), [URL](https://review.firstround.com/the-30-best-pieces-of-company-building-advice-we-heard-in-2025/)
**Связь с авторскими тезисами:** Расширяет А2 + А8 — конкретная альтернатива интервью
**Глубина:** 🔬 Средний
**Актуальность:** 📅 Актуальный 2025+
**Спорный?** Нет — подтверждено множеством кейсов

---

## Дебаты команды (ключевые споры)

### Спор 1: "AI ускоряет" vs "AI создаёт новые ловушки"
- **Позиция expert-hunter:** Bessemer 2025 — AI-специфичные PMF-ловушки (novelty ≠ value, experimental ARR ≠ durable ARR). AI помогает, но нужны новые guardrails.
- **Вызов contrarian:** Формулировка "не заменяет" слишком мягкая. METR data: -19% speed при +20% perception. Velocity Trap. 95% AI pilots fail. AI АКТИВНО мешает валидации.
- **Результат:** Тезис А4 усилен. Финальная формулировка: "AI создаёт новый тип ловушки — Velocity Trap и ложный PMF через novelty effect."

### Спор 2: "80+ механик" vs "Инфобиз-обещание"
- **Позиция knowledge-researcher:** 80+ механик — реальная библиотека из AURA. "Если не знаешь про механику — не найдёшь в интервью."
- **Вызов contrarian:** "80+ механик" для Grit Daily звучит как lead magnet. Nintendo десятилетиями использует одну стратегию.
- **Результат:** Тезис А3 переформулирован: вместо "80+ механик" → "3-5 ключевых механик с кейсами". Упоминание "80+" сохранено как контекст, но не как заголовок.

### Спор 3: "PMF как градиент" vs "PMF — устаревшая концепция"
- **Позиция expert-hunter:** Todd Jackson 4 levels, Lenny data, BitsOrBricks 5 factors — gradient работает.
- **Вызов contrarian:** Rand Fishkin: "fit" как метафора вредит. Balfour: 4 fit, не один. RCKT: Model-Market Fit > PMF (Casper vs Purple).
- **Результат:** Тезис А5 расширен: "PMF как градиент, НО PMF alone недостаточен — нужны 4 fit." Добавлен новый тезис Н6 (Model-Market Fit).

---

## Примеры и кейсы (для статьи)

### Кейс 1: Retool — инвертированный сегмент
David Hsu (Retool) был уверен: ранние пользователи = FileMaker-разработчики + малый бизнес. Оказалось НАОБОРОТ: enterprise-компании, тратящие $400M/год на internal tools. Тот же продукт, другой сегмент = PMF.
— [First Round Review](https://review.firstround.com/20-lessons-from-20-different-paths-to-product-market-fit-advice-for-founders-from-founders/)

### Кейс 2: Superhuman — PMF через пересегментацию
PMF score вырос с 22% до 32% без единого изменения продукта — только через изоляцию "very disappointed" пользователей и фокус на их профиле. За 3 квартала итераций — 58%.
— [First Round Review](https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/)

### Кейс 3: Vanta — рынок "размером с палец"
Christina Cacioppo построила голосового ассистента для лаборантов ("they wear gloves, can't use keyboards"). Рынок оказался крошечным. Ошибка: build first, find customers second.
— [First Round Review](https://review.firstround.com/20-lessons-from-20-different-paths-to-product-market-fit-advice-for-founders-from-founders/)

### Кейс 4: Twiggy — пивот через assumption change (из KB)
Начали с "более удобного Excel для немецких предпринимателей". Интервью показали: удобный Excel не нужен. Но job "получить заёмные средства" выполняется очень больно (средний срок до кредита — 2 года). Сменили assumption set → нашли PMF.
— `1-Context/AURA-Theses/RAT/risk-assumption-test.md`

### Кейс 5: Гонг (Gong) — 92% конверсия design partners
12 design partners → 11 конвертировались в платящих (92%). Искали "innovators", а не "plug-and-play" клиентов.
— [First Round Review](https://review.firstround.com/20-lessons-from-20-different-paths-to-product-market-fit-advice-for-founders-from-founders/)

---

## Все ссылки и источники

### Из Knowledge Base (AURA/AJTBD)
- `1-Context/AURA-Theses/AJTBD/fundamentals.md` — Causal Chain, 3 ошибки сегментации, "работы первичны"
- `1-Context/AURA-Theses/AJTBD/segmentation.md` — Формула выбора сегмента, ложная сегментация
- `1-Context/AURA-Theses/AJTBD/value-creation.md` — 80+ механик, "если не знаешь — не найдёшь"
- `1-Context/AURA-Theses/RAT/risk-assumption-test.md` — 5 базовых рисков, 0.6^7=3%, парадигма покупки знаний, PMF gradient, Traction Map, Lean Startup critique
- `1-Context/AURA-Theses/HowTos/validate-value.md` — Валидация через продажи (итерации по 6), 100 проверок
- `1-Context/AURA-Theses/Algorithms/launch-product.md` — Top-Down Algorithm, Segment Score, Kill Don't Launch, Expert Interviews
- `1-Context/AURA-Theses/AURA/overview.md` — AURA meta-framework
- `1-Context/AURA-Theses/AURA/local-vs-global-optimum.md` — Локальный vs глобальный оптимум

### Эксперты Tier 1 (прямые авторитеты)
- [Bob Moesta — SaaS Club podcast](https://saasclub.io/podcast/jobs-to-be-done-bob-moesta-423/) — JTBD, 10 interviews = 90%, 4 forces
- [Rahul Vohra — First Round Review](https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/) — PMF Engine, пересегментация +10pp
- [April Dunford — One Knight in Product](https://www.oneknightinproduct.com/april-dunford/) — PMF "не существует", actionable segmentation
- [Todd Jackson — Lenny's Newsletter](https://www.lennysnewsletter.com/p/a-framework-for-finding-product-market) — 4 уровня PMF
- [Brian Balfour — blog](https://brianbalfour.com/essays/product-market-fit-isnt-enough) — 4-fit framework
- [Bessemer VP — BVP Atlas](https://www.bvp.com/atlas/mastering-product-market-fit-a-detailed-playbook-for-ai-founders) — AI PMF Playbook, "buying shoes for a growing kid"

### Эксперты Tier 2 (VC, HBR, MIT)
- [a16z — Product-User Fit](https://a16z.com/product-user-fit-comes-before-product-market-fit/) — PUF ≠ PMF
- [a16z — 12 Things About PMF](https://a16z.com/12-things-about-product-market-fit/) — "Market wins"
- [First Round Review — 20 Lessons](https://review.firstround.com/20-lessons-from-20-different-paths-to-product-market-fit-advice-for-founders-from-founders/) — Retool, Vanta, Material Security, Gong
- [First Round Review — 30 Best Advice 2025](https://review.firstround.com/the-30-best-pieces-of-company-building-advice-we-heard-in-2025/) — Logan Randolph, Immad Akhund
- [Lenny Rachitsky — PMF timeline](https://www.lennysnewsletter.com/p/finding-product-market-fit) — ~2 years median
- [Teresa Torres — Behind the Build](https://airfocus.com/resources/events/behind-the-build-teresa-torres-first-ai-product/) — AI discovery
- [OpenAI PMF framework — The VC Corner](https://www.thevccorner.com/p/ai-product-market-fit-framework-openai) — "Moving target"

### Данные и исследования
- [Startup Genome — Premature Scaling](https://startupgenome.com/articles/a-deep-dive-into-the-anatomy-of-premature-scaling-new-infographic) — 74% die from premature scaling
- [CB Insights — Failure Reasons](https://www.cbinsights.com/research/report/startup-failure-reasons-top/) — 42% fail from no PMF
- [Failory — Startup Failure Rate](https://www.failory.com/blog/startup-failure-rate) — 90% fail
- [METR Study](https://techstartups.com/2025/12/11/the-vibe-coding-delusion-why-thousands-of-startups-are-now-paying-the-price-for-ai-generated-technical-debt/) — AI -19% speed vs +20% perceived
- [Dual Boot Partners — Velocity Trap](https://www.dualbootpartners.com/insights/the-velocity-trap/) — velocity drop 50-70%
- [Sonar 2025 / SketchFlow](https://www.sketchflow.ai/blog/guides/how-to-validate-a-startup-idea-with-ai-prototyping/) — 42% code AI-assisted

### Контраргументы и альтернативные фреймворки
- [Reforge — Lean Startup Problems](https://www.reforge.com/blog/lean-startup-methodology-problems) — Andy Rachleff, "non-consensus insight"
- [SparkToro — PMF Is Broken](https://sparktoro.com/blog/product-market-fit-is-a-broken-concept-theres-a-better-way/) — Rand Fishkin
- [RCKT — Model-Market Fit](https://www.therckt.com/blog/model-market-fit) — Casper vs Purple
- [Costanoa VC — Market-Product Fit](https://costanoa.vc/product-market-fit-pmf-is-dead-for-early-stage-startups-its-market-product-fit/) — MPF > PMF
- [LeanFoundry — Cognitive Bias](https://www.leanfoundry.com/lean-1-2-3/jul-3-2025) — 6 biases
- [Presta — Validation Framework 2026](https://wearepresta.com/startup-validation-framework-2026-the-ultimate-guide-to-testing-ideas/) — behavior > words
- [M Accelerator — False Pivot](https://maccelerator.la/en/blog/entrepreneurship/false-pivot-why-founders-change-products-need-tactical-adjustment/) — false pivot mechanism

---

## Ключевые статистики (готовые для статьи)

| Факт | Цифра | Источник |
|------|-------|----------|
| Стартапы, которые проваливаются | 90% | Startup Genome |
| Провал из-за отсутствия PMF | 42-43% | CB Insights / Failory |
| Premature scaling как причина провала | 74% | Startup Genome (3200+ стартапов) |
| Стартапы, масштабирующиеся преждевременно | 70% | Startup Genome |
| PMF boost от пересегментации (Superhuman) | +10pp (22% → 32%) | Rahul Vohra |
| Пивотившиеся хотя бы раз до PMF | 92% | Vanderbuild |
| Customer segment pivots (доля всех пивотов) | 38% | Vanderbuild |
| Медианное время идея → PMF | ~2 года | Lenny Rachitsky |
| AI-assisted код | 42% | Sonar 2025 |
| AI pilots без revenue | 95% | MIT 2025 |
| METR speed perception gap | -19% actual vs +20% perceived | METR 2025 |
| Velocity drop после AI sprint | 50-70% | Dual Boot Partners |
| Стартапы с 1-2 пивотами → фандинг | 2.5x больше | Vanderbuild |
| Bob Moesta: интервью для 90% рынка | 10 штук | SaaS Club |
| RAT: 7 рисков при 40% success | 3% шанс | AURA KB |

---

## Цитаты для статьи (готовые)

1. **Lauri Moore (Bessemer):** "Market and buyer preferences are changing at the same time founders try to find PMF. It's like buying shoes for a growing kid."
2. **Paul Graham (YC):** "It's better to have 100 customers that love you than a million customers that just sort of like you."
3. **April Dunford:** PMF "doesn't exist, isn't operationally useful, and is a VC pipe dream."
4. **Rahul Vohra (Superhuman):** "Companies that struggled to find growth almost always had less than 40% of users respond 'very disappointed.'"
5. **Immad Akhund (Mercury):** "In the beginning, spend all your time doing the thing you're the least capable of proving to the world that you can do."
6. **Tren Griffin / a16z:** "When a lousy team meets a great market, market wins."
7. **Sonar 2025:** "42% of code is AI-assisted — which means you can build the wrong thing faster than ever."
8. **Ivan Zamesin (KB):** "If you're confident your idea will fly, the algorithm for you is: pray."

---

## TODO автора
- [ ] Выбрать 1-2 кейса для статьи (рекомендация: Retool + Superhuman или Vanta + Twiggy)
- [ ] Найти внутреннюю ссылку на Grit Daily (про стартапы/лидерство/инновации)
- [ ] Решить: использовать "30-Day Discovery Sprint" или "PMF Algorithm" как центральный нарратив
- [ ] Решить по новым тезисам: какие включить в короткую статью (600-1200 слов вместит ~5-7 тезисов)

## Рекомендации по фокусу статьи (для 600-1200 слов)

**Рекомендованный набор для draft-этапа (6 тезисов):**
1. **А1** (центральный конфликт: ищут не там) + **Н1** (Superhuman data) = ОТКРЫТИЕ
2. **А4 усиленный** (AI = новая ловушка, Velocity Trap) = AI-УГОЛ
3. **А7** (RAT, 5 рисков, 0.6^7 = 3%) = МЕХАНИКА
4. **А6** (покупаем знания, не запускаем продукт) = ПЕРЕОСМЫСЛЕНИЕ
5. **А8** (30-Day Discovery Sprint) = ПЛАН ДЕЙСТВИЙ
6. **Н8** (selling > surveying) = ACTIONABLE TWIST

**Структура статьи:**
- Hook: mini-story (Retool или Vanta) → конфликт "ищут не там"
- Problem: почему классический подход сломан (А2 кратко)
- Insight: AI делает хуже, не лучше (А4 усиленный)
- Algorithm: 5 рисков + покупаем знания (А7 + А6)
- Action: 30-Day Sprint (А8)
- Close: Superhuman data — пересегментация > product change (Н1)

---

## Исходный поток мыслей

> The Startup PMF Algorithm: Why Most Founders Search in All the Wrong Places
>
> ГАЙДЛАЙНЫ ИЗДАНИЯ:
> https://gritdaily.com/home/
> 600–1200 слов, лучше 800–1000
> Статья в формате narrative/feature: история + выводы, не учебник
> Короткие абзацы (2–3 предложения), много воздуха, читаемо с мобилки
> Язык для фаундеров и стартап-команд: живой, простой английский без академичности
> Без рекламы «мы в нашей компании…», «наш продукт…»
> Чёткий конфликт/проблема в начале (фаундеры ищут PMF "не там"), дальше — объяснение и решение (алгоритм)
> Нужны 1–2 мини-кейса (обезличенные или с публичными примерами), чтобы это было похоже на реальную стартап-историю
> Желательно вставить 1 внутреннюю ссылку на релевантную статью Grit Daily
>
> ОРИЕНТИРЫ ПО ТЕЗИСАМ:
> Вступление: проблема PMF у фаундеров, мини-история и тезис про "ищем не там, а не ленимся"
> Почему классический поиск PMF ломается: интервью без структуры, фреймворки без сегментов
> Самые классные работающие стратегии из тех 80ти
> Где помогает ИИ
> Кейс и 30-дневный план: короткий пример "до/после" и 3-5 шагов для читателя на месяц
>
> Давай напишем на основе вебинаров, которые я делал, про то, как меняется создание продуктов с ИТ.
> Прочитай в записях Zoom созвонов. Найди вебинары про то, как меняется процесс создания продуктов, и выдели оттуда тезисы.
