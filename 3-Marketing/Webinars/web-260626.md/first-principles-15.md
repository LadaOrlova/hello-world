# 15 новых принципов создания продуктов (from first principles)

> **Контекст:** Дополнение к 6 основным принципам из программы вебинара 26.02.2026
> **Метод:** Анализ из первых принципов на основе публикаций экспертов и исследований 2025-2026
> **Дата:** 25 февраля 2026

---

## Группа A: Конкурентная динамика и рынки

---

### Принцип 1: "Продукт = работник, а не инструмент"

**Аксиома:** Стоимость когнитивного труда на задачу стремится к нулю. Между 2022 и 2024 стоимость inference упала в 280x.

**Логика:** Если единица когнитивного труда → $0 → софт перестаёт быть инструментом, который помогает человеку → софт становится самим работником → метрика ценности: не MAU (Monthly Active Users), а ATC (Autonomous Task Completion) → продукт конкурирует не с другими инструментами, а с наёмными сотрудниками.

**Неочевидный вывод:** Ценообразование будущего: не $115/мес за "сиденье", а $0.99 за решённый тикет. Fortune 50 планируют сократить лицензии Salesforce/ServiceNow на 60%, заменяя сотни "сидений" десятком AI-агентов. Это Outcome-as-a-Service.

**Источники:**
- [Zero Marginal Cost Intelligence](https://compoundingthoughts.substack.com/p/zero-marginal-cost-intelligence-is)
- [The $1 Trillion Software Carnage](https://markets.financialcontent.com/stocks/article/marketminute-2026-2-24-the-1-trillion-software-carnage-how-ai-agents-broke-the-saas-model)
- [a16z: Outcome-Based Pricing](https://a16z.com/newsletter/december-2024-enterprise-newsletter-ai-is-driving-a-shift-towards-outcome-based-pricing/)

**Слайд:** "Продукт будущего — не инструмент, а работник. Продавай результат, а не кресло."

---

### Принцип 2: "Закон Кристенсена для AI: интеллект — commodity, контекст — дефицит"

**Аксиома:** Общий интеллект (GPT, Claude, Gemini) — взаимозаменяем для 80% задач.

**Логика:** Закон сохранения привлекательных прибылей Кристенсена: когда один слой коммодитизируется, прибыль перетекает в смежный → интеллект (inference) коммодитизируется → прибыль перетекает в **контекст**: проприетарные данные о workflow, институциональное знание, специфика отрасли → тот, кто владеет контекстом, забирает маржу.

**Неочевидный вывод:** Победитель — не тот, кто создаёт AI, а тот, кто владеет "последней милей" до пользователя. Harvey побеждает в юриспруденции, Cursor в коде — не моделью, а глубиной встроенности в workflow. HBR (февраль 2026): "When every company can use the same AI models, context becomes a competitive advantage."

**Источники:**
- [Ben Thompson / Stratechery: Conservation of Attractive Profits](https://stratechery.com/2015/netflix-and-the-conservation-of-attractive-profits/)
- [Elad Gil: AI Market Clarity](https://blog.eladgil.com/p/ai-market-clarity)
- [HBR: Context as Competitive Advantage](https://hbr.org/2026/02/when-every-company-can-use-the-same-ai-models-context-becomes-a-competitive-advantage)

**Слайд:** "Интеллект — commodity. Прибыль ушла в контекст: кто знает workflow клиента, тот забирает маржу."

---

### Принцип 3: "Flywheel обучения бьёт flywheel данных"

**Аксиома:** Данные перестали быть моатом. Синтетические данные дают результат в пределах 2% от реальных.

**Логика:** Если данные можно синтезировать → объём данных перестаёт быть барьером → старый data moat разрушается → новый моат = **скорость обучения** на данных пользователей (learning velocity) → across-user learning создаёт network effects → within-user learning создаёт switching costs.

**Неочевидный вывод:** Netflix и Waymo доказали: огромный lead по данным НЕ гарантирует доминирования. 96% организаций с AI показывают рост, но только 5% извлекают value at scale. Эти 5% получают 1.7x рост выручки и 3.6x рост TSR. Разрыв — не в данных, а в скорости замкнутого цикла "использование → данные → улучшение → больше использования".

**Источники:**
- [The AI Flywheel: Data Network Effects](https://hgbr.org/research_articles/the-ai-flywheel-how-data-network-effects-drive-competitive-advantage/)
- [The New Software Moats](https://bloomvp.substack.com/p/the-new-software-moats-stickiness)
- [The Great SaaS Unbundling](https://www.uncoveralpha.com/p/the-great-saas-unbundling-why-ai)

**Слайд:** "Данных у всех хватает. Побеждает не объём, а скорость learning loop."

---

### Принцип 4: "Рынки открываются ступенями GPT-лестницы"

**Аксиома:** Capability моделей растёт дискретными скачками, каждый из которых "разблокирует" новые рынки.

**Логика:** Рынки открываются на конкретных порогах: Legal стало возможным на GPT-4, Coding — на Claude 3.5 → стартап, который строит продукт для ещё не разблокированного рынка, получает фору → первый на "ступени" забирает 80% рынка → capability release dates важнее execution quality.

**Неочевидный вывод:** Инвертирует конкурентный анализ. Вместо "какая команда лучше исполнит?" правильный вопрос: "кто стоит на пороге следующей ступени, когда модель дозреет?" Accounting, compliance, financial tools, security — рынки без победителей, ждущие свою ступень (Elad Gil).

**Источники:**
- [Elad Gil: AI Market Clarity](https://blog.eladgil.com/p/ai-market-clarity)
- [TechCrunch: Which AI Markets Are Still Wide Open](https://techcrunch.com/2025/11/03/elad-gil-on-which-ai-markets-have-winners-and-which-are-still-wide-open/)

**Слайд:** "Рынки открываются ступенями. Строй продукт для следующей ступени — сегодня."

---

## Группа B: Продуктовый дизайн и UX

---

### Принцип 5: "Дизайн для двух аудиторий: человека и его AI-агента"

**Аксиома:** AI-агенты, действующие от имени пользователя (покупают, бронируют, ресёрчат), стали массовыми. 400 млн еженедельных пользователей OpenAI.

**Логика:** Агенты = "второй пользователь" вашего продукта → продукт, который не читается агентами, теряет клиентов → дизайнер проектирует для двух аудиторий: Human UX + Agent Experience (AX) → API > GUI, структура > визуал, машиночитаемость > эстетика.

**Неочевидный вывод:** Красивый дизайн, который непонятен AI-агентам, *теряет* клиентов. John Maeda вводит термин "Agent Experience" (AX). Если ваш сервис непрозрачен для агента пользователя — агент порекомендует конкурента.

**Источники:**
- [John Maeda: Autodesigners on Autopilot](https://johnmaeda.medium.com/autodesigners-on-autopilot-88c5b07609b9)
- [Beyond UX: Interfaces for AI, Not Humans](https://theaieconomy.substack.com/p/beyond-ux-why-the-future-of-tech)
- [AX: The Next Evolution in UX](https://agentexperience.ax/research/ax-the-next-evolution-in-ux/)

**Слайд:** "Два пользователя: человек и его AI-агент. Кого агент не поймёт — того не порекомендует."

---

### Принцип 6: "Впервые за 60 лет новая парадигма интерфейса"

**Аксиома:** Понимание естественного языка стало бесплатным.

**Логика:** Компьютер понимает намерение → пользователю не нужно учить интерфейс → GUI перестаёт быть обязательным → продукт из "набора экранов" превращается в "телепортатор к результату" → дизайнер проектирует не user flow, а outcome space.

**Неочевидный вывод:** Jakob Nielsen: первая парадигма со времён command-line (1964). НО: ~50% населения — low-literacy пользователи, которым сложно формулировать промпты. Чистый чат — **элитарный дизайн**. Будущее — гибрид: intent + GUI-подсказки. Дизайнер проектирует "коридор допустимых намерений".

**Источники:**
- [Jakob Nielsen: AI Is First New UI Paradigm in 60 Years](https://jakobnielsenphd.substack.com/p/ai-is-first-new-ui-paradigm-in-60)
- [Nielsen: The Articulation Barrier](https://jakobnielsenphd.substack.com/p/prompt-driven-ai-ux-hurts-usability)
- [Luke Wroblewski: Chat Interfaces & Intent](https://lukew.com/ff/entry.asp?2085=)

**Слайд:** "Пользователь говорит ЧТО, а не КАК. Но чат — элитарный интерфейс: 80% не могут промптить."

---

### Принцип 7: "Продукт-для-одного: фиксированный дизайн мёртв"

**Аксиома:** Генерация уникального UI в реальном времени стала бесплатной.

**Логика:** Каждый пользователь видит свою версию продукта → фиксированный макет = анахронизм → дизайнер проектирует не экраны, а **правила адаптации** → продукт из артефакта превращается в живую систему.

**Неочевидный вывод:** +20-30% CLV у компаний с AI-персонализацией. Дизайнер из "создателя макетов" превращается в тренера ML-модели: задаёт пространство вариаций, этические границы, критерии "хорошего опыта". Julie Zhuo (Sundial): нужны не дизайнеры — нужны "билдеры", проектирующие системы, а не статичные артефакты.

**Источники:**
- [Fast Company: Hyper-Personalization at Scale](https://www.fastcompany.com/91433849/ai-unlocks-hyper-personalization-at-scale)
- [Julie Zhuo: Death of Product Development As We Know It](https://joulee.medium.com/the-death-of-product-development-as-we-know-it-1bcae948ce61)
- [CES 2026: AI-Driven Hyper-Personalization](https://www.assurant.com/news-insights/articles/CES-2026-AI-driven-hyper-personalization)

**Слайд:** "Фиксированный дизайн мёртв. Каждый видит свой продукт. Дизайнер — тренер ML, а не рисовальщик макетов."

---

## Группа C: Инновационный процесс

---

### Принцип 8: "Провал стал бесплатным — побеждает тот, кто проваливается быстрее"

**Аксиома:** Стоимость неудачного эксперимента стремится к нулю.

**Логика:** Провал стоил дорого → страх ошибки → бюрократия согласований → стейдж-гейты, комитеты (не для качества, а для страховки) → если эксперимент стоит $0 → страх провала иррационален → бюрократия теряет смысл → оптимальная стратегия: **максимизировать количество провалов в единицу времени**.

**Неочевидный вывод:** Конкурентное преимущество — от "умения выбирать правильные идеи" к **"скорости перебора неправильных"**. Компания с лучшим процессом убийства гипотез побеждает компанию с лучшим процессом их отбора. PwC: "New disruptors use AI to mimic scaled capabilities of mature businesses" — масштаб перестаёт быть защитой.

**Источники:**
- [AI Has Changed the Cost of Experimentation](https://securityboulevard.com/2025/11/ai-has-changed-the-cost-of-experimentation/)
- [Rapid Prototyping Accelerates AI Innovation — ASU](https://tech.asu.edu/rapid-prototyping-accelerates-cost-effective-ai-innovation)
- [PwC: Speed Matters More, Scale Matters Less](https://www.pwc.com/us/en/tech-effect/ai-analytics/competing-in-age-of-ai.html)

**Слайд:** "Провал стал бесплатным — побеждает тот, кто проваливается быстрее всех."

---

### Принцип 9: "Дилемма инноватора ускорилась в 100x"

**Аксиома:** Время от "good enough" до "best-in-class" сжалось с лет до месяцев.

**Логика:** Классика Кристенсена: disruptor входит снизу, медленно улучшается за 5-10 лет → с AI этот цикл = месяцы → DeepSeek за месяцы воспроизвёл возможности OpenAI → "окно безопасности" инкумбента схлопнулось → PYMNTS (2026): "Good enough 2025 = best-in-class 2026."

**Неочевидный вывод:** Стратегия "наблюдай, потом реагируй" больше не работает — к моменту реакции уже поздно. Единственная жизнеспособная стратегия для инкумбента: автономная команда с мандатом построить компанию, которая убьёт тебя самого.

**Источники:**
- [Christensen Institute: Why AI Is Different](https://www.christenseninstitute.org/blog/why-ai-is-different-and-what-disruptive-innovation-theory-predicts/)
- [PYMNTS: Big Tech Faces the AI Innovator's Dilemma](https://www.pymnts.com/artificial-intelligence-2/2026/big-tech-faces-the-ai-innovators-dilemma)
- [AI Agents: The Innovator's Dilemma Comes for Knowledge Work](https://nextfutures.substack.com/p/ai-agents-the-innovators-dilemma)

**Слайд:** "Дисрапшн — не 10 лет, а 10 месяцев. К моменту реакции уже поздно."

---

### Принцип 10: "Экспертиза расщепилась: ответы — commodity, вопросы — дефицит"

**Аксиома:** Доступ к экспертным знаниям (ответам) стал бесплатным.

**Логика:** HBR: экспертиза трансформируется из "давать ответы" в "задавать незаданные вопросы" → MIT Sloan: миллионы людей получают одинаковые AI-ответы → **конвергенция мышления** → все думают одинаково → инновация = видеть unknown unknowns.

**Неочевидный вывод:** AI делает экспертизу ценнее для ~12% (крутые кривые обучения) и обесценивает для ~19% (explicit knowledge). Самый ценный навык — видеть вопросы, которые никто не задаёт. Чем лучше AI отвечает, тем ценнее люди, умеющие спрашивать.

**Источники:**
- [HBR: How Gen AI Could Change the Value of Expertise](https://hbr.org/2025/03/how-gen-ai-could-change-the-value-of-expertise)
- [HBR: AI Is Changing How We Learn at Work](https://hbr.org/2025/12/ai-is-changing-how-we-learn-at-work/)
- [MIT Sloan: Intellectual Convergence Risk](https://medium.com/@srini.hebbar/the-end-of-deep-expertise-how-ai-is-redefining-career-success-in-2025-eb5be85d3047)

**Слайд:** "AI commoditize-ит ответы. Самый дефицитный ресурс — правильные вопросы."

---

### Принцип 11: "Build-Measure-Learn мёртв. Prompt-Test-Learn."

**Аксиома:** Создание работающего прототипа перестало требовать инженера.

**Логика:** Раньше: idea → PRD → design → engineering → QA → launch (6-12 недель) → теперь: idea → prompt → working prototype (6-12 часов) → это не ускорение, а **схлопывание пирамиды**: слои согласований исчезают → supply продуктов взрывается, demand (внимание) фиксирован.

**Неочевидный вывод:** "Кембрийский взрыв" продуктов. Andrew Chen: "Building software is cheap, user acquisition remains costly." Bottleneck сместился от build к distribution. Teresa Torres: прототип должен тестировать ОДНУ рискованную предпосылку, иначе — "Homer Simpson car".

**Источники:**
- [ACM: The Vibe Coding Imperative for PMs](https://cacm.acm.org/blogcacm/the-vibe-coding-imperative-for-product-managers/)
- [Andrew Chen: AI Will Change How We Build Startups](https://andrewchen.substack.com/p/ai-will-change-how-we-build-startups)
- [Teresa Torres: AI Product Discovery](https://www.news.aakashg.com/p/teresa-torres-podcast)

**Слайд:** "Build-Measure-Learn мёртв. Prompt-Test-Learn: 'build' больше не отдельный этап."

---

## Группа D: Оргдизайн и бизнес-модели

---

### Принцип 12: "Бремя доказательства перевернулось: найм надо обосновывать"

**Аксиома:** AI-агент = $1-10 за задачу vs. человек = $50-150/час.

**Логика:** Раньше менеджер обосновывал "зачем автоматизация" → теперь обосновывает "зачем этот найм" → headcount из KPI роста превращается в KPI неэффективности → Shopify (Tobi Lutke): "Докажи, что AI не может."

**Неочевидный вывод:** Klarna: -40% сотрудников, +$1M revenue/сотрудник. Duolingo: тот же штат, 4-5x контента. НО Klarna потом нанимала людей обратно — качество упало. Реальное правило: "человек нанимается только на то, что AI доказанно не может."

**Источники:**
- [Shopify CEO Memo](https://www.cnbc.com/2025/04/07/shopify-ceo-prove-ai-cant-do-jobs-before-asking-for-more-headcount.html)
- [Klarna: AI Shrunk Workforce 40%](https://www.cnbc.com/2025/05/14/klarna-ceo-says-ai-helped-company-shrink-workforce-by-40percent.html)
- [Klarna Reversal: Rehiring Humans](https://www.reworked.co/employee-experience/klarna-claimed-ai-was-doing-the-work-of-700-people-now-its-rehiring/)
- [Duolingo: 4-5x Without Layoffs](https://www.cnbc.com/2025/09/17/duolingo-ceo-how-ai-makes-my-employees-more-productive-without-layoffs.html)

**Слайд:** "Headcount — больше не метрика роста. Найм теперь надо обосновывать, а не автоматизацию."

---

### Принцип 13: "Средний менеджмент испаряется — оргструктура = песочные часы"

**Аксиома:** Координация стала бесплатной. AI автоматизирует scheduling, reporting, monitoring, status updates.

**Логика:** Middle managers = передача информации вверх-вниз → если это бесплатно → функция исчезает → Gartner: 20% компаний уберут >50% middle management к 2026 → организация из пирамиды → песочные часы: мало наверху (стратегия), почти никого в середине, AI-агенты внизу (исполнение).

**Неочевидный вывод:** Тёмная сторона: 41% сотрудников без менеджеров чувствуют себя "без направления" (Korn Ferry). Менеджеры были source of context, coaching, career guidance. Jensen Huang: "IT-отдел станет HR для AI-агентов." Появляется НОВЫЙ средний слой — люди, которые нанимают, онбордят, обучают и оценивают AI-агентов.

**Источники:**
- [Fortune: Extinction of Middle Manager](https://fortune.com/2025/09/19/surviving-great-flattening-coming-extinction-of-middle-manager-layoffs/)
- [Gartner: 20% Orgs Flatten, >50% Mgmt Cut](https://gloat.com/blog/ai-workforce-trends/)
- [Jensen Huang: IT Will Become HR for AI](https://fortune.com/2025/01/09/nvidia-ceo-jensen-huangt-take-over-hr-ai-agents/)
- [Korn Ferry: 41% Feel Directionless](https://www.kornferry.com/insights/featured-topics/talent-recruitment/ai-in-recruitment-trends)

**Слайд:** "Оргструктура = песочные часы. Средний менеджмент → менеджеры AI-агентов."

---

### Принцип 14: "SaaS мёртв, живи SaS (Service-as-Software)"

**Аксиома:** AI-агент делает работу за $1/задача. Бенчмарки превысили порог "60% замены труда".

**Логика:** Зачем покупать инструмент за $100/мес/seat, чтобы ЧЕЛОВЕК делал работу? → per-seat модель теряет смысл → выигрывает тот, кто продаёт РЕЗУЛЬТАТ → SaaS (Software as a Service) → SaS (Service as Software) → $/seat → $/outcome.

**Неочевидный вывод:** Это не смена ценообразования — это **взрыв TAM**. SaaS = ~$300B. Рынок труда, который SaS замещает = $4.6T (x15). Компания Salient (a16z) вместо продажи софта коллекторам — ЗАМЕНЯЕТ самих коллекторов. PitchBook (Q1 2026): "SaaS is Dead, Long Live SaS."

**Источники:**
- [PitchBook: SaaS is Dead, Long Live SaS](https://pitchbook.com/news/reports/q1-2026-pitchbook-analyst-note-saas-is-dead-long-live-sas)
- [a16z: Outcome-Based Pricing](https://a16z.com/newsletter/december-2024-enterprise-newsletter-ai-is-driving-a-shift-towards-outcome-based-pricing/)
- [Foundation Capital: Service as Software](https://foundationcapital.com/ai-service-as-software/)
- [Thoughtworks: Service-as-Software Model](https://www.thoughtworks.com/insights/blog/generative-ai/service-as-software-a-new-economic-model-for-age-of-ai-agents)

**Слайд:** "SaaS продавал инструмент. SaS продаёт результат работы. TAM вырос с $300B до $4.6T."

---

### Принцип 15: "AI поедает посевной фонд: нет джуниоров сегодня = нет сеньоров через 7 лет"

**Аксиома:** Junior-level работа стала бесплатной — AI делает её быстрее и дешевле.

**Логика:** Junior-работа бесплатна → компании не нанимают джуниоров (UK: -46% entry-level позиций, US: -67% по ряду данных) → поколение 2023-2025 "пропущено" — никогда не нанято → через 5-7 лет нет mid-level → через 10 лет — катастрофическая нехватка seniors.

**Неочевидный вывод:** Парадоксальная инвестиционная возможность. Компании, которые ПРОДОЛЖАЮТ нанимать и обучать джуниоров (при перестроенном training), через 5-7 лет будут владеть самым дефицитным ресурсом — людьми, понимающими систему ниже уровня AI-абстракции. Stanford: -20% занятость разработчиков 22-25 лет. Традиционные 4-летние CS-программы теряют смысл.

**Источники:**
- [Stack Overflow: AI vs Gen Z — Career Pathway Broken](https://stackoverflow.blog/2025/12/26/ai-vs-gen-z/)
- [Junior Developer Extinction: 67% Hiring Collapse](https://byteiota.com/junior-developer-extinction-67-hiring-collapse-explained/)
- [Stanford: Employment for 22-25 Declined 20%](https://www.rezi.ai/posts/entry-level-jobs-and-ai-2026-report)
- [CIO: Demand for Junior Developers Softens](https://www.cio.com/article/4062024/demand-for-junior-developers-softens-as-ai-takes-over.html)

**Слайд:** "Не нанимаешь джуниоров сегодня — через 7 лет без сеньоров. AI поедает посевной фонд."

---

## Сводная таблица: 15 принципов

| # | Группа | Принцип | Что free | Что scarce | Слайд |
|---|--------|---------|----------|-----------|-------|
| 1 | Рынки | Product-as-Worker | Когнитивный труд | Оркестрация outcomes | Продавай результат, не кресло |
| 2 | Рынки | Закон Кристенсена для AI | Общий интеллект | Контекст и workflow | Прибыль ушла в контекст |
| 3 | Рынки | Learning Velocity > Data | Данные (синтетика) | Скорость learning loop | Побеждает скорость обучения |
| 4 | Рынки | GPT-лестница | Текущий уровень AI | Позиция на следующей ступени | Строй для следующей ступени |
| 5 | UX | Dual Audience (Human + Agent) | AI-агенты у пользователей | Agent Experience дизайн | Два пользователя: человек и агент |
| 6 | UX | Intent > Interface | Понимание языка | Артикуляция намерений | Первая парадигма за 60 лет |
| 7 | UX | Product-of-One | Генерация UI | Правила адаптации | Фиксированный дизайн мёртв |
| 8 | Инновации | Провал бесплатен | Стоимость эксперимента | Скорость перебора | Побеждает кто проваливается быстрее |
| 9 | Инновации | Дисрапшн x100 | Время disruption-цикла | Время на реакцию | 10 месяцев, не 10 лет |
| 10 | Инновации | Экспертиза расщепилась | Знания (ответы) | Вопросы (unknown unknowns) | Дефицит — правильные вопросы |
| 11 | Инновации | Prompt-Test-Learn | Создание прототипа | Дистрибуция и внимание | Build — больше не этап |
| 12 | Оргдизайн | Бремя доказательства | Когнитивные задачи | Обоснование найма | Найм надо обосновывать |
| 13 | Оргдизайн | Песочные часы | Координация | Context и coaching | Middle management → AI-менеджеры |
| 14 | Оргдизайн | SaaS → SaS | Работа ($1/задача) | Outcome delivery | TAM x15: $300B → $4.6T |
| 15 | Оргдизайн | Посевной фонд | Junior-работа | Люди ниже AI-абстракции | Нет джуниоров = нет сеньоров |
