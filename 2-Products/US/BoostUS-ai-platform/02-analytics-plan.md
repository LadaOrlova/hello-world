# Аналитический план LaunchPilot — PostHog

Дата: 2026-03-01
Версия: 1.0

---

## 1. Ключевые воронки

### Единая AARRR-воронка продукта

LaunchPilot — гибрид SaaS + обучение. Ниже описана общая воронка, а затем особенности по сегментам.

#### Acquisition — как пользователь попадает в продукт

Каналы привлечения: SEO/GEO, контент-маркетинг (статьи, LinkedIn, YouTube), paid ads (Google, Meta, X/Twitter). Пользователь попадает на лендинг `launchpilot.app`, нажимает "Start free", регистрируется через Google OAuth или email.

**Шаги:**
1. Просмотр лендинга (`page_viewed`, page_name = "landing")
2. Клик на CTA (`cta_clicked`, cta_name = "start_free")
3. Начало регистрации (`signup_started`)
4. Завершение регистрации (`signup_completed`)

**Как определить в аналитике:** конверсия page_viewed → signup_completed по utm-меткам и каналам.

#### Activation — Aha-момент

**Aha-момент для всех приоритетных сегментов:** пользователь видит работающий лендинг своего продукта в preview (шаг 3 guided flow). Это конкретное событие `landing_generated` + `preview_opened`.

**Обоснование через core job:**
- **Founders 0→1** (core job: превратить идею в работающий прототип) — видят свою идею реализованной в браузере за 15 минут. Момент перехода от абстракции к конкретному артефакту.
- **Solopreneurs** (core job: построить SaaS/digital product) — видят, что их продуктовая идея реализуема без разработчика. Видят свой бизнес материализованным.
- **Career Builders** (core job: освоить AI-инструменты) — впервые создают работающий артефакт с помощью AI. Ощущение "я тоже могу".

**Составное событие Aha-момента:** `aha_moment_reached` — трекается когда пользователь провёл > 5 секунд на preview сгенерированного лендинга (подтверждение, что увидел результат, а не просто кликнул).

**Сегмент-специфичные Aha-моменты:**
- **Founders 0→1, Career Builders, AI Future-Proofers:** preview лендинга > 5 сек (`trigger_type: landing_preview`)
- **Solopreneurs:** PRD + MVP-прототип + рекомендации "что делать для первых продаж" (`trigger_type: mvp_with_recommendations`)
- **Builders в организации:** прототип внутреннего инструмента (`trigger_type: mvp_preview`)

**Шаги активации:**
1. Начал guided flow (`guided_flow_started`)
2. AI-интервью: описал идею (`idea_described`)
3. Получил PRD (`prd_generated`)
4. **Сгенерировал лендинг** (`landing_generated`) — **Aha-момент**
5. Открыл preview (`preview_opened`)
6. Сгенерировал MVP (`mvp_generated`)
7. Задеплоил проект (`project_deployed`)

**Как определить в аналитике:** воронка signup_completed → aha_moment_reached, с замером time_to_aha.

#### Revenue — момент оплаты

Пользователь видит paywall после Aha-момента: при попытке создать 4-й проект, подключить кастомный домен, или при исчерпании лимита AI-запросов.

**Шаги:**
1. Увидел paywall (`paywall_shown`, trigger, plan_shown)
2. Кликнул "Upgrade" (`upgrade_initiated`)
3. Начал оплату (`purchase_initiated`)
4. Завершил оплату (`purchase_completed`)
5. Продлил подписку (`subscription_renewed`) — автоматически через Stripe
6. Обновил план (`upgrade_completed`) — с Pro на Builder

**Как определить в аналитике:** конверсия free → paid по когортам, ARPU, MRR.

#### Retention — что означает "вернулся"

Для LaunchPilot "вернулся" означает **начал новую сессию с осмысленным действием** (не просто открыл страницу). Ключевое окно: **неделя** (weekly retention).

**Почему неделя:**
- Guided flow рассчитан на 30-60 минут, но пользователь может возвращаться для итераций
- Solopreneurs работают по вечерам/выходным — недельный цикл естественен
- Email-nudges рассчитаны на D+1, D+3, D+7 — недельная каденция

**Retention-действия (любое из):**
- Начал новый проект (`project_created`)
- Итерировал существующий проект (`iteration_completed`)
- Использовал AI-помощник (`ai_chat_message_sent`)
- Открыл аналитику проекта (`project_analytics_viewed`)
- Задеплоил обновление (`project_redeployed`)

**Как определить в аналитике:** когортная таблица, ось X — недели после signup, ячейка — % пользователей с хотя бы одним retention-действием.

#### Referral — как привести других

- Пользователь делится ссылкой на свой задеплоенный продукт — на лендинге стоит бейдж "Built with LaunchPilot" (free tier)
- Реферальная ссылка в dashboard ("Invite a friend, get 1 extra project")
- Шеринг PRD / результата в соцсети ("I just built my product in 30 minutes!")

**Шаги:**
1. Поделился ссылкой (`share_link_clicked`, share_type: social/copy/email)
2. Посетитель перешёл по ссылке с бейджа (`referral_link_clicked`)
3. Реферал зарегистрировался (`referral_converted`)

---

### Особенности воронки по сегментам

#### Сегмент 1: Non-technical Founders "0→1" (приоритетный)

| Шаг AARRR | Специфика сегмента | Ключевая метрика |
|---|---|---|
| Acquisition | SEO: "how to build app without coding", paid ads: "turn idea into product" | CAC < $15 |
| Activation | Aha = работающий лендинг за 15 мин. Высокий риск застревания на шаге 1 (формулировка идеи) | Time to Aha < 15 мин, Flow Completion > 50% |
| Revenue | Paywall на кастомном домене и доп. проектах. Сегмент чувствителен к цене (< $500 на валидацию) | Free-to-Paid > 3% |
| Retention | Возвращаются для: итерации после фидбека, нового проекта. Ожидаемый цикл: 1-2 недели | D7 > 30%, D30 > 15% |
| Referral | Делятся ссылкой на продукт в сообществах (Reddit, X, ProductHunt) | Referral rate > 5% |

#### Сегмент 3: Solopreneurs / Side-hustlers (приоритетный)

| Шаг AARRR | Специфика сегмента | Ключевая метрика |
|---|---|---|
| Acquisition | SEO: "build SaaS side project", контент: Indie Hackers, r/SaaS. Paid ads: "build SaaS in a weekend" | CAC < $20 |
| Activation | Aha = PRD + прототип + конкретные рекомендации "что делать для первых продаж". Более глубокая активация, чем у Founders | Time to Aha < 20 мин, Flow Completion > 60% |
| Revenue | Готовы платить за инструмент, который экономит время. Paywall на Stripe-интеграции — сильный мотиватор | Free-to-Paid > 5% |
| Retention | Возвращаются для: подключения оплаты, итерации, новых проектов. Более длинный lifecycle | D7 > 35%, D30 > 20% |
| Referral | Делятся в Indie Hackers, Twitter. Бейдж "Built with LaunchPilot" — органический канал | Referral rate > 8% |

#### Сегмент 2: Career Builders (вторичный)

| Шаг AARRR | Специфика сегмента | Ключевая метрика |
|---|---|---|
| Acquisition | SEO: "learn AI tools for PM", контент: LinkedIn. Paid ads: "AI skills for product managers" | CAC < $25 |
| Activation | Aha = работающий демо-прототип, который можно показать руководству | Time to Aha < 20 мин, Flow Completion > 40% |
| Revenue | Менее готовы платить (не бизнес-задача, а обучение). Paywall на доп. проектах | Free-to-Paid > 2% |
| Retention | Короткий lifecycle: 1-3 проекта, потом уходят. Retention через библиотеку знаний | D7 > 20%, D30 > 10% |
| Referral | Рекомендуют коллегам. LinkedIn-посты о своём опыте | Referral rate > 3% |

---

## 2. Полный план событий

### Acquisition Events

| Название события | Описание | Когда трекать | Properties | Тип |
|---|---|---|---|---|
| `page_viewed` | Просмотр страницы продукта | При загрузке каждой страницы | `page_name`, `referrer`, `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term` | funnel |
| `cta_clicked` | Клик на CTA-кнопку | При клике на любой CTA | `cta_name`, `cta_location`, `page_name` | funnel |
| `signup_started` | Начал процесс регистрации | При открытии формы/модалки регистрации | `method` (email/google), `referrer`, `utm_source` | funnel |
| `signup_completed` | Завершил регистрацию | При успешном создании аккаунта | `method`, `referrer`, `utm_source`, `utm_medium`, `utm_campaign` | funnel, cohort |

### Onboarding & Activation Events

| Название события | Описание | Когда трекать | Properties | Тип |
|---|---|---|---|---|
| `onboarding_question_answered` | Ответил на вопрос онбординга | При выборе ответа "What best describes you?" | `question`, `answer`, `segment_assigned` | funnel, cohort |
| `guided_flow_started` | Начал пошаговый guided flow | При входе в первый шаг (AI-интервью) | `project_id`, `segment`, `is_first_project` | funnel |
| `guided_flow_step_completed` | Завершил шаг guided flow | При завершении каждого из 7 шагов | `step_number` (1-7), `step_name`, `project_id`, `time_spent_seconds`, `segment` | funnel |
| `guided_flow_step_skipped` | Пропустил шаг guided flow | При нажатии "Skip" | `step_number`, `step_name`, `project_id` | funnel |
| `guided_flow_completed` | Прошёл весь guided flow | При завершении последнего шага | `project_id`, `total_time_seconds`, `steps_completed`, `steps_skipped`, `segment` | funnel |
| `aha_moment_reached` | Достиг Aha-момента | При просмотре preview лендинга > 5 секунд | `segment`, `trigger` (landing_preview), `time_from_signup_seconds`, `project_id` | funnel, cohort |
| `aha_moment_reached_segment` | Сегмент-специфичный Aha-момент | При достижении Aha для конкретного сегмента | `segment`, `trigger_type` (landing_preview/mvp_preview/prd_with_recommendations), `time_from_signup_seconds`, `project_id` | funnel, cohort |

### Core Job Events — Product Thinking (FR-1.x)

| Название события | Описание | Когда трекать | Properties | Тип |
|---|---|---|---|---|
| `idea_described` | Описал идею продукта | После завершения AI-интервью (шаг 1) | `project_id`, `idea_length_chars`, `ai_questions_count`, `time_spent_seconds` | funnel |
| `prd_generated` | Получил PRD | После генерации PRD (шаг 2) | `project_id`, `sections_count`, `generation_time_seconds` | funnel |
| `prd_edited` | Отредактировал PRD | При каждом изменении PRD через AI-диалог | `project_id`, `edit_type` (manual/ai_suggested), `section_edited` | cohort |
| `segment_selected` | Выбрал целевой сегмент | При выборе сегмента из рекомендаций AI | `project_id`, `segment_name`, `segments_suggested_count` | funnel |
| `mvp_scope_defined` | Определил MVP-скоуп | При завершении MVP-скоупинга (шаг 1 подшаг) | `project_id`, `features_must_have`, `features_deferred` | funnel |

### Core Job Events — AI-Coding (FR-2.x)

| Название события | Описание | Когда трекать | Properties | Тип |
|---|---|---|---|---|
| `landing_generated` | Сгенерировал лендинг | После генерации лендинга (шаг 3) | `project_id`, `generation_time_seconds`, `template_used` | funnel |
| `mvp_generated` | Сгенерировал MVP-приложение | После генерации MVP (шаг 4) | `project_id`, `generation_time_seconds`, `stack`, `pages_count` | funnel |
| `preview_opened` | Открыл предпросмотр | При клике на preview | `project_id`, `preview_type` (landing/mvp), `viewport` (desktop/mobile) | funnel |
| `preview_time_spent` | Провёл время в предпросмотре | При закрытии preview (или переключении) | `project_id`, `duration_seconds`, `preview_type` | cohort |
| `iteration_requested` | Запросил доработку через AI | При отправке промпта на итерацию (шаг 5) | `project_id`, `prompt_length_chars`, `iteration_number` | cohort |
| `iteration_completed` | AI завершил доработку | После применения изменений | `project_id`, `iteration_number`, `changes_applied`, `generation_time_seconds` | cohort |
| `code_error_occurred` | Произошла ошибка генерации | При ошибке AI-генерации | `project_id`, `error_type`, `auto_fixed` | cohort |

### Core Job Events — Launch (FR-3.x)

| Название события | Описание | Когда трекать | Properties | Тип |
|---|---|---|---|---|
| `deploy_initiated` | Начал деплой | При нажатии "Deploy" / "Publish" | `project_id`, `deploy_type` (first/update) | funnel |
| `project_deployed` | Проект задеплоен | При успешном деплое | `project_id`, `deploy_time_seconds`, `domain_type` (subdomain/custom), `deploy_number`, `time_from_signup_seconds` | funnel, cohort |
| `project_redeployed` | Обновил задеплоенный проект | При повторном деплое | `project_id`, `redeploy_number`, `days_since_first_deploy` | cohort |
| `custom_domain_connected` | Подключил кастомный домен | При успешной настройке DNS | `project_id`, `domain` | revenue |
| `deploy_link_copied` | Скопировал ссылку на задеплоенный проект | При клике "Copy link" | `project_id` | cohort |

### Core Job Events — Validation (FR-4.x)

| Название события | Описание | Когда трекать | Properties | Тип |
|---|---|---|---|---|
| `validation_plan_viewed` | Открыл план валидации | При открытии "Получи первых пользователей" (шаг 7) | `project_id` | funnel |
| `validation_checklist_item_completed` | Выполнил пункт чек-листа валидации | При отметке пункта | `project_id`, `item_name`, `items_total`, `items_completed` | cohort |
| `project_analytics_viewed` | Открыл аналитику проекта | При переходе на dashboard аналитики | `project_id`, `visitors_count` | cohort |
| `feedback_submitted` | Ввёл фидбек от пользователей | При отправке фидбека в AI-помощник | `project_id`, `feedback_length_chars` | cohort |
| `ai_recommendation_applied` | Применил AI-рекомендацию по итерации | При нажатии "Apply" на рекомендации | `project_id`, `recommendation_type` | cohort |

### Core Job Events — Monetization (FR-5.x)

| Название события | Описание | Когда трекать | Properties | Тип |
|---|---|---|---|---|
| `stripe_integration_started` | Начал подключение Stripe | При входе в flow подключения Stripe | `project_id` | revenue |
| `stripe_integration_completed` | Подключил Stripe | При успешном подключении | `project_id`, `payment_type` (one-time/subscription) | revenue |

### Core Job Events — Learning (FR-6.x)

| Название события | Описание | Когда трекать | Properties | Тип |
|---|---|---|---|---|
| `learning_tip_shown` | Показана обучающая подсказка | При показе контекстного объяснения | `tip_id`, `step_name`, `topic` | cohort |
| `learning_tip_expanded` | Кликнул "Узнать больше" | При развёртывании подсказки | `tip_id`, `topic` | cohort |
| `learning_tip_dismissed` | Закрыл подсказку | При закрытии без чтения | `tip_id`, `topic` | cohort |
| `knowledge_base_article_viewed` | Открыл статью в библиотеке знаний | При просмотре статьи | `article_id`, `article_title`, `category`, `reading_time_seconds` | cohort |
| `knowledge_base_searched` | Искал в библиотеке знаний | При вводе поискового запроса | `query`, `results_count` | cohort |

### Anti-Stuck Events (FR-7.2)

| Название события | Описание | Когда трекать | Properties | Тип |
|---|---|---|---|---|
| `stuck_detected` | Обнаружено бездействие > 3 мин | При срабатывании таймера | `step_number`, `step_name`, `project_id`, `idle_seconds` | cohort |
| `stuck_help_shown` | Показана помощь "не застрять" | При показе подсказки AI | `step_number`, `help_type` (tip/template/example) | cohort |
| `stuck_help_used` | Воспользовался помощью | При клике на подсказку/шаблон | `step_number`, `help_type`, `template_name` | cohort |
| `escape_hatch_clicked` | Нажал "Я застрял, помоги" | При клике на escape hatch | `step_number`, `step_name`, `project_id` | cohort |
| `template_project_started` | Начал проект из шаблона | При выборе предзаполненного шаблона | `template_name`, `project_id` | funnel |

### Revenue Events

| Название события | Описание | Когда трекать | Properties | Тип |
|---|---|---|---|---|
| `paywall_shown` | Показан paywall | При достижении лимита | `trigger` (project_limit/domain/ai_requests/stripe), `current_plan`, `suggested_plan` | funnel, revenue |
| `paywall_dismissed` | Закрыл paywall без действия | При закрытии paywall | `trigger`, `current_plan` | funnel |
| `upgrade_initiated` | Кликнул "Upgrade" | При нажатии кнопки upgrade | `from_plan`, `to_plan`, `trigger` | funnel, revenue |
| `purchase_initiated` | Начал процесс оплаты | При переходе на Stripe Checkout | `plan` (pro/builder), `price`, `currency`, `billing_period` (monthly/annual) | funnel, revenue |
| `purchase_completed` | Оплата прошла успешно | При получении webhook от Stripe | `plan`, `price`, `currency`, `payment_method`, `billing_period`, `time_from_signup_days` | funnel, revenue, cohort |
| `checkout_abandoned` | Пользователь начал оплату, но не завершил | Когда purchase_initiated есть, а purchase_completed нет в течение 30 минут (серверный cron) | `plan`, `price`, `currency`, `step_abandoned` (payment_form/processing/3ds), `time_in_checkout_seconds` | revenue |
| `subscription_renewed` | Подписка продлена | При автоматическом списании | `plan`, `period_number`, `revenue`, `lifetime_days` | revenue, cohort |
| `upgrade_completed` | Перешёл на более дорогой план | При смене плана Pro → Builder | `from_plan`, `to_plan`, `revenue_delta`, `days_on_previous_plan` | revenue |
| `downgrade_completed` | Перешёл на более дешёвый план | При смене плана Builder → Pro | `from_plan`, `to_plan`, `revenue_delta` | revenue |
| `subscription_cancelled` | Отменил подписку | При отмене подписки | `plan`, `reason` (user_provided), `lifetime_days`, `total_revenue`, `projects_count` | revenue, churn |

### Session & Retention Events

| Название события | Описание | Когда трекать | Properties | Тип |
|---|---|---|---|---|
| `session_started` | Начал сессию | При загрузке приложения (если > 30 мин с последней активности) | `session_number`, `days_since_signup`, `days_since_last_session` | cohort |
| `session_ended` | Завершил сессию | При закрытии/неактивности 30 мин | `session_duration_seconds`, `actions_count`, `projects_touched` | cohort |
| `project_created` | Создал новый проект | При клике "New project" | `project_number`, `is_from_template`, `days_since_signup` | cohort |
| `ai_chat_message_sent` | Отправил сообщение AI-помощнику | При отправке сообщения в AI-чат | `project_id`, `message_length_chars`, `context` (iteration/validation/general) | cohort |
| `feature_used` | Использовал фичу продукта | При использовании ключевых фич | `feature_name`, `usage_count_total`, `project_id` | cohort |

### Churn Events

| Название события | Описание | Когда трекать | Properties | Тип |
|---|---|---|---|---|
| `churn_risk_detected` | Сигнал оттока | При обнаружении паттерна оттока (серверная логика) | `days_inactive`, `last_action`, `plan`, `projects_count`, `risk_score` | churn |
| `win_back_email_sent` | Отправлено win-back письмо | При отправке email неактивному пользователю | `email_type` (d7/d14/d30), `days_inactive` | churn |
| `win_back_email_clicked` | Кликнул на win-back email | При клике на ссылку в win-back | `email_type`, `days_inactive` | churn |

### Referral Events

| Название события | Описание | Когда трекать | Properties | Тип |
|---|---|---|---|---|
| `share_link_clicked` | Нажал "Поделиться" | При клике на кнопку шеринга | `share_type` (twitter/linkedin/copy/email), `project_id`, `context` (deploy_success/dashboard) | referral |
| `referral_link_clicked` | Кликнул по реферальной ссылке | При переходе по ref-ссылке или бейджу "Built with LaunchPilot" | `referrer_user_id`, `source` (badge/invite_link) | referral |
| `referral_converted` | Реферал зарегистрировался | При signup реферала | `referrer_user_id`, `source` | referral |

### Email & Nudge Events

| Название события | Описание | Когда трекать | Properties | Тип |
|---|---|---|---|---|
| `email_sent` | Отправлен email | При отправке любого автоматического email | `email_type` (d1_continue/d3_feedback/d7_iterate/d14_monetize/churn_risk), `user_id` | cohort |
| `email_opened` | Email открыт | При трекинге открытия | `email_type` | cohort |
| `email_clicked` | Кликнул ссылку в email | При клике | `email_type`, `link_name` | cohort |
| `email_unsubscribed` | Отписался от рассылки | При клике "Unsubscribe" | `email_type` | churn |

### Security Events

| Название события | Описание | Когда трекать | Properties | Тип |
|---|---|---|---|---|
| `prompt_injection_detected` | Обнаружена попытка prompt injection | При срабатывании фильтра ввода | `project_id`, `input_snippet` (first 100 chars), `filter_type`, `action_taken` (blocked/sanitized) | security |
| `secret_leak_detected` | Обнаружен секрет в сгенерированном коде | При обнаружении паттерна sk_live_, sk_test_ и др. | `project_id`, `secret_type`, `location` (file, line), `auto_removed` | security |
| `security_scan_failed` | Pre-deploy security scan обнаружил проблему | При обнаружении XSS, SQL injection и др. перед деплоем | `project_id`, `vulnerability_type`, `severity`, `auto_fixed` | security |
| `deploy_failed` | Деплой завершился ошибкой | При неуспешном деплое | `project_id`, `error_type`, `auto_retry_count`, `resolved`, `fallback_used` | funnel |
| `session_interrupted` | Сессия прервана (потеря соединения, закрытие вкладки) | При обнаружении потери соединения или при возврате после перерыва | `project_id`, `step_at_interruption`, `progress_saved`, `reconnected`, `interruption_duration_seconds` | cohort |
| `content_moderation_triggered` | Сработала модерация контента | При обнаружении запрещённого контента | `project_id`, `category`, `action_taken` (warned/blocked) | security |
| `resource_limit_exceeded` | Приложение пользователя превысило лимиты ресурсов | При автоматическом throttling/отключении | `project_id`, `resource_type` (cpu/ram/bandwidth), `action_taken` | security |

---

## 3. Код для PostHog (TypeScript)

### Инициализация и конфигурация

```typescript
// === PostHog Initialization ===
import posthog from 'posthog-js'

posthog.init('YOUR_POSTHOG_API_KEY', {
  api_host: 'https://app.posthog.com', // или self-hosted URL
  capture_pageview: false, // ручной контроль page_viewed
  capture_pageleave: true,
  persistence: 'localStorage+cookie',
  autocapture: false, // только явные события
  session_recording: {
    maskAllInputs: false,
    maskInputOptions: {
      password: true,
    },
  },
})
```

### Утилиты

```typescript
// === Utility: Get UTM parameters ===
function getUtmParams(): Record<string, string | null> {
  const urlParams = new URLSearchParams(window.location.search)
  return {
    utm_source: urlParams.get('utm_source'),
    utm_medium: urlParams.get('utm_medium'),
    utm_campaign: urlParams.get('utm_campaign'),
    utm_content: urlParams.get('utm_content'),
    utm_term: urlParams.get('utm_term'),
  }
}

// === Utility: Time tracker ===
class TimeTracker {
  private startTimes: Map<string, number> = new Map()

  start(key: string): void {
    this.startTimes.set(key, Date.now())
  }

  elapsed(key: string): number | null {
    const startTime = this.startTimes.get(key)
    if (!startTime) return null
    return Math.round((Date.now() - startTime) / 1000)
  }

  stop(key: string): number | null {
    const elapsed = this.elapsed(key)
    this.startTimes.delete(key)
    return elapsed
  }
}

const timeTracker = new TimeTracker()
```

### Identify — пользовательские свойства

```typescript
// === User Identification ===
// Вызывать при signup_completed и при каждом логине
function identifyUser(
  userId: string,
  properties: {
    email: string
    signupMethod: 'email' | 'google'
    segment: string
    signupDate: string
    utmSource?: string | null
    utmMedium?: string | null
    utmCampaign?: string | null
  }
): void {
  posthog.identify(userId, {
    email: properties.email,
    signup_method: properties.signupMethod,
    segment: properties.segment,
    signup_date: properties.signupDate,
    plan: 'free',
    projects_count: 0,
    projects_deployed_count: 0,
    guided_flows_completed: 0,
    aha_moment_reached: false,
    utm_source_first: properties.utmSource,
    utm_medium_first: properties.utmMedium,
    utm_campaign_first: properties.utmCampaign,
  })
}

// === Update user properties ===
// Вызывать при изменении состояния пользователя
function updateUserProperties(properties: Record<string, any>): void {
  posthog.people.set(properties)
}

// Примеры вызовов:
// При завершении guided flow:
// updateUserProperties({ guided_flows_completed: 1, first_flow_completed_at: new Date().toISOString() })

// При покупке:
// updateUserProperties({ plan: 'pro', plan_started_at: new Date().toISOString() })

// При деплое:
// updateUserProperties({ projects_deployed_count: 1 })
```

### Acquisition Events

```typescript
// === Acquisition Events ===

// page_viewed — при загрузке каждой страницы
posthog.capture('page_viewed', {
  page_name: 'landing', // 'landing' | 'pricing' | 'blog' | 'knowledge_base' | 'dashboard' | ...
  referrer: document.referrer,
  ...getUtmParams(),
})

// cta_clicked — при клике на CTA
posthog.capture('cta_clicked', {
  cta_name: 'start_free', // 'start_free' | 'see_pricing' | 'learn_more' | ...
  cta_location: 'hero_section', // 'hero_section' | 'pricing_table' | 'nav_bar' | ...
  page_name: 'landing',
})

// signup_started — при открытии формы регистрации
posthog.capture('signup_started', {
  method: 'google', // 'email' | 'google'
  referrer: document.referrer,
  utm_source: getUtmParams().utm_source,
})

// signup_completed — при успешном создании аккаунта
posthog.capture('signup_completed', {
  method: 'google', // 'email' | 'google'
  referrer: document.referrer,
  ...getUtmParams(),
})
```

### Onboarding & Activation Events

```typescript
// === Onboarding & Activation Events ===

// onboarding_question_answered — ответ на "What best describes you?"
posthog.capture('onboarding_question_answered', {
  question: 'what_describes_you',
  answer: 'business_idea', // 'business_idea' | 'side_project' | 'learn_ai_tools'
  segment_assigned: 'founder_0_to_1', // 'founder_0_to_1' | 'solopreneur' | 'career_builder'
})

// Также обновляем user properties
posthog.people.set({ segment: 'founder_0_to_1' })

// guided_flow_started — при входе в guided flow
timeTracker.start('guided_flow')
timeTracker.start('time_to_aha')

posthog.capture('guided_flow_started', {
  project_id: projectId,
  segment: userSegment,
  is_first_project: isFirstProject,
})

// guided_flow_step_completed — при завершении каждого шага
const stepTimeKey = `step_${stepNumber}`
const timeSpent = timeTracker.stop(stepTimeKey)

posthog.capture('guided_flow_step_completed', {
  step_number: stepNumber, // 1-7
  step_name: stepName, // 'describe_idea' | 'generate_prd' | 'generate_landing' | 'generate_mvp' | 'customize' | 'deploy' | 'validation_plan'
  project_id: projectId,
  time_spent_seconds: timeSpent,
  segment: userSegment,
})

// Начинаем трекать время следующего шага
timeTracker.start(`step_${stepNumber + 1}`)

// guided_flow_step_skipped — при пропуске шага
posthog.capture('guided_flow_step_skipped', {
  step_number: stepNumber,
  step_name: stepName,
  project_id: projectId,
})

// guided_flow_completed — при завершении всех шагов
const totalTime = timeTracker.stop('guided_flow')

posthog.capture('guided_flow_completed', {
  project_id: projectId,
  total_time_seconds: totalTime,
  steps_completed: stepsCompleted, // число
  steps_skipped: stepsSkipped, // число
  segment: userSegment,
})

posthog.people.set({
  guided_flows_completed: guidedFlowsCompleted,
  first_flow_completed_at: new Date().toISOString(),
})

// aha_moment_reached — при просмотре preview > 5 секунд
// Логика: таймер запускается при открытии preview лендинга
// Если пользователь остаётся > 5 секунд — трекаем событие
let ahaTimer: ReturnType<typeof setTimeout> | null = null

function onPreviewOpened(projectId: string, previewType: string): void {
  posthog.capture('preview_opened', {
    project_id: projectId,
    preview_type: previewType, // 'landing' | 'mvp'
    viewport: window.innerWidth > 768 ? 'desktop' : 'mobile',
  })

  if (previewType === 'landing' && !ahaReached) {
    ahaTimer = setTimeout(() => {
      const timeFromSignup = timeTracker.elapsed('time_to_aha')

      posthog.capture('aha_moment_reached', {
        segment: userSegment,
        trigger: 'landing_preview',
        time_from_signup_seconds: timeFromSignup,
        project_id: projectId,
      })

      posthog.people.set({
        aha_moment_reached: true,
        aha_moment_at: new Date().toISOString(),
        time_to_aha_seconds: timeFromSignup,
      })

      ahaReached = true
    }, 5000) // 5 секунд
  }
}

function onPreviewClosed(projectId: string, previewType: string, durationSeconds: number): void {
  if (ahaTimer) {
    clearTimeout(ahaTimer)
    ahaTimer = null
  }

  posthog.capture('preview_time_spent', {
    project_id: projectId,
    duration_seconds: durationSeconds,
    preview_type: previewType,
  })
}
```

### Core Job Events — Product Thinking

```typescript
// === Core Job: Product Thinking (FR-1.x) ===

// idea_described — после завершения AI-интервью
posthog.capture('idea_described', {
  project_id: projectId,
  idea_length_chars: ideaText.length,
  ai_questions_count: questionsAsked,
  time_spent_seconds: timeTracker.stop('step_1'),
})

// prd_generated — после генерации PRD
posthog.capture('prd_generated', {
  project_id: projectId,
  sections_count: prdSections.length,
  generation_time_seconds: generationTime,
})

// prd_edited — при редактировании PRD
posthog.capture('prd_edited', {
  project_id: projectId,
  edit_type: 'ai_suggested', // 'manual' | 'ai_suggested'
  section_edited: 'target_audience', // 'target_audience' | 'features' | 'value_proposition' | ...
})

// segment_selected — при выборе целевого сегмента
posthog.capture('segment_selected', {
  project_id: projectId,
  segment_name: selectedSegment,
  segments_suggested_count: suggestedSegments.length,
})

// mvp_scope_defined — при завершении MVP-скоупинга
posthog.capture('mvp_scope_defined', {
  project_id: projectId,
  features_must_have: mustHaveFeatures.length,
  features_deferred: deferredFeatures.length,
})
```

### Core Job Events — AI-Coding

```typescript
// === Core Job: AI-Coding (FR-2.x) ===

// landing_generated — после генерации лендинга
posthog.capture('landing_generated', {
  project_id: projectId,
  generation_time_seconds: generationTime,
  template_used: templateName || null,
})

// mvp_generated — после генерации MVP
posthog.capture('mvp_generated', {
  project_id: projectId,
  generation_time_seconds: generationTime,
  stack: 'nextjs_tailwind_postgres', // 'nextjs_tailwind_postgres' | 'nextjs_tailwind_sqlite'
  pages_count: pagesGenerated,
})

// iteration_requested — при запросе доработки
posthog.capture('iteration_requested', {
  project_id: projectId,
  prompt_length_chars: promptText.length,
  iteration_number: iterationCount,
})

// iteration_completed — после применения изменений
posthog.capture('iteration_completed', {
  project_id: projectId,
  iteration_number: iterationCount,
  changes_applied: changesCount,
  generation_time_seconds: generationTime,
})

// code_error_occurred — при ошибке генерации
posthog.capture('code_error_occurred', {
  project_id: projectId,
  error_type: errorType, // 'syntax' | 'runtime' | 'build' | 'timeout'
  auto_fixed: wasAutoFixed,
})
```

### Core Job Events — Launch

```typescript
// === Core Job: Launch (FR-3.x) ===

// deploy_initiated — при нажатии Deploy
posthog.capture('deploy_initiated', {
  project_id: projectId,
  deploy_type: isFirstDeploy ? 'first' : 'update',
})

// project_deployed — при успешном деплое
const timeFromSignup = timeTracker.elapsed('time_to_aha')

posthog.capture('project_deployed', {
  project_id: projectId,
  deploy_time_seconds: deployTime,
  domain_type: 'subdomain', // 'subdomain' | 'custom'
  deploy_number: deployCount,
  time_from_signup_seconds: timeFromSignup,
})

posthog.people.set({
  projects_deployed_count: totalDeployedProjects,
  last_deploy_at: new Date().toISOString(),
})

// project_redeployed — при обновлении деплоя
posthog.capture('project_redeployed', {
  project_id: projectId,
  redeploy_number: redeployCount,
  days_since_first_deploy: daysSinceFirstDeploy,
})

// custom_domain_connected — при подключении домена
posthog.capture('custom_domain_connected', {
  project_id: projectId,
  domain: customDomain,
})

// deploy_link_copied — при копировании ссылки
posthog.capture('deploy_link_copied', {
  project_id: projectId,
})
```

### Core Job Events — Validation

```typescript
// === Core Job: Validation (FR-4.x) ===

// validation_plan_viewed — при открытии плана валидации
posthog.capture('validation_plan_viewed', {
  project_id: projectId,
})

// validation_checklist_item_completed — при отметке пункта
posthog.capture('validation_checklist_item_completed', {
  project_id: projectId,
  item_name: itemName, // 'share_on_social' | 'collect_feedback' | 'analyze_traffic' | ...
  items_total: totalItems,
  items_completed: completedItems,
})

// project_analytics_viewed — при просмотре аналитики проекта
posthog.capture('project_analytics_viewed', {
  project_id: projectId,
  visitors_count: visitorsCount,
})

// feedback_submitted — при вводе фидбека
posthog.capture('feedback_submitted', {
  project_id: projectId,
  feedback_length_chars: feedbackText.length,
})

// ai_recommendation_applied — при применении рекомендации AI
posthog.capture('ai_recommendation_applied', {
  project_id: projectId,
  recommendation_type: recType, // 'add_feature' | 'change_copy' | 'redesign_section' | ...
})
```

### Core Job Events — Monetization & Learning

```typescript
// === Core Job: Monetization (FR-5.x) ===

// stripe_integration_started
posthog.capture('stripe_integration_started', {
  project_id: projectId,
})

// stripe_integration_completed
posthog.capture('stripe_integration_completed', {
  project_id: projectId,
  payment_type: 'subscription', // 'one-time' | 'subscription'
})

// === Core Job: Learning (FR-6.x) ===

// learning_tip_shown
posthog.capture('learning_tip_shown', {
  tip_id: tipId,
  step_name: currentStep,
  topic: 'jtbd_segmentation', // 'jtbd_segmentation' | 'mvp_definition' | 'vibe_coding_basics' | ...
})

// learning_tip_expanded
posthog.capture('learning_tip_expanded', {
  tip_id: tipId,
  topic: tipTopic,
})

// learning_tip_dismissed
posthog.capture('learning_tip_dismissed', {
  tip_id: tipId,
  topic: tipTopic,
})

// knowledge_base_article_viewed
posthog.capture('knowledge_base_article_viewed', {
  article_id: articleId,
  article_title: articleTitle,
  category: 'product_thinking', // 'product_thinking' | 'vibe_coding' | 'deployment' | 'monetization'
  reading_time_seconds: readingTime,
})

// knowledge_base_searched
posthog.capture('knowledge_base_searched', {
  query: searchQuery,
  results_count: resultsCount,
})
```

### Anti-Stuck Events

```typescript
// === Anti-Stuck Events (FR-7.2) ===

// stuck_detected — при бездействии > 3 мин
posthog.capture('stuck_detected', {
  step_number: currentStep,
  step_name: currentStepName,
  project_id: projectId,
  idle_seconds: idleSeconds,
})

// stuck_help_shown — при показе помощи
posthog.capture('stuck_help_shown', {
  step_number: currentStep,
  help_type: 'template', // 'tip' | 'template' | 'example'
})

// stuck_help_used — при использовании помощи
posthog.capture('stuck_help_used', {
  step_number: currentStep,
  help_type: helpType,
  template_name: templateName || null,
})

// escape_hatch_clicked — при нажатии "Я застрял"
posthog.capture('escape_hatch_clicked', {
  step_number: currentStep,
  step_name: currentStepName,
  project_id: projectId,
})

// template_project_started — при выборе шаблона
posthog.capture('template_project_started', {
  template_name: templateName, // 'saas_freelancers' | 'landing_page_builder' | 'habit_tracker'
  project_id: projectId,
})
```

### Revenue Events

```typescript
// === Revenue Events ===

// paywall_shown — при показе paywall
posthog.capture('paywall_shown', {
  trigger: 'project_limit', // 'project_limit' | 'custom_domain' | 'ai_requests_limit' | 'stripe_integration' | 'advanced_analytics'
  current_plan: 'free',
  suggested_plan: 'pro', // 'pro' | 'builder'
})

// paywall_dismissed — при закрытии paywall
posthog.capture('paywall_dismissed', {
  trigger: paywallTrigger,
  current_plan: currentPlan,
})

// upgrade_initiated — при клике "Upgrade"
posthog.capture('upgrade_initiated', {
  from_plan: 'free',
  to_plan: 'pro', // 'pro' | 'builder'
  trigger: paywallTrigger,
})

// purchase_initiated — при переходе на Stripe Checkout
posthog.capture('purchase_initiated', {
  plan: 'pro', // 'pro' | 'builder'
  price: 29, // 29 | 49
  currency: 'USD',
  billing_period: 'monthly', // 'monthly' | 'annual'
})

// purchase_completed — при получении Stripe webhook (серверная сторона)
// СЕРВЕРНЫЙ КОД (Node.js)
posthogServer.capture({
  distinctId: userId,
  event: 'purchase_completed',
  properties: {
    plan: 'pro',
    price: 29,
    currency: 'USD',
    payment_method: 'card', // 'card' | 'paypal'
    billing_period: 'monthly',
    time_from_signup_days: daysSinceSignup,
    $set: {
      plan: 'pro',
      plan_started_at: new Date().toISOString(),
      total_revenue: totalRevenue,
    },
  },
})

// Checkout abandoned (серверный cron, проверка каждые 5 минут)
// Если purchase_initiated > 30 мин назад без purchase_completed
posthog.capture('checkout_abandoned', {
  plan: 'pro',
  price: 2990,
  currency: 'USD',
  step_abandoned: 'payment_form', // payment_form | processing | 3ds
  time_in_checkout_seconds: 1847
})

// subscription_renewed — при автоматическом продлении (Stripe webhook)
posthogServer.capture({
  distinctId: userId,
  event: 'subscription_renewed',
  properties: {
    plan: 'pro',
    period_number: periodNumber, // 2, 3, 4...
    revenue: 29,
    lifetime_days: daysSinceFirstPurchase,
  },
})

// upgrade_completed — при смене плана (Stripe webhook)
posthogServer.capture({
  distinctId: userId,
  event: 'upgrade_completed',
  properties: {
    from_plan: 'pro',
    to_plan: 'builder',
    revenue_delta: 20, // $49 - $29
    days_on_previous_plan: daysOnPreviousPlan,
  },
})

// downgrade_completed — при понижении плана
posthogServer.capture({
  distinctId: userId,
  event: 'downgrade_completed',
  properties: {
    from_plan: 'builder',
    to_plan: 'pro',
    revenue_delta: -20,
  },
})

// subscription_cancelled — при отмене
posthogServer.capture({
  distinctId: userId,
  event: 'subscription_cancelled',
  properties: {
    plan: 'pro',
    reason: cancellationReason, // 'too_expensive' | 'not_using' | 'found_alternative' | 'other'
    lifetime_days: daysSinceFirstPurchase,
    total_revenue: totalRevenueFromUser,
    projects_count: projectsCount,
    $set: {
      plan: 'free',
      churned_at: new Date().toISOString(),
      churn_reason: cancellationReason,
    },
  },
})
```

### Session, Retention & Churn Events

```typescript
// === Session & Retention Events ===

// session_started — при загрузке приложения
posthog.capture('session_started', {
  session_number: sessionNumber,
  days_since_signup: daysSinceSignup,
  days_since_last_session: daysSinceLastSession,
})

// session_ended — при закрытии (beforeunload) или неактивности 30 мин
posthog.capture('session_ended', {
  session_duration_seconds: sessionDuration,
  actions_count: actionsInSession,
  projects_touched: projectsTouchedInSession.length,
})

// project_created — при создании нового проекта
posthog.capture('project_created', {
  project_number: totalProjects,
  is_from_template: isFromTemplate,
  days_since_signup: daysSinceSignup,
})

posthog.people.set({ projects_count: totalProjects })

// ai_chat_message_sent — при отправке сообщения AI
posthog.capture('ai_chat_message_sent', {
  project_id: projectId,
  message_length_chars: messageText.length,
  context: 'iteration', // 'iteration' | 'validation' | 'general' | 'stuck_help'
})

// feature_used — при использовании ключевых фич
posthog.capture('feature_used', {
  feature_name: 'code_preview', // 'code_preview' | 'ai_interview' | 'prd_generator' | 'deploy' | 'analytics' | 'stripe_setup' | 'knowledge_base'
  usage_count_total: totalUsageCount,
  project_id: projectId,
})

// === Churn Events (серверная сторона) ===

// churn_risk_detected — серверная CRON-задача
posthogServer.capture({
  distinctId: userId,
  event: 'churn_risk_detected',
  properties: {
    days_inactive: daysInactive,
    last_action: lastActionName,
    plan: currentPlan,
    projects_count: projectsCount,
    risk_score: riskScore, // 0-100
  },
})

// win_back_email_sent
posthogServer.capture({
  distinctId: userId,
  event: 'win_back_email_sent',
  properties: {
    email_type: 'd7', // 'd7' | 'd14' | 'd30'
    days_inactive: daysInactive,
  },
})
```

### Referral Events

```typescript
// === Referral Events ===

// share_link_clicked — при нажатии "Поделиться"
posthog.capture('share_link_clicked', {
  share_type: 'twitter', // 'twitter' | 'linkedin' | 'copy' | 'email'
  project_id: projectId,
  context: 'deploy_success', // 'deploy_success' | 'dashboard'
})

// referral_link_clicked — при переходе по реферальной ссылке (серверная сторона)
posthogServer.capture({
  distinctId: visitorDistinctId,
  event: 'referral_link_clicked',
  properties: {
    referrer_user_id: referrerUserId,
    source: 'badge', // 'badge' | 'invite_link'
  },
})

// referral_converted — при регистрации реферала (серверная сторона)
posthogServer.capture({
  distinctId: newUserId,
  event: 'referral_converted',
  properties: {
    referrer_user_id: referrerUserId,
    source: 'badge',
  },
})
```

### Email & Nudge Events

```typescript
// === Email & Nudge Events (серверная сторона) ===

// email_sent
posthogServer.capture({
  distinctId: userId,
  event: 'email_sent',
  properties: {
    email_type: 'd1_continue', // 'd1_continue' | 'd3_feedback' | 'd7_iterate' | 'd14_monetize' | 'churn_risk' | 'win_back'
  },
})

// email_opened — через webhook от email-сервиса (Resend/Postmark)
posthogServer.capture({
  distinctId: userId,
  event: 'email_opened',
  properties: {
    email_type: emailType,
  },
})

// email_clicked — через redirect-ссылки
posthogServer.capture({
  distinctId: userId,
  event: 'email_clicked',
  properties: {
    email_type: emailType,
    link_name: linkName, // 'continue_flow' | 'view_project' | 'upgrade'
  },
})

// email_unsubscribed
posthogServer.capture({
  distinctId: userId,
  event: 'email_unsubscribed',
  properties: {
    email_type: emailType,
  },
})
```

### Security Events

```typescript
// === Security Events ===

posthog.capture('prompt_injection_detected', {
  project_id: projectId,
  input_snippet: userInput.substring(0, 100),
  filter_type: 'pattern_match', // pattern_match | ml_classifier
  action_taken: 'sanitized' // blocked | sanitized | logged
})

posthog.capture('secret_leak_detected', {
  project_id: projectId,
  secret_type: 'stripe_secret_key', // stripe_secret_key | api_key | password
  location: 'src/pages/api/checkout.ts:15',
  auto_removed: true
})

posthog.capture('security_scan_failed', {
  project_id: projectId,
  vulnerability_type: 'xss', // xss | sql_injection | open_endpoint
  severity: 'high', // critical | high | medium
  auto_fixed: true
})

posthog.capture('deploy_failed', {
  project_id: projectId,
  error_type: 'build_error', // build_error | timeout | dependency_conflict | resource_limit
  auto_retry_count: 2,
  resolved: true,
  fallback_used: 'shareable_preview' // null | shareable_preview | simplified_deploy
})

posthog.capture('session_interrupted', {
  project_id: projectId,
  step_at_interruption: 4, // guided flow step number
  progress_saved: true,
  reconnected: true,
  interruption_duration_seconds: 3600
})
```

### Revenue Tracking (PostHog Revenue Analytics)

```typescript
// === Revenue tracking через PostHog ===
// PostHog автоматически рассчитает MRR, ARPU, LTV если настроить revenue events

// При purchase_completed — установить revenue-свойства на пользователя
posthog.people.set({
  plan: 'pro',
  monthly_revenue: 29,
  total_revenue: totalRevenueFromUser,
  first_purchase_at: firstPurchaseDate,
  ltv: totalRevenueFromUser,
})

// При subscription_cancelled — обнулить monthly_revenue
posthog.people.set({
  plan: 'free',
  monthly_revenue: 0,
  churned_at: new Date().toISOString(),
})
```

### Group Analytics (для проектов)

```typescript
// === Group Analytics — группировка по проектам ===
// Позволяет анализировать метрики на уровне проекта

posthog.group('project', projectId, {
  name: projectName,
  type: projectType, // 'landing' | 'saas' | 'tool'
  owner_id: userId,
  owner_segment: userSegment,
  created_at: projectCreatedAt,
  status: 'draft', // 'draft' | 'deployed' | 'active' | 'archived'
  deploy_count: 0,
  iteration_count: 0,
})

// Обновлять при изменении состояния проекта
posthog.group('project', projectId, {
  status: 'deployed',
  deploy_count: deployCount,
  first_deployed_at: new Date().toISOString(),
})
```

---

## 4. Дашборды

### Дашборд 1: Воронка активации (Activation Funnel)

**Цель:** Видеть конверсию на каждом шаге от визита до деплоя. Находить точки потерь.

**Графики:**

1. **Основная воронка (Funnel):**
   - page_viewed (landing) → cta_clicked → signup_started → signup_completed → guided_flow_started → aha_moment_reached → project_deployed
   - Фильтры: по сегменту, по utm_source, по дате
   - Отображение: % конверсии между шагами, абсолютные числа

2. **Детальная воронка guided flow (Funnel):**
   - guided_flow_started → step_1 (idea_described) → step_2 (prd_generated) → step_3 (landing_generated) → step_4 (mvp_generated) → step_5 (iteration) → step_6 (project_deployed) → step_7 (validation_plan_viewed)
   - Фильтры: по сегменту

3. **Time to Aha (Distribution):**
   - Гистограмма распределения time_from_signup_seconds для события aha_moment_reached
   - Медиана, 75-й перцентиль, 90-й перцентиль
   - Цель: медиана < 900 секунд (15 минут)

4. **Guided Flow Completion Rate (Trend):**
   - % пользователей, завершивших guided flow от начавших — по неделям
   - Цель: > 50%

5. **Drop-off по шагам (Bar chart):**
   - На каком шаге guided flow теряется больше всего пользователей
   - Сегментация по segment

6. **Anti-Stuck эффективность (Table):**
   - Кол-во stuck_detected по шагам
   - % из stuck, использовавших помощь (stuck_help_used / stuck_detected)
   - % из stuck, завершивших шаг после помощи

**Ключевые числа (KPI Indicators):**
- Signup → Flow Start Rate: цель > 80%
- Flow Completion Rate: цель > 50%
- Time to Aha (медиана): цель < 15 мин
- Time to First Deploy (медиана): цель < 60 мин

---

### Дашборд 2: Когортный анализ Retention

**Цель:** Видеть, как retention меняется по когортам. Находить, какие когорты лучше удерживаются и почему.

**Графики:**

1. **Когортная матрица (Retention Table):**
   - Ось Y: неделя регистрации (когорта)
   - Ось X: неделя после регистрации (week 0, week 1, ... week 12)
   - Ячейка: % пользователей когорты, совершивших retention-действие
   - Retention-действие: любое из (project_created, iteration_completed, ai_chat_message_sent, project_analytics_viewed, project_redeployed)

2. **Retention curves (Line chart):**
   - Линии retention по неделям для последних 4-6 когорт
   - Наложение друг на друга для сравнения
   - Цели: D7 > 30%, D30 > 15%

3. **Retention по сегментам (Retention Table):**
   - Отдельные когортные таблицы для каждого сегмента (founder_0_to_1, solopreneur, career_builder)
   - Сравнение кривых retention между сегментами

4. **Retention: Aha vs No-Aha (Line chart):**
   - Две кривые retention: пользователи, достигшие aha_moment_reached vs не достигшие
   - Ожидание: Aha-пользователи удерживаются в 2-3 раза лучше

5. **Retention по каналу привлечения (Retention Table):**
   - Когортные кривые по utm_source (google, twitter, linkedin, organic)
   - Помогает определить, какой канал приводит наиболее качественных пользователей

**Ключевые числа (KPI Indicators):**
- Week 1 Retention: цель > 30%
- Week 4 Retention: цель > 15%
- Week 12 Retention: цель > 8%

---

### Дашборд 3: Юнит-экономика по когортам

**Цель:** Считать CAC, LTV, payback period. Определять рентабельность каналов привлечения.

**Графики:**

1. **CAC по каналам (Bar chart):**
   - CAC = Spend по каналу / signup_completed по каналу
   - Каналы: Google Ads, Meta Ads, Twitter Ads, SEO (organic), Content, Referral
   - Данные по рекламным расходам — ввод вручную или через интеграцию

2. **LTV по когортам (Line chart):**
   - Кумулятивный revenue на пользователя когорты по месяцам
   - LTV = sum(purchase_completed.price + subscription_renewed.revenue) / cohort_size
   - Прогноз LTV на 12 месяцев на основе retention и ARPU

3. **Payback Period (Table):**
   - Для каждой когорты: в каком месяце кумулятивный LTV превышает CAC
   - Цель: < 3 месяцев

4. **LTV/CAC Ratio по каналам (Bar chart):**
   - LTV/CAC для каждого канала привлечения
   - Цель: > 3.0

5. **Unit Economics Summary (Table):**

   | Метрика | Текущее значение | Цель |
   |---|---|---|
   | CAC (blended) | $X | < $20 |
   | LTV (12 мес) | $X | > $60 |
   | LTV/CAC | X.X | > 3.0 |
   | Payback period | X мес | < 3 мес |
   | ARPU (paid) | $X | $29-49 |
   | Monthly churn rate | X% | < 8% |

6. **Конверсия free → paid по когортам (Line chart):**
   - % пользователей каждой когорты, совершивших purchase_completed, по неделям после регистрации
   - Видеть, улучшается ли конверсия от когорты к когорте

**Ключевые числа (KPI Indicators):**
- CAC (blended): цель < $20
- LTV (прогноз 12 мес): цель > $60
- LTV/CAC: цель > 3.0
- Payback: цель < 3 мес

---

### Дашборд 4: Конверсия по сегментам

**Цель:** Сравнить поведение сегментов на каждом шаге воронки. Найти, какой сегмент наиболее ценен.

**Графики:**

1. **Воронка по сегментам (Multi-funnel):**
   - Одна и та же воронка (signup → flow_start → aha → deploy → purchase) для каждого сегмента
   - Сегменты: founder_0_to_1, solopreneur, career_builder, org_builder, ai_future_proofer

2. **Conversion Rate по шагам и сегментам (Stacked bar chart):**
   - Ось X: шаги воронки
   - Столбики: conversion rate для каждого сегмента
   - Наглядно видно, где какой сегмент теряется

3. **Time to Aha по сегментам (Box plot / Distribution):**
   - Распределение time_to_aha для каждого сегмента
   - Медиана, 25/75 перцентили

4. **Paid Conversion по сегментам (Bar chart):**
   - Free-to-Paid conversion rate для каждого сегмента
   - Цели: Founders > 3%, Solopreneurs > 5%, Career Builders > 2%

5. **Revenue per Segment (Pie chart + Table):**
   - Доля MRR от каждого сегмента
   - ARPU по сегментам

6. **Feature Usage по сегментам (Heatmap):**
   - Ось Y: фичи (ai_interview, prd_generator, landing_generator, mvp_generator, deploy, analytics, stripe, knowledge_base)
   - Ось X: сегменты
   - Ячейка: % пользователей сегмента, использовавших фичу

**Ключевые числа (KPI Indicators):**
- Лучший сегмент по конверсии в paid
- Лучший сегмент по retention
- Самый большой сегмент по кол-ву регистраций

---

### Дашборд 5: Revenue Breakdown

**Цель:** Мониторить MRR, ARPU, churn rate. Принимать решения о ценообразовании и retention.

**Графики:**

1. **MRR Trend (Line chart):**
   - Ежемесячный MRR
   - Разбивка: New MRR (новые подписки) + Expansion MRR (апгрейды) - Contraction MRR (даунгрейды) - Churn MRR (отмены)
   - Stacked area chart для визуализации составляющих

2. **ARPU Trend (Line chart):**
   - ARPU = MRR / paying_users
   - По месяцам
   - Цель: $29-49

3. **Plan Distribution (Pie chart):**
   - Распределение платящих пользователей по планам: Pro vs Builder
   - Динамика по месяцам

4. **Churn Rate (Line chart):**
   - Monthly churn rate = subscription_cancelled / active_subscriptions_at_start
   - Цель: < 8%
   - Revenue churn vs Logo churn

5. **Churn Reasons (Bar chart):**
   - Распределение причин отмены (subscription_cancelled.reason)
   - Топ причин

6. **Paywall Performance (Funnel):**
   - paywall_shown → upgrade_initiated → purchase_initiated → purchase_completed
   - По триггерам paywall (project_limit, domain, ai_requests, stripe)
   - Какой триггер лучше конвертирует

7. **Revenue per Project (Distribution):**
   - Сколько revenue генерирует каждый проект в среднем
   - Корреляция: кол-во проектов → вероятность конверсии в paid

**Ключевые числа (KPI Indicators):**
- MRR: цель > $5K к 3 месяцам
- ARPU (paid): цель $29-49
- Monthly churn rate: цель < 8%
- Net MRR Growth: цель > 15% м/м

---

### Дашборд 6: Aha-момент

**Цель:** Подтвердить гипотезу Aha-момента, измерить его влияние на retention и конверсию.

**Графики:**

1. **% достигших Aha-момента (Trend):**
   - % пользователей (от signup_completed), достигших aha_moment_reached — по неделям
   - Цель: > 60%

2. **Time to Aha Distribution (Histogram):**
   - Распределение time_from_signup_seconds
   - Медиана, 75-й, 90-й перцентили
   - Цель: медиана < 900 сек (15 мин)

3. **Aha → Retention корреляция (Line chart):**
   - Две кривые retention: Aha (aha_moment_reached = true) vs No-Aha
   - Week 1, 2, 4, 8, 12
   - Ожидание: Aha-пользователи ретенятся в 2-3x лучше

4. **Aha → Paid Conversion корреляция (Bar chart):**
   - Conversion rate в paid для Aha-пользователей vs No-Aha
   - Ожидание: Aha-пользователи конвертируются в 3-5x лучше

5. **Aha Rate по сегментам (Bar chart):**
   - % достигших Aha по каждому сегменту
   - Помогает понять, для какого сегмента product-experience работает лучше

6. **Aha Rate по каналам (Bar chart):**
   - % достигших Aha по utm_source
   - Помогает оценить качество трафика: канал с высоким Aha rate = качественный трафик

7. **Путь до Aha (User Paths / Sankey):**
   - Визуализация путей пользователей до aha_moment_reached
   - Какие пути самые частые, какие самые быстрые

**Ключевые числа (KPI Indicators):**
- Aha Rate: цель > 60%
- Time to Aha (медиана): цель < 15 мин
- Aha → D7 Retention: ожидание > 50%
- Aha → Paid Conversion: ожидание > 5%

---

### Дашборд 7: Каналы привлечения (Acquisition Channels)

**Цель:** Оценить эффективность каналов привлечения, оптимизировать бюджет.

**Графики:**

1. **Регистрации по каналам (Stacked area chart):**
   - signup_completed по неделям, разбивка по utm_source
   - Каналы: google_ads, meta_ads, twitter_ads, organic_search, linkedin, referral, direct

2. **CAC по каналам (Bar chart):**
   - Стоимость привлечения одного пользователя для каждого канала
   - Рекламные расходы / signup_completed

3. **Качество трафика по каналам (Table):**

   | Канал | Signups | Aha Rate | Flow Completion | Paid Conversion | D7 Retention | CAC | LTV/CAC |
   |---|---|---|---|---|---|---|---|
   | Google Ads | X | X% | X% | X% | X% | $X | X.X |
   | SEO | X | X% | X% | X% | X% | $X | X.X |
   | ... | ... | ... | ... | ... | ... | ... | ... |

4. **Funnel по каналам (Multi-funnel):**
   - Одна воронка для каждого канала
   - signup → aha → deploy → purchase

5. **Landing Page Performance (Table):**
   - Для каждой landing page: page_viewed → cta_clicked → signup_started → signup_completed
   - Conversion rate
   - Bounce rate (page_viewed без cta_clicked)

6. **Referral Channel (Trend):**
   - referral_link_clicked → referral_converted — по неделям
   - Referral coefficient: referral_converted / total_signups
   - Viral coefficient: среднее кол-во рефералов на пользователя

**Ключевые числа (KPI Indicators):**
- Total signups per week
- Blended CAC
- Best channel by LTV/CAC
- Referral rate

---

### Дашборд 8: Security & Reliability

**Цель:** Мониторить безопасность и надёжность платформы. Отслеживать инциденты, скорость реагирования и стабильность деплоев.

**Графики:**

1. **prompt_injection_detected count по дням (Line chart):**
   - Количество обнаруженных попыток prompt injection по дням
   - Разбивка по action_taken (blocked/sanitized)

2. **secret_leak_detected count (KPI + Trend):**
   - Количество обнаруженных секретов в коде (должен быть 0 после auto-remove)
   - Разбивка по secret_type

3. **Deploy Failed Rate (Line chart):**
   - deploy_failed / deploy_initiated — процент неуспешных деплоев
   - Разбивка по error_type
   - Цель: < 5%

4. **Session Interrupted Rate (Line chart + KPI):**
   - session_interrupted rate и % с progress_saved = true
   - Разбивка по step_at_interruption

5. **Security Scan Failed — severity distribution (Stacked bar chart):**
   - security_scan_failed по severity (critical/high/medium)
   - % с auto_fixed = true

6. **content_moderation_triggered и resource_limit_exceeded (Trend):**
   - Количество срабатываний по дням

**Фильтры:** по периоду, по severity

**Ключевые числа (KPI Indicators):**
- Deploy Success Rate: цель > 95%
- Secret Leaks (post auto-remove): цель = 0
- Progress Saved Rate при interruption: цель > 90%
- Critical security_scan_failed: цель = 0

---

## 5. Триггеры для автоматических коммуникаций

### Онбординг

| Триггер | Условие | Действие | Канал | Timing |
|---|---|---|---|---|
| Незавершённый signup | signup_started без signup_completed через 1 час | Email: "You started signing up — finish in 30 seconds" | Email | +1ч |
| Не начал guided flow | signup_completed без guided_flow_started через 24 часа | Email: "You signed up — start building your product now (takes 30 min)" | Email | +24ч |
| Застрял на шаге 1 | guided_flow_step_completed (step=1) без step=2 через 24 часа | Email: "Your PRD is one click away — continue where you left off" | Email | +24ч |
| Не достиг Aha | signup_completed без aha_moment_reached через 48 часов | Email: "See your idea come to life — it takes 15 minutes" + ссылка на guided flow | Email | +48ч |
| Сгенерировал, но не задеплоил | landing_generated или mvp_generated без project_deployed через 72 часа | Email: "Your product is ready — deploy it in 2 minutes and share with the world" | Email | +72ч |
| Задеплоил, но не видел план валидации | project_deployed без validation_plan_viewed через 24 часа | Email: "Your product is live! Here's how to get your first 10 users" | Email | +24ч |

### Retention

| Триггер | Условие | Действие | Канал | Timing |
|---|---|---|---|---|
| D+1 после деплоя | project_deployed, прошёл 1 день | Email: "Your product has been live for 24h — check if anyone visited" | Email | D+1 |
| D+3 после деплоя | project_deployed, прошло 3 дня | Email: "3 days live — time to collect feedback. Here's how" | Email | D+3 |
| D+7 без сессии | Нет session_started за 7 дней | Email: "It's been a week — time to iterate. Here's what you can improve" | Email | D+7 |
| D+14 без сессии | Нет session_started за 14 дней | Email: "Your product is waiting — check your analytics and make it better" | Email | D+14 |
| D+7 после деплоя (активный) | project_deployed + session_started за последние 7 дней | Email: "Ready to monetize? Here's how to add Stripe payments" | Email | D+7 |
| Проект без обновлений 14 дней | project_deployed без project_redeployed за 14 дней (для активных пользователей) | In-app notification: "Your [project_name] hasn't been updated in 2 weeks. Want to iterate?" | In-app | 14 дней без redeployment |

### Churn Prevention

| Триггер | Условие | Действие | Канал | Timing |
|---|---|---|---|---|
| Churn risk — начальный | churn_risk_detected с risk_score > 50 | Email: "We miss you! Here's what's new in LaunchPilot" | Email | Немедленно |
| Churn risk — критический | churn_risk_detected с risk_score > 80 | Email: персонализированное письмо с конкретными предложениями (скидка, feature highlight) | Email | Немедленно |
| Подписка отменена | subscription_cancelled | Email: "Sorry to see you go. Can you tell us why?" + опрос (3 вопроса) | Email | +1ч |
| Подписка скоро истечёт | 3 дня до окончания billing_period (для пользователей с churn_risk_score > 30) | In-app banner: "Your subscription renews in 3 days. See what you've built" | In-app | -3 дня |
| 30 дней неактивности (free) | Нет session_started 30 дней, plan = free | Email: "Last chance — your projects will be archived in 30 days" | Email | D+30 |

### Checkout Recovery

| Триггер | Условие | Действие | Канал | Timing |
|---|---|---|---|---|
| Checkout abandoned (первый раз) | `checkout_abandoned` | Email: "Your upgrade is waiting" с прямой ссылкой на оплату | Email | +1ч после checkout_abandoned |
| Checkout abandoned (повторный) | `checkout_abandoned` 2+ раза | In-app survey: "What stopped you from upgrading?" | In-app | При следующей сессии |

### Upsell

| Триггер | Условие | Действие | Канал | Timing |
|---|---|---|---|---|
| Лимит проектов | Пользователь создал 3 проекта (free limit) и пытается создать 4-й | Paywall: "Upgrade to Pro for unlimited projects — $29/mo" | In-app (paywall) | Немедленно |
| Лимит AI-запросов | Исчерпаны AI-запросы за день (free: 20) | Paywall: "You've used all your AI credits today. Upgrade for 100/day" | In-app (paywall) | Немедленно |
| Stripe-интеграция | Пользователь кликнул "Connect Stripe" на free плане | Paywall: "Accept payments from your customers — available in Pro" | In-app (paywall) | Немедленно |
| Кастомный домен | Пользователь кликнул "Connect custom domain" | Paywall: "Use your own domain — available in Pro" | In-app (paywall) | Немедленно |
| Активный free-пользователь | projects_deployed_count >= 2 + session_started в каждую из последних 2 недель + plan = free | Email: "You're building amazing things! Unlock Pro features" + показать конкретную ценность | Email | Еженедельно (макс 2 раза) |
| Pro → Builder upsell | plan = pro + projects_count > 5 ИЛИ iteration_completed count > 50 за месяц | In-app subtle banner: "Need more power? Builder plan gives you unlimited projects and 3x more AI credits" | In-app (banner) | При достижении порога |
| High-usage free user | feature_used count > 15 за неделю + plan = free | In-app notification: "You're a power user! Pro would save you time with [specific features]" | In-app | Еженедельно |

### Engagement & Celebration

| Триггер | Условие | Действие | Канал | Timing |
|---|---|---|---|---|
| Первый деплой | project_deployed (deploy_number = 1) | In-app celebration: "Your product is LIVE! Share it with the world" + share buttons | In-app (modal) | Немедленно |
| Все шаги пройдены | guided_flow_completed | In-app celebration: "You did it! You built a product from scratch" + next steps CTA | In-app (modal) | Немедленно |
| Первый посетитель проекта | Данные из PostHog аналитики проекта: visitors > 0 | Email: "Someone visited your product! Check your analytics" | Email | В течение часа |
| 100 посетителей | visitors > 100 для задеплоенного проекта | Email: "100 people have seen your product! Time to iterate based on their behavior" | Email | В течение часа |

---

## Приложение: Серверная логика для churn_risk_detected

```typescript
// === Серверная CRON-задача (ежедневно) ===
// Определяет пользователей с риском оттока

interface ChurnRiskFactors {
  daysInactive: number
  hasDeployedProject: boolean
  hasReachedAha: boolean
  isPaying: boolean
  projectsCount: number
  totalSessions: number
}

function calculateChurnRiskScore(factors: ChurnRiskFactors): number {
  let score = 0

  // Дни неактивности — главный фактор
  if (factors.daysInactive >= 3) score += 15
  if (factors.daysInactive >= 7) score += 25
  if (factors.daysInactive >= 14) score += 30
  if (factors.daysInactive >= 30) score += 30

  // Не достиг Aha — высокий риск
  if (!factors.hasReachedAha) score += 20

  // Не задеплоил — высокий риск
  if (!factors.hasDeployedProject) score += 15

  // Мало сессий — не вовлечён
  if (factors.totalSessions <= 2) score += 10

  // Платящий — меньший риск (вложил деньги)
  if (factors.isPaying) score -= 15

  // Много проектов — вовлечён
  if (factors.projectsCount >= 3) score -= 10

  return Math.max(0, Math.min(100, score))
}
```

---

## Приложение: Чек-лист внедрения

### Фаза 1: MVP (неделя 1)
- [ ] Инициализация PostHog (клиент + сервер)
- [ ] Acquisition events: page_viewed, signup_started, signup_completed
- [ ] Activation events: guided_flow_started, guided_flow_step_completed, aha_moment_reached
- [ ] Core deploy event: project_deployed
- [ ] User identification (posthog.identify)
- [ ] Дашборд 1: Воронка активации
- [ ] Дашборд 6: Aha-момент (базовый)

### Фаза 2: Revenue & Retention (неделя 2)
- [ ] Revenue events: paywall_shown, purchase_initiated, purchase_completed, checkout_abandoned, subscription_cancelled
- [ ] Session events: session_started, session_ended
- [ ] Retention events: project_created, iteration_completed
- [ ] Churn events: churn_risk_detected
- [ ] Дашборд 2: Когортный анализ
- [ ] Дашборд 5: Revenue Breakdown
- [ ] Email-триггеры: онбординг (незавершённый flow, не достиг Aha)
- [ ] Email-триггеры: checkout recovery (checkout_abandoned)

### Фаза 3: Полная аналитика (неделя 3-4)
- [ ] Все Core Job events (product thinking, coding, validation, learning)
- [ ] Anti-Stuck events
- [ ] Referral events
- [ ] Email & nudge events
- [ ] Security events: prompt_injection_detected, secret_leak_detected, security_scan_failed, deploy_failed, session_interrupted, content_moderation_triggered, resource_limit_exceeded
- [ ] Group analytics (проекты)
- [ ] Дашборд 3: Юнит-экономика
- [ ] Дашборд 4: Конверсия по сегментам
- [ ] Дашборд 7: Каналы привлечения
- [ ] Дашборд 8: Security & Reliability
- [ ] Все email-триггеры (retention, churn, upsell, checkout recovery)
- [ ] Серверная логика churn risk scoring
