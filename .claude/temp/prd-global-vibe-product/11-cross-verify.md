# Cross-Verification: Аудит согласованности продуктового пакета LaunchPilot

Дата: 2026-03-01
Аудитор: Agent 6 (Скептик)

---

## Проверка 1: PRD <-> Аналитика

### 1.1. Core Jobs из PRD покрыты событиями аналитики?

| Core Job в PRD | FR | Покрытие в аналитике | Статус |
|---|---|---|---|
| Сформулировать, что строить (Product Thinking) | FR-1.x | idea_described, prd_generated, prd_edited, segment_selected, mvp_scope_defined | Покрыто |
| Построить работающий прототип (AI-Coding) | FR-2.x | landing_generated, mvp_generated, preview_opened, iteration_requested, iteration_completed, code_error_occurred | Покрыто |
| Задеплоить и показать людям (Launch) | FR-3.x | deploy_initiated, project_deployed, project_redeployed, custom_domain_connected, deploy_link_copied | Покрыто |
| Валидировать идею (Validation) | FR-4.x | validation_plan_viewed, validation_checklist_item_completed, project_analytics_viewed, feedback_submitted, ai_recommendation_applied | Покрыто |
| Монетизировать продукт (Monetization) | FR-5.x | stripe_integration_started, stripe_integration_completed | Покрыто |
| Освоить AI-инструменты (Learning) | FR-6.x | learning_tip_shown, learning_tip_expanded, learning_tip_dismissed, knowledge_base_article_viewed, knowledge_base_searched | Покрыто |

**Вывод:** Все 6 core jobs имеют соответствующие события. Покрытие полное.

### 1.2. Aha-момент: PRD vs Аналитика

- **PRD (раздел "Aha-момент"):** "Пользователь видит свою идею превращённой в работающий лендинг с кодом, который можно открыть в браузере -- за первые 15-20 минут" (для Non-technical Founders).
- **Аналитика:** `aha_moment_reached` трекается когда пользователь провёл > 5 секунд на preview сгенерированного лендинга. Составное событие: `landing_generated` + `preview_opened` + 5 секунд.

**РАЗРЫВ:** В PRD описаны РАЗНЫЕ Aha-моменты для разных сегментов (для Solopreneurs: PRD + прототип + рекомендации; для Career Builders: демо-прототип для руководства), но в аналитике есть ТОЛЬКО ОДИН aha_moment_reached, привязанный к preview лендинга. Aha-момент Solopreneurs (шаг 4) и Career Builders (шаг 3, но с другим определением) не трекаются отдельно.

### 1.3. Метрики успеха из PRD трекаются в аналитике?

| Метрика из PRD (раздел 8) | Трекается в аналитике? | Как |
|---|---|---|
| Projects Deployed per Week (North Star) | ДА | project_deployed, агрегация по неделям |
| Sign-up to Guided Flow Start Rate > 80% | ДА | signup_completed -> guided_flow_started |
| Guided Flow Completion Rate > 50% | ДА | guided_flow_started -> guided_flow_completed |
| Time to Aha-moment < 15 мин | ДА | aha_moment_reached.time_from_signup_seconds |
| Time to First Deploy < 60 мин | ДА | project_deployed.time_from_signup_seconds |
| D7 Retention > 30% | ДА | когортная таблица |
| D30 Retention > 15% | ДА | когортная таблица |
| Free-to-Paid Conversion > 3% | ДА | signup_completed -> purchase_completed |
| MRR > $5K к 3 мес | ДА | purchase_completed + subscription_renewed |
| ARPU $29-49 | ДА | MRR / paying_users |
| Payback Period < 3 мес | ДА | Дашборд 3 |
| Projects per User > 1.5 | ДА | project_created агрегация |
| Sessions per Week > 2 | ДА | session_started агрегация |

**Вывод:** Все метрики успеха покрыты. Сильная работа.

### 1.4. Воронка в аналитике покрывает полный путь?

Путь в PRD: Регистрация -> AI-интервью -> PRD -> Лендинг (Aha) -> MVP -> Итерация -> Деплой -> Валидация.

Воронка в аналитике: page_viewed -> cta_clicked -> signup_started -> signup_completed -> guided_flow_started -> idea_described -> prd_generated -> landing_generated -> preview_opened (aha) -> mvp_generated -> project_deployed -> validation_plan_viewed.

**Вывод:** Полный путь покрыт. Но есть пробел: шаг "Customize" (итерация, FR-2.3) в воронке guided flow не выделен отдельным шагом. Есть iteration_requested/iteration_completed, но они не являются обязательной частью воронки активации.

---

## Проверка 2: Сегменты <-> Лендинг

### 2.1. Все выбранные сегменты представлены в лендинге?

| Сегмент из 03-chosen-segments | Представлен в блоке "Sound familiar?" | Статус |
|---|---|---|
| Сегмент 1: Non-technical Founders "0->1" | ДА, "The Non-Technical Founder" | OK |
| Сегмент 2: Career Builders | ДА, "The Career Builder" | OK |
| Сегмент 3: Solopreneurs / Side-hustlers | ДА, "The Solopreneur / Side-Hustler" | OK |
| Сегмент 4: Builders в организации | НЕТ | РАЗРЫВ |
| Сегмент 5: AI Future-Proofers | НЕТ | РАЗРЫВ |

**РАЗРЫВ:** Сегменты 4 и 5 из файла 03-chosen-segments полностью отсутствуют в лендинге. Они помечены как "вторичные", но это не оговорено как сознательное решение. В PRD для них описаны требования и критерии, что создаёт ожидание покрытия в маркетинге.

### 2.2. Jobs из сегментов корректно отражены в лендинге?

| Core Job из 03-chosen-segments | Как отражена в лендинге | Корректность |
|---|---|---|
| Founders: превратить идею в работающий прототип, не тратить $10-50K | "I can't code, every developer wanted $15,000 just for an MVP" | Корректно |
| Career Builders: освоить AI-инструменты, оставаться конкурентоспособным | "My colleague showed a working prototype to our VP... I feel behind" | Корректно |
| Solopreneurs: построить SaaS, не терять месяцы, повторить путь indie hackers | "I follow Pieter Levels and Marc Lou... Started 4 side projects. Finished zero." | Корректно |

**Вывод:** Для представленных 3 сегментов jobs транслированы точно и эмоционально. Сильная работа.

### 2.3. Утверждения лендинга vs анализ конкурентов?

**РАЗРЫВ в лендинге:** "Production-ready code... the same stack used by Vercel, Netflix, and Notion." В PRD (FR-2.2) стек определён как Next.js + Tailwind + PostgreSQL/SQLite. Упоминание Netflix и Notion как пользователей этого стека -- допустимое, но рискованное утверждение. Netflix использует микросервисы на Java, а Notion -- кастомный стек. Это может подорвать доверие у технически грамотной аудитории.

**РАЗРЫВ в лендинге:** "You can export the code and keep building." В PRD (раздел 9, Что НЕ входит в scope) явно указано: "Экспорт кода (download project) -- MVP -- код живёт на платформе. Экспорт -- в paid tier следующего этапа." Лендинг обещает функциональность, которая не входит в MVP.

### 2.4. Критерии успеха в лендинге vs сегменты?

| Критерий из 03-chosen-segments | Критерий в лендинге | Совпадение |
|---|---|---|
| Founders: прототип за < 2 недели | "30-60 minutes" | Лендинг обещает НАМНОГО больше, чем критерий сегмента. Риск завышенных ожиданий, но в правильную сторону |
| Founders: не потратить > $500 | "$0 to start", "$29/month" | Совпадает |
| Solopreneurs: продукт за < 1 месяц | "30-60 minutes" | Лендинг обещает больше. Но "30-60 минут" -- это прототип, а не готовый бизнес. Может запутать |
| Solopreneurs: не тратить > $100/мес | "$0-29/month" | Совпадает |

---

## Проверка 3: Конкуренты <-> PRD <-> Лендинг

### 3.1. Функциональный паритет выдержан?

Из анализа конкурентов (06-competitors.md), таблица конкурентных фич:

| Критическая фича конкурентов | Есть ли в PRD? | Статус |
|---|---|---|
| AI-генерация кода из промптов | ДА (FR-2.1, FR-2.2) | OK |
| Работа без навыков кодинга | ДА (вся концепция) | OK |
| Встроенный деплой | ДА (FR-3.1) | OK |
| Предпросмотр в реальном времени | ДА (FR-2.4) | OK |
| Freemium модель | ДА (Приложение A) | OK |
| Self-service | ДА | OK |
| Монетизация через Stripe (Replit, Maven) | ДА (FR-5.1) | OK |
| GitHub-интеграция (Lovable) | НЕТ | ВНИМАНИЕ |
| Шаблоны проектов (Lovable: 50+) | ЧАСТИЧНО (FR-7.2: предзаполненные шаблоны, но не библиотека) | ВНИМАНИЕ |
| Мобильные приложения (Maven) | НЕТ (явно исключено) | OK (осознанное решение) |

**РАЗРЫВ:** GitHub-интеграция -- ключевая фича Lovable ("Real code, no vendor lock-in"). В PRD нет GitHub sync, а экспорт кода исключён из MVP. При этом лендинг утверждает "You can export the code and keep building", создавая ложное ожидание отсутствия lock-in.

### 3.2. Заявленные преимущества в лендинге обеспечены PRD?

| Заявление лендинга | Обеспечено в PRD? | Статус |
|---|---|---|
| "Turns your idea into a working product in 30 minutes" | ДА (FR-7.1: 30-60 мин) | OK |
| "Built-in product thinking" (PRD, сегменты, jobs) | ДА (FR-1.1-1.4) | OK |
| "Guided step-by-step by AI" | ДА (FR-7.1, FR-7.2) | OK |
| "Same stack used by Netflix and Notion" | СПОРНО (см. выше) | РИСК |
| "You can export the code and keep building" | НЕТ в MVP | КРИТИЧЕСКИЙ РАЗРЫВ |
| "12,000+ product builders trained" | ДА (данные из существующих продуктов автора) | OK, но пруф для НОВОГО продукта отсутствует |
| "AI generates payment code, you connect your Stripe" | ДА (FR-5.1) | OK |
| "Validation playbook: where to find first 10 users" | ДА (FR-4.2) | OK |

### 3.3. "Увольнение конкурентов" опирается на реальные слабости?

| Утверждение в блоке "увольнение" | Подтверждено анализом конкурентов? | Статус |
|---|---|---|
| "Bolt/Lovable/Replit don't help you figure out WHAT to build" | ДА: сводная таблица подтверждает -- "Продуктовая стратегия / JTBD" = Нет у всех | OK |
| "Maven/FI: $599-799 for 2-5 weeks, fixed schedule" | ДА: Maven $799, FI $599 | OK |
| "Bubble: no-code is becoming obsolete" | СПОРНО: Bubble -- зрелая платформа с 6000+ плагинами, называть её "obsolete" рискованно | РИСК |
| "They're a hammer. We're the architect + the hammer + the blueprint" | Метафора соответствует анализу: gap = "Обучение + Инструмент" | OK |

---

## Проверка 4: Риски <-> PRD <-> Аналитика

### 4.1. Все выбранные риски учтены в PRD?

| Риск из 05-chosen-risks | Учтён в PRD? | Как | Статус |
|---|---|---|---|
| Риск #1 (10.0): Guided AI experience не даёт результата | ДА | FR-7.1 (guided flow), FR-7.2 (anti-stuck), раздел 7 PRD | Полностью покрыт |
| Риск #2 (7.5): Не готовы платить за self-service подписку | ДА | Aha до paywall, free tier, Приложение A, раздел 7 PRD | Полностью покрыт |
| Риск #6 (5.3): Retention будет низким | ДА | FR-8.1-8.3, раздел 7 PRD, retention-механики | Полностью покрыт |

**Вывод:** Все 3 учитываемых риска детально проработаны в PRD. Сильная работа.

### 4.2. Есть ли события аналитики для раннего обнаружения рисков?

| Риск | Аналитические сигналы | Покрытие |
|---|---|---|
| Guided experience не даёт результата | stuck_detected, escape_hatch_clicked, code_error_occurred, guided_flow_step_skipped, guided_flow drop-off воронка | ПОЛНОЕ |
| Не готовы платить | paywall_shown -> paywall_dismissed (высокий dismiss rate), purchase_initiated -> abandoned (не завершили оплату), subscription_cancelled.reason | ПОЛНОЕ, но нет события abandon_checkout |
| Низкий retention | churn_risk_detected, session_started gaps, win_back_email_sent -> win_back_email_clicked (низкий click rate) | ПОЛНОЕ |

**РАЗРЫВ:** Нет события `purchase_abandoned` или `checkout_abandoned` -- когда пользователь начал оплату (purchase_initiated), но не завершил (не дошёл до purchase_completed). Это критический сигнал для Риска #2.

### 4.3. Маркетинговые гипотезы учитывают риски?

- **Риск #1** (guided experience): Гипотезы M-2 (Twitter thread) и M-7 (YouTube tutorial) показывают полный guided flow, что создаёт ожидания. Если flow не работает, эти каналы генерируют разочарование. Рисков в маркетинге нет -- это нормально, но следует учитывать.
- **Риск #2** (не готовы платить): Все маркетинговые гипотезы акцентируют "free", что правильно. Но ни одна гипотеза не описывает стратегию конверсии free -> paid. Маркетинг привлекает, но не конвертирует.
- **Риск #6** (retention): Retention-механики есть в лендинге (10-landing-copy, часть 4), email-nudges покрыты. Но маркетинговые гипотезы полностью сфокусированы на acquisition. Нет ни одной retention-маркетинговой гипотезы (re-engagement campaigns, win-back).

---

## Проверка 5: Revenue-события аналитики <-> Бизнес-модель

### 5.1. Монетизационная модель отражена в revenue events?

- **Бизнес-модель (01-business-context):** Freemium -> платная конверсия.
- **Тиры (PRD, Приложение A):** Free ($0) -> Pro ($29/мес) -> Builder ($49/мес).
- **Revenue events в аналитике:** paywall_shown, upgrade_initiated, purchase_initiated, purchase_completed, subscription_renewed, upgrade_completed (Pro->Builder), downgrade_completed, subscription_cancelled.

**Вывод:** Полная цепочка покрыта. Отлично.

### 5.2. Трекаются ли ключевые метрики для юнит-экономики?

| Метрика юнит-экономики | Данные для расчёта | Покрытие |
|---|---|---|
| CAC | utm_source + рекламные расходы (вручную) / signup_completed | ДА (Дашборд 3, 7) |
| LTV | purchase_completed + subscription_renewed кумулятивно | ДА (Дашборд 3) |
| LTV/CAC | расчёт из вышеперечисленных | ДА |
| Payback Period | CAC / monthly_revenue | ДА (Дашборд 3) |
| ARPU | MRR / paying_users | ДА |
| Monthly Churn Rate | subscription_cancelled / active_subscriptions | ДА (Дашборд 5) |
| Net MRR Growth | New + Expansion - Contraction - Churn | ДА (Дашборд 5, MRR Trend) |

**Вывод:** Все ключевые метрики юнит-экономики покрыты. Сильная работа.

### 5.3. Cross-sell / upsell из лендинга имеют события?

| Механика из лендинга (часть 4) | Событие аналитики | Статус |
|---|---|---|
| Cross-sell 1: AI Marketing Assistant (после деплоя) | НЕТ специального события | РАЗРЫВ |
| Cross-sell 2: Stripe Setup Wizard | stripe_integration_started / completed | ДА |
| Cross-sell 3: Новый проект | project_created | ДА |
| Cross-sell 4: Growth Playbook | НЕТ специального события | РАЗРЫВ |
| Cross-sell 5: Become a Mentor / реферальная программа | share_link_clicked, referral_converted | ЧАСТИЧНО |
| Upsell 1: Лимит проектов -> Pro | paywall_shown (trigger: project_limit) | ДА |
| Upsell 2: Pro -> Builder | upgrade_completed | ДА |
| Upsell 3: Кастомный домен -> Pro | paywall_shown (trigger: custom_domain) | ДА |

**РАЗРЫВ:** Cross-sell механики 1 (AI Marketing Assistant) и 4 (Growth Playbook) описаны в лендинге как будущие фичи, но для них нет ни функциональных требований в PRD, ни событий в аналитике. Это фантомные обещания.

---

## Проверка 6: Edge-cases <-> PRD

### 6.1. Critical и High edge-кейсы включены в PRD?

| Edge-кейс (Critical) | Учтён в PRD как требование? | Статус |
|---|---|---|
| #1: AI генерирует нерабочий код | ЧАСТИЧНО: FR-7.2 (auto-fix ошибок), но нет явного FR на pipeline lint->build->smoke test | ПРОБЕЛ |
| #2: Потеря соединения при генерации | НЕТ явного FR на серверное сохранение промежуточных результатов | ПРОБЕЛ |
| #3: Деплой падает из-за ошибки в коде | ЧАСТИЧНО: FR-3.1 упоминает деплой, но нет pre-deploy validation | ПРОБЕЛ |
| #4: Закрытие браузера на середине flow | НЕТ явного FR на persistence состояния guided flow | ПРОБЕЛ |
| #5: Google OAuth падает | НЕТ явного FR на fallback авторизации (только "Google OAuth + email/password" в NF-10) | ЧАСТИЧНО |
| #6: Claude API таймаут/rate limit | НЕТ явного FR на retry, queue, fallback модель | ПРОБЕЛ |
| #7: Утечка данных между пользователями | ДА: NF-12, NF-13 | OK |
| #8: Утёкшие Stripe API-ключи в коде | НЕТ явного FR на валидацию секретов | ПРОБЕЛ |
| #9: Prompt injection | НЕТ явного FR на input sanitization | ПРОБЕЛ |
| #10: XSS в задеплоенных приложениях | НЕТ явного FR на security scan | ПРОБЕЛ |

**КРИТИЧЕСКИЙ ВЫВОД:** 8 из 10 Critical edge-кейсов НЕ имеют соответствующих явных функциональных требований в PRD. Edge-кейсы выявлены, рекомендации даны, но PRD их не включает. Это означает, что разработчик, работающий только по PRD, НЕ реализует защиты от этих кейсов.

| Edge-кейс (High) | Учтён в PRD? | Статус |
|---|---|---|
| #11: Ввод на не-английском языке | НЕТ | ПРОБЕЛ |
| #12: Слишком абстрактная идея | ЧАСТИЧНО (FR-7.2: шаблоны) | ЧАСТИЧНО |
| #14: 50+ итераций ломают код | НЕТ явного FR на code refactoring / snapshot | ПРОБЕЛ |
| #20: AI-галлюцинации в PRD | НЕТ disclaimer как FR | ПРОБЕЛ |
| #21: Лимит запросов на середине flow | ПРОТИВОРЕЧИЕ: PRD говорит "1 полный guided flow" в free, но нет явного FR, гарантирующего это | ПРОТИВОРЕЧИЕ |
| #25: Один flow для tech и non-tech | ЧАСТИЧНО (онбординг с 1 вопросом), но нет FR на адаптивный flow | ПРОБЕЛ |

### 6.2. Есть ли edge-кейсы, убивающие ключевые jobs?

| Edge-кейс | Какой job убивает? | Серьёзность |
|---|---|---|
| #1: Нерабочий код | Core Job 2: "Построить работающий прототип" -- полностью убивает Aha-момент | ФАТАЛЬНО |
| #3: Падение деплоя | Core Job 3: "Задеплоить и показать людям" -- обрыв на последнем шаге | ФАТАЛЬНО |
| #6: API таймаут | Core Job 2: "Построить прототип" -- блокирует Aha-момент | ФАТАЛЬНО |
| #4: Потеря состояния | Все jobs -- обнуление 30 минут усилий | КРИТИЧНО |
| #9: Prompt injection | Core Job 1: "Сформулировать, что строить" -- компрометация AI | КРИТИЧНО |

### 6.3. Есть ли в аналитике события для детектирования критических edge-кейсов?

| Critical Edge-кейс | Событие аналитики для детекции | Покрытие |
|---|---|---|
| #1: Нерабочий код | code_error_occurred (error_type, auto_fixed) | ДА |
| #2: Потеря соединения | НЕТ события (нет connection_lost или session_interrupted) | НЕТ |
| #3: Падение деплоя | deploy_initiated без project_deployed (по воронке) | КОСВЕННО |
| #4: Закрытие на середине | guided_flow_started без guided_flow_completed + session_ended | КОСВЕННО |
| #5: OAuth падает | signup_started без signup_completed | КОСВЕННО |
| #6: API таймаут | code_error_occurred (error_type: timeout) | ДА |
| #7: Утечка данных | НЕТ security audit event | НЕТ |
| #8: Утечка ключей Stripe | НЕТ secret_leak_detected event | НЕТ |
| #9: Prompt injection | НЕТ injection_attempt_detected event | НЕТ |
| #10: XSS | НЕТ security_scan_failed event | НЕТ |

**РАЗРЫВ:** 4 из 10 Critical edge-кейсов не имеют ни прямых, ни косвенных событий аналитики для их обнаружения. Security-события полностью отсутствуют в аналитическом плане.

---

## Критические разрывы (ОБЯЗАТЕЛЬНО исправить)

| # | Документ А | Документ Б | Противоречие / разрыв | Рекомендация по исправлению |
|---|---|---|---|---|
| 1 | 10-landing-copy (Блок 9) | 07-prd (раздел 9, Исключения) | Лендинг обещает "You can export the code and keep building", но PRD явно исключает экспорт кода из MVP: "Экспорт кода (download project) -- код живёт на платформе". Это прямой обман пользователя | Удалить утверждение об экспорте из лендинга ИЛИ добавить экспорт кода в MVP scope |
| 2 | 08-edge-cases (10 Critical) | 07-prd (FR-требования) | 8 из 10 Critical edge-кейсов не имеют соответствующих функциональных требований в PRD. Разработчик по PRD не реализует защиту от нерабочего кода, потери соединения, API-таймаута, prompt injection, XSS | Добавить в PRD минимум 5 критических FR: (1) FR-9.1 Code Validation Pipeline, (2) FR-9.2 State Persistence, (3) FR-9.3 API Resilience, (4) FR-9.4 Input Sanitization, (5) FR-9.5 Deploy Security Scan |
| 3 | 07-prd (Aha-момент, разные по сегментам) | 09-analytics-plan (один aha_moment_reached) | PRD определяет РАЗНЫЕ Aha-моменты для разных сегментов, но аналитика трекает ТОЛЬКО один -- preview лендинга > 5 сек. Aha-момент для Solopreneurs (PRD + прототип + рекомендации, шаг 4) не трекается | Добавить сегмент-специфичные aha-события ИЛИ пересмотреть определение Aha-момента и унифицировать его в PRD |
| 4 | 09-analytics-plan (revenue events) | 07-prd (risk #2) | Нет события purchase_abandoned / checkout_abandoned. Пользователь начал оплату (purchase_initiated) но не завершил -- это критический сигнал для Риска #2 (не готовы платить). Без этого события невозможно диагностировать, проблема в цене, в UX оплаты или в доверии | Добавить событие checkout_abandoned: когда purchase_initiated есть, а purchase_completed нет в течение 30 минут |
| 5 | 03-chosen-segments (5 сегментов) | 10-landing-copy (3 сегмента в блоке "Sound familiar?") | Сегменты 4 (Builders в организации) и 5 (AI Future-Proofers) полностью отсутствуют в лендинге. В PRD для них есть отдельные разделы с jobs, критериями, даже метриками -- но маркетинг их не адресует | Либо (а) добавить эти сегменты в лендинг, либо (б) явно задокументировать решение НЕ таргетировать их в MVP и убрать из PRD детальные описания |

---

## Важные улучшения (рекомендуется исправить)

| # | Документ | Что упущено | Рекомендация |
|---|---|---|---|
| 1 | 09-analytics-plan | Нет security-событий: prompt_injection_detected, secret_leak_detected, security_scan_failed. Edge-кейсы #7-10 невозможно обнаружить через аналитику | Добавить секцию "Security Events" с 4-5 событиями для мониторинга безопасности |
| 2 | 09-analytics-plan | Нет события connection_lost или session_interrupted для детекции edge-кейса #2 (потеря соединения при генерации). Один из самых болезненных сценариев не детектируется | Добавить событие session_interrupted с properties: step, progress_saved, reconnected |
| 3 | 10-landing-copy (Блок 9) | Лендинг утверждает "same stack used by Vercel, Netflix, and Notion". Netflix использует Java-based микросервисы, Notion -- кастомный стек. Технически грамотная аудитория (Career Builders) может заметить | Заменить на компании, которые реально используют Next.js: Vercel, Hulu, TikTok, или убрать конкретные имена |
| 4 | 10-landing-copy | Cross-sell 1 (AI Marketing Assistant) и Cross-sell 4 (Growth Playbook) описаны как часть стратегии, но не имеют ни FR в PRD, ни событий в аналитике. Это фантомные обещания | Либо удалить из стратегии, либо добавить минимум события-заглушки для трекинга интереса |
| 5 | 07-prd | Нет явного FR на адаптивный guided flow для разных уровней пользователей (edge-кейс #25). Один вопрос онбординга "What best describes you?" определяет сегмент, но flow одинаковый | Добавить FR-7.4: Adaptive Flow с минимум 2 вариантами (tech/non-tech), включая возможность пропуска шагов для опытных |
| 6 | 07-prd | Нет FR на disclaimer для AI-генерируемого контента (edge-кейс #20). PRD генерирует оценки рынка и конкурентов, которые могут быть галлюцинациями | Добавить FR-1.5: AI Content Disclaimer -- маркировка AI-оценок как "Estimate", disclaimer на PRD |
| 7 | 10-landing-copy | "12,000+ product builders trained" -- это данные о существующих русскоязычных продуктах (BOOST + ProductHowTo). LaunchPilot -- новый продукт с 0 пользователей. Утверждение "Join 12,000+ builders who turned ideas into products" создаёт ложное впечатление, что 12000 человек уже используют LaunchPilot | Переформулировать: "From the creators of BOOST Intensive (9.6/10) and ProductHowTo (12,000+ graduates)" -- ссылка на экспертизу, а не на базу пользователей нового продукта |
| 8 | 07-prd (Приложение A) | Free tier: "1 полный guided flow + 2 базовых" -- но edge-кейс #21 и сам PRD одновременно указывают лимит 20 AI-запросов/день. Нет явного FR, гарантирующего завершение первого flow без ограничений | Добавить явный FR: "Первый guided flow не ограничен лимитом AI-запросов" с технической реализацией (флаг is_first_flow) |
| 9 | 09-analytics-plan | Нет события для deploy_failed. deploy_initiated есть, project_deployed есть, но провал деплоя не трекается. Для edge-кейса #3 это необходимо | Добавить событие deploy_failed с properties: error_type, auto_retry_count, resolved |
| 10 | 01-business-context | Горизонт "< 2 недель до первого рабочего результата (MVP)" -- но PRD содержит 50+ функциональных требований, 6 core jobs, 7-шаговый guided flow, интеграции PostHog+Stripe+OAuth. Это невозможно реализовать за 2 недели даже с vibe-coding | Пересмотреть scope MVP или timeline. Предложение: выделить "MVP-0" (1-2 недели): только FR-1.1 + FR-2.1 + FR-2.4 (AI-интервью -> лендинг -> preview). Остальное -- MVP-1 (4-6 недель) |

---

## Предложения по усилению (nice to have)

| # | Область | Идея | Ожидаемый эффект |
|---|---|---|---|
| 1 | 09-analytics-plan | Добавить A/B тест Aha-момента: вариант A (текущий: preview лендинга) vs вариант B (интерактивная 3D-карточка продукта). PostHog feature flags позволяют это из коробки | Валидация гипотезы Aha-момента данными, а не интуицией |
| 2 | 10-landing-copy | Добавить блок с 1-2 реальными кейсами пользователей бета-версии перед запуском. Сейчас лендинг не имеет ни одного отзыва от реального пользователя LaunchPilot | Повышение конверсии через социальное доказательство от реальных, а не гипотетических пользователей |
| 3 | 07-prd | Добавить FR для "Showcase Gallery" -- публичная галерея проектов, созданных на LaunchPilot. Виральная механика + социальное доказательство | Referral coefficient рост, снижение CAC, доказательство ценности |
| 4 | 06-competitors | Добавить раздел "Потенциальные новые конкуренты": что если Bolt.new или Lovable добавят guided flow? Какова защитная стратегия? | Стратегическая готовность к ответу конкурентов |
| 5 | 09-analytics-plan | Добавить трекинг NPS/CSAT: micro-survey после первого деплоя ("How likely are you to recommend?", 1 вопрос) | Ранний сигнал product-market fit, коррелирует с retention |
| 6 | 07-prd | Рассмотреть модель "one-time purchase" как fallback для Риска #2 (не готовы платить подписку). PRD упоминает "Launch Pack за $99", но нет FR | Снижение зависимости от subscription-only модели. Расширение воронки монетизации |
| 7 | 10-landing-copy | Добавить маркетинговую гипотезу для сегмента 4 (Builders в организации): B2B LinkedIn Ads + кейс "PM built internal tool in 1 hour" | Раскрытие потенциала 4-го сегмента, B2B = более высокий ARPU |

---

## Вердикт

**Оценка согласованности пакета: 7/10**

### Обоснование

Пакет документов демонстрирует высокий уровень проработки и внутренней логики. Все 6 core jobs связаны от сегментов через PRD до аналитики. Воронка покрывает полный путь пользователя. Юнит-экономика трекается полностью. Однако обнаружены 5 критических разрывов, из которых 2 представляют реальную угрозу: ложное обещание экспорта кода в лендинге и отсутствие критических edge-кейсов в функциональных требованиях PRD.

### Топ-3 сильные стороны

1. **Аналитический план -- эталонный.** 70+ событий, 7 дашбордов, полный TypeScript-код, триггеры для автоматических коммуникаций, серверная логика churn risk scoring. Каждая метрика из PRD имеет соответствующее событие. Это лучший документ в пакете.

2. **Конкурентный анализ -> PRD -> Лендинг: цепочка работает.** Gap на рынке (обучение + инструмент) идентифицирован, преобразован в 6 core jobs в PRD, и транслирован в конкретные блоки лендинга. "Увольнение конкурентов" опирается на реальные слабости.

3. **Учёт рисков в PRD -- системный.** Все 3 выбранных риска имеют конкретные FR, метрики валидации и целевые значения. Anti-stuck механики (FR-7.2), retention-механики (FR-8.x) и стратегия paywall -- продуманы и взаимосвязаны.

### Топ-3 слабые стороны

1. **Edge-кейсы отделены от PRD.** 58 edge-кейсов выявлены и приоритизированы, но 8 из 10 Critical НЕ превращены в функциональные требования. Документ 08-edge-cases остаётся "рекомендательным", а не "обязательным" -- разработчик его проигнорирует. Это системная ошибка процесса: edge-кейсы должны порождать FR, а не жить в отдельном документе.

2. **Лендинг обещает больше, чем PRD.** Экспорт кода ("keep building"), "12,000+ builders" (подмена базы нового продукта экспертизой автора), "Netflix и Notion" (некорректные примеры стека). Маркетинг опережает продукт -- это создаёт "expectation gap", который убьёт retention даже если привлечение сработает.

3. **Scope vs Timeline -- нереалистичное ожидание.** Бизнес-контекст ставит "< 2 недель до MVP", но PRD описывает продукт на 2-3 месяца разработки: 6 core jobs, 50+ FR, интеграции с PostHog/Stripe/OAuth, guided flow из 7 шагов, retention-механики, email-автоматизация. Без чёткого выделения "MVP-0" (минимально работающее ядро) команда из 1-3 человек не сможет выполнить обещания ни PRD, ни лендинга.
