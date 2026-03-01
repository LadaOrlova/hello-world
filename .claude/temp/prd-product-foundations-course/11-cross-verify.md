# Cross-Verification Report: From Zero to First Product

Дата: 2026-03-01
Роль: Скептик и аудитор продуктовых решений

---

## Проверка 1: PRD <-> Аналитика

### 1.1. Покрытие Core Jobs событиями аналитики

**Non-Technical Founders:**
- "Понять что строить и в каком порядке" — покрывается через `exercise_completed` (describe_product_jobs), `prompt_copied`, `prompt_result_saved`. OK.
- "Научиться думать системно" — косвенно: `video_watched`, `module_completed`. Нет прямого измерения "стал думать системно". Слабое покрытие.
- "Уметь формулировать ЧТО строить AI-кодеру" — НЕТ СОБЫТИЯ. Нет трекинга того, использовал ли студент результаты курса для постановки задачи AI-кодеру или разработчику. Это ключевой core job, и его выполнение не измеряется.

**Solopreneurs:**
- "Быстро понять стоит ли идея времени" — покрывается `prompt_copied` (idea_validator), `aha_moment_reached`. OK.
- "Получить компактный framework" — косвенно через `module_completed`. Нет прямого измерения. Приемлемо.
- "Понять как ставить задачу AI-кодеру" — аналогично Founders: НЕТ СОБЫТИЯ.

**AI-Era Career Builders:**
- "Освоить AI для продуктов" — покрывается через `prompt_copied`, `skill_downloaded`. OK.
- "Иметь framework для product thinking" — косвенно. Нет прямого измерения.
- "Иметь кейс в портфолио" — НЕТ СОБЫТИЯ. Критерий успеха из PRD ("имеет кейс в портфолио") не трекается. Нет события "portfolio_case_created" или "project_exported".

**AI Skills Seekers:**
- "Получить практические навыки с AI" — покрывается через `prompt_copied`, `skill_downloaded`. OK.
- "Структурированный путь обучения" — `progress_milestone_reached`, `module_completed`. OK.

### 1.2. Aha-момент: PRD vs Аналитика

**ПРОТИВОРЕЧИЕ ОБНАРУЖЕНО.**

PRD описывает **РАЗНЫЕ Aha-моменты для каждого сегмента** (секция "Aha-момент для каждого сегмента"):
- Non-Technical Founders: "У меня есть PRD + лендинг + понимание клиента — за 2 часа!"
- Solopreneurs: "За 30 минут понял, жизнеспособна ли идея"
- AI-Era Career Builders: "Могу системно проанализировать любой продукт"
- AI Skills Seekers: "Создал работающий лендинг/прототип одним промптом"

Аналитика определяет **ЕДИНЫЙ Aha-момент для всех сегментов**: `aha_moment_reached` = exercise_completed (describe_product_jobs) + prompt_result_saved (idea_validator) + >30 сек на результате.

Это серьёзный разрыв: аналитический план унифицирует Aha-момент, хотя PRD чётко говорит, что для разных сегментов он разный. В частности, Aha для AI Skills Seekers ("создал работающий лендинг/прототип") наступает в Module 5, а не в Module 1. Аналитика это не отловит.

### 1.3. Метрики успеха из PRD vs Аналитический план

PRD определяет метрики по сегментам:
- "% студентов, запустивших landing page" — НЕТ СОБЫТИЯ `landing_page_launched` или аналогичного. Skill downloaded трекается, но факт создания лендинга — нет.
- "% студентов, проведших RAT" — покрывается через `prompt_copied` (idea_validator). OK, но RAT-чеклист и AI-промпт — разные вещи; PRD упоминает RAT как отдельное упражнение в Module 1 (FR-1.5), но в аналитике нет события для прохождения RAT-чеклиста отдельно от промпта.
- "% использовавших 3+ промпта" / "5+ промптов" — покрывается через user property `prompts_copied` (increment). OK.

PRD North Star Metric: "Количество студентов, которые завершили Module 1 + выполнили минимум 1 практическое задание" — аналитика покрывает через `module_completed` (1) + `exercise_completed`. OK.

### 1.4. Воронка в аналитике vs путь пользователя из PRD

PRD описывает путь: Лендинг -> Регистрация -> Module 1 (Урок 1: Ценность -> Урок 2: Jobs -> Упражнение -> AI-промпт -> Урок 3: RAT -> CTA).

Аналитика описывает воронку: page_viewed -> cta_clicked -> signup_started -> signup_completed -> module_started -> video_watched -> exercise_completed -> prompt_copied -> aha_moment_reached -> module_completed -> paywall_shown -> purchase_initiated -> purchase_completed.

**РАЗРЫВ:** В PRD есть шаг "Урок 3: RAT" ПОСЛЕ AI-промпта, но в аналитической воронке Aha-момент наступает при prompt_result_saved, а video_watched (1.3 — RAT) не является частью Aha-условия. Если студент пропускает урок о RAT, но делает упражнение и промпт — Aha засчитывается. Это может искажать данные.

**РАЗРЫВ:** В воронке аналитики отсутствует событие `onboarding_question_answered` как обязательный шаг. При этом в плане событий оно есть, и от него зависит присвоение сегмента. Если пользователь пропустит онбординг-вопрос, все сегментные метрики будут пустыми.

---

## Проверка 2: Сегменты <-> Лендинг

### 2.1. Представленность сегментов в блоке "Узнаёшь себя?"

Лендинг содержит Блок 6 "This Course Is Built For You If..." с описанием всех 4 сегментов:
1. Non-Technical Founders — OK
2. Solopreneurs / Side-Hustlers — OK
3. AI-Era Career Builders — OK
4. AI Skills Seekers — OK

Все 4 сегмента из 03-chosen-segments представлены. **Без нареканий.**

### 2.2. Jobs из сегментов vs лендинг-копи

**Non-Technical Founders Core Jobs:**
- "Понять что строить и в каком порядке" — отражено в Hero: "teaches you what to build". OK.
- "Научиться думать системно, чтобы не выбросить $5-20K" — отражено в Блоке 2: "waste months and $5,000-$20,000 building something nobody wants". OK.
- "Уметь формулировать ЧТО строить AI-кодеру" — отражено в Блоке 5, Job 3: "Create a PRD that an AI coder can actually execute". OK.

**Solopreneurs Core Jobs:**
- "Быстро понять стоит ли идея времени" — Блок 3, Micro Job 1: "Validate any idea in 30 minutes". OK.
- "Получить компактный framework" — Блок 5, Job 4: "6 modules, each 40-60 minutes". OK.
- "Понять как ставить задачу AI-кодеру" — частично через Job 3, но фокус на Non-Technical Founders. Solopreneurs-специфика ("вечера и выходные", "ограниченное время") слабее.

**ЗАМЕЧАНИЕ:** Big Job Solopreneurs ("финансовая свобода и независимость от работодателя") в лендинге НЕ артикулирован явно. Блок 8 "Where You'll Be 6 Weeks From Now" для Solopreneurs говорит: "your side-project has a segment, value proposition, and early traction. Your evenings have purpose." Но Big Job — это "финансовая свобода", а не "вечера с целью". Лендинг недокручивает эмоцию.

### 2.3. Утверждения лендинга vs анализ конкурентов

Лендинг заявляет (Блок 10, Конкурент 2): "Same caliber of product thinking (AURA is more rigorous than most PM courses)".

Анализ конкурентов (06-competitors) НЕ содержит сравнения глубины методологий. Утверждение "AURA is more rigorous" — ничем не подкреплено. Reforge имеет 40+ экспертных курсов с контентом от топовых экспертов Silicon Valley. Lenny привлекает Ken Norton, Andrew Chen, Teresa Torres. Заявление о превосходстве AURA как методологии над контентом Reforge — потенциально вводящее в заблуждение.

Лендинг заявляет (Блок 10, Конкурент 4): "Deeper product methodology" (чем YC Startup School).

Это обоснованное утверждение — анализ конкурентов подтверждает, что YC не даёт JTBD, сегментацию, позиционирование. OK.

### 2.4. Критерии успеха

PRD определяет критерии для Non-Technical Founders: "через 2 недели — PRD + описание сегмента; через 4 недели — работающий лендинг". Лендинг (Блок 2): "In 4-6 weeks, you'll have a validated product idea, a clear segment, a live landing page, and a go-to-market plan."

**Тайминги согласованы.** Лендинг обещает 4-6 недель, PRD описывает 2-4 недели для первых результатов. Лендинг чуть завышает сроки (осторожнее), что правильно.

---

## Проверка 3: Конкуренты <-> PRD <-> Лендинг

### 3.1. Функциональный паритет

Анализ конкурентов выявил ключевые фичи:
- **Community (Slack/Discord):** Reforge, Product School, ZTM имеют сообщества. PRD включает Discord (FR-P.8). OK.
- **Практические задания:** Все конкуренты дают задания. PRD: 6 упражнений. OK.
- **Freemium:** YC (бесплатный), Greg Isenberg (бесплатный курс), Coursera (trial). PRD: Module 1 бесплатный. OK.
- **Сертификация:** Product School даёт PMC, SPMC, PLC. PRD явно исключает сертификацию (секция 9, пункт 5).

**КРИТИЧЕСКИЙ РАЗРЫВ:** Maven (David Jorjani) — ближайший конкурент — предлагает 20+ frameworks, product discovery, customer journey mapping, позиционирование и сегментацию. PRD описывает 6 модулей с AURA Framework. Но PRD НЕ содержит customer journey mapping, и не описывает, как именно 16+ механик создания ценности сравниваются с 20+ frameworks Maven. Конкурентный паритет с Maven неясен.

**ВАЖНЫЙ ПРОПУСК:** Greg Isenberg предлагает Co-founder matching и AI Research Agent (market research за 30 минут). PRD не адресует потребность в co-founder matching (релевантно для Non-Technical Founders) и не предлагает аналога market research инструмента. Эти фичи закрывают real jobs сегмента.

### 3.2. Заявленные преимущества vs функциональность PRD

Лендинг заявляет: "9 ready-to-use AI prompts that do the heavy lifting."
PRD описывает 9 промптов: Idea Validator, Segment Generator, AJTBD Interview Guide, Positioning Generator, Job Graph Generator, Value Hypothesis Generator, Landing Generator, Funnel Generator, Unit Economics Calculator. **Совпадение полное.** OK.

Лендинг заявляет: "2 Claude Code Skills."
PRD описывает: Landing from PRD (Module 5), PRD from Interview (Module 6). **Совпадение полное.** OK.

Лендинг заявляет: "Built by an instructor who trained 11,000+ students."
00-product-idea: "11,000+ студентов". OK, но в 01-business-context: "11K+ студентов" — расхождение на языковом уровне, но по сути совпадает.

**ПРОТИВОРЕЧИЕ:** Лендинг (подзаголовок Hero): "Built by an instructor who trained 11,000+ students." В 00-product-idea: "Как делать продукт — 11,000+ студентов". Но BOOST — это другой продукт с ~4 потоками. Лендинг ссылается на общую цифру, не уточняя, что 11K+ — это русскоязычный курс по другой теме (AJTBD), а не по vibe-coding+product thinking combo. Это потенциально misleading.

### 3.3. "Увольнение конкурентов" в лендинге

Блок 10 лендинга увольняет 5 конкурентов:
1. Free YouTube/Twitter — "fragmented, no system". Анализ подтверждает фрагментарность Greg Isenberg. OK.
2. PM courses (Reforge, Product School, Lenny) — "designed for career PMs, not founders". Анализ подтверждает: Reforge — "не для founders 0-to-1", Product School — "фокус на карьерных PM". OK.
3. Vibe-coding courses — "teach HOW, not WHAT". Анализ подтверждает: Coursera, ZTM — "нет product thinking". OK.
4. YC Startup School — "doesn't go deep on product thinking". Анализ подтверждает. OK.
5. Product consultant — "$200-500 per session, no reusable system". Этого нет в анализе конкурентов как категории. Добавлено в лендинге без аналитической основы. Незначительный разрыв.

---

## Проверка 4: Риски <-> PRD <-> Аналитика

### 4.1. Учёт рисков в PRD

| Риск | Учтён в PRD? | Детали |
|------|-------------|--------|
| Риск 2 (Score 16.0): Нет спроса на combo | ДА | Freemium, модульная структура, A/B тесты заголовков |
| Риск 1 (Score 12.5): EN-аудитория не заплатит | ДА | Aha до оплаты, money-back, social proof |
| Риск 6 (Score 9.0): Конкурентный ландшафт | ДА | Уникальная комбинация, ценовой sweet spot |
| Риск 3 (Score 8.0): CAC слишком высок | ДА | Freemium снижает CAC, SEO, viral промпты |
| Риск 5 (Score 6.0): AI Skills Seekers размыт | ДА | Вторичный сегмент, Module 1 как фильтр |
| Риск 8 (Score 4.5): Контент как "перевод" | ДА | EN-native примеры, субтитры, текстовые промпты |
| Риск 4 (Score 4.0): Низкий completion rate | ДА | Короткие уроки, свой продукт, промпты, community |
| Риск 7 (Score 4.0): Freemium CR ниже 3% | ДА | Aha до оплаты, CTA, money-back, email-nurturing |

Все 8 рисков учтены. **Без критических пропусков в PRD.**

### 4.2. Аналитические события для обнаружения рисков

| Риск | Есть события для раннего обнаружения? |
|------|--------------------------------------|
| Нет спроса на combo | ЧАСТИЧНО. Есть signup_completed, но нет A/B тестирования позиционирования combo vs раздельного. Нет события для трека "какой аспект привлёк" (product thinking vs vibe-coding vs combo). |
| EN-аудитория не заплатит | ДА. purchase_completed с price, refund_requested. Но нет трекинга причины отказа — paywall_dismissed не содержит reason. |
| Конкурентный ландшафт | СЛАБО. Нет трекинга "откуда пришёл конкурент" — нет вопроса "What did you consider instead?" |
| CAC слишком высок | ДА. utm_source на всех событиях, purchase_completed с каналом. OK. |
| AI Skills Seekers размыт | ЧАСТИЧНО. Сегмент определяется по onboarding_question, но если пользователь пропустит вопрос — сегмент не определён. |
| Контент как "перевод" | НЕТ. Нет события для трекинга жалоб на акцент/качество. NPS-комментарий — единственный канал, но это post-hoc. |
| Низкий completion rate | ДА. course_completed, drop_off_detected, churn_risk_detected. OK. |
| Freemium CR < 3% | ДА. module_completed(1) -> purchase_completed. OK. |

**КРИТИЧЕСКИЙ РАЗРЫВ:** Для Риска 2 (главный риск, Score 16.0) нет механизма раннего обнаружения, ПОЧЕМУ combo не резонирует. Событие paywall_dismissed не содержит reason. Нет exit-survey для free users, которые не конвертируются. Это значит, что при реализации главного риска команда не будет знать, combo не работает потому что: (a) product thinking не нужен, (b) vibe-coding не нужен, или (c) combo не ценен. Без этого невозможно пивотнуть.

### 4.3. Маркетинговые гипотезы и риски

Маркетинговые гипотезы из 10-landing-copy учитывают риски:
- Риск 1 (неизвестный автор): M-3 (paid ads) использует бесплатный промпт как entry point, обходя проблему доверия. OK.
- Риск 3 (высокий CAC): M-1, M-2 (SEO) — бесплатное привлечение; M-6 (Twitter) — виральный формат. OK.
- Риск 6 (контент как "перевод"): НЕ УЧТЁН в маркетинговых гипотезах. Все гипотезы предполагают, что контент воспринимается как native EN. Если акцент отпугивает — все каналы привлечения пострадают.

---

## Проверка 5: Revenue-события <-> Бизнес-модель

### 5.1. Монетизационная модель в аналитике

01-business-context: "Freemium -> оплата курса (бесплатный вход, конверсия в платный курс)."

Revenue events в аналитике:
- `paywall_shown` — OK
- `purchase_initiated` — OK (с price, currency, plan)
- `purchase_completed` — OK (с полным набором properties)
- `checkout_abandoned` — OK
- `refund_requested` / `refund_completed` — OK

**Модель покрыта полностью.** Событие `purchase_completed` содержит price, plan (standard/premium), что позволяет считать revenue.

### 5.2. Метрики для юнит-экономики

PRD определяет бизнес-метрики:
- Revenue = 1000 x $199-399 — трекается через sum(purchase_completed.price). OK.
- CAC < $50 — требует внешних данных (marketing spend). Аналитика явно это указывает ("PostHog Trends + внешние данные"). OK.
- LTV/CAC > 4 — рассчитывается. OK.
- Free -> Paid CR > 10% — signup_completed / purchase_completed. OK.

**НО:** PRD указывает два тарифных плана ($199 standard и $399 premium), но нигде в PRD не описано, ЧТО входит в premium vs standard. Нет FR (функционального требования) для premium-плана. Аналитика трекает `plan` property, но PRD не определяет разницу. Это серьёзный пропуск.

### 5.3. Cross-sell / Upsell события

Лендинг (10-landing-copy, Часть 4) описывает:
- 5 cross-sell механик (PRD from Interview $49, Templates Pack $29, Community Pro $19/мес, Prompt Pack $39, Certificate $19)
- 3 upsell механики (Advanced Course $299-499, 1-on-1 Review $199, Cohort Bootcamp $699-999)

**КРИТИЧЕСКИЙ РАЗРЫВ:** В аналитическом плане НЕТ НИ ОДНОГО события для cross-sell и upsell:
- Нет `cross_sell_offered`, `cross_sell_purchased`
- Нет `upsell_offered`, `upsell_purchased`
- Нет `subscription_started` (для Community Pro $19/мес)
- Нет `advanced_course_purchased`
- Нет `consultation_booked`

Это означает, что 8 дополнительных revenue streams описаны в лендинге/маркетинге, но ПОЛНОСТЬЮ невидимы в аналитике. Юнит-экономика не учитывает upsell/cross-sell revenue, хотя лендинг описывает потенциальный дополнительный revenue ~$100K+/год.

---

## Проверка 6: Edge-cases <-> PRD

### 6.1. Critical и High edge-кейсы как требования PRD

| Edge-case | Приоритет | Включён в PRD? |
|-----------|-----------|----------------|
| #1: Двойная оплата (idempotency) | Critical | НЕТ. FR-P.7 описывает оплату через Stripe, но не упоминает idempotency, дедупликацию, дизейбл кнопки. |
| #2: Webhook не дошёл | Critical | НЕТ. FR-P.7 не описывает reconciliation job, ручной механизм "I paid but no access". |
| #3: Money-back abuse | Critical | ЧАСТИЧНО. FR-P.7 упоминает "14 дней без вопросов", но не описывает мониторинг паттернов abuse. |
| #4: OAuth fallback | Critical | ЧАСТИЧНО. FR-P.1 перечисляет "email или Google/GitHub OAuth", но не описывает fallback при недоступности OAuth. |
| #5: Потеря данных упражнений | Critical | ЧАСТИЧНО. FR-P.4 упоминает "автосохранение", но не описывает localStorage буфер, offline-режим, визуальный индикатор. |
| #6: AI-промпт сломался | Critical | НЕТ. Нет требования к еженедельному тестированию промптов, версионированию, fallback-инструкциям. |
| #7: Боты и фейковые аккаунты | Critical | НЕТ. FR-P.1 и FR-P.2 не упоминают rate limiting, CAPTCHA, email verification. |
| #8: Видео не загружается (CDN) | High | ЧАСТИЧНО. NFR-9 упоминает CDN, но нет fallback на текстовую версию. |
| #18: Нет Claude Code подписки | High | НЕТ. FR-5.5 не описывает альтернативный путь для пользователей без Claude Code. |

**ВЫВОД:** Из 7 Critical edge-кейсов — 0 полностью включены в PRD как требования. 3 частично учтены, 4 отсутствуют. PRD написан "happy path" — без учёта критических граничных случаев.

### 6.2. Edge-кейсы, убивающие ключевые jobs

**Edge-case #18 (Claude Code недоступен) УБИВАЕТ core job AI Skills Seekers:**
Core Job: "Получить практические навыки с AI (промпты, skills, workflows)."
Если пользователь не имеет Claude Code ($20-100/мес подписка), он не может использовать 2 из 11 ключевых инструментов курса. Для Non-Technical Founders (приоритетный сегмент!) установка Claude Code через CLI — высокий барьер.

**Edge-case #30 (нет идеи продукта) УБИВАЕТ activation для Сегмента 4:**
AI Skills Seekers часто приходят "посмотреть", без конкретной идеи. Все 6 упражнений требуют собственного продукта. Без идеи — упражнения невыполнимы, Aha-момент не наступает, конверсия в paid нулевая. PRD не предлагает "example project" или альтернативный путь.

**Edge-case #6 (промпт сломался) УБИВАЕТ Aha-момент для ВСЕХ сегментов:**
Aha-момент стратегически сдвинут в бесплатный Module 1 и зависит от AI-промпта "Idea Validator". Если промпт перестаёт работать (новая версия Claude/ChatGPT, изменение формата ответа), Aha-момент уничтожается. При этом нет автоматического тестирования промптов и нет fallback.

### 6.3. Аналитика для детектирования критических edge-кейсов

| Edge-case | Есть аналитика? |
|-----------|----------------|
| Двойная оплата | НЕТ — нет серверного трекинга дубликатов |
| Webhook failure | НЕТ — нет события "payment_received_but_access_not_granted" |
| Money-back abuse | ЧАСТИЧНО — refund_requested содержит modules_completed, но нет автоматического flagging |
| OAuth unavailable | НЕТ — нет мониторинга доступности OAuth |
| Потеря данных | НЕТ — нет события "autosave_failed" или "data_recovery_triggered" |
| Промпт сломался | НЕТ — нет события "prompt_error" или "prompt_quality_check" |
| Боты | НЕТ — нет события "rate_limit_hit" или "captcha_shown" |

---

## Критические разрывы (ОБЯЗАТЕЛЬНО исправить)

| # | Документ А | Документ Б | Противоречие / разрыв | Рекомендация по исправлению |
|---|-----------|-----------|----------------------|---------------------------|
| 1 | 07-prd (Aha-моменты по сегментам) | 09-analytics-plan (единый aha_moment_reached) | PRD описывает 4 разных Aha-момента для 4 сегментов, аналитика трекает только один (Module 1, промпт Idea Validator). Aha для AI Skills Seekers (Module 5) и Career Builders (Module 4) не отслеживается | Добавить в аналитику сегмент-специфичные Aha-события: `aha_segment_founders` (exercise_1 + prompt_1), `aha_segment_seekers` (skill_downloaded + landing created), `aha_segment_career` (exercise_4 + 3+ prompts used) |
| 2 | 10-landing-copy (cross-sell/upsell, 8 механик) | 09-analytics-plan (нет revenue-событий для cross/upsell) | 8 дополнительных revenue-потоков (Templates $29, Certificate $19, Community Pro $19/мес, Advanced Course $299-499, Bootcamp $699-999 и др.) полностью отсутствуют в аналитике | Добавить события: `cross_sell_shown`, `cross_sell_purchased` (с product_name, price), `subscription_started`, `subscription_renewed`, `subscription_cancelled`. Добавить дашборд "Upsell/Cross-sell Revenue" |
| 3 | 05-chosen-risks (Риск 2, Score 16.0: нет спроса на combo) | 09-analytics-plan (нет диагностического события) | Главный риск продукта (нет спроса на combo product+vibe-coding) не имеет механизма диагностики причин. paywall_dismissed не содержит reason. Нет exit-survey | Добавить exit-survey для free users, которые не купили через 14 дней: "What stopped you?" с вариантами: "Didn't need product thinking" / "Didn't need vibe-coding" / "Too expensive" / "Didn't trust instructor" / "Other". Событие: `exit_survey_completed` |
| 4 | 07-prd (FR-P.7: оплата, FR-P.1: регистрация, FR-P.4: упражнения) | 08-edge-cases (7 Critical кейсов) | Ни один из 7 Critical edge-кейсов (двойная оплата, webhook failure, money-back abuse, OAuth fallback, потеря данных, промпт failure, боты) не включён в PRD как функциональное требование | Добавить в PRD секцию "Robustness Requirements": FR-R.1 (idempotency платежей), FR-R.2 (reconciliation job), FR-R.3 (rate limiting + CAPTCHA), FR-R.4 (autosave с localStorage), FR-R.5 (prompt health monitoring), FR-R.6 (OAuth fallback) |
| 5 | 07-prd (два тарифа $199/$399) | 07-prd (нет FR для premium плана) | PRD упоминает цену "$199-399" и аналитика трекает plan: "standard/premium", но нигде не описано, чем standard отличается от premium. Нет функциональных требований для premium | Определить в PRD: что входит в standard ($199) vs premium ($399). Варианты: premium = курс + 1-on-1 review; premium = курс + community pro; premium = курс + advanced prompts. Без этого невозможно ни реализовать, ни маркетить |

---

## Важные улучшения (рекомендуется исправить)

| # | Документ | Что упущено | Рекомендация |
|---|---------|------------|-------------|
| 1 | 09-analytics-plan | Нет события для трекинга, что студент СОЗДАЛ лендинг (ключевой критерий успеха Non-Technical Founders) | Добавить событие `artifact_created` (type: landing_page / prd / funnel_plan) — трекать, когда студент использовал Skill и получил результат |
| 2 | 09-analytics-plan | Нет события для трекинга "пользователь без идеи" — edge-case #30, убивающий активацию Сегмента 4 | Добавить в онбординг вопрос "Do you have a product idea?" и трекать `has_product_idea: boolean`. Показывать example projects для тех, у кого нет |
| 3 | 07-prd | Claude Code Skills (FR-5.5, FR-6.7) не имеют fallback для пользователей без Claude Code подписки | Добавить FR-5.5b: альтернативный путь — "If you don't have Claude Code, use this ChatGPT/Claude web prompt" для каждого Skill |
| 4 | 10-landing-copy | Утверждение "AURA is more rigorous than most PM courses" не подкреплено анализом конкурентов | Либо убрать утверждение, либо обосновать: конкретно описать, что AURA покрывает (AJTBD + UE + RAT + ABCDX), чего нет у Reforge/Lenny. Заменить "more rigorous" на "more integrated" — менее спорное заявление |
| 5 | 10-landing-copy | Страх "Автор неизвестен" (Блок 9) отрабатывается статистикой RU-рынка, но нет плана получения EN social proof до запуска | Запланировать beta-программу: 20-30 EN-студентов бесплатно за отзыв и кейс. Включить в PRD как этап pre-launch. Добавить конкретные сроки |
| 6 | 07-prd | PRD не описывает A/B тестирование лендинга, хотя секция рисков (Риск 2) говорит: "A/B тест заголовков" | Добавить FR-L.6: A/B testing framework — какие элементы тестируем (заголовок, CTA, цена), минимальный размер выборки, инструмент (PostHog Experiments) |
| 7 | 09-analytics-plan | onboarding_question_answered — единственный способ определить сегмент, но PRD (секция 4, путь пользователя) не включает онбординг-вопрос. Регистрация: "email + имя, без обязательных полей" | Согласовать: либо добавить онбординг-вопрос в PRD (FR-P.1b: "после регистрации — 1 вопрос What describes you best"), либо определить альтернативный способ сегментации (по поведению, UTM) |
| 8 | 01-business-context | Горизонт "1-2 месяца до первого рабочего результата", но PRD описывает платформу с видео, упражнениями, Stripe, Discord, CDN — объём работ явно превышает 2 месяца для команды 1-3 человека | Добавить фазирование: Фаза 1 (2 мес) = лендинг + Module 1 + Stripe + email; Фаза 2 (+ 2 мес) = Modules 2-6 + платформа; Фаза 3 (+ 1 мес) = Community + gamification. Иначе есть риск "вечного запуска" |
| 9 | 06-competitors | Greg Isenberg предлагает Co-founder matching — релевантно для Non-Technical Founders, но нигде не адресовано | Рассмотреть: (a) добавить в Discord канал #cofounders, (b) упомянуть в лендинге как future feature, или (c) осознанно исключить с обоснованием |
| 10 | 10-landing-copy (маркетинг) | Маркетинговые гипотезы не учитывают Риск 8 (контент как "перевод"). Если акцент автора отпугивает EN-аудиторию, все каналы пострадают | Добавить маркетинговую гипотезу M-0 (pre-launch): тестирование восприятия акцента — 5-10 EN-native зрителей смотрят 5-минутный фрагмент, NPS > 7 как gate criterion. Если Nет — рассмотреть AI-voiceover или EN co-instructor |

---

## Предложения по усилению (nice to have)

| # | Область | Идея | Ожидаемый эффект |
|---|--------|------|-----------------|
| 1 | Аналитика | Добавить "Health Score" для каждого промпта: автоматическая проверка 1 раз в сутки, что промпт выдаёт ожидаемый формат ответа в Claude и ChatGPT. Событие `prompt_health_check` (status: pass/fail) | Раннее обнаружение поломки промптов (edge-case #6). Если fail — автоматический alert команде |
| 2 | Лендинг | Интерактивный мини-валидатор идеи прямо на лендинге (Блок 4): текстовое поле + упрощённый AI-анализ без регистрации | Сдвиг Aha-момента ещё левее — до регистрации. Потенциальный рост CR лендинга с 20% до 25%+ |
| 3 | PRD | Добавить "Artifact Export" — возможность скачать все результаты упражнений + промптов как PDF "My Product Plan" | Закрывает job Career Builders "иметь кейс в портфолио". Становится виральным артефактом (шеринг в LinkedIn) |
| 4 | Аналитика + PRD | Отслеживать post-course outcomes: "Did you launch a product?" через email-опрос через 3 месяца после завершения | Единственный способ измерить реальную ценность курса. Также мощный source social proof |
| 5 | Конкуренты + Лендинг | Создать публичную comparison page: "From Zero to First Product vs Reforge vs Lenny vs Coursera" — SEO-страница | Перехват трафика по запросам "Reforge alternatives", "product management course comparison". Канал M-4 усиливается |
| 6 | Маркетинг | Создать бесплатный Telegram/WhatsApp бот "Idea Validator" как standalone лид-магнит | Новый канал привлечения с нулевым CAC. Бот шерится виральная. Каждый результат содержит ссылку на курс |

---

## Вердикт

**Оценка согласованности пакета: 6.5/10**

### Обоснование

Пакет документов демонстрирует высокий уровень продуктового мышления и глубокое понимание AURA-методологии. Каждый документ по отдельности написан качественно. Однако при cross-verification обнаруживаются системные разрывы между документами, которые создают риски при реализации.

Главная проблема: **документы писались последовательно, каждый следующий агент добросовестно развивал идеи предыдущего, но обратная связь между поздними и ранними документами отсутствует.** Аналитический план не обновил определение Aha-момента после того, как PRD описал 4 разных варианта. Edge-кейсы выявили 7 Critical проблем, но PRD не был дополнен. Cross-sell/upsell механики появились в лендинге, но не попали в аналитику.

### Топ-3 сильные стороны

1. **Глубокая работа с сегментами и Jobs.** Все 4 сегмента последовательно прослежены через весь пакет: от 03-chosen-segments через PRD, лендинг, аналитику. Core Jobs формулировки единообразны и конкретны. Лендинг корректно отражает все сегменты в блоке "Узнаёшь себя?"

2. **Качественный конкурентный анализ и дифференциация.** 12 конкурентов проанализированы детально, незанятая ниша (Product Thinking + Vibe-Coding + AI Prompts) чётко артикулирована и последовательно прослежена через PRD и лендинг. "Увольнение конкурентов" в лендинге опирается на реальные слабости.

3. **Freemium-стратегия и Aha-момент.** Стратегия "Aha до оплаты" последовательна от PRD до лендинга и аналитики. Module 1 бесплатный, промпт "Idea Validator" доступен без оплаты, CTA контекстные. Это сильная продуктовая механика.

### Топ-3 слабые стороны

1. **Разрыв между edge-кейсами и PRD.** 7 Critical и 15 High edge-кейсов не включены в PRD как требования. PRD описывает "happy path", что создаёт серьёзные риски при реализации: двойная оплата, потеря данных, поломка промптов, боты — всё это вызовет негативный опыт и потерю конверсии.

2. **Аналитика не покрывает ключевые бизнес-решения.** Нет событий для cross-sell/upsell ($100K+ потенциального revenue), нет диагностики причин неконверсии (главный риск Score 16.0), нет сегмент-специфичных Aha-моментов, нет трекинга создания ключевых артефактов (лендинг, PRD).

3. **Разрыв между scope PRD и ресурсами.** Бизнес-контекст указывает "1-2 месяца, команда 1-3 человека", PRD описывает полноценную платформу (видео-плеер, упражнения с автосохранением, Stripe, OAuth, Discord, CDN, прогресс-бар, 9 промптов, 2 Skills, 15+ видеоуроков, A/B тесты). Нет фазирования и MVP-скоупа. Это рецепт задержки запуска.
