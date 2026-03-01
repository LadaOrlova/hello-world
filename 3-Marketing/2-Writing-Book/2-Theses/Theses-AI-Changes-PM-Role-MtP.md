---
## Инструкция для draft-этапа

> *[Это поле заполняет автор — инструкции для следующего этапа (draft)]*

---

## Фидбэк автора для итерации

> *[Заполни это поле и запусти `/new-chapter-thesis-dr` снова — скилл автоматически перейдёт в режим доработки]*
>
> Примеры фидбэка:
> - "Углуби тезис 3 — мало конкретики, нужны цифры и кейсы"
> - "Удали тезис 5 — не подходит для этой главы"
> - "Объедини тезисы 2 и 4 — они про одно и то же"
> - "Добавь тезис про влияние AI на {тему}"

---

# AI Changes the PM Role: From Feature Requestor to Strategic Builder

> **Статус:** Расширенные тезисы (фаза расхождения)
> **Версия:** 1
> **Модель ресерча:** gpt-5.2-pro (Deep Research, reasoning: xhigh)
> **Модель синтеза:** claude-opus-4-6
> **Дата:** 2026-02-25 22:00
> **Тезисов автора:** 6
> **Новых тезисов от Deep Research + KB:** 10
> **Всего тезисов:** 16
> **Коэффициент расширения:** 1.67x
> **Режим:** Deep Research + Knowledge-Researcher
> **Coverage Score:** 90.6%

---

## Главная тема

Как AI, vibe coding и AI-агенты трансформируют роль PM: от заказчика фич к стратегу, оператору конвейера гипотез и full-stack builder-у. Статья для MindTheProduct.com (English, 1000-1800 слов, practical + actionable).

---

## Coverage Score (метрики качества ресерча)

| Критерий | Оценка | Комментарий |
|----------|--------|-------------|
| Tier 1 экспертов | 10 | Cagan, Cagan+Nika, Torres, Rachitsky, Traynor, Chennapragada, Chesky, Karpathy, Dunford, Mehta |
| Tier 2 экспертов/источников | 22 | VC, академические, отраслевые отчёты |
| Tier 3 источников | 11 | Медиа, опросы, вторичные пересказы |
| Всего уникальных источников | 43 | 100% за 2024-2026 |
| Контраргументов к авторским | 13 | A1:2, A2:4, A3:2, A4:3, A5:3, A6:1 |
| Контраргументов к новым | 3 | К N4, N5, N6 |
| Новых тезисов от DR | 10 | N1-N10 |
| Ключевых дебатов | 5 | Все с обеих сторон |

---

## Оценка ценности для сегментов

| Сегмент | Описание | Релевантность KB | Ключевой Job |
|---------|----------|------------------|--------------|
| Корпоративные PM | PM в крупных компаниях, столкнувшиеся с AI-трансформацией | Наивысшая (10/10 по 8 из 18 находок) | "Понять, как AI меняет мою роль, и не потерять карьеру" |
| Product-lead стагнирующего продукта | PM, чей продукт перестал расти | Высокая (10/10 по 5 из 18 находок) | "Найти точки роста стагнирующего продукта с помощью AI" |
| Фаундер 0->1 | Основатели, запускающие продукт с нуля | Средне-высокая (10/10 по 3 из 18 находок) | "Быстро и дешево валидировать идею / купить знания" |
| VC/Инвесторы | Оценивают PM-команды и фаундеров | Средне-высокая (10/10 по 2 из 18 находок) | "Оценить, правильно ли команда использует AI" |

---

## Карта экспертов по теме

| Эксперт | Credentials | Ключевой тезис | URL | Год | Tier |
|---------|-------------|----------------|-----|-----|------|
| Marty Cagan | Founder SVPG; ex-eBay/Netscape | AI делает PRD/roadmap-театр заменяемым; PM = outcome-лидер | https://www.svpg.com/product-coaching-and-ai/ | 2026 | Tier 1 |
| Marty Cagan & Marily Nika | SVPG | Риски AI-продуктов и ответственность PM | https://www.svpg.com/ai-product-management/ | 2024 | Tier 1 |
| Teresa Torres | Discovery-коуч; автор Continuous Discovery Habits | AI-прототипирование радикально ускоряет discovery-циклы | https://www.producttalk.org/ai-prototyping-lovable/ | 2025 | Tier 1 |
| Lenny Rachitsky | ex-PM lead; крупнейший PM-ньюслеттер/подкаст | AI смещает PM-ценность в стратегию/vision/коммуникацию | https://www.lennysnewsletter.com/p/how-ai-will-impact-product-management | 2024 | Tier 1 |
| Des Traynor | Co-founder/CSO Intercom | "Death of SaaS / Dawn of Agents"; агенты меняют продукт/цены/структуры | https://destraynor.com/speaking/ | 2025 | Tier 1 |
| Aparna Chennapragada | Microsoft; строит Copilot/агентов | Prompt sets как новая спецификация: intent+examples+итерации | https://www.linkedin.com/posts/aparnacd_ive-been-saying-for-a-while-on-lenny-rachitskys-activity-7367028030768123904-Cq9r | 2025 | Tier 1 |
| Brian Chesky | CEO Airbnb | Роль PM трансформируется (меньше PM; больше product marketing + program mgmt) | https://www.theverge.com/decoder-podcast-with-nilay-patel/677324/airbnb-ceo-brian-chesky-services-redesign-app-future-travel | 2025 | Tier 1 |
| Andrej Karpathy | ex-Tesla AI; co-founder OpenAI | "Vibe coding" — AI пишет код, человек направляет | https://x.com/karpathy/status/1886192184808149383 | 2025 | Tier 1 |
| April Dunford | Автор Obviously Awesome; позиционирование B2B | "AI" сам по себе не дифференциатор; PoC != traction | https://businessofsoftware.org/2025/06/positioning-in-the-age-of-ai-what-founders-need-to-know/ | 2025 | Tier 1 |
| Ravi Mehta | ex-TripAdvisor/Facebook/Tinder; Reforge AI Strategy | Shift from craft to judgement; стратегический выбор уязвимостей | https://www.atlassian.com/blog/artificial-intelligence/shift-from-craft-to-judgement-ai | 2025 | Tier 1 |
| Boris Cherny | Head of Claude Code, Anthropic | 100% кода через Claude Code; +200% productivity | (Lenny's Podcast, 2026) | 2026 | Tier 1 |
| Marc Andreessen | a16z co-founder | "Mexican standoff" PM/eng/design; "don't be fungible" | (Lenny's Podcast, 2026) | 2026 | Tier 1 |
| Marty Cagan (из raw) | SVPG founder, "Inspired" автор | PM роль MORE essential с judgment + AI | (из 01-raw-theses) | 2025 | Tier 1 |
| Lenny Rachitsky (из raw) | #1 PM newsletter | 55% PMs: AI превзошёл ожидания; user research biggest untapped | (из 01-raw-theses) | 2025-2026 | Tier 1 |
| Tomer Cohen | LinkedIn CPO | Full-Stack Builder программа | (из 01-raw-theses) | 2025 | Tier 1 |
| Teresa Torres (из raw) | Continuous Discovery автор | Discovery ещё важнее; AI ускоряет и провалы | (из 01-raw-theses) | 2025 | Tier 1 |
| Claire Vo | LaunchDarkly CPO, ChatPRD | "Product Management is Dead" | (из 01-raw-theses) | 2024 | Tier 1 |
| Shreyas Doshi | Ex-Stripe, Twitter PM | AI сжимает feedback loop; 3-4 чел. = 30-50 | (из 01-raw-theses) | 2025 | Tier 1 |
| a16z (Angela Strange, James da Costa) | Топ-VC; enterprise/fintech | Copilot -> agent; SOR и данные — ключевой wedge | https://a16z.com/ai-copilot-ai-agent-white-collar-roles/ | 2024 | Tier 2 |
| Reforge (AI Evals) | Практики growth/product | "Evals aren't optional": AI-продукт = вероятностная система | https://www.reforge.com/blog/ai-evals-course | 2026 | Tier 2 |
| Mind the Product (Artem Chigrinets) | MtP; AI product strategy | Unit economics, reversibility, kill criteria, circuit breakers | https://www.mindtheproduct.com/the-2026-ai-product-strategy-huide-how-to-plan-budget-and-build-without-buying-into-the-hype/ | 2026 | Tier 2 |
| Mind the Product (Louron Pratt) | MtP; LinkedIn Jobs on the Rise | Product thinking как ключевой навык для AI-рынка | https://www.mindtheproduct.com/product-thinking-driving-fastest-growing-jobs/ | 2026 | Tier 2 |
| MIT Sloan Management Review | Авторитетный management-журнал | Ambiguity вызывает защитные реакции; нужна дисциплина работы с неопределённостью | https://sloanreview.mit.edu/article/why-mindful-leaders-are-better-at-managing-change/ | 2025 | Tier 2 |
| Infosys + MIT Technology Review Insights | Опрос 500 бизнес-лидеров | 83% считают psych safety измеримо влияющей на AI-успех | https://www.infosys.com/newsroom/press-releases/2025/psychological-safety-driving-ai-initiatives.html | 2025 | Tier 2 |
| Veracode | AppSec-лидер; отчёты по уязвимостям | AI-код часто небезопасен; безопасность не "самоулучшается" с моделями | https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/ | 2025 | Tier 2 |
| Daniotti et al. | Исследователи; 80M commits | AI-кодинг массовый, но неравномерный; влияет на output | https://arxiv.org/abs/2506.08945 | 2025 | Tier 2 |
| WORKBank (Brynjolfsson, Yang et al.) | Аудит задач для агентов | Автоматизация должна совпадать с желанием работников по human agency | https://arxiv.org/abs/2506.06576 | 2025 | Tier 2 |
| "Responsible GenAI Use by Product Managers" | Академическое исследование | PM как gatekeepers ответственности в genAI-использовании | https://arxiv.org/abs/2501.16531 | 2025 | Tier 2 |
| METR RCT (через TechCrunch) | Рандомизированный контролируемый эксперимент | -19% скорость у опытных разработчиков с AI-тулом | https://techcrunch.com/2025/07/11/ai-coding-tools-may-not-speed-up-every-developer-study-shows/ | 2025 | Tier 2 |
| GitClear | Анализ на больших данных | Refactoring падает, duplication растёт | https://www.gitclear.com/recent_ai_developer_productivity_code_quality_research | 2025 | Tier 2 |
| CodeRabbit | Code review данные | AI-PRs несут больше logic/correctness проблем | https://www.helpnetsecurity.com/2025/12/23/coderabbit-ai-assisted-pull-requests-report/ | 2025 | Tier 2 |
| YC / Jared Friedman (через TechCrunch) | Y Combinator | ~25% стартапов W25 имеют ~95% AI-код | https://techcrunch.com/2025/03/06/a-quarter-of-startups-in-ycs-current-cohort-have-codebases-that-are-almost-entirely-ai-generated/ | 2025 | Tier 2 |
| Rep. Valerie Foushee (US House) | Конгрессвумен; отчёт о layoffs | 54,694 AI-related сокращения в 2025 | https://foushee.house.gov/media/press-releases/amid-historic-layoffs-surge-rep-foushee-releases-report-on-ais-impact-on-american-jobs-and-demands-clarity-from-industry-leaders | 2025 | Tier 2 |
| LeadDev (AI Impact Report 2025) | Отраслевой отчёт | 54% engineering leaders ожидают снижение junior-найма | https://leaddev.com/hiring/what-happens-when-learn-code-fails-generation | 2025 | Tier 2 |
| EY Agentic AI Workplace Survey | Глобальный опрос | Высокие доли "falling behind / hesitancy" у desk-workers | https://www.ey.com/en_us/insights/consumer-products/how-workers-in-consumer-products-feel-about-agentic-ai | 2026 | Tier 2 |
| Lenny Distilled (Madhavan Ramanujam) | Pricing expert; 400+ компаний | AI pricing: outcome-based, не seat-based | https://www.lennydistilled.com/episodes/pricing-your-ai-product-lessons-from-400-companies-and-50-unicorns/ | 2025 | Tier 2 |
| GitHub (Copilot study) | Платформа разработки | Claims про улучшение quality/maintainability | https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/ | 2025 | Tier 2 |
| Brian Chesky — через Fortune | CEO Airbnb | AI = best thing; "самодестабилизируйтесь" | https://fortune.com/2026/02/17/airbnb-ceo-brian-chesky-says-ai-best-thing-ever-happened-company-warns-other-founders-get-onboard-or-else/ | 2026 | Tier 2 |
| Brian Chesky — через LA Times | CEO Airbnb | Инструменты "ещё не готовы" (отказ от интеграции с ChatGPT) | https://www.latimes.com/business/story/2025-10-21/chesky-says-openai-tools-not-ready-for-chatgpt-tie-up-with-airbnb-app | 2025 | Tier 2 |
| Meta (как симптом) | PM-ы ребрендятся в "AI builders" | Границы ролей размываются | https://www.businessinsider.com/meta-pms-ai-builders-tech-industry-2026-2 | 2026 | Tier 3 |
| Jason Lemkin | SaaStr | Агентность доходит до sales/SDR | https://www.businessinsider.com/godfather-of-saas-jason-lemkin-replace-humans-ai-agents-sales-2026-1 | 2026 | Tier 3 |
| Jack Clark / Anthropic (через прессу) | Co-founder Anthropic | "Ценность junior-ролей сомнительна"; найм -> senior-judgment | https://www.businessinsider.com/anthropic-ai-value-of-junior-roles-dubious-senior-talent2026-2 | 2026 | Tier 3 |
| SnapLogic survey (через TechRadar) | Опрос менеджеров | Доверяют агентам больше, чем junior-сотрудникам | https://www.techradar.com/pro/many-managers-say-they-trust-ai-agents-more-than-junior-workers | 2025 | Tier 3 |
| Dayforce study (через прессу) | Опрос | Разрыв внедрения AI: executives vs остальные | https://www.businessinsider.com/executives-adopting-ai-higher-rates-than-workers-research-2025-10 | 2025 | Tier 3 |
| Компании, наращивающие entry-level hiring | Обзор рынка | K-форма может смягчаться стратегией обучения | https://www.businessinsider.com/companies-boosting-hiring-entry-level-engineers-2026-2 | 2026 | Tier 3 |
| "Vibe coding" (Guardian) | Collins Dictionary Word of the Year | Массовое закрепление термина | https://www.theguardian.com/technology/2025/nov/06/vibe-coding-collins-dictionary-word-of-the-year-2025 | 2025 | Tier 3 |
| Workday report (через Investopedia) | Опрос | "AI bosses"; трансформация управленческих ролей | https://www.investopedia.com/are-ai-bosses-the-future-11795779 | 2025 | Tier 3 |
| Kelly briefing (LinkedIn AI Confidence Survey) | Опрос | AI confidence в рабочей среде | https://www.kellyservices.us/news-and-insights/need-to-know-briefing-february-2-2026 | 2026 | Tier 3 |
| General Assembly survey | Опрос PM-ов | AI и product management | https://generalassemb.ly/blog/ai-and-product-management-survey/ | 2025 | Tier 3 |
| a16z-VCs (через TechCrunch) | VC-комментарий | "Никто не знает, что такое agent" | https://techcrunch.com/2025/05/12/even-a16z-vcs-say-no-one-really-knows-what-an-ai-agent-is/ | 2025 | Tier 3 |

---

## Тезисы автора (обогащённые)

### Тезис А1: Business Judgment и стратегическое влияние — через psychological safety

**Суть:**
Абсолютно критичный навык в эпоху AI — business judgment: способность принимать правильные бизнес-решения в условиях неопределённости. Когда AI автоматизирует исполнение, ключевым дифференциатором становится не скорость делания, а качество решений: какие гипотезы проверять, какие рынки выбирать, какие trade-offs делать. Knowledge Base даёт judgment точное определение через AURA: способность диагностировать ГДЕ в каузальной цепочке (Рынок - Сегменты - Jobs - Ценность - Коммуникация - Юнит-экономика - Прибыль) проблема, и сделать ПРАВИЛЬНЫЙ стратегический выбор. Формула RAT математически доказывает: когда AI обрушивает стоимость проверки (знаменатель), доминирует числитель — идентификация рисков и оценка последствий. PM-ы, которые "двигают таски в Task Tracker" — их ТОЧНО заменят. Cagan (SVPG, 2026) подтверждает: AI делает "PM-театр" (PRD/roadmap/user stories) дешёвым и заменяемым агентом; ценность PM смещается к ответственности за outcomes. Mehta (Reforge, 2025): ключевой вопрос — как не быть "съеденным" горизонтальными AI-платформами. Но этот подъём болезненный: 67% PM сообщают о тревоге (Perspective AI). КРИТИЧЕСКИ ВАЖНЫЙ REFRAME: Infosys+MIT (2025): 83% лидеров считают psychological safety измеримо влияющей на успех AI-инициатив. HBR: "Hesitation grounded in ambiguity, not ego." Нейронаука KB усиливает: мозг действует как инвестор метаболических ресурсов, AI не может оценить субъективную БОЛЬ клиента — judgment развивается через практику. Vibe coding без judgment = "проклятый цикл фич" на стероидах: AI ускоряет execution, но если direction неверный, скорость только увеличивает потери.

**Происхождение:** Авторский (из потока мыслей)
**Глубина:** Глубокий — 5 почему пройдены, first principles через RAT + нейронауку (Brain-as-Investor)
**Актуальность:** Вечнозелёный (judgment как навык вне времени + актуальные данные 2025-2026)
**Статус:** Подтверждается

**Ценность для сегментов:** Корп. PM 10/10, Product-lead 9/10, Фаундер 8/10, VC 9/10

**Из Knowledge Base (AURA/AJTBD):**

1. **Формула RAT (Risk Assumption Test Priority Formula):** Приоритет = (Вероятность риска x Последствия в деньгах) / Стоимость проверки. AI обрушивает знаменатель -> числитель (human judgment) доминирует. PM, который не умеет оценивать вероятность и последствия, генерирует бесполезные проверки, даже если они дешевы.
   - Файл: `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/RAT/risk-assumption-test.md`

2. **Привычка = физическое изменение мозга (3x переоценка готовности):** Мозг вырастил нейросеть для координационной работы PM. Люди В 3 РАЗА переоценивают готовность поменять привычку. Первая реакция на смену способа — отказ и тревога. PM, который говорит "я готов стать builder" — в реальности будет менять привычки в 3 раза медленнее.
   - Файл: `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/AJTBD/main-idea.md`

3. **Feature Mill Trap (проклятый цикл фич):** 90% ресурсов инвестируются в мертворожденные фичи. С AI цикл может УСКОРИТЬСЯ катастрофически: PM может создавать мертворожденные фичи в 10x быстрее. Нет бэклога с ценностью — есть бэклог с фичами.
   - Файл: `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/AJTBD/value-creation.md`

4. **Мультипликативная модель рисков:** 7 рисков при 40% вероятности подтверждения дают 3% шанс на успех. AI делает создание сложного продукта дешевым, но НЕ снижает количество рисков. Каждое добавление МНОЖИТ риски.
   - Файл: `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/RAT/risk-assumption-test.md`

5. **Brain-as-Investor Model:** Мозг как инвестор метаболических ресурсов: инсула при цене (боль), нуклеус аккумбенс при оффере (предвкушение). AI не может оценить субъективную БОЛЬ клиента — judgment развивается через практику (интервью, эмпатию).
   - Файл: `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/AJTBD/psychology.md`

**Экспертные мнения (от Deep Research):**

| Эксперт | Позиция | URL | Tier | Год |
|---------|---------|-----|------|-----|
| Marty Cagan | AI делает "PM-театр" заменяемым; PM = outcome-лидер | https://www.svpg.com/product-coaching-and-ai/ | Tier 1 | 2026 |
| Ravi Mehta | Shift from craft to judgement; стратегический выбор уязвимостей | https://www.atlassian.com/blog/artificial-intelligence/shift-from-craft-to-judgement-ai | Tier 1 | 2025 |
| Infosys + MIT Technology Review | 83% лидеров: psych safety измеримо влияет на AI-успех | https://www.infosys.com/newsroom/press-releases/2025/psychological-safety-driving-ai-initiatives.html | Tier 2 | 2025 |
| MIT Sloan Management Review | Сопротивление = "защитная реакция" на ambiguity | https://sloanreview.mit.edu/article/why-mindful-leaders-are-better-at-managing-change/ | Tier 2 | 2025 |

**Контраргументы:**

| Кто | Суть | URL | Tier | Год |
|-----|------|-----|------|-----|
| a16z (Strange, da Costa) | Каждая white-collar роль получит copilot; "judgment PM" ценен только при высоком контексте/цене ошибки; заменяемость растёт | https://a16z.com/ai-copilot-ai-agent-white-collar-roles/ | Tier 2 | 2024 |
| SnapLogic survey | Менеджеры уже доверяют агентам больше, чем junior-сотрудникам; снижает переговорную силу knowledge workers без сильного judgment | https://www.techradar.com/pro/many-managers-say-they-trust-ai-agents-more-than-junior-workers | Tier 3 | 2025 |

**First Principles углубление:**
- Аксиома: execution (код/PRD/мокапы) стал почти бесплатным
- Цепочка: execution дешевеет -> растёт option space решений/гипотез -> выбор и trade-offs = главный bottleneck -> выбор под высокой неоднозначностью и личной ответственностью -> конкурентное преимущество PM переезжает из "написать/собрать" в "выдержать ambiguity, принять решение и нести ответственность"
- НЕОЧЕВИДНЫЙ ВЫВОД: это невозможно без среды, где безопасно экспериментировать и ошибаться — psychological safety становится продуктовой переменной, а не HR-лозунгом

**Что изменилось в 2025-2026:**
- SVPG перекалибровал позицию: AI обнажает театральные артефакты, вынуждая PM становиться outcome-лидерами
- В enterprise "психологическая безопасность" стала измеримой управленческой переменной (а не HR-лозунгом)
- Цифру "67% тревожности PM из Perspective AI" как первоисточник найти не удалось; рекомендовано опираться на проверяемые опросы

---

### Тезис А2: PM-ы становятся full-stack builders

**Суть:**
Все PM будут становиться full-stack builder-ами. Точка перелома: ноябрь-декабрь 2025. Boris Cherny (Head of Claude Code): с ноября 2025 100% его кода пишется Claude Code, ни одной строки вручную. Productivity per engineer +200%. Karpathy (2025) ввёл термин "vibe coding" — человек говорит "что хочу", AI пишет код, роль человека — смотреть результат, итеративно править. YC W25: 25% стартапов имеют 95% AI-генерированного кода. Marc Andreessen: "Mexican standoff" между PM, инженерами и дизайнерами — каждый верит, что может делать работу двух других с AI, и они все правы. T-shaped -> E/F-shaped навыки. LinkedIn формализовал: "Associate Product Builder" (Dec 2025). Torres (2025): AI-прототипирование сокращает время до интерактивного прототипа до часов. Meta (2026): PM-ы ребрендятся в "AI builders". KB через AJTBD объясняет механику: PM с vibe coding буквально "убивает работы" — написание PRD, создание мокапов, код прототипа перестают существовать. PM поднимается на уровень Big Job (стратегия + создание ценности), убивая десятки Small Jobs. Full-stack builder PM решает проблему рассинхронизации функций: сам проводит ресерч, создаёт прототип, тестирует, коммуницирует ценность. Но 5 почему из DR: full-stack builder — это не "PM научился кодить", а "PM научился держать production-качество через тесты, ревью, ограничения и экономику".

**Происхождение:** Авторский (из потока мыслей)
**Глубина:** Глубокий — AJTBD-механики "Kill a Job" + "Level Up" дают фреймворк
**Актуальность:** Актуальный 2025+ (vibe coding = Word of the Year 2025, Meta ребрендинг 2026)
**Статус:** Подтверждается с оговорками (сильные контраргументы по quality/security)

**Ценность для сегментов:** Корп. PM 9/10, Product-lead 10/10, Фаундер 9/10, VC 8/10

**Из Knowledge Base (AURA/AJTBD):**

1. **Механика "Убить работу" (Kill a Job):** Работы ниже уровня просто исчезают как класс. PM с vibe coding буквально убивает работы (написание PRD, мокапы, код прототипа). Объясняет "Mexican standoff" Andreessen — когда работы PM/eng/design убиты, нет причин для разделения ролей.
   - Файл: `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/AJTBD/value-creation.md`

2. **Выход на работу выше уровня (Level Up):** PM, который остается на уровне Core Job (координация) — это cPanel. PM, который поднимается на Big Job (стратегия + создание ценности) — это Tilda. AI — инструмент подъёма. AJTBD прямо говорит об "угрозе AI" через механику подъёма на уровень выше.
   - Файл: `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/AJTBD/value-creation.md`

3. **Рассинхронизация функций (AURA-Desync Problem):** Исследователи делают исследования, которые не используются; продукт пилит фичи, которые не продаются. Full-stack builder PM решает эту проблему: один человек + AI-агенты выполняет всю цепочку. Рассинхронизация невозможна.
   - Файлы: `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/AURA/overview.md`, `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/AURA/product-strategy.md`

4. **Job-based Communication как irreducible skill:** AI может генерировать текст лендинга, но НЕ МОЖЕТ определить: какой сегмент фокусный, какие у него работы, критерии успеха, барьеры. PM определяет ЧТО коммуницировать (judgment), AI генерирует КАК (execution).
   - Файл: `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/AJTBD/communication.md`

**Экспертные мнения (от Deep Research):**

| Эксперт | Позиция | URL | Tier | Год |
|---------|---------|-----|------|-----|
| Andrej Karpathy | "Vibe coding" — AI пишет код, человек направляет | https://x.com/karpathy/status/1886192184808149383 | Tier 1 | 2025 |
| Teresa Torres | AI-прототипирование сокращает время до часов | https://www.producttalk.org/ai-prototyping-lovable/ | Tier 1 | 2025 |
| YC / Jared Friedman | ~25% стартапов W25 имеют ~95% AI-код | https://techcrunch.com/2025/03/06/a-quarter-of-startups-in-ycs-current-cohort-have-codebases-that-are-almost-entirely-ai-generated/ | Tier 2 | 2025 |
| Meta (как симптом) | PM-ы ребрендятся в "AI builders" | https://www.businessinsider.com/meta-pms-ai-builders-tech-industry-2026-2 | Tier 3 | 2026 |

**Контраргументы:**

| Кто | Суть | URL | Tier | Год |
|-----|------|-----|------|-----|
| METR RCT | Опытные OSS-разработчики на 19% медленнее с AI-тулом; "ощущение продуктивности" может быть ложным | https://techcrunch.com/2025/07/11/ai-coding-tools-may-not-speed-up-every-developer-study-shows/ | Tier 2 | 2025 |
| Veracode | AI-код "ломал безопасность" в ~45% случаев; новые модели не показывают улучшений | https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/ | Tier 2 | 2025 |
| CodeRabbit | AI-coauthored PRs несут больше logic/correctness проблем и security findings | https://www.helpnetsecurity.com/2025/12/23/coderabbit-ai-assisted-pull-requests-report/ | Tier 2 | 2025 |
| GitClear | Падает рефакторинг, растёт копипаст/дублирование — ускорение "компаундит" техдолг | https://www.gitclear.com/recent_ai_developer_productivity_code_quality_research | Tier 2 | 2025 |

**First Principles углубление:**
- Аксиома: "первый черновик кода" почти бесплатен
- Цепочка: PM может проверять гипотезы без очереди к инженерам -> скорость цикла растёт -> роль "собрать руками" теряет премию -> но стоимость ошибок/уязвимостей остаётся высокой
- НЕОЧЕВИДНЫЙ ВЫВОД: full-stack builder — это не "PM научился кодить", а "PM научился держать production-качество через тесты, ревью, ограничения и экономику"

**Что изменилось в 2025-2026:**
- "Vibe coding" стало массовым понятием (Word of the Year по Collins Dictionary)
- Одновременно появились жёсткие эмпирические "холодные души" (slowdown, security, техдолг)

---

### Тезис А3: PM как оператор конвейера гипотез, оркестратор агентов и маленьких команд

**Суть:**
PM станут управлять конвейером проверки гипотез И оркестрировать флоты AI-агентов в маленьких командах. AI позволяет в единицу времени проверять на порядок больше гипотез — индустриальный конвейер. KB даёт парадигму: "Мы не запускаем продукты — мы покупаем знания." PM как "оператор конвейера гипотез" — буквальное описание: PM покупает знания через AI-агентов. Главный алгоритм AURA становится blueprint для hypothesis pipeline: бизнес-цель -> гипотетический граф -> механики -> ресерч -> реальный граф -> RAT -> реализация. Каждый шаг может быть делегирован AI-агенту. Но делегирование идёт по уровню риска (KB): AI-агенты = "менее компетентные сотрудники" — им низкорискованные задачи (A/B-тесты, анализ данных), PM оставляет высокорискованные (выбор сегмента, стратегия, ethical judgment). Chennapragada (Microsoft, 2025): "Prompt sets — новые PRD." Reforge (2026): AI-продукты вероятностные — нужны eval-системы и наблюдаемость качества. Команды становятся меньше: Shreyas Doshi: "3-4 person startups = impact of 30-50." PM сдвигается от документации к curriculum design: PRD мертвы, PM пишет "prompt sets" — живые артефакты, одновременно спецификация и тренировочные данные. 90% решений бессознательны (KB) — эмпатическое интервью, считывание эмоций, понимание глубинных потребностей — навыки, которые AI не автоматизирует. Это "irreducible human core" роли PM.

**Происхождение:** Авторский (из потока мыслей)
**Глубина:** Глубокий — Main Algorithm AURA + RAT delegation model дают конкретный blueprint
**Актуальность:** Актуальный 2025+ (evals/prompt sets — лексика 2025-2026)
**Статус:** Подтверждается

**Ценность для сегментов:** Корп. PM 10/10, Product-lead 10/10, Фаундер 9/10, VC 8/10

**Из Knowledge Base (AURA/AJTBD):**

1. **Парадигма "Мы покупаем знания, не запускаем продукты":** Наиболее вероятный исход — провал; задача PM — максимально быстро и дешево это выяснить. Конвейер гипотез = конвейер покупки знаний.
   - Файл: `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/RAT/risk-assumption-test.md`

2. **Главный алгоритм AURA как blueprint:** Бизнес-цель -> Гипотетический граф -> Механики -> Ресерч -> Реальный граф -> Применить механики -> Ранжировать по RICE -> RAT -> Реализовать. ChatGPT уже строит гипотетический граф.
   - Файлы: `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/Algorithms/main-algorithm.md`, `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/Algorithms/create-value.md`

3. **Делегирование по уровню риска (RAT Delegation Model):** Дорогие риски — топ-менеджменту (самым компетентным), дешевые — менее компетентным. AI-агенты = "менее компетентные сотрудники".
   - Файл: `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/RAT/risk-assumption-test.md`

4. **90% решений бессознательны:** Мозг принимает 200+ решений про еду в день, человек помнит 37. AI анализирует осознаваемые данные, но 90% мотиваций бессознательны — "irreducible human core".
   - Файл: `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/AJTBD/psychology.md`

5. **Job-based Communication:** Описанные работы можно передать в ChatGPT и получить черновик лендинга. PM определяет ЧТО коммуницировать (prompt set из Jobs/Value/Barriers), AI генерирует КАК.
   - Файл: `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/AJTBD/communication.md`

**Экспертные мнения (от Deep Research):**

| Эксперт | Позиция | URL | Tier | Год |
|---------|---------|-----|------|-----|
| Aparna Chennapragada | "Prompt sets — новые PRD": intent + examples + итерации | https://www.linkedin.com/posts/aparnacd_ive-been-saying-for-a-while-on-lenny-rachitskys-activity-7367028030768123904-Cq9r | Tier 1 | 2025 |
| Reforge (AI Evals) | AI-продукты вероятностные; нужны eval-системы и наблюдаемость качества | https://www.reforge.com/blog/ai-evals-course | Tier 2 | 2026 |
| a16z | Агенты "естественно" встраиваются в system-of-record; данные/контекст — ключевой wedge | https://a16z.com/ai-copilot-ai-agent-white-collar-roles/ | Tier 2 | 2024 |

**Контраргументы:**

| Кто | Суть | URL | Tier | Год |
|-----|------|-----|------|-----|
| a16z-VCs (через TechCrunch) | Слово "agent" размыто; "замена человека" требует почти AGI и пока "не работает" как обещают | https://techcrunch.com/2025/05/12/even-a16z-vcs-say-no-one-really-knows-what-an-ai-agent-is/ | Tier 2 | 2025 |
| WORKBank (Brynjolfsson, Yang et al.) | Автоматизация должна совпадать с желанием работников по human agency; иначе внедрение ломается на доверии | https://arxiv.org/abs/2506.06576 | Tier 2 | 2025 |

**First Principles углубление:**
- Аксиома: throughput экспериментов растёт благодаря AI
- Цепочка: "артефакты управления" превращаются в исполняемые контракты (prompts/evals) -> качество = "распределение", которое надо сужать -> агентные цепочки требуют ограничений (cost, безопасность, права)
- НЕОЧЕВИДНЫЙ ВЫВОД: PM становится оператором "линии качества": определяет поведенческие контракты, измерения, стоп-условия и экономику

**Что изменилось в 2025-2026:**
- Сформировалась управленческая лексика "prompt spec" и "evals" как продуктовые (не сугубо ML) артефакты
- Скепсис переместился с "можно ли сделать агента" на "как определить агента и доказать пользу/надёжность"

---

### Тезис А4: Полный цикл до продакшена и продаж — через 12-24 месяца

**Суть:**
Через год-два появится полный цикл вплоть до тестов и продаж. Сейчас можно делать прототипы, но безопасность и deploy не позволяют катать эксперименты в существующем продукте. Des Traynor (Intercom, 2025) артикулирует "конец SaaS / восход агентов" — переформатирование продуктов, pricing и оргструктур. Brian Chesky (Airbnb, 2026): AI = best thing that ever happened; призыв "самодестабилизироваться". Jason Lemkin (SaaStr, 2026): агентность доходит до sales/SDR. Boris Cherny: "We're starting to branch out of coding — paying parking tickets, project management, messaging on Slack." Но KB через Critical Chain предупреждает: от прототипа до production — цепочка разрывается на security, DevOps, compliance. Скорость цепи = скорость самого медленного звена. AI ускоряет отдельные звенья (код), но если цепочка рвётся — результат не достигается. Математика рисков: AI удешевляет creation, но каждый добавленный компонент множит вероятность провала. Сам Chesky (через LA Times, 2025) признаёт: инструменты "ещё не готовы". April Dunford (2025): PoC-выручка часто ошибочно принимается за traction; AI-продукты массово застревают в пилотах.

**Происхождение:** Авторский (гипотеза-прогноз)
**Глубина:** Средний — KB даёт фреймворк Critical Chain, но конкретных данных мало
**Актуальность:** Актуальный 2025+ (быстро меняется; данные Chesky Feb 2026)
**Статус:** Спорный (сильные контраргументы; сам Chesky признаёт "не готово")

**Ценность для сегментов:** Корп. PM 10/10, Product-lead 8/10, Фаундер 9/10, VC 7/10

**Из Knowledge Base (AURA/AJTBD):**

1. **Критическая цепочка (Critical Chain of Jobs):** Последовательность обязательных работ для достижения результата. Скорость цепи = скорость самого медленного звена. Циклы (возврат на доработку) — главная угроза.
   - Файл: `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/AJTBD/critical-chain.md`

2. **Мультипликативная модель рисков:** 7 рисков при 40% — 3% шанс. AI удешевляет creation, но НЕ снижает количество рисков.
   - Файл: `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/RAT/risk-assumption-test.md`

**Экспертные мнения (от Deep Research):**

| Эксперт | Позиция | URL | Tier | Год |
|---------|---------|-----|------|-----|
| Des Traynor | "Конец SaaS / восход агентов"; переформатирование продуктов/цен/структур | https://destraynor.com/speaking/ | Tier 1 | 2025 |
| Brian Chesky | AI = best thing for Airbnb; "самодестабилизируйтесь" | https://fortune.com/2026/02/17/airbnb-ceo-brian-chesky-says-ai-best-thing-ever-happened-company-warns-other-founders-get-onboard-or-else/ | Tier 1 | 2026 |
| Jason Lemkin | Агентность доходит до sales/SDR | https://www.businessinsider.com/godfather-of-saas-jason-lemkin-replace-humans-ai-agents-sales-2026-1 | Tier 3 | 2026 |

**Контраргументы:**

| Кто | Суть | URL | Tier | Год |
|-----|------|-----|------|-----|
| Brian Chesky (LA Times) | Инструменты "ещё не готовы" (отказ от интеграции с ChatGPT) | https://www.latimes.com/business/story/2025-10-21/chesky-says-openai-tools-not-ready-for-chatgpt-tie-up-with-airbnb-app | Tier 2 | 2025 |
| April Dunford | PoC-выручка часто ошибочно принимается за traction; AI-продукты застревают в пилотах | https://businessofsoftware.org/2025/06/positioning-in-the-age-of-ai-what-founders-need-to-know/ | Tier 2 | 2025 |
| Veracode | Security-провалы системны; "полный цикл до продакшена" = "полный цикл до инцидента" | https://www.veracode.com/blog/genai-code-security-report/ | Tier 2 | 2025 |

**First Principles углубление:**
- Аксиома: агенты закрывают цепочки задач
- Цепочка: GTM/ops часто формализуемы -> компании начинают менять организацию под скорость -> production-барьеры (security, cost-runaway, комплаенс) выше, чем барьеры прототипа
- НЕОЧЕВИДНЫЙ ВЫВОД: end-to-end появится прежде всего там, где риск дешевле; в enterprise победит тот, кто умеет делать reversibility + kill criteria + circuit breakers

**Что изменилось в 2025-2026:**
- "Agent talk" из технологического хайпа переехал в продуктовые/организационные решения и кейсы в sales/support

---

### Тезис А5: Спрос на Knowledge Workers растёт, а не падает

**Суть:**
PM, разбирающиеся в JTBD, создании ценности, юнит-экономике + умеющие строить agent pipeline — будут супер востребованы. AI PMs зарабатывают на 35% больше. 75% работодателей не могут найти qualified AI-PM. Marc Andreessen: "If we didn't have AI, we'd be in a panic about the economy. Remaining human workers at a premium, not a discount. Task loss, not job loss." MtP (2026): продуктовый бэкграунд — один из главных "мостов" в новые AI-роли. Daniotti et al. (2025): AI-кодинг массовый и связан с ростом output — растёт спрос на тех, кто определяет что строить. Но 5 почему из DR уточняют: спрос растёт НЕ "на всех knowledge workers", а на тех, кто умеет управлять агентами и отвечать за эффект. KB через ABCDX-сегментацию объясняет: A-сегмент = builder-PM, B = готовы меняться, C = жалуются и требуют "защиты профессии", D = активно сопротивляются. Компании перераспределяют ресурсы: фокус на A/B, отказ от C/D. "Task loss, not job loss" = перераспределение ABCDX. Контраргументы ОЧЕНЬ СИЛЬНЫЕ: 54,000+ AI-сокращений в US 2025 (Foushee), 54% eng leaders нанимают МЕНЬШЕ джуниоров (LeadDev), Jack Clark/Anthropic: "ценность junior-ролей сомнительна".

**Происхождение:** Авторский (из потока мыслей)
**Глубина:** Средний — нуждается в нюансировке; ABCDX даёт фреймворк
**Актуальность:** Актуальный 2025+ (данные меняются быстро)
**Статус:** Спорный (сильные контраргументы по сокращениям и junior-найму)

**Ценность для сегментов:** Корп. PM 9/10, Product-lead 8/10, Фаундер 6/10, VC 8/10

**Из Knowledge Base (AURA/AJTBD):**

1. **ABCDX-сегментация PM-рынка:** A = builder-PM (маржинальные, удовлетворенные), B = готовы меняться, C = жалуются, D = токсичные. C и D занимают 80% энергии, принося 20% ценности. Компании перераспределяют ресурсы.
   - Файл: `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/ABCDX/abcdx-segmentation.md`

**Экспертные мнения (от Deep Research):**

| Эксперт | Позиция | URL | Tier | Год |
|---------|---------|-----|------|-----|
| Mind the Product (Louron Pratt) | Продуктовый бэкграунд — мост в AI-роли | https://www.mindtheproduct.com/product-thinking-driving-fastest-growing-jobs/ | Tier 2 | 2026 |
| Daniotti et al. | AI-кодинг массовый и связан с ростом output | https://arxiv.org/abs/2506.08945 | Tier 2 | 2025 |

**Контраргументы:**

| Кто | Суть | URL | Tier | Год |
|-----|------|-----|------|-----|
| Rep. Valerie Foushee | 54,694 сокращения в 2025 прямо помечены как AI-related | https://foushee.house.gov/media/press-releases/amid-historic-layoffs-surge-rep-foushee-releases-report-on-ais-impact-on-american-jobs-and-demands-clarity-from-industry-leaders | Tier 2 | 2025 |
| LeadDev | 54% engineering leaders ожидают долгосрочное снижение junior-найма | https://leaddev.com/hiring/what-happens-when-learn-code-fails-generation | Tier 2 | 2025 |
| Jack Clark / Anthropic | "Ценность junior-ролей сомнительна"; найм -> senior-judgment | https://www.businessinsider.com/anthropic-ai-value-of-junior-roles-dubious-senior-talent2026-2 | Tier 3 | 2026 |

**First Principles углубление:**
- Аксиома: AI расширяет объём потенциально создаваемого ПО
- Цепочка: растут рынки автоматизации -> растёт спрос на ownership и смысл (strategy/economics/risk) -> "джун-работа" как набор рутинных задач частично автоматизируется
- НЕОЧЕВИДНЫЙ ВЫВОД: спрос растёт не "на всех knowledge workers", а на тех, кто умеет управлять агентами и отвечать за эффект

**Что изменилось в 2025-2026:**
- Одновременно "плюс" (рост AI-ролей и переходов) и "минус" (AI-маркированные сокращения, сжатие junior-входа)

---

### Тезис А6: Расслоение и K-shaped бифуркация — через psychological safety

**Суть:**
PM-рынок раскалывается в форме K: surging demand на полюсах (AI-специалисты +35% и AI-усиленные senior generalists) при вымывании mid-level ролей. AI-savvy джуниоры outperform senior-ов, создавая "performance inversion". KB через Four Forces объясняет: AI-builder PM — высокая добавочная ценность, сильные проблемы текущего подхода, низкие барьеры (Claude Code, Cursor доступны). Traditional PM — привычка к координационной модели ОГРОМНА, страхи перед кодингом высоки. Рынок раскалывается на тех, у кого силы "вперёд" (builders) и "назад" (coordinators). KB через Local vs Global Optimum: AI отлично справляется с задачами ЛОКАЛЬНОГО оптимума (A/B тесты, UX-улучшения) — PM, который работает только на local, вымывается AI; PM, который работает на global, становится незаменимым. Дилемма инноватора (KB): компании, которые разрушаются, НЕ плохо работают, а ХОРОШО — текущий процесс "работает", менять страшно, стартапы с AI-PM обходят. Daniotti et al. (2025): неравномерное прибытие AI-кодинга по странам и cohorts усиливает разрыв. EY (2026): высокие доли "falling behind / hesitancy". Люди в 3 раза переоценивают готовность сменить привычку (KB). REFRAME: Не "адаптируйся или умри", а "создай безопасную среду". Это не только индивидуальный выбор — СТРУКТУРНОЕ неравенство. 5 почему из DR: расслоение — следствие не "таланта", а архитектуры среды: обучения, политик доступа, правил ответственности.

**Происхождение:** Авторский (утверждение + framework)
**Глубина:** Глубокий — 4 слоя объяснения из KB + количественные данные из DR
**Актуальность:** Актуальный 2025+ (GitHub diffusion data, EY 2026)
**Статус:** Подтверждается

**Ценность для сегментов:** Корп. PM 10/10, Product-lead 10/10, Фаундер 7/10, VC 9/10

**Из Knowledge Base (AURA/AJTBD):**

1. **Четыре силы прогресса (Four Forces):** (1) добавочная ценность нового, (2) проблемы текущего, (3) страхи перед новым, (4) привычка к старому. AI-builder PM: силы 1-2 сильные, 3-4 слабые. Traditional PM: наоборот.
   - Файл: `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/AJTBD/main-idea.md`

2. **Локальный vs Глобальный оптимум:** Local = +10-30%, задача junior/middle. Global = x2-x10, задача founders/C-level. AI отлично справляется с local. PM local = вымывается, PM global = незаменим.
   - Файл: `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/AURA/local-vs-global-optimum.md`

3. **Дилемма инноватора:** Большие компании разрушаются не потому что плохо работают, а потому что хорошо. Фокус на текущих клиентах мешает адаптироваться. Стартапы с AI-PM обходят.
   - Файл: `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/AURA/product-strategy.md`

4. **Привычка как барьер:** 3x переоценка готовности к изменениям. PM говорят "я за AI" но продолжают работать по-старому.
   - Файл: `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/AJTBD/main-idea.md`

**Экспертные мнения (от Deep Research):**

| Эксперт | Позиция | URL | Tier | Год |
|---------|---------|-----|------|-----|
| Daniotti et al. | Неравномерное прибытие AI-кодинга по странам и cohorts | https://arxiv.org/abs/2506.08945 | Tier 2 | 2025 |
| Dayforce study | Разрыв внедрения AI: executives vs остальные | https://www.businessinsider.com/executives-adopting-ai-higher-rates-than-workers-research-2025-10 | Tier 3 | 2025 |
| EY Agentic AI Workplace Survey | Высокие доли "falling behind / hesitancy" у desk-workers | https://www.ey.com/en_us/insights/consumer-products/how-workers-in-consumer-products-feel-about-agentic-ai | Tier 2 | 2026 |

**Контраргументы:**

| Кто | Суть | URL | Tier | Год |
|-----|------|-----|------|-----|
| Компании, наращивающие entry-level hiring | K-форма может смягчаться стратегией обучения/найма (ставка на AI-native молодёжь) | https://www.businessinsider.com/companies-boosting-hiring-entry-level-engineers-2026-2 | Tier 3 | 2026 |

**First Principles углубление:**
- Аксиома: AI комплементарен к сильным mental models и доменному контексту
- Цепочка: "делегирование без понимания" ухудшает способность заметить ошибку -> доступ к качественным пайплайнам обучения/данным/наставникам распределён неравномерно
- НЕОЧЕВИДНЫЙ ВЫВОД: расслоение — следствие не "таланта", а архитектуры среды: обучения, политик доступа, правил ответственности

**Что изменилось в 2025-2026:**
- Появились количественные метрики неравномерности (GitHub diffusion) и организационных разрывов (exec vs employee adoption)

---

## Новые тезисы от Deep Research + KB (фаза расхождения)

### Тезис Н1: Evals-first PM — вместо фич вы управляете распределением качества

**Суть:**
В AI-продуктах "правильность" не бинарна — один запрос даёт распределение ответов. Классический PM-подход "написали требования -> проверили -> shipped" ломается. Побеждает тот, кто строит eval-инфраструктуру: метрики, автоматические и human-rated проверки, мониторинг деградаций по сегментам, быстрые циклы улучшения. PM превращается во владельца quality-pipeline. "Product taste" и "human judgement" становятся частью измерительной системы, а не только стратегии. Reforge (2026): "Evals aren't optional" — AI-продукт = вероятностная система; user feedback часто "направляющий, но не диагностический".

**First Principles:**
- Аксиома: генерация дешёвая, но поведение недетерминированное
- Цепочка: "фидбек пользователей" не объясняет причину -> нужны eval-наборы и диагностические проверки -> "product taste" становится частью измерительной системы
- Почему важно: PM, который не владеет evals, не может управлять качеством AI-продукта — это как PM без метрик в 2015

**Происхождение:** Deep Research
**Откуда взялся:** Reforge — https://www.reforge.com/blog/ai-evals-course (2026)
**Почему автор мог не упомянуть:** Evals — относительно новая продуктовая (не ML) практика; автор фокусировался на роли PM, а не на инструментах измерения
**Связь с авторскими тезисами:** Расширяет А3 (оркестрация агентов)
**Глубина:** Глубокий
**Актуальность:** Актуальный 2025+
**Спорный?** Да — "Evals = новая бюрократия" vs "Evals = единственный способ масштаба"

---

### Тезис Н2: Reversibility, circuit breakers и kill criteria — новая продуктовая гигиена

**Суть:**
AI-фича имеет переменную стоимость на каждый запрос (tokens/retrieval/latency). "Зомби-фичи" финансово опасны: не просто занимают место, а жгут маржу. Нужны: (1) обратимость (замена модели/провайдера), (2) kill criteria (явные условия удаления), (3) circuit breakers (лимиты шагов/стоимости). PM отвечает не только за value, но и за границы ущерба. "Delete" становится позитивным продуктовым действием (защита P&L), а не поражением.

**First Principles:**
- Аксиома: маржинальная стоимость AI-фич != 0
- Цепочка: популярность может ухудшать unit economics -> roadmap должен включать "ограничители" -> "delete" = защита P&L
- Почему важно: AI-фича без kill criteria = финансовая бомба замедленного действия

**Происхождение:** Deep Research
**Откуда взялся:** Artem Chigrinets (Mind the Product) — https://www.mindtheproduct.com/the-2026-ai-product-strategy-huide-how-to-plan-budget-and-build-without-buying-into-the-hype/ (2026)
**Почему автор мог не упомянуть:** Фокус на трансформации роли, а не на unit economics AI-фич
**Связь с авторскими тезисами:** Дополняет A4 (путь в продакшен)
**Глубина:** Глубокий
**Актуальность:** Актуальный 2025+
**Спорный?** Нет (скорее "неприятно", но практически неизбежно)

---

### Тезис Н3: Контекст — это новый продукт: PM должен управлять context supply chain

**Суть:**
В агентной экономике выигрывает не тот, у кого "самая умная модель", а тот, у кого лучший контекст: данные, права доступа, актуальность, структуры, мульти-источники. Контекстирование (retrieval, источники, обновления, политика свежести, источники истины) — самостоятельный продуктовый контур. PM-ам придётся относиться к контексту как к supply chain: входы, качество, контроль загрязнений, SLA обновления, ownership. Data-операционные процессы становятся частью продуктовой стратегии (а не "внутренней инженерии").

**First Principles:**
- Аксиома: reasoning дешевеет; ошибки контекста дорогие
- Цепочка: качество контекста определяет качество действий -> конкурентный барьер = доступ к данным и их организация -> data-ops = часть продуктовой стратегии
- Почему важно: PM, который управляет context supply chain, создаёт moat без бесконечной гонки моделей

**Происхождение:** Deep Research
**Откуда взялся:** a16z (SOR / multimodal system of record) — https://a16z.com/ai-copilot-ai-agent-white-collar-roles/ (2024)
**Почему автор мог не упомянуть:** "Контекст как продукт" — инженерный термин, который только начинает входить в PM-лексику
**Связь с авторскими тезисами:** Расширяет A3 (оркестрация) и A4 (в прод)
**Глубина:** Глубокий
**Актуальность:** Актуальный 2025+
**Спорный?** Да — "контекст-инженерия = инженерная зона" vs "контекст = продуктовый актив"

---

### Тезис Н4: Apprenticeship debt — сокращая junior-найм из-за AI, вы создаёте дефицит seniors завтра

**Суть:**
AI заменяет существенную часть "джун-работы" (рутина, шаблоны, простые исправления), и лидеры ожидают сокращение junior-позиций (54% по LeadDev). Но senior-инженеры выращиваются через годы "грязной" практики на прод-инцидентах. Если организации "выкупят скорость" ценой pipeline, через 3-5 лет они получат кадровый провал: некому будет делать архитектуру, ревью, безопасность, интеграции. "Экономия на джунах" превращается в стратегический риск (talent risk), сравнимый с техдолгом. Без сильных seniors PM-оркестрация агентов упирается в качество/риски.

**First Principles:**
- Аксиома: выполнение задач джуна стало дешевле
- Цепочка: джун-роль исчезает -> исчезает обучение на практике -> падает предложение мидлов/сеньоров -> "экономия на джунах" = talent risk
- Почему важно: PM-лидам нужно сознательно выбирать talent-стратегию, а не "плыть по рынку"

**Происхождение:** Deep Research
**Откуда взялся:** LeadDev (AI Impact Report 2025) — https://leaddev.com/hiring/what-happens-when-learn-code-fails-generation (2025)
**Почему автор мог не упомянуть:** Фокус на индивидуальной трансформации PM, а не на организационных последствиях
**Связь с авторскими тезисами:** Спорит с A5 ("спрос растёт" — да, но pipeline может обрушиться)
**Глубина:** Глубокий
**Актуальность:** Актуальный 2025+
**Спорный?** Да — есть обратные стратегии ("наращивать entry-level hiring") — https://www.businessinsider.com/companies-boosting-hiring-entry-level-engineers-2026-2

---

### Тезис Н5: PM <-> Product Marketing fusion — роль PM сдвигается к narrative, positioning и distribution

**Суть:**
Если "сделать" стало дешевле, дифференциация переезжает в: (1) story, (2) позиционирование, (3) каналы дистрибуции, (4) доверие и правила использования. Brian Chesky: меньше классических PM, больше "inbound+outbound" продуктового мышления, плюс сильная program management функция. PM-лидерство в AI-эру оценивается по способности продать "почему/кому/почему сейчас" и выстроить GTM. "Продукт" и "маркетинг" снова сближаются (как в раннем стартапе), особенно в AI-категориях.

**First Principles:**
- Аксиома: производство софта дешевеет; конкурентов больше
- Цепочка: внимание/доверие/категория становятся дефицитом -> PM должен управлять narrative/позиционированием -> PM и PMM снова сближаются
- Почему важно: PM, который не умеет в positioning и GTM, теряет влияние на бизнес-результат

**Происхождение:** Deep Research
**Откуда взялся:** Brian Chesky (Decoder / The Verge) — https://www.theverge.com/decoder-podcast-with-nilay-patel/677324/airbnb-ceo-brian-chesky-services-redesign-app-future-travel (2025)
**Почему автор мог не упомянуть:** PM-сообщество традиционно фокусируется на inbound; outbound = "не наше"
**Связь с авторскими тезисами:** Расширяет A1 (стратегическое влияние) и A2 (full-stack)
**Глубина:** Средний
**Актуальность:** Актуальный 2025+
**Спорный?** Да — часть сообщества считает, что "PM должен остаться inbound", а outbound = отдельная функция

---

### Тезис Н6: Agent UX / Agent Interop — продукт нужно проектировать для других AI, не только для людей

**Суть:**
AI-ассистенты и агенты начинают "дезинтермедиировать" приложения: пользователь просит ассистента "найди/забронируй/сделай", минуя ваш UI. PM должен создавать агент-дружелюбную поверхность продукта: API, tool calls, политики авторизации, проверяемые артефакты выполнения, понятные ограничения и статусы. Это новая форма "дистрибуции": не SEO, а "agent-to-app interop". Часть PM-работы превращается в "product for agents" (как когда-то "mobile-first", но жёстче).

**First Principles:**
- Аксиома: стоимость координации и выполнения падает; агенты учатся действовать
- Цепочка: "UI-привычка" теряет силу -> нужно продавать себя агентам (через интерфейсы/правила) -> "product for agents" как новая парадигма
- Почему важно: продукт без agent-interop рискует потерять канал дистрибуции через AI-ассистентов

**Происхождение:** Deep Research
**Откуда взялся:** The Verge (дискуссия Chesky) — https://www.theverge.com/decoder-podcast-with-nilay-patel/677324/airbnb-ceo-brian-chesky-services-redesign-app-future-travel (2025)
**Почему автор мог не упомянуть:** Agent-interop — пока нишевая тема; массовый канал ещё формируется
**Связь с авторскими тезисами:** Дополняет A4 (полный цикл) и A3 (оркестрация)
**Глубина:** Средний
**Актуальность:** Актуальный 2025+
**Спорный?** Да — в B2B и regulated-индустриях агент-дезинтермедиация может идти медленнее

---

### Тезис Н7: Security & Responsible AI — это продуктовый риск, который нельзя делегировать инженерам

**Суть:**
При vibe-coding скорость генерации кода растёт, но безопасность не растёт. Veracode: устойчивые провалы по security (~45% случаев). PM обязан включить в продуктовые артефакты security-ограничения, eval-наборы на уязвимости, гайды безопасного использования, и чёткую систему "кто отвечает за последствия". PM становится совладельцем security-качества (как качества UX), иначе скорость оборачивается регрессом бизнеса. Академическое исследование "Responsible GenAI Use by Product Managers" (2025) прямо позиционирует PM как gatekeepers ответственности.

**First Principles:**
- Аксиома: генерация кода дешёвая; цена инцидента высокая
- Цепочка: "ship быстрее" = растёт attack surface -> безопасность должна быть встроена в definition of done -> PM = совладелец security-качества
- Почему важно: один security-инцидент может стоить больше, чем все "ускорения" от vibe coding

**Происхождение:** Deep Research
**Откуда взялся:** Veracode — https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/ (2025); "Responsible GenAI Use by Product Managers" — https://arxiv.org/abs/2501.16531 (2025)
**Почему автор мог не упомянуть:** Security традиционно воспринимается как инженерная зона ответственности
**Связь с авторскими тезисами:** Спорит с A2 (если full-stack = "ship без ревью") и расширяет A3
**Глубина:** Глубокий
**Актуальность:** Актуальный 2025+
**Спорный?** Частично — многие компании пытаются "засунуть" это в AppSec, но данные упираются в продуктовые решения

---

### Тезис Н8: Tech-debt compounding — AI ускоряет не только выпуск, но и накопление долга

**Суть:**
AI-ускорение переносит работу из "написать" в "свести/встроить/починить", а качество кода деградирует: GitClear — падение рефакторинга и рост дублирования; CodeRabbit — рост issues/логических ошибок. Скорость релизов без debt-управления создаёт "скоростную хрупкость": каждый следующий релиз дороже и рискованнее. PM-механика должна включать debt-OKR, capacity на рефакторинг, метрики maintainability. Компания может стать "быстрой" локально и "медленной" глобально (системно).

**First Principles:**
- Аксиома: написание нового кода стало дешевле, чем понимание старого
- Цепочка: легко добавлять -> растёт объём легаси -> ревью/интеграция дорожают -> "быстрая" локально = "медленная" глобально
- Почему важно: PM, который не управляет техдолгом, создаёт "скоростную хрупкость" — каждый релиз дороже предыдущего

**Происхождение:** Deep Research
**Откуда взялся:** GitClear — https://www.gitclear.com/recent_ai_developer_productivity_code_quality_research (2025); CodeRabbit — https://www.helpnetsecurity.com/2025/12/23/coderabbit-ai-assisted-pull-requests-report/ (2025)
**Почему автор мог не упомянуть:** Фокус на "builder" narrativ-е; техдолг — "скучная" тема
**Связь с авторскими тезисами:** Дополняет A2 и A3
**Глубина:** Глубокий
**Актуальность:** Актуальный 2025+
**Спорный?** Нет (скорее неудобный)

---

### Тезис Н9: K-shape — это не только рынок труда, но и продуктовая задача: multi-tier user journeys

**Суть:**
AI-диффузия неоднородна (страны, возраст, роли, уверенность). Продукт должен иметь multi-tier сценарии: human-first (без AI), AI-assisted (подсказки), AI-supervised automation (агент с подтверждением), AI-autonomous (полная автономность) — и понятные переключатели ответственности. "Progressive autonomy" как продуктовая стратегия удержания. Способность пользоваться AI неравномерна — единый UX ломает часть аудитории — нужен градиент автономности + обучение.

**First Principles:**
- Аксиома: способность пользоваться AI неравномерна
- Цепочка: единый UX ломает часть аудитории -> нужен градиент автономности + обучение -> "progressive autonomy" = стратегия удержания
- Почему важно: продукт с единым AI-UX потеряет пользователей на обоих полюсах — и "слишком просто" и "слишком страшно"

**Происхождение:** Deep Research
**Откуда взялся:** Daniotti et al. — https://arxiv.org/abs/2506.08945 (2025); EY — https://www.ey.com/en_us/insights/consumer-products/how-workers-in-consumer-products-feel-about-agentic-ai (2026)
**Почему автор мог не упомянуть:** Фокус на роли PM, а не на UX-паттернах AI-продуктов
**Связь с авторскими тезисами:** Расширяет A6 (K-shaped бифуркация)
**Глубина:** Средний
**Актуальность:** Актуальный 2025+
**Спорный?** Да — увеличивает сложность продукта и QA, но снижает риск отторжения

---

### Тезис Н10: Pricing & value capture в AI-эру — PM обязан считать ценность на задачу, а не за сиденье

**Суть:**
AI-фичи меняют pricing: (a) cost structure переменный, (b) value измеряется "сэкономленным трудом" / "снижением риска", (c) buyer покупает AI из бюджетных причин или избегает из-за комплаенса. PM должен связывать unit economics (стоимость запроса/задачи) с outcome-экономикой клиента. Иначе "крутой демо-AI" съедает маржу или не проходит procurement. Seat-pricing ломается; pricing должен привязываться к outcome/usage caps/tiers. PM становится со-владельцем монетизации и финмодели раньше, чем это было "нормой".

**First Principles:**
- Аксиома: код дешевеет, но inference/контекст/агенты имеют running cost
- Цепочка: seat-pricing ломается -> pricing привязывается к outcome/usage -> PM = со-владелец монетизации
- Почему важно: PM без понимания unit economics AI-фич не может принимать roadmap-решения

**Происхождение:** Deep Research
**Откуда взялся:** Lenny Distilled (Madhavan Ramanujam) — https://www.lennydistilled.com/episodes/pricing-your-ai-product-lessons-from-400-companies-and-50-unicorns/ (2025); April Dunford — https://businessofsoftware.org/2025/06/positioning-in-the-age-of-ai-what-founders-need-to-know/ (2025)
**Почему автор мог не упомянуть:** Pricing традиционно вне скоупа PM; AI тянет его обратно
**Связь с авторскими тезисами:** Расширяет A4 и A5
**Глубина:** Средний
**Актуальность:** Актуальный 2025+
**Спорный?** Да — многие PM-организации держат pricing вне PM; но AI тянет его обратно в продукт

---

## Ключевые дебаты (где эксперты не согласны)

### Дебат 1: "Агенты уже готовы заменять людей" vs "Это пока не работает как обещают"
- **ЗА:** a16z — copilot -> agent, часть ролей будет полностью автоматизирована — https://a16z.com/ai-copilot-ai-agent-white-collar-roles/
- **ПРОТИВ:** TechCrunch (со ссылкой на a16z-VCs) — термин "agent" размытый; "замена" требует почти AGI — https://techcrunch.com/2025/05/12/even-a16z-vcs-say-no-one-really-knows-what-an-ai-agent-is/
- **Следствие для PM:** Строить roadmap с "градиентом автономности", а не с бинарным "всё автоматизируем".

### Дебат 2: "Vibe coding = прорыв продуктивности" vs "Иллюзия продуктивности и рост рисков"
- **ЗА:** Karpathy — vibe coding как способ прототипирования — https://x.com/karpathy/status/1886192184808149383
- **ПРОТИВ:** METR RCT — опытные разработчики на 19% медленнее с AI-тулом — https://techcrunch.com/2025/07/11/ai-coding-tools-may-not-speed-up-every-developer-study-shows/
- **Следствие для PM:** Нужны метрики и eval-контуры, иначе решения о процессе на ощущениях.

### Дебат 3: "AI-код качественнее" vs "AI-код небезопаснее и хуже поддерживается"
- **ЗА:** GitHub (Copilot study) — claims про улучшение quality/maintainability — https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/
- **ПРОТИВ:** Veracode + GitClear + CodeRabbit — рост уязвимостей/дублирования/issue-нагрузки — https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/ / https://www.gitclear.com/recent_ai_developer_productivity_code_quality_research / https://www.helpnetsecurity.com/2025/12/23/coderabbit-ai-assisted-pull-requests-report/
- **Следствие для PM:** "Скорость" без governance = риск.

### Дебат 4: "PM роль исчезает/сужается" vs "PM становится ключевее, но другой"
- **ЗА (сужается):** Chesky — меньше классических PM; рефрейм в product marketing + program mgmt — https://www.theverge.com/decoder-podcast-with-nilay-patel/677324/airbnb-ceo-brian-chesky-services-redesign-app-future-travel
- **ЗА (ключевее):** Cagan — PM-театр исчезает, но роль outcome-PM становится критичнее — https://www.svpg.com/product-coaching-and-ai/
- **Следствие для PM:** Спор не "нужны ли PM", а "какие PM".

### Дебат 5: "Junior-рынок схлопнется" vs "Джуны нужны, просто новые"
- **ЗА (схлопнется):** LeadDev — 54% ждут долгосрочное снижение junior-найма — https://leaddev.com/hiring/what-happens-when-learn-code-fails-generation
- **ЗА (нужны новые):** Business Insider — компании наращивают entry-level hiring в 2026 — https://www.businessinsider.com/companies-boosting-hiring-entry-level-engineers-2026-2
- **Следствие для PM:** PM-лидам нужно сознательно выбирать talent-стратегию, а не "плыть по рынку".

---

## Примеры и кейсы (из оригинала)

1. **Boris Cherny / Anthropic** — 100% AI-code since Nov 2025, +200% productivity, "coding is largely solved"
2. **Marc Andreessen / a16z** — "Mexican standoff" PM/eng/design, "superpowered individual", "don't be fungible"
3. **LinkedIn APB Program** — Associate Product Builder (Dec 2025)
4. **Airbnb AI** — Brian Chesky: "best thing ever happened" (Feb 2026)
5. **METR Study** — 19% slower despite 20% perceived speedup (July 2025)
6. **Perspective AI** — 67% PM report anxiety (June 2025)
7. **Spotify** — best developers haven't written code since December (2026)

---

## Все ссылки и источники

### Из Knowledge Base (AURA/AJTBD)

1. `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/AJTBD/fundamentals.md`
2. `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/AJTBD/value-creation.md`
3. `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/AURA/overview.md`
4. `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/RAT/risk-assumption-test.md`
5. `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/AJTBD/main-idea.md`
6. `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/AURA/product-strategy.md`
7. `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/AJTBD/psychology.md`
8. `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/ABCDX/abcdx-segmentation.md`
9. `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/Algorithms/main-algorithm.md`
10. `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/AURA/local-vs-global-optimum.md`
11. `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/AJTBD/critical-chain.md`
12. `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/AJTBD/graph-of-jobs.md`
13. `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/AJTBD/communication.md`
14. `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/UnitEconomics/growth-points.md`
15. `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/Algorithms/create-value.md`
16. `/Users/zamesinivan/Documents/Cursor/1-Zamesin/2-AURA-Theses/Knowledge/AJTBD/segmentation.md`

### Эксперты Tier 1

1. Marty Cagan — https://www.svpg.com/product-coaching-and-ai/ (SVPG; 2026)
2. Marty Cagan & Marily Nika — https://www.svpg.com/ai-product-management/ (SVPG; 2024)
3. Teresa Torres — https://www.producttalk.org/ai-prototyping-lovable/ (Product Talk; 2025)
4. Aparna Chennapragada — https://www.linkedin.com/posts/aparnacd_ive-been-saying-for-a-while-on-lenny-rachitskys-activity-7367028030768123904-Cq9r (Microsoft; 2025)
5. Brian Chesky — https://www.theverge.com/decoder-podcast-with-nilay-patel/677324/airbnb-ceo-brian-chesky-services-redesign-app-future-travel (Airbnb; 2025)
6. Des Traynor — https://destraynor.com/speaking/ (Intercom; 2025)
7. Andrej Karpathy — https://x.com/karpathy/status/1886192184808149383 (2025)
8. Lenny Rachitsky — https://www.lennysnewsletter.com/p/how-ai-will-impact-product-management (2024)
9. April Dunford — https://businessofsoftware.org/2025/06/positioning-in-the-age-of-ai-what-founders-need-to-know/ (2025)
10. Ravi Mehta — https://www.atlassian.com/blog/artificial-intelligence/shift-from-craft-to-judgement-ai (2025)

### Эксперты Tier 2

11. a16z — https://a16z.com/ai-copilot-ai-agent-white-collar-roles/ (2024)
12. Reforge — https://www.reforge.com/blog/ai-evals-course (2026)
13. Mind the Product (Artem Chigrinets) — https://www.mindtheproduct.com/the-2026-ai-product-strategy-huide-how-to-plan-budget-and-build-without-buying-into-the-hype/ (2026)
14. Mind the Product (Louron Pratt) — https://www.mindtheproduct.com/product-thinking-driving-fastest-growing-jobs/ (2026)
15. MIT Sloan Management Review — https://sloanreview.mit.edu/article/why-mindful-leaders-are-better-at-managing-change/ (2025)
16. Infosys + MIT Technology Review Insights — https://www.infosys.com/newsroom/press-releases/2025/psychological-safety-driving-ai-initiatives.html (2025)
17. Veracode — https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/ (2025)
18. Veracode (blog) — https://www.veracode.com/blog/genai-code-security-report/ (2025)
19. Daniotti et al. — https://arxiv.org/abs/2506.08945 (2025)
20. WORKBank (Brynjolfsson, Yang et al.) — https://arxiv.org/abs/2506.06576 (2025)
21. Responsible GenAI Use by Product Managers — https://arxiv.org/abs/2501.16531 (2025)
22. METR study (TechCrunch) — https://techcrunch.com/2025/07/11/ai-coding-tools-may-not-speed-up-every-developer-study-shows/ (2025)
23. GitClear — https://www.gitclear.com/recent_ai_developer_productivity_code_quality_research (2025)
24. CodeRabbit (HelpNetSecurity) — https://www.helpnetsecurity.com/2025/12/23/coderabbit-ai-assisted-pull-requests-report/ (2025)
25. YC W25 AI-код (TechCrunch) — https://techcrunch.com/2025/03/06/a-quarter-of-startups-in-ycs-current-cohort-have-codebases-that-are-almost-entirely-ai-generated/ (2025)
26. Fortune (Chesky) — https://fortune.com/2026/02/17/airbnb-ceo-brian-chesky-says-ai-best-thing-ever-happened-company-warns-other-founders-get-onboard-or-else/ (2026)
27. LA Times (Chesky) — https://www.latimes.com/business/story/2025-10-21/chesky-says-openai-tools-not-ready-for-chatgpt-tie-up-with-airbnb-app (2025)
28. LeadDev — https://leaddev.com/hiring/what-happens-when-learn-code-fails-generation (2025)
29. Rep. Foushee (layoffs report) — https://foushee.house.gov/media/press-releases/amid-historic-layoffs-surge-rep-foushee-releases-report-on-ais-impact-on-american-jobs-and-demands-clarity-from-industry-leaders (2025)
30. EY Agentic AI Workplace Survey — https://www.ey.com/en_us/insights/consumer-products/how-workers-in-consumer-products-feel-about-agentic-ai (2026)
31. Lenny Distilled (Madhavan Ramanujam) — https://www.lennydistilled.com/episodes/pricing-your-ai-product-lessons-from-400-companies-and-50-unicorns/ (2025)
32. GitHub Copilot study — https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/ (2025)

### Twitter/X

7. Andrej Karpathy — https://x.com/karpathy/status/1886192184808149383 (2025; vibe coding)

### Tier 3

33. Business Insider (Meta "AI builders") — https://www.businessinsider.com/meta-pms-ai-builders-tech-industry-2026-2 (2026)
34. Business Insider (Anthropic: junior value "dubious") — https://www.businessinsider.com/anthropic-ai-value-of-junior-roles-dubious-senior-talent2026-2 (2026)
35. Business Insider (entry-level hiring up) — https://www.businessinsider.com/companies-boosting-hiring-entry-level-engineers-2026-2 (2026)
36. SnapLogic survey (TechRadar) — https://www.techradar.com/pro/many-managers-say-they-trust-ai-agents-more-than-junior-workers (2025)
37. Investopedia (Workday report) — https://www.investopedia.com/are-ai-bosses-the-future-11795779 (2025)
38. Dayforce study (Business Insider) — https://www.businessinsider.com/executives-adopting-ai-higher-rates-than-workers-research-2025-10 (2025)
39. Business Insider (Lemkin) — https://www.businessinsider.com/godfather-of-saas-jason-lemkin-replace-humans-ai-agents-sales-2026-1 (2026)
40. Kelly briefing — https://www.kellyservices.us/news-and-insights/need-to-know-briefing-february-2-2026 (2026)
41. General Assembly survey — https://generalassemb.ly/blog/ai-and-product-management-survey/ (2025)
42. "Vibe coding" (Guardian) — https://www.theguardian.com/technology/2025/nov/06/vibe-coding-collins-dictionary-word-of-the-year-2025 (2025)
43. a16z-VCs "no one knows what an agent is" (TechCrunch) — https://techcrunch.com/2025/05/12/even-a16z-vcs-say-no-one-really-knows-what-an-ai-agent-is/ (2025)

---

## TODO автора
- [ ] Раскрыть тему ИНАЧЕ, чем в статье для Startup Growth Guide
- [ ] Обеспечить оригинальность текста (MtP проверит на плагиат)

---

## Рекомендации по усилению главы

**Для корпоративных продактов:** Использовать RAT-формулу как центральный фреймворк (Приоритет = Вероятность x Последствия / Стоимость проверки). Показать, что AI обрушивает знаменатель, и если PM не умеет оценивать числитель (judgment) — он генерирует бесполезные проверки. Привычка = физическое изменение мозга; 3x переоценка готовности. Four Forces как self-assessment tool. Рассинхронизация функций (AURA-Desync) как диагностика текущих проблем.

**Для product-leads:** "Kill a Job" + "Level Up" как AURA-объяснение трансформации. Аналогия cPanel vs Tilda: PM на уровне Core Job = cPanel; PM на Big Job = Tilda. Local vs Global Optimum: AI отлично справляется с local — PM, который работает только на local, вымывается. Главный алгоритм AURA как blueprint для hypothesis pipeline + AI-агенты. Evals-first PM (N1) как новый продуктовый навык.

**Для фаундеров:** "Мы покупаем знания, не запускаем продукты" (RAT paradigm). Critical Chain: скорость = самое медленное звено; AI ускоряет код, но security/DevOps/compliance — bottleneck. 7 рисков при 40% = 3% шанс — каждый компонент множит провал. Pricing (N10): seat -> outcome меняет бизнес-модель.

**Для VC:** ABCDX-сегментация PM-рынка: A/B растут, C/D вымываются. K-shaped через дилемму инноватора: компании, которые "хорошо работают" — наиболее уязвимы. Apprenticeship debt (N4) как talent risk при оценке портфельных компаний. Мультипликативная модель рисков для оценки стартапов.

---

## Рекомендованный порядок тезисов (нарратив)

1. **Сдвиг базы:** execution стал дешёвым -> **A2** (PM становится builder)
2. **Новый bottleneck:** качество решений и ambiguity -> **A1** (judgment + safety)
3. **Операционная модель AI-продуктов:** **A3 + Н1** (prompt sets + evals/наблюдаемость)
4. **Производственная дисциплина:** **Н7 + Н8** (security + tech debt)
5. **Экономика и масштаб:** **Н2 + Н10** (unit economics, kill criteria, pricing)
6. **Стратегия/дистрибуция в мире агентов:** **Н6 + Н3 + Н5** (agent UX + контекст как moat + PM<->PMM)
7. **Рынок труда и орг-последствия:** **A5 + A6 + Н4** (рост спроса, K-shape, apprenticeship debt)

---

## Исходный поток мыслей

### ТЕЗИС А1: Business Judgment и стратегическое влияние — через psychological safety (merged: А1+А3 из v2)

**Тип:** Утверждение (комплексный, объединённый)
**Суть (развёрнуто):**
Абсолютно критичный навык в эпоху нейронок — business judgment: способность принимать правильные бизнес-решения в условиях неопределённости. Когда AI автоматизирует исполнение, ключевым дифференциатором становится не скорость делания, а качество решений: какие гипотезы проверять, какие рынки выбирать, какие trade-offs делать, как обеспечить прибыль компании. Knowledge Base даёт judgment точное определение через AHEA: способность диагностировать ГДЕ в каузальной цепочке (Рынок - Сегменты - Jobs - Ценность - Коммуникация - Юнит-экономика - Прибыль) проблема, и сделать ПРАВИЛЬНЫЙ стратегический выбор.

PM-ы будут вынуждены подняться на уровень выше по влиянию на бизнес. Execution-level PM-работа (PRD, user stories, эксперименты) автоматизируется — PM должен подняться до strategy-level. KB даёт математическое доказательство через формулу RAT: когда AI обрушивает стоимость тестирования (знаменатель), доминирует числитель — идентификация рисков и оценка последствий. PM-ы, которые "двигают таски в Task Tracker" — их ТОЧНО заменят. a16z подтверждает: модели генерируют "bland, derivative" идеи — инструменты для ДЕЛАНИЯ есть, для ДУМАНИЯ — нет. Marc Andreessen через Larry Summers: "Don't be fungible" — не будь заменяемым.

Но этот подъём — болезненный процесс. 67% PM сообщают о тревоге по поводу своей роли (Perspective AI). КРИТИЧЕСКИ ВАЖНЫЙ REFRAME: То, что выглядит как "ego resistance" — на самом деле rational response на ambiguity. HBR: "Hesitation grounded in ambiguity, not ego." Когда мир турбулентный, лучшее что вы можете сделать — создать безопасную среду для себя и коллег, чтобы люди могли меняться. Boris Cherny: "You have to give people psychological safety that it's okay to fail."

PM-ы, которые разбираются в бизнесе + используют AI для быстрой реализации — получают огромное карьерное преимущество. Top performers adopt AI fastest.

**Ключевые цитаты из оригинала:**
- "Приоритет риска = (Вероятность x Последствия) / Стоимость проверки. AI обрушивает знаменатель -> числитель (человеческий judgment) доминирует."
- "Don't be fungible" (Andreessen через Larry Summers)
- "Hesitation grounded in ambiguity, not ego" (HBR)
- "You have to give people psychological safety that it's okay to fail" (Boris Cherny)
- 67% PM report anxiety (Perspective AI)

---

### ТЕЗИС А2: PM-ы становятся full-stack builders (enriched: Boris Cherny + Marc Andreessen)

**Тип:** Утверждение с кейсами
**Суть (развёрнуто):**
Все PM будут становиться full-stack builder-ами. Точка перелома: ноябрь-декабрь 2025. Boris Cherny (Head of Claude Code): с ноября 2025 100% его кода пишется Claude Code, ни одной строки вручную. Productivity per engineer +200%. 4% всех GitHub коммитов от Claude Code. "Coding is largely solved." "К концу года everyone's going to be a product manager and everyone codes. Титул software engineer заменит builder."

Marc Andreessen: "Mexican standoff" между PM, инженерами и дизайнерами — каждый верит, что может делать работу двух других с AI, и они все правы. T-shaped -> E/F-shaped навыки. "The superpowered individual" — глубок в одном + AI помогает быть хорошим в двух других. LinkedIn формализовал: "Associate Product Builder" как карьерная лестница.

**Ключевые цитаты:**
- "100% of my code is written by Claude Code. Not edited a single line by hand since November." (Boris Cherny)
- "Mexican standoff between PM, eng, design. They're all kind of correct." (Andreessen)
- "The additive effect of being good at two things is more than double." (Andreessen)
- LinkedIn: "Associate Product Builder" — формальный титул (Dec 2025)

**Контраргументы (из файла):**
1. Качество кода: 62% AI-кода содержит security flaws; 1.7x больше major issues
2. Opportunity cost: час на vibe coding = час НЕ на стратегию
3. Boris Cherny сам: "I do look at the code. Not at the point where you can be totally hands-off."
4. METR study: разработчики на 19% МЕДЛЕННЕЕ с AI, хотя ДУМАЮТ что на 20% быстрее

---

### ТЕЗИС А3: PM как оператор конвейера гипотез, оркестратор агентов и маленьких команд (merged: А4+А8 из v2)

**Тип:** Утверждение (комплексный)
**Суть (развёрнуто):**
PM станут управлять конвейером проверки гипотез И оркестрировать флоты AI-агентов в маленьких командах. AI позволяет в единицу времени проверять на порядок больше гипотез — индустриальный конвейер, не 2-3 гипотезы в спринт. "PM как оператор фабрики." KB: "90% ресурсов инвестируются в мертворожденные фичи" — если можно тестировать 10 идей за время одной, throughput растёт 10x.

Команды становятся меньше. Shreyas Doshi: "3-4 person startups = impact of 30-50." Andreessen: "the most leading edge founders are thinking — can you have entire companies where the founder does everything." Cherny: "Underfund things a little bit — people use Claude and ship quickly. One engineer on a project."

PM сдвигается от документации к curriculum design: PRD мертвы, PM пишет "prompt sets" — живые артефакты, одновременно спецификация и тренировочные данные. Агенты НЕ МОГУТ: стратегия, tradeoff prioritization, ethical judgment — это за PM.

**Ключевые цитаты:**
- "90% ресурсов инвестируются в мертворожденные фичи" (KB)
- "3-4 person startups with same impact as 30-50" (Shreyas Doshi)
- "Prompt sets = new PRDs" (Aparna Chennapragada)
- "Claude is starting to come up with ideas. Looking through feedback, bug reports, telemetry." (Boris Cherny)

**Контраргументы (из файла):**
- METR: 19% МЕДЛЕННЕЕ с AI. AI агенты завершают 2.5% проектов. Gartner: 40%+ agentic AI провалятся к 2027
- Faros AI: AI adoption = 9% рост багов, 154% рост размера PR. Один человек = single point of failure

---

### ТЕЗИС А4: Полный цикл до продакшена и продаж — через 12-24 месяца

**Тип:** Гипотеза (прогноз)
**Суть (развёрнуто):**
Через год-два появится полный цикл вплоть до тестов и продаж. Сейчас можно делать прототипы, но безопасность и deploy не позволяют катать эксперименты в существующем продукте. Бизнес будет ВЫНУЖДЕН перестроить процессы: от автоматического создания рекламных кампаний до запуска "цифровых продажников."

Boris Cherny: "We're starting to branch out of coding. I use co-work every day for things not related to coding — paying parking tickets, project management, syncing spreadsheets, messaging on Slack."

**Ключевые цитаты:**
- "AI is the best thing that ever happened to Airbnb. AI handles a third of customer service." (Brian Chesky)
- "76% product leaders увеличивают инвестиции в AI в 2026." (Mind the Product)
- "Branching out of coding into general tasks." (Boris Cherny)

**Контраргументы:**
- AI агенты завершают 2.5% проектов. Только 11% организаций имеют агентов в продакшене.

---

### ТЕЗИС А5: Спрос на Knowledge Workers растёт, а не падает

**Тип:** Утверждение
**Суть (развёрнуто):**
PM, разбирающиеся в JTBD, создании ценности, юнит-экономике + умеющие строить agent pipeline — будут супер востребованы. AI PMs зарабатывают на 35% больше. 75% работодателей не могут найти qualified AI-PM.

Marc Andreessen: "If we didn't have AI, we'd be in a panic about the economy. 50 years of slow technological change + declining population. The timing has worked out miraculously well. Remaining human workers at a premium, not a discount." + "Task loss, not job loss. The job persists longer than the individual tasks."

**Ключевые цитаты:**
- "Remaining human workers at a premium. Task loss, not job loss." (Andreessen)
- AI PMs +35% зарплата. 75% работодателей не находят AI-PM (Agents Today)

**Контраргументы (ОЧЕНЬ СИЛЬНЫЕ):**
- 54,000+ AI-сокращений в US 2025. 40%+ затронули software engineers. 54% eng leaders нанимают МЕНЬШЕ джуниоров. Спрос растёт только для элиты (top 10-20%).

---

### ТЕЗИС А6: Расслоение и K-shaped бифуркация — через psychological safety

**Тип:** Утверждение + framework
**Суть (развёрнуто):**
PM-рынок раскалывается в форме K: surging demand на полюсах (AI-специалисты +35% и AI-усиленные senior generalists) при вымывании mid-level ролей. AI-savvy джуниоры outperform senior-ов, создавая "performance inversion".

KB через Four Forces: что тянет к новому (ценность AI), что толкает от старого (frustration), что удерживает (страхи), что держит у старого (привычка — физическое изменение мозга). Люди в 3 раза переоценивают способность сменить привычку.

REFRAME: Не "адаптируйся или умри", а "создай безопасную среду". Это не только индивидуальный выбор — СТРУКТУРНОЕ неравенство. Microsoft: AI adoption gap Global North 24.7% vs Global South 14.1%. Совет: не "преодолей эго", а "найди/создай среду, которая поддерживает изменения."

**Ключевые цитаты:**
- "K-shaped bifurcation: middle hollows out." (Agents Today)
- "Hesitation grounded in ambiguity, not ego." (HBR)
- "Люди в среднем в 3 раза переоценивали свою способность сменить привычку." (KB)
- Microsoft AI adoption gap: Global North 24.7% vs Global South 14.1%
