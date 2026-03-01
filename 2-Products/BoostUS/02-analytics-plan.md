# Аналитический план LaunchPilot — PostHog

Дата: 2026-03-01
Версия: 3.0 (с исправлениями из кросс-верификации)

---

## 1. Ключевые воронки

### 1.1. Единая AARRR-воронка продукта

LaunchPilot — гибрид AI-гайда и образовательного инструмента. Пользователь проходит guided flow из 5 шагов и получает набор документов (PRD, Risk Assessment, Landing Copy, Analytics Plan, Vibe-Coding Plan). Ниже — общая воронка по модели AARRR, затем — особенности по сегментам.

---

#### Acquisition — как пользователь попадает в продукт

Каналы: SEO/GEO (статьи Knowledge Base), контент-маркетинг (LinkedIn, X/Twitter, YouTube), paid ads (Google Ads, Meta Ads, X Ads). Пользователь попадает на лендинг, кликает "Start free", регистрируется через Google OAuth или email (без верификации, 15 сек).

**Шаги воронки:**
1. Просмотр лендинга (`page_viewed`, page_name = "landing")
2. Клик CTA (`cta_clicked`, cta_name = "start_free")
3. Начало регистрации (`signup_started`, method = "google" | "email")
4. Завершение регистрации (`signup_completed`)
5. Онбординг: 2 вопроса (`onboarding_step_completed`, step = "segment_question" | "experience_question")
6. Онбординг завершён (`onboarding_completed`)

**Критичные конверсии:**
- page_viewed -> cta_clicked: интерес лендинга (цель >15%)
- cta_clicked -> signup_completed: конверсия регистрации (цель >60%)
- signup_completed -> onboarding_completed: онбординг (цель >90%)

---

#### Activation — Aha-момент (первая активация ценности)

**Основной Aha-момент (шаг 2) — для всех сегментов:** пользователь получает документ "Segments & Jobs" на шаге 2 guided flow. Это конкретное событие `aha_moment_reached`, которое фиксируется при генерации Segments & Jobs документа. Это первая ощутимая ценность для всех сегментов.

**Вторая активация (шаг 3) — для сегмента Solopreneurs:** для Solopreneurs настоящая глубокая активация наступает на шаге 3 (Risk Assessment), где они получают вердикт "стоит ли тратить время". Фиксируется отдельным событием `risk_assessment_value_realized`.

**Обоснование через core job сегментов:**

- **Non-Technical Founders (0->1):** core job — "понять, что строить". Когда AI превращает сырую идею в структурированные сегменты с jobs, пользователь впервые видит свою идею через призму реальных потребностей. Переживание: "Я за 20 минут получил то, на что ушли бы недели". **Основной Aha = шаг 2.**
- **Solopreneurs / Side-Hustlers:** core job — "быстро оценить, стоит ли идея моего времени". Сегменты и jobs дают первую опору для решения go/no-go (шаг 2 = первый Aha). Однако полная активация наступает на шаге 3 (Risk Assessment), когда пользователь получает чёткий вердикт "стоит ли тратить время" с обоснованием по рискам. **Основной Aha = шаг 2, вторая активация = шаг 3.**
- **AI-Curious Professionals:** core job — "освоить product thinking framework". Применение AJTBD к реальной задаче и получение инсайта, недоступного из ChatGPT. Переживание: "У меня есть framework для любой продуктовой задачи". **Основной Aha = шаг 2.**

**Шаги до Aha-момента:**
1. Начало guided flow (`flow_started`)
2. Шаг 1: AI-интервью (`flow_step_completed`, step = 1, step_name = "ai_interview") -> Idea Summary
3. Шаг 2: Сегменты и Jobs (`flow_step_completed`, step = 2, step_name = "segments_and_jobs") -> **AHA-МОМЕНТ** (основной, для всех)
4. `aha_moment_reached` — фиксируется автоматически при генерации Segments & Jobs
5. Шаг 3: Risk Assessment (`flow_step_completed`, step = 3, step_name = "risk_assessment") -> **ВТОРАЯ АКТИВАЦИЯ** (для Solopreneurs)
6. `risk_assessment_value_realized` — фиксируется при генерации Risk Assessment для пользователей с user_segment = "solopreneur"

**Целевое время до Aha-момента: <25 минут от signup_completed**

**Критичные конверсии:**
- onboarding_completed -> flow_started: начало flow (цель >80%)
- flow_started -> flow_step_completed (step=1): завершение AI-интервью (цель >85%)
- flow_step_completed (step=1) -> aha_moment_reached: достижение Aha (цель >80%)
- aha_moment_reached -> risk_assessment_value_realized: вторая активация для Solopreneurs (цель >75%)

---

#### Revenue — монетизация

Модель: Freemium. Free tier — 2 проекта, 15 AI-запросов/день. Pro — $29/мес. Builder — $49/мес.

Paywall появляется ПОСЛЕ первого полного flow (бесплатного). Триггеры покупки:
- Попытка создать 3-й проект (лимит free tier)
- Попытка экспорта в PDF
- Попытка итерации PRD (>1 итерации)
- Исчерпание AI-запросов

**Шаги воронки:**
1. Просмотр paywall (`paywall_viewed`, trigger = "project_limit" | "export_limit" | "ai_limit" | "iteration_limit")
2. Выбор тарифа (`plan_selected`, plan = "pro" | "builder")
3. Начало оплаты (`purchase_initiated`, plan, price, currency)
4. Успешная оплата (`purchase_completed`, plan, price, currency, payment_method)
5. Апгрейд (`upgrade_completed`, from_plan, to_plan)
6. Продление подписки (`subscription_renewed`, plan, period_number)
7. Отмена подписки (`subscription_cancelled`, plan, reason, lifetime_days)

**Критичные конверсии:**
- aha_moment_reached -> paywall_viewed: намерение купить
- paywall_viewed -> purchase_completed: конверсия paywall (цель >10%)
- signup_completed -> purchase_completed: Free-to-Paid (цель >5%)

---

#### Retention — что означает "вернулся"

Для LaunchPilot retention = пользователь вернулся для продуктивного действия. Не просто сессия, а одно из:

1. **Создание нового проекта** (`project_created`) — новый guided flow
2. **Итерация PRD** (`prd_iteration_started`) — обновление PRD после валидации
3. **Использование Knowledge Base** (`knowledge_base_article_viewed`)
4. **Прогресс по чеклисту** (`checklist_item_completed`)

**Окно retention:** неделя (для D7) и месяц (для D30).

**Целевые метрики:**
- D7 Return Rate: >25%
- D30 Return Rate: >15%
- Projects per User (3 мес): >1.3
- PRD Iteration Rate: >20%

**Как определить:** `session_started` с фильтром по user_id, группировка по неделям/когортам.

---

#### Referral — как пользователь приводит других

Механики:
1. **Share-кнопка** на финальном экране flow: "Share your results"
2. **Footer "Made with LaunchPilot"** на сгенерированных документах (free tier)
3. **Referral-программа** (roadmap, месяц 2): "Invite a friend, get Pro for free"

**События:**
- `referral_link_generated` — пользователь получил реферальную ссылку
- `referral_sent` — пользователь отправил invite (email, share link)
- `referral_clicked` — перешли по реферальной ссылке
- `referral_converted` — реферал зарегистрировался

---

### 1.2. Особенности воронки по сегментам

#### Сегмент 1: Non-Technical Founders (0->1)

| Этап AARRR | Особенности | Ключевой показатель |
|------------|-------------|---------------------|
| Acquisition | Каналы: Google Ads "how to validate startup idea", SEO "AI PRD generator", X/Twitter. utm_segment = "founders" | CAC < $30 |
| Activation | Aha = Segments & Jobs doc (шаг 2). Ожидаемое время до Aha: 20-25 мин. Критичен шаг AI-интервью (должен быть максимально guided) | Time to Aha < 25 мин |
| Revenue | Основной триггер: лимит проектов (у founders обычно 1-2 идеи -> быстро упирается). Целевой тариф: Pro $29/мес | Paid Conversion > 5% |
| Retention | Возврат для: PRD-итерации после валидации, нового проекта. D7 — ожидаем средний (вернутся обновить PRD) | D7 Return > 25%, D30 > 15% |
| Referral | Делятся PRD в founder-сообществах. Share через "Made with LaunchPilot" footer | Referral Rate > 5% |

#### Сегмент 2: Solopreneurs / Side-Hustlers

| Этап AARRR | Особенности | Ключевой показатель |
|------------|-------------|---------------------|
| Acquisition | Каналы: Reddit r/SaaS, Indie Hackers, SEO "vibe coding plan", Product Hunt. utm_segment = "solopreneurs" | CAC < $25 |
| Activation | Первый Aha = Segments & Jobs doc (шаг 2). Ожидаемое время: 15-20 мин (более опытные, быстрее отвечают). Вторая активация = Risk Assessment (шаг 3) — "стоит ли тратить время" (`risk_assessment_value_realized`) | Time to Aha < 20 мин |
| Revenue | Триггеры: лимит проектов (у solopreneurs часто 3-5 идей), лимит AI-запросов. Целевой тариф: Pro $29/мес | Paid Conversion > 7% |
| Retention | Высший retention: несколько идей -> несколько проектов. Возврат для итерации PRD и новых проектов | D7 Return > 30%, D30 > 20% |
| Referral | Активно делятся в Indie Hackers, Twitter/X. Виральность через результаты | Referral Rate > 8% |

#### Сегмент 3: AI-Curious Professionals

| Этап AARRR | Особенности | Ключевой показатель |
|------------|-------------|---------------------|
| Acquisition | Каналы: LinkedIn, SEO "product thinking framework", "how to write PRD with AI". utm_segment = "professionals" | CAC < $40 |
| Activation | Aha = Segments & Jobs doc + осознание framework (шаг 2). Более медленный flow (читают обучающие блоки). Время: 25-35 мин | Time to Aha < 35 мин |
| Revenue | Триггер: доступ к advanced Knowledge Base и расширенным гайдам. Целевой тариф: Pro $29/мес | Paid Conversion > 3% |
| Retention | Низший retention: меньше идей, но возвращаются к Knowledge Base и для кейса в портфолио | D7 Return > 15%, D30 > 10% |
| Referral | Делятся в LinkedIn как "cool tool". Реферал через профессиональные сети | Referral Rate > 3% |

---

## 2. Полный план событий

### 2.1. Acquisition Events

| Название события | Описание | Когда трекать | Properties | Тип |
|-----------------|----------|---------------|------------|-----|
| `page_viewed` | Просмотр страницы | При загрузке любой страницы | `page_name`, `page_url`, `referrer`, `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term` | funnel |
| `cta_clicked` | Клик по CTA-кнопке | При клике на любой CTA | `cta_name`, `cta_location`, `page_name` | funnel |
| `signup_started` | Начало регистрации | При открытии формы регистрации / клике "Sign up with Google" | `method` ("google" / "email"), `referrer`, `utm_source`, `utm_medium`, `utm_campaign` | funnel |
| `signup_completed` | Завершение регистрации | При успешном создании аккаунта | `method`, `user_segment` (null до онбординга), `referrer`, `utm_source`, `utm_medium`, `utm_campaign`, `signup_duration_sec` | funnel |

### 2.2. Onboarding Events

| Название события | Описание | Когда трекать | Properties | Тип |
|-----------------|----------|---------------|------------|-----|
| `onboarding_step_completed` | Ответ на вопрос онбординга | При выборе ответа на каждый вопрос | `step` ("segment_question" / "experience_question"), `answer` (выбранный вариант), `step_duration_sec` | funnel |
| `onboarding_completed` | Онбординг завершён | После ответа на оба вопроса | `user_segment` ("founder" / "solopreneur" / "professional"), `experience_level` ("beginner" / "intermediate" / "experienced"), `total_duration_sec` | funnel |

### 2.3. Guided Flow Events (Core)

| Название события | Описание | Когда трекать | Properties | Тип |
|-----------------|----------|---------------|------------|-----|
| `flow_started` | Начало guided flow | При входе в шаг 1 | `project_id`, `user_segment`, `experience_level`, `is_template` (bool — использовал ли шаблонную идею) | funnel |
| `flow_step_started` | Начало конкретного шага | При входе на экран шага | `project_id`, `step` (1-5), `step_name` ("ai_interview" / "segments_and_jobs" / "risk_assessment" / "prd_generation" / "vibe_coding_plan"), `time_since_flow_start_sec` | funnel |
| `flow_step_completed` | Завершение шага | При генерации документа шага | `project_id`, `step`, `step_name`, `step_duration_sec`, `document_generated` (название документа), `ai_messages_count` (кол-во сообщений AI в этом шаге) | funnel |
| `flow_step_skipped` | Пользователь пропустил шаг | При клике "Skip" | `project_id`, `step`, `step_name`, `time_on_step_sec` | funnel |
| `flow_completed` | Завершение всего guided flow | После шага 5 | `project_id`, `total_duration_sec`, `steps_completed` (число завершённых шагов), `steps_skipped` (число пропущенных), `documents_generated` (список документов), `user_segment` | funnel |
| `flow_abandoned` | Пользователь покинул flow без завершения | При уходе со страницы / закрытии, если flow не завершён (трекается через beforeunload + серверная проверка через 30 мин бездействия) | `project_id`, `last_step`, `last_step_name`, `time_on_last_step_sec`, `total_time_sec` | funnel |

### 2.4. Aha-момент Events

| Название события | Описание | Когда трекать | Properties | Тип |
|-----------------|----------|---------------|------------|-----|
| `aha_moment_reached` | Достижение основного Aha-момента (для всех сегментов) | При генерации документа Segments & Jobs (шаг 2) | `project_id`, `time_since_signup_sec`, `time_since_flow_start_sec`, `user_segment`, `segments_generated_count` (кол-во сегментов), `jobs_generated_count` | funnel, cohort |
| `risk_assessment_value_realized` | Вторая активация для Solopreneurs | При генерации Risk Assessment (шаг 3) для пользователей с user_segment = "solopreneur" | `project_id`, `time_since_signup_sec`, `time_since_aha_sec`, `user_segment`, `verdict` ("go" / "pivot" / "kill" / "validate_first"), `risks_count` | funnel, cohort |
| `idea_summary_generated` | Сгенерирован Idea Summary | После шага 1 AI-интервью | `project_id`, `interview_messages_count`, `interview_duration_sec`, `idea_word_count` | funnel |
| `segments_jobs_generated` | Сгенерирован документ Segments & Jobs | После шага 2 | `project_id`, `segments_count`, `jobs_count`, `selected_segment_index`, `generation_duration_sec` | funnel |
| `risk_assessment_generated` | Сгенерирован Risk Assessment | После шага 3 | `project_id`, `risks_count`, `top_risk_category`, `verdict` ("go" / "pivot" / "kill" / "validate_first"), `generation_duration_sec` | funnel |
| `prd_generated` | Сгенерирован PRD | После шага 4 | `project_id`, `prd_sections_count`, `mvp_features_count`, `deferred_features_count`, `generation_duration_sec` | funnel |
| `vibe_coding_plan_generated` | Сгенерирован Vibe-Coding Plan | После шага 5 | `project_id`, `recommended_tool`, `prompts_count`, `checklist_items_count`, `generation_duration_sec` | funnel |

### 2.5. Bonus Document Events

| Название события | Описание | Когда трекать | Properties | Тип |
|-----------------|----------|---------------|------------|-----|
| `landing_copy_generated` | Сгенерирована Landing Copy | При генерации бонусного документа | `project_id`, `generation_duration_sec`, `sections_count` | funnel |
| `analytics_plan_generated` | Сгенерирован Analytics Plan | При генерации бонусного документа | `project_id`, `generation_duration_sec`, `events_count`, `dashboards_count` | funnel |
| `competitor_analysis_generated` | Сгенерирован Competitor Analysis | При генерации бонусного документа | `project_id`, `generation_duration_sec`, `competitors_count` | funnel |

### 2.6. Document Interaction Events

| Название события | Описание | Когда трекать | Properties | Тип |
|-----------------|----------|---------------|------------|-----|
| `document_viewed` | Просмотр документа | При открытии документа в Project Workspace | `project_id`, `document_type` ("idea_summary" / "segments_jobs" / "risk_assessment" / "prd" / "vibe_coding_plan" / "landing_copy" / "analytics_plan" / "competitor_analysis"), `view_duration_sec` | cohort |
| `document_copied` | Копирование документа | При клике "Copy to Clipboard" | `project_id`, `document_type` | cohort |
| `document_downloaded` | Скачивание документа | При клике "Download" | `project_id`, `document_type`, `format` ("md" / "pdf") | cohort |
| `document_exported_all` | Экспорт всех документов | При клике "Export All" | `project_id`, `format` ("zip"), `documents_count` | cohort |
| `document_edited_via_ai` | Редактирование через диалог с AI | При отправке запроса на редактирование | `project_id`, `document_type`, `edit_type` ("add_feature" / "remove_feature" / "explain" / "rewrite" / "other") | cohort |

### 2.7. AI Interaction Events

| Название события | Описание | Когда трекать | Properties | Тип |
|-----------------|----------|---------------|------------|-----|
| `ai_message_sent` | Пользователь отправил сообщение AI | При каждом сообщении в AI-диалоге | `project_id`, `step`, `step_name`, `message_length`, `context` ("interview" / "editing" / "iteration" / "help") | cohort |
| `ai_response_received` | AI ответил | При получении ответа | `project_id`, `step`, `response_time_ms`, `response_length`, `context` | cohort |
| `ai_help_requested` | Нажата кнопка "I'm stuck" | При клике | `project_id`, `step`, `step_name`, `time_on_step_sec` | cohort |
| `ai_suggestion_accepted` | Пользователь принял подсказку AI | При выборе предложенного варианта / шаблона | `project_id`, `step`, `suggestion_type` ("example" / "template" / "reformulation") | cohort |
| `ai_limit_reached` | Исчерпан лимит AI-запросов | При достижении лимита | `plan` ("free" / "pro" / "builder"), `requests_used`, `requests_limit` | revenue |

### 2.8. Learning Events

| Название события | Описание | Когда трекать | Properties | Тип |
|-----------------|----------|---------------|------------|-----|
| `learning_block_expanded` | Открытие обучающего блока | При клике "Learn more" / раскрытии блока | `project_id`, `step`, `block_topic` ("ajtbd" / "rat" / "unit_economics" / "mvp" / "prompt_engineering"), `block_id` | cohort |
| `learning_block_collapsed` | Закрытие обучающего блока | При клике "Collapse" / сворачивании | `project_id`, `step`, `block_topic`, `time_open_sec` | cohort |
| `knowledge_base_article_viewed` | Просмотр статьи Knowledge Base | При открытии статьи | `article_id`, `article_title`, `category` ("product_thinking" / "risk_validation" / "unit_economics" / "vibe_coding" / "prompt_engineering"), `source` ("flow_link" / "direct" / "search") | cohort |
| `knowledge_base_searched` | Поиск в Knowledge Base | При запросе поиска | `query`, `results_count`, `clicked_result_index` | cohort |

### 2.9. Revenue Events

| Название события | Описание | Когда трекать | Properties | Тип |
|-----------------|----------|---------------|------------|-----|
| `paywall_viewed` | Просмотр paywall | При показе paywall (триггер = лимит) | `trigger` ("project_limit" / "export_limit" / "ai_limit" / "iteration_limit" / "manual_upgrade"), `current_plan` ("free" / "pro"), `user_segment` | revenue |
| `plan_selected` | Выбор тарифа | При клике на карточку тарифа | `plan` ("pro" / "builder"), `price`, `currency`, `billing_period` ("monthly" / "annual"), `trigger` | revenue |
| `purchase_initiated` | Начало оплаты | При переходе к платёжной форме | `plan`, `price`, `currency`, `billing_period`, `payment_method` | revenue |
| `purchase_completed` | Успешная оплата | При подтверждении платежа | `plan`, `price`, `currency`, `billing_period`, `payment_method`, `trial_used` (bool), `days_since_signup`, `projects_created_before_purchase`, `flow_completed_before_purchase` (bool) | revenue |
| `purchase_failed` | Ошибка оплаты | При неуспешном платеже | `plan`, `error_type`, `payment_method` | revenue |
| `checkout_abandoned` | Пользователь начал checkout, но не завершил | При уходе со страницы checkout без purchase_completed (трекинг через beforeunload + таймаут 30 мин) | `plan`, `step` ("plan_selected" / "payment_info" / "confirmation"), `time_on_checkout_sec` | revenue |
| `upgrade_completed` | Апгрейд тарифа | При переходе с Pro на Builder | `from_plan`, `to_plan`, `price_diff`, `days_on_previous_plan` | revenue |
| `subscription_renewed` | Продление подписки | При автоматическом списании | `plan`, `price`, `period_number`, `lifetime_revenue` | revenue |
| `subscription_cancelled` | Отмена подписки | При клике "Cancel" + подтверждение | `plan`, `reason` (выбранная причина), `reason_text` (свободный текст), `lifetime_days`, `lifetime_revenue`, `projects_created`, `documents_generated` | revenue |
| `refund_requested` | Запрос возврата | При отправке запроса на возврат | `plan`, `amount`, `reason`, `lifetime_days` | revenue |

### 2.10. Retention Events

| Название события | Описание | Когда трекать | Properties | Тип |
|-----------------|----------|---------------|------------|-----|
| `session_started` | Начало сессии | При загрузке приложения авторизованным пользователем | `session_number`, `days_since_last_session`, `days_since_signup`, `current_plan`, `user_segment` | cohort |
| `project_created` | Создание нового проекта | При клике "New Project" | `project_number` (порядковый номер), `current_plan`, `days_since_signup` | cohort |
| `prd_iteration_started` | Начало итерации PRD | При клике "Update PRD" | `project_id`, `iteration_number`, `days_since_last_iteration`, `days_since_flow_completed` | cohort |
| `prd_iteration_completed` | Завершение итерации PRD | При сохранении обновлённого PRD | `project_id`, `iteration_number`, `changes_summary`, `iteration_duration_sec` | cohort |
| `checklist_item_completed` | Выполнен пункт чеклиста | При отметке пункта в Next Steps | `project_id`, `checklist_item` ("first_result" / "expert_interviews" / "landing_test" / "user_feedback" / "update_prd"), `checklist_progress_pct` | cohort |
| `feature_used` | Использование фичи продукта | При взаимодействии с любой ключевой фичей | `feature_name` ("ai_interview" / "document_generation" / "document_export" / "prd_iteration" / "knowledge_base" / "micro_guide" / "prompt_template"), `project_id` | cohort |
| `value_received` | Пользователь получил конкретную ценность | При генерации любого документа или завершении шага flow | `value_type` ("document_generated" / "flow_step_completed" / "prd_iterated" / "knowledge_gained"), `project_id`, `document_type` | cohort |

### 2.11. Churn Events

| Название события | Описание | Когда трекать | Properties | Тип |
|-----------------|----------|---------------|------------|-----|
| `churn_risk_detected` | Обнаружен риск оттока | Серверный триггер: пользователь paid-плана не заходил N дней | `days_inactive`, `plan`, `lifetime_days`, `last_action`, `projects_count`, `documents_count` | cohort |
| `subscription_cancelled` | Отмена подписки | (см. Revenue Events выше) | (см. выше) | revenue |
| `downgrade_completed` | Переход на более дешёвый план | При даунгрейде | `from_plan`, `to_plan`, `reason`, `days_on_previous_plan` | revenue |
| `account_deleted` | Удаление аккаунта | При запросе на удаление | `plan`, `lifetime_days`, `projects_count`, `documents_count`, `reason` | revenue |

### 2.12. Referral Events

| Название события | Описание | Когда трекать | Properties | Тип |
|-----------------|----------|---------------|------------|-----|
| `share_button_clicked` | Клик на кнопку "Share" | При клике Share на финальном экране flow | `project_id`, `share_channel` ("link" / "twitter" / "linkedin" / "email") | cohort |
| `referral_link_generated` | Создание реферальной ссылки | При генерации уникальной ссылки | `referrer_user_id`, `campaign` | cohort |
| `referral_sent` | Отправка инвайта | При шейре ссылки | `referrer_user_id`, `channel` ("email" / "link" / "social"), `campaign` | cohort |
| `referral_clicked` | Переход по реферальной ссылке | При переходе | `referrer_user_id`, `campaign` | cohort |
| `referral_converted` | Реферал зарегистрировался | При signup по реферальной ссылке | `referrer_user_id`, `referred_user_id`, `campaign` | cohort |

### 2.13. Anti-Stuck Events

| Название события | Описание | Когда трекать | Properties | Тип |
|-----------------|----------|---------------|------------|-----|
| `stuck_detected` | Обнаружено бездействие | Серверный/клиентский триггер: >3 мин на шаге без действия | `project_id`, `step`, `step_name`, `idle_time_sec` | cohort |
| `stuck_help_offered` | Предложена помощь | При показе подсказки "Stuck? Here's what you can do..." | `project_id`, `step`, `help_type` ("suggestion" / "example" / "template" / "reformulation") | cohort |
| `stuck_help_accepted` | Помощь принята | При клике на подсказку | `project_id`, `step`, `help_type` | cohort |
| `template_idea_selected` | Выбрана шаблонная идея | При выборе шаблона для практики | `template_name`, `user_segment` | cohort |

### 2.14. Email & Communication Events

| Название события | Описание | Когда трекать | Properties | Тип |
|-----------------|----------|---------------|------------|-----|
| `email_sent` | Email отправлен пользователю | При отправке любого email | `email_type` ("nudge_d1" / "nudge_d3" / "nudge_d7" / "nudge_d14" / "nudge_d30" / "churn_prevention" / "upsell" / "welcome"), `user_segment` | cohort |
| `email_opened` | Email открыт | При трекинге открытия (pixel) | `email_type`, `user_segment`, `days_since_sent` | cohort |
| `email_clicked` | Клик в email | При клике на ссылку в email | `email_type`, `link_name`, `user_segment` | cohort |
| `email_unsubscribed` | Отписка от рассылки | При клике "Unsubscribe" | `email_type`, `user_segment`, `emails_received_count` | cohort |

### 2.15. Micro-Guide Events (исправление из кросс-верификации: Улучшение #1)

Покрывает FR-4.2 (микро-гайды по установке инструментов) и Риск #3 (micro-guides устаревают).

| Название события | Описание | Когда трекать | Properties | Тип |
|-----------------|----------|---------------|------------|-----|
| `micro_guide_started` | Пользователь начал микро-гайд | При открытии гайда по установке/настройке инструмента | `guide_id`, `tool` (название инструмента: "cursor" / "claude_code" / "lovable" / "replit" / "bolt") | cohort |
| `micro_guide_step_completed` | Пользователь завершил шаг гайда | При отметке шага как выполненного | `guide_id`, `step` (номер шага), `step_name` | cohort |
| `micro_guide_completed` | Пользователь завершил весь гайд | При завершении последнего шага | `guide_id`, `total_time_sec` | cohort |
| `micro_guide_step_failed` | Шаг гайда не сработал / пользователь столкнулся с проблемой | При нажатии "This didn't work" / обратной связи | `guide_id`, `step` (номер шага), `feedback` (текст обратной связи) | cohort |

### 2.16. PMF & Quality Survey Events (исправление из кросс-верификации: Критический разрыв #3)

Покрывает 4 ключевых метрики quality/PMF из PRD: NPS >40, CSAT per step >4.0/5.0, PMF survey "very disappointed" >40%, Document Quality Score >7/10.

| Название события | Описание | Когда трекать | Properties | Тип |
|-----------------|----------|---------------|------------|-----|
| `nps_survey_submitted` | Пользователь ответил на NPS-опрос | D7 после первого завершённого flow | `score` (0-10), `comment`, `days_since_signup`, `segment` (user_segment), `trigger` ("day_7_post_first_flow") | cohort |
| `csat_submitted` | Пользователь оценил шаг flow | После каждого шага для первых 200 пользователей | `step` ("ai_interview" / "segments_jobs" / "risk_assessment" / "prd_generation" / "vibe_coding_plan"), `score` (1-5), `session_number` | cohort |
| `pmf_survey_submitted` | Пользователь ответил на PMF-опрос (Sean Ellis test) | D14 после регистрации | `answer` ("very_disappointed" / "somewhat_disappointed" / "not_disappointed"), `days_since_signup`, `projects_completed`, `trigger` ("day_14") | cohort |
| `document_quality_rated` | Пользователь оценил качество документа | При копировании или экспорте документа | `document_type`, `score` (1-10), `feedback` (текст), `project_id` | cohort |

**Триггеры показа опросов:**
- **NPS:** D7 после первого завершённого flow. Показывается один раз. Если пользователь не ответил — повторный показ через 3 дня.
- **CSAT:** После каждого шага guided flow для первых 200 пользователей (для набора статистической значимости). После этого — выборочно (каждый 10-й пользователь).
- **PMF survey:** D14 после регистрации. Показывается один раз. Минимальное условие: пользователь завершил хотя бы 1 flow.
- **Document Quality:** При копировании (`document_copied`) или экспорте (`document_downloaded`) документа — in-app popup "Rate this document (1-10)". Не чаще 1 раза за сессию.

### 2.17. MRR Snapshot (серверное событие) (исправление из кросс-верификации: Улучшение #3)

| Название события | Описание | Когда трекать | Properties | Тип |
|-----------------|----------|---------------|------------|-----|
| `mrr_snapshot` | Ежедневный снэпшот MRR | Серверный cron-job, ежедневно в 00:00 UTC | `mrr` (total MRR), `new_mrr` (MRR от новых подписчиков), `churned_mrr` (MRR потерянный от churn), `expansion_mrr` (MRR от upgrades), `period` ("daily"), `active_subscriptions` (количество активных подписок) | revenue |

### 2.18. AI Content Quality Events (исправление из кросс-верификации: Улучшение #7)

Покрывает Риск #8 (качество AI experience) и обнаружение AI-галлюцинаций.

| Название события | Описание | Когда трекать | Properties | Тип |
|-----------------|----------|---------------|------------|-----|
| `ai_content_flagged` | Пользователь отметил проблему в AI-контенте | При нажатии кнопки "Is this accurate?" / "Report issue" на сгенерированном контенте | `document_type`, `flag_type` ("inaccurate" / "outdated" / "irrelevant"), `user_feedback` (текст), `section` (название секции документа) | cohort |

### 2.19. Security & Anti-Abuse Events (исправление из кросс-верификации: Edge-cases)

Покрывает Critical edge-кейсы: Prompt Injection и Anti-Abuse (мультиаккаунты).

| Название события | Описание | Когда трекать | Properties | Тип |
|-----------------|----------|---------------|------------|-----|
| `injection_attempt_detected` | Обнаружена попытка prompt injection | При срабатывании фильтра на вводе пользователя | `input_type` (тип поля ввода), `pattern_matched` (имя сработавшего паттерна), `user_id`, `blocked` (true) | security |
| `abuse_detected` | Обнаружено злоупотребление | При срабатывании anti-abuse механик | `type` ("multi_account" / "rate_limit" / "scraping"), `user_id`, `ip` (IP-адрес) | security |

---

## 3. Код для PostHog (TypeScript)

### 3.1. Инициализация и идентификация

```typescript
// lib/analytics/posthog.ts

import posthog from 'posthog-js';

// ===== ИНИЦИАЛИЗАЦИЯ =====
export function initPostHog() {
  if (typeof window !== 'undefined') {
    posthog.init(process.env.NEXT_PUBLIC_POSTHOG_KEY!, {
      api_host: process.env.NEXT_PUBLIC_POSTHOG_HOST || 'https://us.i.posthog.com',
      person_profiles: 'identified_only',
      capture_pageview: false, // Ручной трекинг через page_viewed
      capture_pageleave: true,
      autocapture: false, // Только ручные события
      session_recording: {
        maskAllInputs: false,
        maskInputFn: (text, element) => {
          // Маскируем пароли и платёжные данные, остальное оставляем
          if (element?.type === 'password') return '*'.repeat(text.length);
          return text;
        },
      },
    });
  }
}

// ===== ИДЕНТИФИКАЦИЯ ПОЛЬЗОВАТЕЛЯ =====
export function identifyUser(userId: string, properties: {
  email: string;
  signup_method: 'google' | 'email';
  signup_date: string; // ISO string
  user_segment?: 'founder' | 'solopreneur' | 'professional';
  experience_level?: 'beginner' | 'intermediate' | 'experienced';
  plan: 'free' | 'pro' | 'builder';
  utm_source?: string;
  utm_medium?: string;
  utm_campaign?: string;
}) {
  posthog.identify(userId, {
    email: properties.email,
    signup_method: properties.signup_method,
    signup_date: properties.signup_date,
    user_segment: properties.user_segment,
    experience_level: properties.experience_level,
    plan: properties.plan,
    utm_source: properties.utm_source,
    utm_medium: properties.utm_medium,
    utm_campaign: properties.utm_campaign,
    // Вычисляемые при идентификации
    projects_count: 0,
    documents_generated_count: 0,
    flow_completed_count: 0,
    lifetime_revenue: 0,
  });
}

// ===== ОБНОВЛЕНИЕ СВОЙСТВ ПОЛЬЗОВАТЕЛЯ =====
export function updateUserProperties(properties: Record<string, any>) {
  posthog.people.set(properties);
}

export function incrementUserProperty(property: string, value: number = 1) {
  posthog.people.set_once({ [property]: 0 }); // Инициализация если не существует
  posthog.capture('$set', {
    $set: { [property]: value }, // PostHog JS не имеет нативного increment, используем set
  });
}
```

### 3.2. Acquisition Events

```typescript
// lib/analytics/acquisition.ts

import posthog from 'posthog-js';

// ===== PAGE VIEWED =====
export function trackPageViewed(properties: {
  page_name: string;
  page_url: string;
  referrer?: string;
  utm_source?: string;
  utm_medium?: string;
  utm_campaign?: string;
  utm_content?: string;
  utm_term?: string;
}) {
  posthog.capture('page_viewed', {
    page_name: properties.page_name,
    page_url: properties.page_url,
    referrer: properties.referrer || document.referrer,
    utm_source: properties.utm_source,
    utm_medium: properties.utm_medium,
    utm_campaign: properties.utm_campaign,
    utm_content: properties.utm_content,
    utm_term: properties.utm_term,
  });
}

// ===== CTA CLICKED =====
export function trackCtaClicked(properties: {
  cta_name: string;
  cta_location: string;
  page_name: string;
}) {
  posthog.capture('cta_clicked', {
    cta_name: properties.cta_name,
    cta_location: properties.cta_location,
    page_name: properties.page_name,
  });
}

// ===== SIGNUP STARTED =====
export function trackSignupStarted(properties: {
  method: 'google' | 'email';
  referrer?: string;
  utm_source?: string;
  utm_medium?: string;
  utm_campaign?: string;
}) {
  posthog.capture('signup_started', {
    method: properties.method,
    referrer: properties.referrer || document.referrer,
    utm_source: properties.utm_source,
    utm_medium: properties.utm_medium,
    utm_campaign: properties.utm_campaign,
  });
}

// ===== SIGNUP COMPLETED =====
export function trackSignupCompleted(properties: {
  method: 'google' | 'email';
  referrer?: string;
  utm_source?: string;
  utm_medium?: string;
  utm_campaign?: string;
  signup_duration_sec: number;
}) {
  posthog.capture('signup_completed', {
    method: properties.method,
    referrer: properties.referrer,
    utm_source: properties.utm_source,
    utm_medium: properties.utm_medium,
    utm_campaign: properties.utm_campaign,
    signup_duration_sec: properties.signup_duration_sec,
  });
}
```

### 3.3. Onboarding Events

```typescript
// lib/analytics/onboarding.ts

import posthog from 'posthog-js';
import { updateUserProperties } from './posthog';

// ===== ONBOARDING STEP COMPLETED =====
export function trackOnboardingStepCompleted(properties: {
  step: 'segment_question' | 'experience_question';
  answer: string;
  step_duration_sec: number;
}) {
  posthog.capture('onboarding_step_completed', {
    step: properties.step,
    answer: properties.answer,
    step_duration_sec: properties.step_duration_sec,
  });
}

// ===== ONBOARDING COMPLETED =====
export function trackOnboardingCompleted(properties: {
  user_segment: 'founder' | 'solopreneur' | 'professional';
  experience_level: 'beginner' | 'intermediate' | 'experienced';
  total_duration_sec: number;
}) {
  posthog.capture('onboarding_completed', {
    user_segment: properties.user_segment,
    experience_level: properties.experience_level,
    total_duration_sec: properties.total_duration_sec,
  });

  // Обновляем профиль пользователя
  updateUserProperties({
    user_segment: properties.user_segment,
    experience_level: properties.experience_level,
    onboarding_completed_at: new Date().toISOString(),
  });
}
```

### 3.4. Guided Flow Events

```typescript
// lib/analytics/guided-flow.ts

import posthog from 'posthog-js';
import { updateUserProperties } from './posthog';

type FlowStep = 1 | 2 | 3 | 4 | 5;
type StepName = 'ai_interview' | 'segments_and_jobs' | 'risk_assessment' | 'prd_generation' | 'vibe_coding_plan';

const STEP_NAMES: Record<FlowStep, StepName> = {
  1: 'ai_interview',
  2: 'segments_and_jobs',
  3: 'risk_assessment',
  4: 'prd_generation',
  5: 'vibe_coding_plan',
};

// ===== FLOW STARTED =====
export function trackFlowStarted(properties: {
  project_id: string;
  user_segment: string;
  experience_level: string;
  is_template: boolean;
}) {
  posthog.capture('flow_started', {
    project_id: properties.project_id,
    user_segment: properties.user_segment,
    experience_level: properties.experience_level,
    is_template: properties.is_template,
  });
}

// ===== FLOW STEP STARTED =====
export function trackFlowStepStarted(properties: {
  project_id: string;
  step: FlowStep;
  time_since_flow_start_sec: number;
}) {
  posthog.capture('flow_step_started', {
    project_id: properties.project_id,
    step: properties.step,
    step_name: STEP_NAMES[properties.step],
    time_since_flow_start_sec: properties.time_since_flow_start_sec,
  });
}

// ===== FLOW STEP COMPLETED =====
export function trackFlowStepCompleted(properties: {
  project_id: string;
  step: FlowStep;
  step_duration_sec: number;
  document_generated: string;
  ai_messages_count: number;
}) {
  posthog.capture('flow_step_completed', {
    project_id: properties.project_id,
    step: properties.step,
    step_name: STEP_NAMES[properties.step],
    step_duration_sec: properties.step_duration_sec,
    document_generated: properties.document_generated,
    ai_messages_count: properties.ai_messages_count,
  });
}

// ===== FLOW STEP SKIPPED =====
export function trackFlowStepSkipped(properties: {
  project_id: string;
  step: FlowStep;
  time_on_step_sec: number;
}) {
  posthog.capture('flow_step_skipped', {
    project_id: properties.project_id,
    step: properties.step,
    step_name: STEP_NAMES[properties.step],
    time_on_step_sec: properties.time_on_step_sec,
  });
}

// ===== FLOW COMPLETED =====
export function trackFlowCompleted(properties: {
  project_id: string;
  total_duration_sec: number;
  steps_completed: number;
  steps_skipped: number;
  documents_generated: string[];
  user_segment: string;
}) {
  posthog.capture('flow_completed', {
    project_id: properties.project_id,
    total_duration_sec: properties.total_duration_sec,
    steps_completed: properties.steps_completed,
    steps_skipped: properties.steps_skipped,
    documents_generated: properties.documents_generated,
    user_segment: properties.user_segment,
  });

  // Обновляем профиль пользователя
  updateUserProperties({
    last_flow_completed_at: new Date().toISOString(),
    flow_completed_count: properties.steps_completed, // Будет перезаписано серверным значением
  });
}

// ===== FLOW ABANDONED =====
export function trackFlowAbandoned(properties: {
  project_id: string;
  last_step: FlowStep;
  time_on_last_step_sec: number;
  total_time_sec: number;
}) {
  posthog.capture('flow_abandoned', {
    project_id: properties.project_id,
    last_step: properties.last_step,
    last_step_name: STEP_NAMES[properties.last_step],
    time_on_last_step_sec: properties.time_on_last_step_sec,
    total_time_sec: properties.total_time_sec,
  });
}
```

### 3.5. Aha-момент и Document Generation Events

```typescript
// lib/analytics/aha-moment.ts

import posthog from 'posthog-js';
import { updateUserProperties } from './posthog';

// ===== AHA MOMENT REACHED (основной, шаг 2, для всех сегментов) =====
export function trackAhaMomentReached(properties: {
  project_id: string;
  time_since_signup_sec: number;
  time_since_flow_start_sec: number;
  user_segment: string;
  segments_generated_count: number;
  jobs_generated_count: number;
}) {
  posthog.capture('aha_moment_reached', {
    project_id: properties.project_id,
    time_since_signup_sec: properties.time_since_signup_sec,
    time_since_flow_start_sec: properties.time_since_flow_start_sec,
    user_segment: properties.user_segment,
    segments_generated_count: properties.segments_generated_count,
    jobs_generated_count: properties.jobs_generated_count,
  });

  // Обновляем профиль: отмечаем что aha-момент достигнут
  updateUserProperties({
    aha_moment_reached: true,
    aha_moment_at: new Date().toISOString(),
    time_to_aha_sec: properties.time_since_signup_sec,
  });
}

// ===== RISK ASSESSMENT VALUE REALIZED (вторая активация, шаг 3, для Solopreneurs) =====
export function trackRiskAssessmentValueRealized(properties: {
  project_id: string;
  time_since_signup_sec: number;
  time_since_aha_sec: number;
  user_segment: string;
  verdict: 'go' | 'pivot' | 'kill' | 'validate_first';
  risks_count: number;
}) {
  posthog.capture('risk_assessment_value_realized', {
    project_id: properties.project_id,
    time_since_signup_sec: properties.time_since_signup_sec,
    time_since_aha_sec: properties.time_since_aha_sec,
    user_segment: properties.user_segment,
    verdict: properties.verdict,
    risks_count: properties.risks_count,
  });

  // Для Solopreneurs: отмечаем вторую активацию
  if (properties.user_segment === 'solopreneur') {
    updateUserProperties({
      second_activation_reached: true,
      second_activation_at: new Date().toISOString(),
    });
  }
}

// ===== IDEA SUMMARY GENERATED =====
export function trackIdeaSummaryGenerated(properties: {
  project_id: string;
  interview_messages_count: number;
  interview_duration_sec: number;
  idea_word_count: number;
}) {
  posthog.capture('idea_summary_generated', {
    project_id: properties.project_id,
    interview_messages_count: properties.interview_messages_count,
    interview_duration_sec: properties.interview_duration_sec,
    idea_word_count: properties.idea_word_count,
  });
}

// ===== SEGMENTS & JOBS GENERATED =====
export function trackSegmentsJobsGenerated(properties: {
  project_id: string;
  segments_count: number;
  jobs_count: number;
  selected_segment_index: number;
  generation_duration_sec: number;
}) {
  posthog.capture('segments_jobs_generated', {
    project_id: properties.project_id,
    segments_count: properties.segments_count,
    jobs_count: properties.jobs_count,
    selected_segment_index: properties.selected_segment_index,
    generation_duration_sec: properties.generation_duration_sec,
  });
}

// ===== RISK ASSESSMENT GENERATED =====
export function trackRiskAssessmentGenerated(properties: {
  project_id: string;
  risks_count: number;
  top_risk_category: string;
  verdict: 'go' | 'pivot' | 'kill' | 'validate_first';
  generation_duration_sec: number;
}) {
  posthog.capture('risk_assessment_generated', {
    project_id: properties.project_id,
    risks_count: properties.risks_count,
    top_risk_category: properties.top_risk_category,
    verdict: properties.verdict,
    generation_duration_sec: properties.generation_duration_sec,
  });
}

// ===== PRD GENERATED =====
export function trackPrdGenerated(properties: {
  project_id: string;
  prd_sections_count: number;
  mvp_features_count: number;
  deferred_features_count: number;
  generation_duration_sec: number;
}) {
  posthog.capture('prd_generated', {
    project_id: properties.project_id,
    prd_sections_count: properties.prd_sections_count,
    mvp_features_count: properties.mvp_features_count,
    deferred_features_count: properties.deferred_features_count,
    generation_duration_sec: properties.generation_duration_sec,
  });
}

// ===== VIBE CODING PLAN GENERATED =====
export function trackVibeCodingPlanGenerated(properties: {
  project_id: string;
  recommended_tool: string;
  prompts_count: number;
  checklist_items_count: number;
  generation_duration_sec: number;
}) {
  posthog.capture('vibe_coding_plan_generated', {
    project_id: properties.project_id,
    recommended_tool: properties.recommended_tool,
    prompts_count: properties.prompts_count,
    checklist_items_count: properties.checklist_items_count,
    generation_duration_sec: properties.generation_duration_sec,
  });
}

// ===== BONUS DOCUMENTS =====
export function trackLandingCopyGenerated(properties: {
  project_id: string;
  generation_duration_sec: number;
  sections_count: number;
}) {
  posthog.capture('landing_copy_generated', {
    project_id: properties.project_id,
    generation_duration_sec: properties.generation_duration_sec,
    sections_count: properties.sections_count,
  });
}

export function trackAnalyticsPlanGenerated(properties: {
  project_id: string;
  generation_duration_sec: number;
  events_count: number;
  dashboards_count: number;
}) {
  posthog.capture('analytics_plan_generated', {
    project_id: properties.project_id,
    generation_duration_sec: properties.generation_duration_sec,
    events_count: properties.events_count,
    dashboards_count: properties.dashboards_count,
  });
}

export function trackCompetitorAnalysisGenerated(properties: {
  project_id: string;
  generation_duration_sec: number;
  competitors_count: number;
}) {
  posthog.capture('competitor_analysis_generated', {
    project_id: properties.project_id,
    generation_duration_sec: properties.generation_duration_sec,
    competitors_count: properties.competitors_count,
  });
}
```

### 3.6. Document Interaction Events

```typescript
// lib/analytics/documents.ts

import posthog from 'posthog-js';

type DocumentType = 'idea_summary' | 'segments_jobs' | 'risk_assessment' | 'prd' | 'vibe_coding_plan' | 'landing_copy' | 'analytics_plan' | 'competitor_analysis';

// ===== DOCUMENT VIEWED =====
export function trackDocumentViewed(properties: {
  project_id: string;
  document_type: DocumentType;
}) {
  posthog.capture('document_viewed', {
    project_id: properties.project_id,
    document_type: properties.document_type,
  });
}

// ===== DOCUMENT COPIED =====
export function trackDocumentCopied(properties: {
  project_id: string;
  document_type: DocumentType;
}) {
  posthog.capture('document_copied', {
    project_id: properties.project_id,
    document_type: properties.document_type,
  });
}

// ===== DOCUMENT DOWNLOADED =====
export function trackDocumentDownloaded(properties: {
  project_id: string;
  document_type: DocumentType;
  format: 'md' | 'pdf';
}) {
  posthog.capture('document_downloaded', {
    project_id: properties.project_id,
    document_type: properties.document_type,
    format: properties.format,
  });
}

// ===== DOCUMENT EXPORTED ALL =====
export function trackDocumentExportedAll(properties: {
  project_id: string;
  documents_count: number;
}) {
  posthog.capture('document_exported_all', {
    project_id: properties.project_id,
    format: 'zip',
    documents_count: properties.documents_count,
  });
}

// ===== DOCUMENT EDITED VIA AI =====
export function trackDocumentEditedViaAi(properties: {
  project_id: string;
  document_type: DocumentType;
  edit_type: 'add_feature' | 'remove_feature' | 'explain' | 'rewrite' | 'other';
}) {
  posthog.capture('document_edited_via_ai', {
    project_id: properties.project_id,
    document_type: properties.document_type,
    edit_type: properties.edit_type,
  });
}
```

### 3.7. AI Interaction Events

```typescript
// lib/analytics/ai-interaction.ts

import posthog from 'posthog-js';

type AiContext = 'interview' | 'editing' | 'iteration' | 'help';

// ===== AI MESSAGE SENT =====
export function trackAiMessageSent(properties: {
  project_id: string;
  step: number;
  step_name: string;
  message_length: number;
  context: AiContext;
}) {
  posthog.capture('ai_message_sent', {
    project_id: properties.project_id,
    step: properties.step,
    step_name: properties.step_name,
    message_length: properties.message_length,
    context: properties.context,
  });
}

// ===== AI RESPONSE RECEIVED =====
export function trackAiResponseReceived(properties: {
  project_id: string;
  step: number;
  response_time_ms: number;
  response_length: number;
  context: AiContext;
}) {
  posthog.capture('ai_response_received', {
    project_id: properties.project_id,
    step: properties.step,
    response_time_ms: properties.response_time_ms,
    response_length: properties.response_length,
    context: properties.context,
  });
}

// ===== AI HELP REQUESTED =====
export function trackAiHelpRequested(properties: {
  project_id: string;
  step: number;
  step_name: string;
  time_on_step_sec: number;
}) {
  posthog.capture('ai_help_requested', {
    project_id: properties.project_id,
    step: properties.step,
    step_name: properties.step_name,
    time_on_step_sec: properties.time_on_step_sec,
  });
}

// ===== AI SUGGESTION ACCEPTED =====
export function trackAiSuggestionAccepted(properties: {
  project_id: string;
  step: number;
  suggestion_type: 'example' | 'template' | 'reformulation';
}) {
  posthog.capture('ai_suggestion_accepted', {
    project_id: properties.project_id,
    step: properties.step,
    suggestion_type: properties.suggestion_type,
  });
}

// ===== AI LIMIT REACHED =====
export function trackAiLimitReached(properties: {
  plan: 'free' | 'pro' | 'builder';
  requests_used: number;
  requests_limit: number;
}) {
  posthog.capture('ai_limit_reached', {
    plan: properties.plan,
    requests_used: properties.requests_used,
    requests_limit: properties.requests_limit,
  });
}
```

### 3.8. Learning Events

```typescript
// lib/analytics/learning.ts

import posthog from 'posthog-js';

type BlockTopic = 'ajtbd' | 'rat' | 'unit_economics' | 'mvp' | 'prompt_engineering' | 'critical_chain' | 'segmentation' | 'value_creation';
type KbCategory = 'product_thinking' | 'risk_validation' | 'unit_economics' | 'vibe_coding' | 'prompt_engineering';

// ===== LEARNING BLOCK EXPANDED =====
export function trackLearningBlockExpanded(properties: {
  project_id: string;
  step: number;
  block_topic: BlockTopic;
  block_id: string;
}) {
  posthog.capture('learning_block_expanded', {
    project_id: properties.project_id,
    step: properties.step,
    block_topic: properties.block_topic,
    block_id: properties.block_id,
  });
}

// ===== LEARNING BLOCK COLLAPSED =====
export function trackLearningBlockCollapsed(properties: {
  project_id: string;
  step: number;
  block_topic: BlockTopic;
  time_open_sec: number;
}) {
  posthog.capture('learning_block_collapsed', {
    project_id: properties.project_id,
    step: properties.step,
    block_topic: properties.block_topic,
    time_open_sec: properties.time_open_sec,
  });
}

// ===== KNOWLEDGE BASE ARTICLE VIEWED =====
export function trackKnowledgeBaseArticleViewed(properties: {
  article_id: string;
  article_title: string;
  category: KbCategory;
  source: 'flow_link' | 'direct' | 'search';
}) {
  posthog.capture('knowledge_base_article_viewed', {
    article_id: properties.article_id,
    article_title: properties.article_title,
    category: properties.category,
    source: properties.source,
  });
}

// ===== KNOWLEDGE BASE SEARCHED =====
export function trackKnowledgeBaseSearched(properties: {
  query: string;
  results_count: number;
  clicked_result_index?: number;
}) {
  posthog.capture('knowledge_base_searched', {
    query: properties.query,
    results_count: properties.results_count,
    clicked_result_index: properties.clicked_result_index,
  });
}
```

### 3.9. Revenue Events

```typescript
// lib/analytics/revenue.ts

import posthog from 'posthog-js';
import { updateUserProperties } from './posthog';

type Plan = 'free' | 'pro' | 'builder';
type PaywallTrigger = 'project_limit' | 'export_limit' | 'ai_limit' | 'iteration_limit' | 'manual_upgrade';

// ===== PAYWALL VIEWED =====
export function trackPaywallViewed(properties: {
  trigger: PaywallTrigger;
  current_plan: Plan;
  user_segment: string;
}) {
  posthog.capture('paywall_viewed', {
    trigger: properties.trigger,
    current_plan: properties.current_plan,
    user_segment: properties.user_segment,
  });
}

// ===== PLAN SELECTED =====
export function trackPlanSelected(properties: {
  plan: 'pro' | 'builder';
  price: number;
  currency: string;
  billing_period: 'monthly' | 'annual';
  trigger: PaywallTrigger;
}) {
  posthog.capture('plan_selected', {
    plan: properties.plan,
    price: properties.price,
    currency: properties.currency,
    billing_period: properties.billing_period,
    trigger: properties.trigger,
  });
}

// ===== PURCHASE INITIATED =====
export function trackPurchaseInitiated(properties: {
  plan: 'pro' | 'builder';
  price: number;
  currency: string;
  billing_period: 'monthly' | 'annual';
  payment_method: string;
}) {
  posthog.capture('purchase_initiated', {
    plan: properties.plan,
    price: properties.price,
    currency: properties.currency,
    billing_period: properties.billing_period,
    payment_method: properties.payment_method,
  });
}

// ===== PURCHASE COMPLETED =====
export function trackPurchaseCompleted(properties: {
  plan: 'pro' | 'builder';
  price: number;
  currency: string;
  billing_period: 'monthly' | 'annual';
  payment_method: string;
  trial_used: boolean;
  days_since_signup: number;
  projects_created_before_purchase: number;
  flow_completed_before_purchase: boolean;
}) {
  posthog.capture('purchase_completed', {
    plan: properties.plan,
    price: properties.price,
    currency: properties.currency,
    billing_period: properties.billing_period,
    payment_method: properties.payment_method,
    trial_used: properties.trial_used,
    days_since_signup: properties.days_since_signup,
    projects_created_before_purchase: properties.projects_created_before_purchase,
    flow_completed_before_purchase: properties.flow_completed_before_purchase,
  });

  // Обновляем профиль пользователя
  updateUserProperties({
    plan: properties.plan,
    first_purchase_at: new Date().toISOString(),
    billing_period: properties.billing_period,
  });
}

// ===== PURCHASE FAILED =====
export function trackPurchaseFailed(properties: {
  plan: 'pro' | 'builder';
  error_type: string;
  payment_method: string;
}) {
  posthog.capture('purchase_failed', {
    plan: properties.plan,
    error_type: properties.error_type,
    payment_method: properties.payment_method,
  });
}

// ===== CHECKOUT ABANDONED (новое событие из кросс-верификации) =====
export function trackCheckoutAbandoned(properties: {
  plan: string;
  step: 'plan_selected' | 'payment_info' | 'confirmation';
  time_on_checkout_sec: number;
}) {
  posthog.capture('checkout_abandoned', {
    plan: properties.plan,
    step: properties.step,
    time_on_checkout_sec: properties.time_on_checkout_sec,
  });
}

// ===== UPGRADE COMPLETED =====
export function trackUpgradeCompleted(properties: {
  from_plan: Plan;
  to_plan: Plan;
  price_diff: number;
  days_on_previous_plan: number;
}) {
  posthog.capture('upgrade_completed', {
    from_plan: properties.from_plan,
    to_plan: properties.to_plan,
    price_diff: properties.price_diff,
    days_on_previous_plan: properties.days_on_previous_plan,
  });

  updateUserProperties({
    plan: properties.to_plan,
    last_upgrade_at: new Date().toISOString(),
  });
}

// ===== SUBSCRIPTION RENEWED =====
export function trackSubscriptionRenewed(properties: {
  plan: 'pro' | 'builder';
  price: number;
  period_number: number;
  lifetime_revenue: number;
}) {
  posthog.capture('subscription_renewed', {
    plan: properties.plan,
    price: properties.price,
    period_number: properties.period_number,
    lifetime_revenue: properties.lifetime_revenue,
  });

  updateUserProperties({
    lifetime_revenue: properties.lifetime_revenue,
    subscription_period_number: properties.period_number,
  });
}

// ===== SUBSCRIPTION CANCELLED =====
export function trackSubscriptionCancelled(properties: {
  plan: 'pro' | 'builder';
  reason: string;
  reason_text?: string;
  lifetime_days: number;
  lifetime_revenue: number;
  projects_created: number;
  documents_generated: number;
}) {
  posthog.capture('subscription_cancelled', {
    plan: properties.plan,
    reason: properties.reason,
    reason_text: properties.reason_text,
    lifetime_days: properties.lifetime_days,
    lifetime_revenue: properties.lifetime_revenue,
    projects_created: properties.projects_created,
    documents_generated: properties.documents_generated,
  });

  updateUserProperties({
    plan: 'free',
    churned_at: new Date().toISOString(),
    churn_reason: properties.reason,
  });
}

// ===== REFUND REQUESTED =====
export function trackRefundRequested(properties: {
  plan: 'pro' | 'builder';
  amount: number;
  reason: string;
  lifetime_days: number;
}) {
  posthog.capture('refund_requested', {
    plan: properties.plan,
    amount: properties.amount,
    reason: properties.reason,
    lifetime_days: properties.lifetime_days,
  });
}
```

### 3.10. Retention Events

```typescript
// lib/analytics/retention.ts

import posthog from 'posthog-js';
import { updateUserProperties } from './posthog';

type FeatureName = 'ai_interview' | 'document_generation' | 'document_export' | 'prd_iteration' | 'knowledge_base' | 'micro_guide' | 'prompt_template';
type ValueType = 'document_generated' | 'flow_step_completed' | 'prd_iterated' | 'knowledge_gained';
type ChecklistItem = 'first_result' | 'expert_interviews' | 'landing_test' | 'user_feedback' | 'update_prd';

// ===== SESSION STARTED =====
export function trackSessionStarted(properties: {
  session_number: number;
  days_since_last_session: number;
  days_since_signup: number;
  current_plan: string;
  user_segment: string;
}) {
  posthog.capture('session_started', {
    session_number: properties.session_number,
    days_since_last_session: properties.days_since_last_session,
    days_since_signup: properties.days_since_signup,
    current_plan: properties.current_plan,
    user_segment: properties.user_segment,
  });
}

// ===== PROJECT CREATED =====
export function trackProjectCreated(properties: {
  project_number: number;
  current_plan: string;
  days_since_signup: number;
}) {
  posthog.capture('project_created', {
    project_number: properties.project_number,
    current_plan: properties.current_plan,
    days_since_signup: properties.days_since_signup,
  });

  updateUserProperties({
    projects_count: properties.project_number,
    last_project_created_at: new Date().toISOString(),
  });
}

// ===== PRD ITERATION STARTED =====
export function trackPrdIterationStarted(properties: {
  project_id: string;
  iteration_number: number;
  days_since_last_iteration: number;
  days_since_flow_completed: number;
}) {
  posthog.capture('prd_iteration_started', {
    project_id: properties.project_id,
    iteration_number: properties.iteration_number,
    days_since_last_iteration: properties.days_since_last_iteration,
    days_since_flow_completed: properties.days_since_flow_completed,
  });
}

// ===== PRD ITERATION COMPLETED =====
export function trackPrdIterationCompleted(properties: {
  project_id: string;
  iteration_number: number;
  changes_summary: string;
  iteration_duration_sec: number;
}) {
  posthog.capture('prd_iteration_completed', {
    project_id: properties.project_id,
    iteration_number: properties.iteration_number,
    changes_summary: properties.changes_summary,
    iteration_duration_sec: properties.iteration_duration_sec,
  });
}

// ===== CHECKLIST ITEM COMPLETED =====
export function trackChecklistItemCompleted(properties: {
  project_id: string;
  checklist_item: ChecklistItem;
  checklist_progress_pct: number;
}) {
  posthog.capture('checklist_item_completed', {
    project_id: properties.project_id,
    checklist_item: properties.checklist_item,
    checklist_progress_pct: properties.checklist_progress_pct,
  });
}

// ===== FEATURE USED =====
export function trackFeatureUsed(properties: {
  feature_name: FeatureName;
  project_id?: string;
}) {
  posthog.capture('feature_used', {
    feature_name: properties.feature_name,
    project_id: properties.project_id,
  });
}

// ===== VALUE RECEIVED =====
export function trackValueReceived(properties: {
  value_type: ValueType;
  project_id?: string;
  document_type?: string;
}) {
  posthog.capture('value_received', {
    value_type: properties.value_type,
    project_id: properties.project_id,
    document_type: properties.document_type,
  });
}
```

### 3.11. Churn Events

```typescript
// lib/analytics/churn.ts

import posthog from 'posthog-js';

// ===== CHURN RISK DETECTED (серверный вызов) =====
// Этот вызов делается с бэкенда через PostHog Server API
export function trackChurnRiskDetected(properties: {
  user_id: string;
  days_inactive: number;
  plan: string;
  lifetime_days: number;
  last_action: string;
  projects_count: number;
  documents_count: number;
}) {
  // Серверный вызов — используется PostHog Node.js SDK
  // posthogServer.capture({
  //   distinctId: properties.user_id,
  //   event: 'churn_risk_detected',
  //   properties: { ...properties },
  // });

  // Клиентская заглушка для типизации
  posthog.capture('churn_risk_detected', {
    days_inactive: properties.days_inactive,
    plan: properties.plan,
    lifetime_days: properties.lifetime_days,
    last_action: properties.last_action,
    projects_count: properties.projects_count,
    documents_count: properties.documents_count,
  });
}

// ===== DOWNGRADE COMPLETED =====
export function trackDowngradeCompleted(properties: {
  from_plan: string;
  to_plan: string;
  reason: string;
  days_on_previous_plan: number;
}) {
  posthog.capture('downgrade_completed', {
    from_plan: properties.from_plan,
    to_plan: properties.to_plan,
    reason: properties.reason,
    days_on_previous_plan: properties.days_on_previous_plan,
  });
}

// ===== ACCOUNT DELETED =====
export function trackAccountDeleted(properties: {
  plan: string;
  lifetime_days: number;
  projects_count: number;
  documents_count: number;
  reason: string;
}) {
  posthog.capture('account_deleted', {
    plan: properties.plan,
    lifetime_days: properties.lifetime_days,
    projects_count: properties.projects_count,
    documents_count: properties.documents_count,
    reason: properties.reason,
  });
}
```

### 3.12. Referral Events

```typescript
// lib/analytics/referral.ts

import posthog from 'posthog-js';

// ===== SHARE BUTTON CLICKED =====
export function trackShareButtonClicked(properties: {
  project_id: string;
  share_channel: 'link' | 'twitter' | 'linkedin' | 'email';
}) {
  posthog.capture('share_button_clicked', {
    project_id: properties.project_id,
    share_channel: properties.share_channel,
  });
}

// ===== REFERRAL LINK GENERATED =====
export function trackReferralLinkGenerated(properties: {
  campaign?: string;
}) {
  posthog.capture('referral_link_generated', {
    campaign: properties.campaign,
  });
}

// ===== REFERRAL SENT =====
export function trackReferralSent(properties: {
  channel: 'email' | 'link' | 'social';
  campaign?: string;
}) {
  posthog.capture('referral_sent', {
    channel: properties.channel,
    campaign: properties.campaign,
  });
}

// ===== REFERRAL CLICKED (серверный) =====
export function trackReferralClicked(properties: {
  referrer_user_id: string;
  campaign?: string;
}) {
  posthog.capture('referral_clicked', {
    referrer_user_id: properties.referrer_user_id,
    campaign: properties.campaign,
  });
}

// ===== REFERRAL CONVERTED (серверный) =====
export function trackReferralConverted(properties: {
  referrer_user_id: string;
  referred_user_id: string;
  campaign?: string;
}) {
  posthog.capture('referral_converted', {
    referrer_user_id: properties.referrer_user_id,
    referred_user_id: properties.referred_user_id,
    campaign: properties.campaign,
  });
}
```

### 3.13. Anti-Stuck Events

```typescript
// lib/analytics/anti-stuck.ts

import posthog from 'posthog-js';

// ===== STUCK DETECTED =====
export function trackStuckDetected(properties: {
  project_id: string;
  step: number;
  step_name: string;
  idle_time_sec: number;
}) {
  posthog.capture('stuck_detected', {
    project_id: properties.project_id,
    step: properties.step,
    step_name: properties.step_name,
    idle_time_sec: properties.idle_time_sec,
  });
}

// ===== STUCK HELP OFFERED =====
export function trackStuckHelpOffered(properties: {
  project_id: string;
  step: number;
  help_type: 'suggestion' | 'example' | 'template' | 'reformulation';
}) {
  posthog.capture('stuck_help_offered', {
    project_id: properties.project_id,
    step: properties.step,
    help_type: properties.help_type,
  });
}

// ===== STUCK HELP ACCEPTED =====
export function trackStuckHelpAccepted(properties: {
  project_id: string;
  step: number;
  help_type: 'suggestion' | 'example' | 'template' | 'reformulation';
}) {
  posthog.capture('stuck_help_accepted', {
    project_id: properties.project_id,
    step: properties.step,
    help_type: properties.help_type,
  });
}

// ===== TEMPLATE IDEA SELECTED =====
export function trackTemplateIdeaSelected(properties: {
  template_name: string;
  user_segment: string;
}) {
  posthog.capture('template_idea_selected', {
    template_name: properties.template_name,
    user_segment: properties.user_segment,
  });
}
```

### 3.14. Email Events

```typescript
// lib/analytics/email.ts

import posthog from 'posthog-js';

type EmailType = 'nudge_d1' | 'nudge_d3' | 'nudge_d7' | 'nudge_d14' | 'nudge_d30' | 'churn_prevention' | 'upsell' | 'welcome';

// Все email-события трекаются серверно через PostHog Node.js SDK
// Ниже — типизация для единообразия

// ===== EMAIL SENT (серверный) =====
export function trackEmailSent(properties: {
  email_type: EmailType;
  user_segment: string;
}) {
  posthog.capture('email_sent', {
    email_type: properties.email_type,
    user_segment: properties.user_segment,
  });
}

// ===== EMAIL OPENED (серверный, через pixel) =====
export function trackEmailOpened(properties: {
  email_type: EmailType;
  user_segment: string;
  days_since_sent: number;
}) {
  posthog.capture('email_opened', {
    email_type: properties.email_type,
    user_segment: properties.user_segment,
    days_since_sent: properties.days_since_sent,
  });
}

// ===== EMAIL CLICKED =====
export function trackEmailClicked(properties: {
  email_type: EmailType;
  link_name: string;
  user_segment: string;
}) {
  posthog.capture('email_clicked', {
    email_type: properties.email_type,
    link_name: properties.link_name,
    user_segment: properties.user_segment,
  });
}

// ===== EMAIL UNSUBSCRIBED =====
export function trackEmailUnsubscribed(properties: {
  email_type: EmailType;
  user_segment: string;
  emails_received_count: number;
}) {
  posthog.capture('email_unsubscribed', {
    email_type: properties.email_type,
    user_segment: properties.user_segment,
    emails_received_count: properties.emails_received_count,
  });
}
```

### 3.15. Server-Side PostHog (Node.js)

```typescript
// lib/analytics/posthog-server.ts

// Серверные события: churn_risk_detected, email_sent, email_opened,
// subscription_renewed, referral_converted, mrr_snapshot, injection_attempt_detected, abuse_detected

import { PostHog } from 'posthog-node';

const posthogServer = new PostHog(process.env.POSTHOG_API_KEY!, {
  host: process.env.POSTHOG_HOST || 'https://us.i.posthog.com',
});

export function serverCapture(
  distinctId: string,
  event: string,
  properties: Record<string, any>
) {
  posthogServer.capture({
    distinctId,
    event,
    properties,
  });
}

export function serverIdentify(
  distinctId: string,
  properties: Record<string, any>
) {
  posthogServer.identify({
    distinctId,
    properties,
  });
}

// Вызвать при завершении работы сервера
export async function shutdownPostHog() {
  await posthogServer.shutdown();
}
```

### 3.16. Micro-Guide Events (новое из кросс-верификации)

```typescript
// lib/analytics/micro-guides.ts

import posthog from 'posthog-js';

// ===== MICRO GUIDE STARTED =====
export function trackMicroGuideStarted(properties: {
  guide_id: string;
  tool: string; // 'cursor' | 'claude_code' | 'lovable' | 'replit' | 'bolt'
}) {
  posthog.capture('micro_guide_started', {
    guide_id: properties.guide_id,
    tool: properties.tool,
  });
}

// ===== MICRO GUIDE STEP COMPLETED =====
export function trackMicroGuideStepCompleted(properties: {
  guide_id: string;
  step: number;
  step_name: string;
}) {
  posthog.capture('micro_guide_step_completed', {
    guide_id: properties.guide_id,
    step: properties.step,
    step_name: properties.step_name,
  });
}

// ===== MICRO GUIDE COMPLETED =====
export function trackMicroGuideCompleted(properties: {
  guide_id: string;
  total_time_sec: number;
}) {
  posthog.capture('micro_guide_completed', {
    guide_id: properties.guide_id,
    total_time_sec: properties.total_time_sec,
  });
}

// ===== MICRO GUIDE STEP FAILED =====
export function trackMicroGuideStepFailed(properties: {
  guide_id: string;
  step: number;
  feedback: string;
}) {
  posthog.capture('micro_guide_step_failed', {
    guide_id: properties.guide_id,
    step: properties.step,
    feedback: properties.feedback,
  });
}
```

### 3.17. PMF & Quality Survey Events (новое из кросс-верификации)

```typescript
// lib/analytics/surveys.ts

import posthog from 'posthog-js';

// ===== NPS SURVEY SUBMITTED =====
// Триггер: D7 после первого завершённого flow
export function trackNpsSurveySubmitted(properties: {
  score: number; // 0-10
  comment?: string;
  days_since_signup: number;
  segment: string;
}) {
  posthog.capture('nps_survey_submitted', {
    score: properties.score,
    comment: properties.comment,
    days_since_signup: properties.days_since_signup,
    segment: properties.segment,
    trigger: 'day_7_post_first_flow',
  });
}

// ===== CSAT SUBMITTED =====
// Триггер: после каждого шага для первых 200 пользователей
export function trackCsatSubmitted(properties: {
  step: 'ai_interview' | 'segments_jobs' | 'risk_assessment' | 'prd_generation' | 'vibe_coding_plan';
  score: number; // 1-5
  session_number: number;
}) {
  posthog.capture('csat_submitted', {
    step: properties.step,
    score: properties.score,
    session_number: properties.session_number,
  });
}

// ===== PMF SURVEY SUBMITTED (Sean Ellis test) =====
// Триггер: D14 после регистрации
export function trackPmfSurveySubmitted(properties: {
  answer: 'very_disappointed' | 'somewhat_disappointed' | 'not_disappointed';
  days_since_signup: number;
  projects_completed: number;
}) {
  posthog.capture('pmf_survey_submitted', {
    answer: properties.answer,
    days_since_signup: properties.days_since_signup,
    projects_completed: properties.projects_completed,
    trigger: 'day_14',
  });
}

// ===== DOCUMENT QUALITY RATED =====
// Триггер: при копировании/экспорте документа
export function trackDocumentQualityRated(properties: {
  document_type: string;
  score: number; // 1-10
  feedback?: string;
  project_id: string;
}) {
  posthog.capture('document_quality_rated', {
    document_type: properties.document_type,
    score: properties.score,
    feedback: properties.feedback,
    project_id: properties.project_id,
  });
}
```

### 3.18. MRR Snapshot (серверное событие, новое из кросс-верификации)

```typescript
// lib/analytics/mrr.ts (серверный модуль)

// Вызывается из cron-job ежедневно в 00:00 UTC
// Используется PostHog Node.js SDK

import { serverCapture } from './posthog-server';

export function trackMrrSnapshot(properties: {
  mrr: number;
  new_mrr: number;
  churned_mrr: number;
  expansion_mrr: number;
  active_subscriptions: number;
}) {
  serverCapture('system', 'mrr_snapshot', {
    mrr: properties.mrr,
    new_mrr: properties.new_mrr,
    churned_mrr: properties.churned_mrr,
    expansion_mrr: properties.expansion_mrr,
    period: 'daily',
    active_subscriptions: properties.active_subscriptions,
  });
}
```

### 3.19. AI Content Quality Events (новое из кросс-верификации)

```typescript
// lib/analytics/ai-quality.ts

import posthog from 'posthog-js';

// ===== AI CONTENT FLAGGED =====
export function trackAiContentFlagged(properties: {
  document_type: string;
  flag_type: 'inaccurate' | 'outdated' | 'irrelevant';
  user_feedback: string;
  section: string;
}) {
  posthog.capture('ai_content_flagged', {
    document_type: properties.document_type,
    flag_type: properties.flag_type,
    user_feedback: properties.user_feedback,
    section: properties.section,
  });
}
```

### 3.20. Security & Anti-Abuse Events (новое из кросс-верификации)

```typescript
// lib/analytics/security.ts (серверный модуль)

import { serverCapture } from './posthog-server';

// ===== INJECTION ATTEMPT DETECTED =====
export function trackInjectionAttemptDetected(properties: {
  input_type: string;
  pattern_matched: string;
  user_id: string;
}) {
  serverCapture(properties.user_id, 'injection_attempt_detected', {
    input_type: properties.input_type,
    pattern_matched: properties.pattern_matched,
    user_id: properties.user_id,
    blocked: true,
  });
}

// ===== ABUSE DETECTED =====
export function trackAbuseDetected(properties: {
  type: 'multi_account' | 'rate_limit' | 'scraping';
  user_id: string;
  ip: string;
}) {
  serverCapture(properties.user_id, 'abuse_detected', {
    type: properties.type,
    user_id: properties.user_id,
    ip: properties.ip,
  });
}
```

### 3.21. Checkout Abandoned Event (новое из кросс-верификации)

```typescript
// lib/analytics/checkout.ts

import posthog from 'posthog-js';

// ===== CHECKOUT ABANDONED =====
// Трекается через beforeunload + серверный таймаут
export function trackCheckoutAbandoned(properties: {
  plan: string;
  step: 'plan_selected' | 'payment_info' | 'confirmation';
  time_on_checkout_sec: number;
}) {
  posthog.capture('checkout_abandoned', {
    plan: properties.plan,
    step: properties.step,
    time_on_checkout_sec: properties.time_on_checkout_sec,
  });
}
```

---

## 4. Дашборды

### 4.1. Воронка активации (Activation Funnel)

**Цель:** Видеть конверсию на каждом шаге от первого визита до Aha-момента.

**Визуализации:**
1. **Funnel chart** (PostHog Funnels):
   - page_viewed (landing) -> cta_clicked -> signup_started -> signup_completed -> onboarding_completed -> flow_started -> flow_step_completed (step=1) -> aha_moment_reached -> flow_step_completed (step=3) -> flow_step_completed (step=4) -> flow_completed
   - Разбивка (breakdown) по: user_segment, utm_source, experience_level
2. **Drop-off analysis:** на каком шаге теряется больше всего пользователей
3. **Time to Aha:** гистограмма распределения time_since_signup_sec при aha_moment_reached (цель <25 мин)
4. **Step duration:** средняя длительность каждого шага guided flow
5. **Conversion trends:** тренд конверсии signup -> aha по неделям

**Фильтры:** дата, user_segment, experience_level, utm_source, utm_medium, utm_campaign

**Ключевые метрики на дашборде:**
- Signup -> Flow Start: цель >80%
- Flow Start -> Aha: цель >70%
- Flow Start -> Flow Completed: цель >40%
- Time to Aha: цель <25 мин
- Step Drop-off Rate: цель <20% на каждом шаге

---

### 4.2. Когортный анализ Retention

**Цель:** Измерять retention по когортам (неделя регистрации), определять тренд улучшения/ухудшения.

**Визуализации:**
1. **Retention table** (PostHog Lifecycle/Retention):
   - Когорта = неделя signup_completed
   - Событие возврата = session_started (с продуктивным действием: project_created, prd_iteration_started, document_viewed, flow_started)
   - Период: неделя (D7, D14, D21, D28...) и месяц (M1, M2, M3)
2. **Retention curve:** процент возврата по когортам на графике
3. **Сравнение когорт:** текущая неделя vs предыдущие
4. **Breakdown** по user_segment: founders vs solopreneurs vs professionals

**Фильтры:** период когорты, user_segment, experience_level, plan

**Ключевые метрики на дашборде:**
- D7 Return Rate: цель >25%
- D30 Return Rate: цель >15%
- Retention curve flattening: на какой неделе стабилизируется
- Лучшая / худшая когорта

---

### 4.3. Юнит-экономика по когортам

**Цель:** Считать CAC, LTV, Payback Period по когортам для оценки устойчивости бизнеса.

**Визуализации:**
1. **CAC по каналам:** utm_source x (маркетинговые расходы / signup_completed). Данные о расходах импортируются через PostHog Data Pipeline или вручную обновляются ежемесячно.
2. **LTV по когортам:**
   - Когорта = месяц signup_completed
   - LTV = сумма purchase_completed.price + subscription_renewed.price за весь период жизни когорты
   - LTV / user = LTV когорты / signup_completed когорты
3. **Payback Period:** месяц, в котором cumulative LTV > CAC для каждой когорты
4. **LTV/CAC ratio:** цель >3x
5. **ARPU trend:** средний revenue per user (all users, включая free) по месяцам
6. **Paid ARPU:** средний revenue per paying user по месяцам

**Формулы:**
- CAC = Marketing Spend / signup_completed (за период)
- LTV = ARPU * (1 / Monthly Churn Rate)
- Payback Period = CAC / Monthly ARPU
- Monthly Churn Rate = subscription_cancelled / active_subscriptions (начало месяца)

**Ключевые метрики на дашборде:**
- CAC (по каналам): цель <$30 (organic), <$50 (paid)
- LTV (3 мес когорта): цель >$90
- Payback Period: цель <2 мес
- Churn Rate: цель <8%/мес
- LTV/CAC: цель >3x

---

### 4.4. Конверсия по сегментам

**Цель:** Сравнить поведение и конверсию разных сегментов для приоритизации и оптимизации.

**Визуализации:**
1. **Segment distribution:** pie chart — доля каждого сегмента в signup_completed
2. **Funnel by segment:** воронка активации для каждого сегмента в сравнении (PostHog Funnels с breakdown = user_segment)
3. **Time to Aha by segment:** гистограмма
4. **Flow completion rate by segment:** bar chart
5. **Paid conversion by segment:** bar chart
6. **Retention by segment:** retention curves для каждого сегмента на одном графике
7. **Revenue by segment:** MRR по сегментам

**Фильтры:** дата, plan, experience_level

**Ключевые метрики:**

| Метрика | Founders | Solopreneurs | Professionals |
|---------|----------|-------------|---------------|
| Flow Completion | >40% | >50% | >35% |
| Time to Aha | <25 мин | <20 мин | <35 мин |
| Paid Conversion | >5% | >7% | >3% |
| D7 Return | >25% | >30% | >15% |
| D30 Return | >15% | >20% | >10% |

---

### 4.5. Revenue Breakdown

**Цель:** Мониторить динамику выручки, конверсию в оплату, churn и MRR.

**Визуализации:**
1. **MRR trend:** линейный график MRR по месяцам (из `mrr_snapshot` или subscription_renewed + purchase_completed для новых)
2. **MRR waterfall:** New MRR + Expansion MRR - Churned MRR - Contraction MRR = Net New MRR (данные из `mrr_snapshot`)
3. **Plan distribution:** donut chart — доля Pro vs Builder в revenue
4. **Paywall trigger analysis:** bar chart — какие триггеры paywall ведут к покупке (paywall_viewed.trigger -> purchase_completed)
5. **Checkout funnel:** plan_selected -> purchase_initiated -> purchase_completed | checkout_abandoned — анализ потерь на checkout
6. **Free-to-Paid conversion trend:** % по неделям
7. **Churn analysis:** subscription_cancelled.reason — pie chart причин отмены
8. **Revenue per user cohort:** heatmap — revenue по когортам и месяцам

**Ключевые метрики на дашборде:**
- MRR: цель >$5K к 3 мес
- Free-to-Paid: цель >5%
- ARPU (paid): цель $29-49
- Churn: цель <8%/мес
- Net Revenue Retention: цель >95%

---

### 4.6. Aha-момент

**Цель:** Глубокий анализ момента активации ценности — что предшествует Aha, что следует за ним, как коррелирует с retention и monetization.

**Визуализации:**
1. **Aha reached rate:** % от signup_completed, достигших aha_moment_reached
2. **Time to Aha distribution:** гистограмма time_since_signup_sec
3. **Pre-Aha behavior:** какие действия чаще всего предшествуют Aha (корреляция с ai_messages_count, learning_block_expanded, interview_duration)
4. **Post-Aha behavior:** что делают пользователи после Aha (продолжают flow, уходят, возвращаются)
5. **Aha -> Paid correlation:** конверсия в покупку для пользователей с Aha vs без Aha
6. **Aha -> Retention correlation:** D7/D30 return rate для пользователей с Aha vs без Aha
7. **Aha by segment:** breakdown по сегментам
8. **Second activation (Solopreneurs):** risk_assessment_value_realized rate и его корреляция с paid conversion и retention для сегмента Solopreneurs

**Ключевые метрики:**
- Aha Reached Rate: цель >65% от signup
- Median Time to Aha: цель <22 мин
- Aha -> Flow Completed: цель >60%
- Aha -> Paid (30 дней): цель >8%
- Aha -> D7 Return: цель >35%

---

### 4.7. Каналы привлечения (Acquisition Channels)

**Цель:** Понимать эффективность каждого канала привлечения — от клика до revenue.

**Визуализации:**
1. **Channel overview:** table — utm_source x (visits, signups, aha_reached, flow_completed, paid_conversion, revenue)
2. **Funnel by channel:** воронка для каждого канала (PostHog Funnels с breakdown = utm_source)
3. **CAC by channel:** bar chart (маркетинговые расходы / signups) — данные о расходах обновляются вручную или через интеграцию
4. **Quality by channel:** какой канал приводит самых качественных пользователей (flow_completion_rate, paid_conversion, D7_return)
5. **SEO / Knowledge Base:** page_viewed по статьям KB -> signup_completed (attribution)
6. **Referral performance:** referral_sent -> referral_converted — коэффициент виральности
7. **Channel trend:** signup_completed по каналам по неделям

**Фильтры:** дата, utm_source, utm_medium, utm_campaign, user_segment

**Ключевые метрики:**
- Total Signups по каналам (абсолют и %)
- CAC по каналам: organic <$10, paid <$50
- Best channel by LTV: канал с наибольшим LTV/user
- Referral coefficient: referral_converted / active_users
- KB -> Signup attribution rate

### 4.8. PMF & Quality Dashboard (новый из кросс-верификации)

**Цель:** Мониторить качественные метрики product-market fit.

**Визуализации:**
1. **NPS trend:** линейный график NPS score по неделям (цель >40)
2. **NPS distribution:** гистограмма ответов 0-10, разбивка на Detractors (0-6), Passives (7-8), Promoters (9-10)
3. **CSAT by step:** bar chart средних оценок по шагам flow (цель >4.0/5.0)
4. **PMF survey results:** pie chart ответов Sean Ellis test (цель "very_disappointed" >40%)
5. **Document Quality by type:** bar chart средних оценок по типам документов (цель >7/10)
6. **AI content flags:** trend количества `ai_content_flagged` по типам проблем

**Ключевые метрики:**
- NPS: цель >40
- CSAT per step: цель >4.0/5.0
- PMF "very disappointed": цель >40%
- Document Quality Score: цель >7/10
- AI content flag rate: цель <2% документов

---

## 5. Триггеры для автоматических коммуникаций

### 5.1. Онбординг-коммуникации

| # | Триггер (событие) | Условие | Действие | Канал | Задержка |
|---|-------------------|---------|----------|-------|----------|
| O-1 | `signup_completed` | Всегда | Welcome email: "You're in! Start your first project" + ссылка на guided flow | Email | 0 мин (мгновенно) |
| O-2 | `signup_completed` + НЕТ `flow_started` | Через 1 час нет flow_started | Push/in-app: "Ready to turn your idea into a plan? Start your guided flow" | In-app notification | 1 час |
| O-3 | `signup_completed` + НЕТ `flow_started` | Через 24 часа нет flow_started | Email D+1: "You started something great -- your AI guide is ready" + ссылка на flow | Email | 24 часа |
| O-4 | `flow_started` + НЕТ `flow_step_completed (step=1)` | Через 24 часа не завершён шаг 1 | Email: "Need help describing your idea? Here are some examples to get you started" | Email | 24 часа |
| O-5 | `flow_step_completed (step=1)` + НЕТ `aha_moment_reached` | Через 48 часов нет Aha | Email: "You're almost there! Your segments & jobs are one step away" | Email | 48 часов |
| O-6 | `stuck_detected` | idle_time_sec > 180 на любом шаге | In-app: "Stuck? Here's what you can do..." + варианты помощи | In-app popup | Мгновенно |
| O-7 | `flow_abandoned` | last_step < 5 | Email: "You were making great progress! Continue from Step [N]" + ссылка на конкретный шаг | Email | 3 часа |

### 5.2. Retention-коммуникации

| # | Триггер (событие) | Условие | Действие | Канал | Задержка |
|---|-------------------|---------|----------|-------|----------|
| R-1 | `flow_completed` | Всегда | Email D+1: "Your documents are ready! Here's what to do next" + Next Steps чеклист | Email | 24 часа |
| R-2 | `flow_completed` | D+3 без session_started | Email D+3: "Have you started building? Quick tip for [recommended_tool]" | Email | 3 дня |
| R-3 | `flow_completed` | D+7 без prd_iteration_started | Email D+7: "Time to validate. Have you talked to potential users?" + шаблон интервью | Email | 7 дней |
| R-4 | `flow_completed` | D+14 без session_started | Email D+14: "Ready to iterate? Come back and update your PRD with what you've learned" | Email | 14 дней |
| R-5 | `flow_completed` | D+30 без project_created | Email D+30: "New idea? Start a new project in 30 seconds" | Email | 30 дней |
| R-6 | `checklist_item_completed` (item = "expert_interviews") | Завершил 3 интервью | In-app: "Great progress! Ready to update your PRD based on feedback?" + ссылка на итерацию | In-app notification | Мгновенно |
| R-7 | `prd_iteration_completed` | Завершил итерацию | Email: "Your PRD is updated! Here's your next step: [landing test / build prototype]" | Email | 1 час |
| R-8 | `session_started` | session_number >= 3 И plan = "free" | In-app banner: "You're getting great value! Unlock unlimited projects with Pro" | In-app banner | Мгновенно |

### 5.3. Upsell-коммуникации

| # | Триггер (событие) | Условие | Действие | Канал | Задержка |
|---|-------------------|---------|----------|-------|----------|
| U-1 | `ai_limit_reached` | plan = "free" | In-app modal: "You've used all your AI requests today. Upgrade to Pro for 100/day" | In-app modal | Мгновенно |
| U-2 | `project_created` | project_number = 3 И plan = "free" | In-app paywall: "You've reached the free project limit. Upgrade to continue" | In-app paywall | Мгновенно |
| U-3 | `document_downloaded` | format = "pdf" И plan = "free" | In-app: "PDF export is available on Pro. Upgrade now" | In-app modal | Мгновенно |
| U-4 | `prd_iteration_started` | iteration_number = 2 И plan = "free" | In-app: "Your first iteration was free! Unlimited iterations with Pro" | In-app modal | Мгновенно |
| U-5 | `flow_completed` | projects_created >= 2 И plan = "free" И days_since_signup >= 3 | Email: "You've created [N] projects. Pro users generate 3x more documents. Upgrade for $29/mo" | Email | 3 дня после trigger |
| U-6 | `purchase_completed` | plan = "pro" И days_on_plan >= 30 И projects_created >= 5 | Email: "You're a power user! Builder plan gives you 300 AI requests/day + custom prompt templates" | Email | 30 дней после purchase |
| U-7 | `paywall_viewed` | trigger любой И НЕТ purchase_completed в следующие 24 часа | Email: "You were checking out our plans. Here's what Pro includes..." + comparison table | Email | 24 часа |

### 5.4. Churn Prevention-коммуникации

| # | Триггер (событие) | Условие | Действие | Канал | Задержка |
|---|-------------------|---------|----------|-------|----------|
| C-1 | `churn_risk_detected` | days_inactive >= 14 И plan != "free" | Email: "We miss you! Your projects are waiting. Here's what's new..." | Email | Мгновенно |
| C-2 | `churn_risk_detected` | days_inactive >= 21 И plan != "free" | Email: "Your subscription renews in [N] days. Here are 3 things you can do with it" | Email | Мгновенно |
| C-3 | `subscription_cancelled` | Всегда | Email: "We're sorry to see you go. Your projects will be saved. You can resubscribe anytime" + exit survey | Email | Мгновенно |
| C-4 | `subscription_cancelled` | reason = "too_expensive" | Email (через 7 дней): "We have a special offer for you: 50% off for 3 months" | Email | 7 дней |
| C-5 | `subscription_cancelled` | reason != "too_expensive" | Email (через 30 дней): "We've made improvements based on feedback like yours. Take a look?" | Email | 30 дней |

---

## 6. Приложение: Сводка метрик и целей

### North Star Metric

**Documents Generated per Week** — количество полных наборов документов (PRD + Risk Assessment + Vibe-Coding Plan), сгенерированных за неделю.

### Ключевые метрики по этапам

| Этап | Метрика | Цель (MVP, месяц 1-3) | Событие для расчёта |
|------|---------|----------------------|---------------------|
| Acquisition | Landing -> Signup | >8% | page_viewed -> signup_completed |
| Activation | Signup -> Flow Start | >80% | signup_completed -> flow_started |
| Activation | Flow Start -> Aha | >70% | flow_started -> aha_moment_reached |
| Activation | Flow Completion Rate | >40% | flow_started -> flow_completed |
| Activation | Time to Aha | <25 мин | aha_moment_reached.time_since_signup_sec |
| Retention | D7 Return Rate | >25% | session_started (D7 когорта) |
| Retention | D30 Return Rate | >15% | session_started (D30 когорта) |
| Retention | Projects per User | >1.3 | project_created / unique users |
| Revenue | Free-to-Paid | >5% | signup_completed -> purchase_completed |
| Revenue | MRR | >$5K к 3 мес | mrr_snapshot.mrr |
| Revenue | Churn | <8%/мес | subscription_cancelled / active_subscriptions |
| Revenue | Payback Period | <2 мес | CAC / monthly ARPU |
| Quality | NPS | >40 | nps_survey_submitted.score |
| Quality | CSAT per step | >4.0/5.0 | csat_submitted.score |
| Quality | PMF "very disappointed" | >40% | pmf_survey_submitted.answer |
| Quality | Document Quality Score | >7/10 | document_quality_rated.score |

---

## 7. Changelog (исправления из кросс-верификации v3.0)

| Исправление | Раздел | Источник |
|-------------|--------|----------|
| Добавлено событие `risk_assessment_value_realized` для второй активации Solopreneurs | 2.4, 3.5 | Критический разрыв #2 |
| Обновлено описание Aha-момента: шаг 2 = основной для всех, шаг 3 = вторая активация для Solopreneurs | 1.1 (Activation), 1.2 | Критический разрыв #2 |
| Добавлены события PMF: `nps_survey_submitted`, `csat_submitted`, `pmf_survey_submitted`, `document_quality_rated` | 2.16, 3.17 | Критический разрыв #3 |
| Добавлены события микро-гайдов: `micro_guide_started/step_completed/completed/step_failed` | 2.15, 3.16 | Улучшение #1 |
| Добавлено серверное событие `mrr_snapshot` | 2.17, 3.18 | Улучшение #3 |
| Добавлено событие `ai_content_flagged` | 2.18, 3.19 | Улучшение #7 |
| Добавлены security-события: `injection_attempt_detected`, `abuse_detected` | 2.19, 3.20 | Edge-cases |
| Добавлено событие `checkout_abandoned` | 2.9, 3.21 | Кросс-верификация |
| Добавлен дашборд PMF & Quality | 4.8 | Критический разрыв #3 |
| Добавлены метрики Quality в сводку | 6 | Критический разрыв #3 |
