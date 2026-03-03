# Index

Карта репозитория с описанием каждого файла. Обновляется автоматически при каждом пуше в main — для изменённых файлов описания генерируются через AI.

## Разделы

| Папка | Что внутри |
|-------|-----------|
| `.codex/` | — |
| `1-Context/` | Базы знаний: AJTBD-методология, интенсив BOOST, тренинг "Как делать продукт" |
| `2-Products/` | Продуктовые материалы и новые продукты |
| `3-Marketing/` | Маркетинг: вебинары, идеи продвижения |
| `4-Hiring/` | — |
| `4-Personal-files/` | Персональные рабочие папки участников команды |
| `5-ZIS/` | Zamesin Innovation School: LMS и идеи |
| `8-Prompts-and-Scripts/` | Промпты и скрипты для автоматизации |

---

## .codex/


### .codex/skills/


**new-article-draft/**

- `SKILL.md` — Скилл: New Article Draft (Double Diamond — СТРУКТУРИРОВАНИЕ)

*agents/*

- `openai.yaml`

*references/*

- `humanity-pass-checklist.md` — Humanity Pass Checklist
- `style-fingerprint-template.md` — Style Fingerprint Template

**new-article-thesis/**

- `SKILL.md` — Скилл: Создание тезисов главы (Double Diamond — РАСХОЖДЕНИЕ)

*agents/*

- `openai.yaml`

### .codex/temp/


**draft-ai-changes-pm-role-mtp/**

- `00-must-include.md` — 00 — MUST-INCLUDE checklist (raw extraction)
- `01-publication-signal-pack.md` — 01 — Publication signal pack (Mind the Product)
- `02-style-fingerprint.md` — 02 — Style fingerprint (Mind the Product)
- `03-case-pack.md` — 03 — Case pack (URLs + boundaries)
- `04-narrative-plan.md` — 04 — Narrative plan (Mind the Product)
- `05-section-briefs.md` — 05 — Section briefs (blueprint for draft)
- `06-draft-v1.md` — 📝 Author notes for iteration
- `07-quality-report.md` — 07 — Quality report (v1)
- `_spring-context.md` — Draft context: AI Changes the PM Role (Mind the Product)

**thesis-changes-how-we-make-products/**

- `_spring-context.md` — Spring Context — Thesis: Changes How We Make Products (MindTheProduct)

**thesis-how-to-find-product-market-fit-fast-and-pivot-the-right-way/**

- `01-raw-theses.md` — 01 — Raw Theses Extract (извлечённые тезисы без потерь)
- `02-first-principles.md` — 02 — First-Principles разбор (декомпозиция на факты, инварианты, допущения)
- `03-order-effects.md` — 03 — Последствия 2-го и 3-го порядка (карта эффектов)
- `03-thesis-bank.md` — 03 — Thesis Bank (30–60 кандидатных тезисов)
- `03-thesis-combinatorics.md` — 03 — Комбинаторика тезисов (гибриды через 5 операторов)
- `04-synthesis.md` — 04 — Synthesis (объединённые тезисы перед финальным файлом)
- `_spring-context.md` — Spring Context — Thesis: How to Find Product-Market Fit Fast — and Pivot the Right Way
- `agent-contrarian.md` — Agent Report — contrarian
- `agent-expert-hunter.md` — Agent Report — expert-hunter
- `agent-knowledge-researcher.md` — Agent Report — knowledge-researcher
- `agent-log.md` — Agent Log
- `agent-requests.md` — Agent Requests
- `coverage-round-1.md` — Coverage Round 1 — Quality Control

---

## 1-Context/

Базы знаний: AJTBD-методология, интенсив BOOST, тренинг "Как делать продукт"


### 1-Context/AURA-Theses/

Тезисы методологии AJTBD и мета-фреймворка AURA, структурированные по темам

- `TODO.md` — Список задач по доработке базы знаний
- `_index.md` — Оглавление базы знаний со ссылками на все файлы по категориям
- `_uncategorized.md` — Тезисы, не вошедшие в основные категории

**ABCDX/**

- `abcdx-segmentation.md` — ABCDX-сегментация: разделение клиентов на группы по маржинальности и удовлетворённости

**AJTBD/**

- `b2b.md` — B2B-специфика AJTBD: отличия от B2C в подходе к созданию продуктов
- `communication.md` — Коммуникация продукта: трансляция подтверждённой ценности подтверждённому сегменту
- `critical-chain.md` — Критическая цепочка работ: все работы ниже уровня, необходимые для выполнения работы выше
- `fundamentals.md` — Фундаментальные принципы AJTBD: человек действует для выполнения целей, формируемых мозгом для удовлетворения потребностей
- `graph-of-jobs.md` — Граф работ — вторая ключевая единица анализа AJTBD, влияющая на стратегию продукта
- `job-structure.md` — Структура описания работы: работа — это прогресс, которого человек хочет достичь в определённом контексте
- `job-types-and-properties.md` — Типы и свойства работ: цепочки шагов для достижения результата
- `main-idea.md` — Четыре силы прогресса — ключевой тезис JTBD, дополненный автором
- `psychology.md` — Психологические основы покупательского поведения и глубинные причины покупок
- `segmentation.md` — Сегментация клиентов по работам вместо демографии
- `value-creation.md` — Создание ценности: фича — не самоцель, разные люди используют одну фичу для разных работ

**AURA/**

- `local-vs-global-optimum.md` — Локальный vs глобальный оптимум: метафора холма для продуктовых решений
- `overview.md` — AURA: интегральный мета-фреймворк, объединяющий AJTBD, Unit Economics, RAT и ABCDX-сегментацию
- `product-strategy.md` — Продуктовая стратегия: все стратегические решения сводятся к выбору работ и сегментов

**Algorithms/**

- `create-acquisition-channel.md` — Алгоритм создания канала привлечения через выход на предыдущую работу
- `create-value.md` — Алгоритм создания ценности: от бизнес-задачи к работающему решению
- `decrease-churn.md` — Алгоритм снижения оттока: привычка как гравитационное притяжение к продукту
- `exit-competition.md` — Алгоритм выхода из прямой конкуренции через смену джобов в графе
- `grow-existing-product.md` — Алгоритм роста существующего продукта через ABCD-сегментацию
- `increase-average-check.md` — Алгоритм повышения среднего чека через работы внутри одного клиента
- `increase-conversion.md` — Алгоритм роста конверсии: устранение барьеров клиента
- `increase-retention.md` — Алгоритм повышения ретеншена через выполнение следующих работ в цепочке
- `launch-product.md` — Алгоритм запуска продукта, применимый и к новым фичам
- `main-algorithm.md` — Главный алгоритм: интегральный подход к принятию продуктовых решений
- `position-product.md` — Алгоритм позиционирования: трансляция ценности с учётом контекста и триггеров клиента
- `scale-product.md` — Алгоритм масштабирования: добавление новых сегментов

**HowTos/**

- `conduct-ajtbd-interviews.md` — Как проводить AJTBD-интервью: универсальные вопросы для изучения работ
- `conduct-b2b-interviews.md` — Как проводить B2B-интервью: специфика работы с ЛПР
- `conduct-expert-interviews.md` — Как проводить экспертные интервью с предпринимателями на целевом рынке
- `do-quantitative-research.md` — Как проводить количественное исследование для проверки гипотез о работах
- `do-switch-interviews.md` — Как проводить Switch-интервью: изучение контекста смены решений
- `find-segmentation-criteria.md` — Как найти критерии сегментации: последовательное применение критериев
- `formulate-jobs-correctly.md` — Как правильно формулировать работы: всё, что начинается с глагола — работа
- `load-activating-knowledge.md` — Как загружать активирующее знание: знание, которое привело к решению о работе
- `run-ux-tests.md` — Как проводить UX-тесты: быстрый и дешёвый поиск ошибок в медиа
- `validate-value.md` — Как валидировать ценность: лучший способ — живые продажи

**RAT/**

- `risk-assumption-test.md` — Risk Assumption Test: фреймворк приоритизации рискованных предположений в продукте

**Raw Source/**

- `ajtbd-key-theses.md` — Исходный документ с полным перечнем тезисов AJTBD и AURA
- `course-transcriptions.md` — Транскрипция воркшопа №1: ввод, правила и методология курса
- `lectures-transcription.md` — Транскрипции лекций
- `mechanics-and-strategies.md` — Каталог механик и стратегий создания ценности по бизнес-задачам

**UnitEconomics/**

- `growth-points.md` — Точки роста: если 1% доли рынка — вероятно, пропускаете привлекательные сегменты
- `unit-economics.md` — Unit Economics: юнит-экономика как фильтр для принятия решений

### 1-Context/Zoom-Transcripts/


**воркшоп/**


*2026-02-04 — СКУД - Проблемы, решения с Perco/*

- `расшифровка — СКУД - Проблемы, решения с Perco.md` — Расшифровка: СКУД: Проблемы, решения с Perco
- `саммари — СКУД - Проблемы, решения с Perco.md` — [Воркшоп] СКУД: Проблемы, решения с Perco
- `саммари_v2 — Разбор проблем СКУД с Perco.md` — [Воркшоп] Разбор проблем СКУД с Perco

**командный-созвон/**


*2026-02-07 — 3 встречи/*

- `расшифровка — Воркшоп 5 - Telegram-бот для картинок.md` — Расшифровка: Воркшоп 5: Telegram-бот для картинок
- `расшифровка — Встреча 2 - Автоматизация рекрутинга чат-ботами.md` — Расшифровка: Встреча 2: Автоматизация рекрутинга чат-ботами
- `расшифровка — Встреча 3 - Обсуждение результатов интенсива.md` — Расшифровка: Встреча 3: Обсуждение результатов интенсива
- `саммари — Воркшоп 5 - Telegram-бот для картинок.md` — [Воркшоп] Воркшоп 5: Telegram-бот для картинок
- `саммари — Встреча 2 - Автоматизация рекрутинга чат-ботами.md` — [Консультация] Встреча 2: Автоматизация рекрутинга чат-ботами
- `саммари — Встреча 3 - Обсуждение результатов интенсива.md` — [Созвон] Встреча 3: Обсуждение результатов интенсива
- `саммари_v2 — Telegram-бот для обработки изображений.md` — [Воркшоп] Telegram-бот для обработки изображений
- `саммари_v2 — Автоматизация рекрутинга чат-ботами.md` — [Командный-созвон] Автоматизация рекрутинга чат-ботами
- `саммари_v2 — Обсуждение результатов первого интенсива.md` — [Продуктовый-созвон] Обсуждение результатов первого интенсива

*2026-02-21 — 3 встречи/*

- `расшифровка — Встреча 2 - Подведение итогов интенсива.md` — Расшифровка: Встреча 2: Подведение итогов интенсива
- `расшифровка — Встреча 3 - Ретроспектива - успешный и гладкий поток.md` — Расшифровка: Встреча 3: Ретроспектива: успешный и гладкий поток
- `расшифровка — Скилы и агенты - отличия и применение.md` — Расшифровка: Скилы и агенты: отличия и применение
- `саммари — Встреча 2 - Подведение итогов интенсива.md` — [Воркшоп] Встреча 2: Подведение итогов интенсива
- `саммари — Встреча 3 - Ретроспектива - успешный и гладкий поток.md` — [Созвон] Встреча 3: Ретроспектива: успешный и гладкий поток
- `саммари — Скилы и агенты - отличия и применение.md` — [Воркшоп] Скилы и агенты: отличия и применение
- `саммари_v2 — Подведение итогов интенсива.md` — [Воркшоп] Подведение итогов интенсива
- `саммари_v2 — Ретроспектива успешного потока.md` — [Командный-созвон] Ретроспектива успешного потока
- `саммари_v2 — Скилы и агенты - сравнение и применение.md` — [Воркшоп] Скилы и агенты: сравнение и применение

*2026-03-03 — Статус задач и планы/*

- `расшифровка — Статус задач и планы.md` — Расшифровка: Статус задач и планы
- `саммари — Статус задач и планы.md` — [Командный-созвон] Статус задач и планы

**консультация/**


*2026-03-02 — Проработка требований к проекту ZIS/*

- `расшифровка — Проработка требований к проекту ZIS.md` — Расшифровка: Проработка требований к проекту ZIS
- `саммари — Проработка требований к проекту ZIS.md` — [Консультация] Проработка требований к проекту ZIS

**продуктовый-созвон/**


*2026-01-29 — Новая модель продаж - self-service/*

- `расшифровка — Новая модель продаж - self-service.md` — Расшифровка: Новая модель продаж: self-service
- `саммари — Новая модель продаж - self-service.md` — [Созвон] Новая модель продаж: self-service
- `саммари_v2 — От sales call к self-service.md` — [Продуктовый-созвон] От sales call к self-service

*2026-02-02 — Идея продукта в commodities trading, Встреча 2 - Aura - Стратегия глобального развития продукта/*

- `расшифровка — Встреча 2 - Aura - Стратегия глобального развития продукта.md` — Расшифровка: Встреча 2: Aura: Стратегия глобального развития продукта
- `расшифровка — Идея продукта в commodities trading.md` — Расшифровка: Идея продукта в commodities trading
- `саммари — Встреча 2 - Aura - Стратегия глобального развития продукта.md` — [Консультация] Встреча 2: Aura: Стратегия глобального развития продукта
- `саммари — Идея продукта в commodities trading.md` — [Консультация] Идея продукта в commodities trading
- `саммари_v2 — Aura - Стратегия развития, поиск роли.md` — [Интервью] Aura: Стратегия развития, поиск роли
- `саммари_v2 — Консультация по продукту в commodities trading.md` — [Консультация] Консультация по продукту в commodities trading

*2026-02-16 — Продающий воркшоп по веб-кодингу/*

- `расшифровка — Продающий воркшоп по веб-кодингу.md` — Расшифровка: Продающий воркшоп по веб-кодингу
- `саммари — Продающий воркшоп по веб-кодингу.md` — [Созвон] Продающий воркшоп по веб-кодингу
- `саммари_v2 — Разработка продающего воркшопа по веб-кодингу.md` — [Продуктовый-созвон] Разработка продающего воркшопа по веб-кодингу

*2026-02-20 — Видение продукта - ИИ-ассистент для действий/*

- `расшифровка — Видение продукта - ИИ-ассистент для действий.md` — Расшифровка: Видение продукта: ИИ-ассистент для действий
- `саммари — Видение продукта - ИИ-ассистент для действий.md` — [Созвон] Видение продукта: ИИ-ассистент для действий
- `саммари_v2 — Продуктовый ИИ-ассистент - Определение действий.md` — [Продуктовый-созвон] Продуктовый ИИ-ассистент: Определение действий

*2026-02-20 — Встреча 1 - Оценка агентов - экспертная арена, Встреча 1 - Команда агентов - оценка кандидатов/*

- `расшифровка — Встреча 1 - Команда агентов - оценка кандидатов.md` — Расшифровка: Встреча 1: Команда агентов: оценка кандидатов
- `расшифровка — Встреча 1 - Оценка агентов - экспертная арена.md` — Расшифровка: Встреча 1: Оценка агентов: экспертная арена
- `саммари — Встреча 1 - Команда агентов - оценка кандидатов.md` — [Созвон] Встреча 1: Команда агентов: оценка кандидатов
- `саммари_v2 — Модель оценки агентов - прикладные кейсы.md` — [Продуктовый-созвон] Модель оценки агентов: прикладные кейсы
- `саммари_v2 — Оценка кандидатов командой агентов.md` — [Продуктовый-созвон] Оценка кандидатов командой агентов

*2026-02-25 — Обсуждение формата воркшопа/*

- `расшифровка — Обсуждение формата воркшопа.md` — Расшифровка: Обсуждение формата воркшопа
- `саммари — Обсуждение формата воркшопа.md` — [Воркшоп] Обсуждение формата воркшопа
- `саммари_v2 — Обсуждение формата воркшопа.md` — [Продуктовый-созвон] Обсуждение формата воркшопа

*2026-02-27 — Встреча 2 - Обсуждение запуска агентов, Встреча 1 - Встреча-знакомство с новым коллегой/*

- `расшифровка — Встреча 1 - Встреча-знакомство с новым коллегой.md` — Расшифровка: Встреча 1: Встреча-знакомство с новым коллегой
- `расшифровка — Встреча 2 - Обсуждение запуска агентов.md` — Расшифровка: Встреча 2: Обсуждение запуска агентов
- `саммари — Встреча 1 - Встреча-знакомство с новым коллегой.md` — [Созвон] Встреча 1: Встреча-знакомство с новым коллегой
- `саммари — Встреча 2 - Обсуждение запуска агентов.md` — [Созвон] Встреча 2: Обсуждение запуска агентов
- `саммари_v2 — Запуск инновационных агентов.md` — [Продуктовый-созвон] Запуск инновационных агентов
- `саммари_v2 — Знакомство с новым коллегой Ладой.md` — [Командный-созвон] Знакомство с новым коллегой Ладой

### 1-Context/boost-knowledge-base/

База знаний об интенсиве BOOST — вайб-кодинг для создания продуктов с AI. Cohort-4, 20–28 марта 2026.

- `01-course-overview.md` — Обзор интенсива: формат (7 воркшопов за неделю), тарифы (29 900–79 900 ₽), автор, проекты 11 выпускников, юрлицо
- `02-target-audience-and-jobs.md` — 6 сегментов ЦА с сайта (фаундеры, владельцы бизнеса, менеджеры, мамы в декрете) + детальный AJTBD-анализ 9 сегментов
- `03-program.md` — Программа: 7 воркшопов от установки до демо, стек Next.js/Tailwind/PostgreSQL, 10 ключевых навыков
- `04-competitors.md` — Анализ 10 конкурентов (Product University, ZeroCoder, Eduson и др.) с ценами и позиционированием
- `05-landing-and-communication.md` — Тексты лендинга, блоки "для кого", барьеры и возражения, 10 отзывов участников, слоганы
- `06-faq.md` — FAQ: нужно ли программировать, тарифы, подготовка, подписка Claude Code Max ($100/мес), возврат денег

### 1-Context/producthowto-knowledge-base/

База знаний о тренинге "Как делать продукт" — курс по Advanced Jobs To Be Done, 12 000+ выпускников.

- `01-course-overview.md` — Обзор тренинга: формат, программа 8 модулей, тарифы, автор Ваня Замесин
- `02-target-audience-and-jobs.md` — Целевая аудитория: продакт-менеджеры, фаундеры, маркетологи и их задачи
- `03-ajtbd-methodology.md` — Методология AJTBD: теория, дающая алгоритмы создания продуктов на основе знания работ клиентов
- `04-book-chapters.md` — Главы книги, основанной на 80+ тренингах и 40+ кейсах
- `05-interview-guides.md` — Гайды интервью: Switch, AJTBD, B2B, экспертные
- `06-cases.md` — 19 кейсов выпускников с применением AJTBD
- `07-results-summary.md` — Сводка результатов: переход от демографической сегментации к сегментации по работам
- `08-reviews.md` — Отзывы: 12 000+ участников, средняя оценка 9.2/10
- `09-faq.md` — FAQ по тренингу

---

## 2-Products/

Продуктовые материалы и новые продукты


### 2-Products/BoostUS-Course/

- `01-prd.md` — PRD: From Zero to First Product — Записанный онлайн-курс
- `02-analytics-plan.md` — Аналитический план: From Zero to First Product — PostHog
- `03-landing-copy.md` — Лендинг-копи: From Zero to First Product
- `04-marketing-hypotheses.md` — Маркетинговые гипотезы: From Zero to First Product
- `05-unit-economics.md` — Юнит-экономика: From Zero to First Product

### 2-Products/BoostUS-ai-platform/

- `01-prd.md` — PRD: LaunchPilot -- AI-платформа "от идеи до работающего продукта"
- `02-analytics-plan.md` — Аналитический план LaunchPilot — PostHog
- `03-landing-copy.md` — LaunchPilot: Landing Page Copy
- `04-marketing-hypotheses.md` — Маркетинговые гипотезы и стратегия воронки: LaunchPilot
- `05-unit-economics.md` — Юнит-экономика: LaunchPilot
- `market-report-анализ-идеи-boostus-go.md` — Анализ идеи: BoostUS — GO

### 2-Products/BoostUS-main/

- `01-prd.md` — PRD: AI-гайд по продуктовому мышлению и вайбкодингу
- `02-analytics-plan.md` — Аналитический план LaunchPilot — PostHog
- `03-landing-copy.md` — LaunchPilot: Landing Page Copy
- `04-marketing-hypotheses.md` — Маркетинговые гипотезы и стратегия воронки: LaunchPilot
- `05-unit-economics.md` — Юнит-экономика: LaunchPilot

**landing/**

- `index.html`

---

## 3-Marketing/

Маркетинг: вебинары, идеи продвижения

- `ideas.md` — Маркетинговые идеи: публичный календарь вебинаров, страница офферов компании, ежемесячные лид-магниты, скилл для написания PRD

### 3-Marketing/1-SMM/

- `IDEAS.md`

**Drafts/**

- `future of Saas.md` — Будущее SaaS: почему спрос изменится
- `future-of-saas-2.md` — TODO
- `hackernoon-article-pmf-pivot-theses.md` — How to Find Product-Market Fit Fast — and Pivot the Right Way
- `love.md`
- `openclaw-and-agents.md`
- `techstory-saas-golden-age-ending-article-final.md` — Is the Golden Age of SaaS Ending?
- `why-four-forces-do-not-work.md`
- `Продажный пост 58 поток.md`

**Experts/**

- `boris_cherny_interview_transcript.txt`
- `marc_andreessen_transcript.txt`

**Linkedin-posts/**

- `2026-02-25-agent-optimization-distribution.md` — Agent Optimization — The Next Distribution Layer
- `2026-03-03-pm-judgment-ai-filter.md`
- `image-styles-library.md` — Image Styles Library for LinkedIn Posts
- `linkedin-post-2026-02-20-pm-hypothesis-factory.md` — LinkedIn Post: PM as Hypothesis Factory Operator
- `linkedin-post-2026-02-21-ceo-vibe-coding.md`

**Telegram-posts/**

- `2026-02-22-vibe-coding-love-work.md` — Telegram-пост: У меня безумная гипотеза про вайбкодинг

### 3-Marketing/1-Webinars/


**web-260626.md/**

- `deep-research-report.md` — Новые принципы создания продуктов из первых принципов в мире, где «построить софт ≈ почти бесплатно»
- `first-principles-15.md` — 15 новых принципов создания продуктов (from first principles)
- `ideas.md`
- `prompt-first-principles-analysis.md` — Промпт: Анализ новых принципов создания продуктов из первых принципов
- `web-260226.md` — TODO

**web-skills.md/**

- `web.md`

### 3-Marketing/2-PR-Articles/

- `web-theses.md` — Тезисы из вебинара: "Внедрение Jobs 3.0: кейс Дениса"
- `web.md` — Расшифровка: Внедрение Jobs 3.0: кейс Дениса

**1-Thoughts/**

- `changes-how-we-make-products.md` — Вводные
- `how-to-find-pmf-hackernoon.md` — Бриф от издания

**2-Theses/**

- `Theses-AI-Changes-PM-Role-MtP.md` — Инструкция для draft-этапа
- `Theses-How-to-Find-Product-Market-Fit-Fast-and-Pivot-the-Right-Way.md` — 📝 Инструкция для draft-этапа

**3-Drafts/**

- `Draft-AI-Changes-PM-Role-MtP.md` — Инструкция от Вани Замесина
- `Draft-How-to-Find-PMF-Fast-and-Pivot-the-Right-Way.md` — 📝 Инструкция от Вани Замесина

### 3-Marketing/2-Writing-Book/

- `bookconcept.md` — Концепт книги AURA Framework
- `ideas.md`
- `linkedin-sprint-detailed-theses.md` — LinkedIn Growth Sprint -- Детальные тезисы для скилла
- `skills.md`
- `zamesin_top50_full.md` — Топ 50 постов @zamesin (полные тексты)

**1-Raw-Thoughts/**

- `changes-how-we-make-products.md` — Вводные
- `chapter-name.md`
- `how-to-find-pmf-hackernoon.md` — Бриф от издания
- `what-for.md`

**2-Theses/**

- `Theses-AI-Changes-PM-Role-MtP.md` — Инструкция для draft-этапа
- `Theses-AI-Changes-PM-Role-condensed.md` — 📝 Инструкция для draft-этапа
- `Theses-AI-Changes-PM-Role.md` — 📝 Инструкция для draft-этапа
- `Theses-How-to-Find-PMF-Fast.md` — 📝 Инструкция для draft-этапа

**3-Drafts/**

- `Draft-AI-Changes-PM-Role-old.md` — 📝 Инструкция от Вани Замесина
- `Draft-From-PRDs-to-Pipelines-MtP.md` — 📝 Инструкция автора для итерации

---

## 4-Hiring/

- `hiring-requirements.md` — Каких людей мы нанимаем

---

## 4-Personal-files/

Персональные рабочие папки участников команды


### 4-Personal-files/Alina-Kovkova/


### 4-Personal-files/Anastasia-Veremyova/


### 4-Personal-files/Anika-Popova/


### 4-Personal-files/Ilya-Izmaylov/


### 4-Personal-files/Ilya-Mokhov/


### 4-Personal-files/Ivan-Zamesin/


**New-Name-US/**

- `Letter to Liam.md` — Letter to Liam
- `Updated Questionnaire.md` — Context for Liam

### 4-Personal-files/Maxim-Kurepov/


### 4-Personal-files/Nastya-Dyachenko/


### 4-Personal-files/Ruslan-Zhuravskiy/


### 4-Personal-files/Valeria-Panteleeva/


**Кураторы КПП/**

- `анализ_кураторов.md` — Анализ работы кураторов: комментарии о студентах

### 4-Personal-files/Vladimir-Glebovets/


### 4-Personal-files/Vladlena-Orlova/


---

## 5-ZIS/

Zamesin Innovation School: LMS и идеи


### 5-ZIS/LMS/

Learning Management System.

- `ideas.md` — Идея: экран "что тебе нужно сделать дальше" для LMS

### 5-ZIS/Requirements/

- `2026-03-03-summary-for-evgeny.md` — Саммари по проекту ЗИС для Евгения Васева

---

## 8-Prompts-and-Scripts/

Промпты и скрипты для автоматизации


### 8-Prompts-and-Scripts/Prompts/

- `generate-segment.md` — Промт: Выбор 5 привлекательных сегментов по AJTBD
- `landing-page-copy.md`
- `riskiest-assumption-test.md` — Что делать первым сообщением

### 8-Prompts-and-Scripts/codex-skills/


**new-article-thesis/**

- `SKILL.md` — New Article Thesis

*agents/*

- `openai.yaml`

---

## Корневые файлы

- `ideas-for-space.md` — Идеи по организации пространства: фреймворки через "what if" вопросы, документы по работе с каждым сотрудником
- `space-todo.md` — Задачи: обновить сегменты клиентов для Figma-курса, экспортировать формы входа/выхода
