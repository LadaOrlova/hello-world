# Аналитический план: From Zero to First Product — PostHog

Дата: 2026-03-01
Версия: 1.0

---

## 1. Ключевые воронки

### Единая AARRR-воронка продукта

"From Zero to First Product" — записанный онлайн-курс с freemium-моделью. Ниже описана общая воронка, а затем особенности по сегментам.

#### Acquisition — как пользователь попадает в продукт

Каналы привлечения: SEO/GEO (статьи про product thinking + vibe-coding), контент-маркетинг (LinkedIn, YouTube, Twitter/X), paid ads (Google, Meta), viral AI-промпты (шеринг "Валидатора идеи" в Reddit, Twitter). Пользователь попадает на лендинг, нажимает "Start Free Module", регистрируется через Google OAuth или email.

**Шаги:**
1. Просмотр лендинга (`page_viewed`, page_name = "landing")
2. Клик на CTA (`cta_clicked`, cta_name = "start_free_module")
3. Начало регистрации (`signup_started`)
4. Завершение регистрации (`signup_completed`)

**Как определить в аналитике:** конверсия page_viewed -> signup_completed по utm-меткам и каналам. Target: CR visitors -> signup = 20%.

#### Activation — Aha-момент

**Aha-момент для всех приоритетных сегментов:** пользователь впервые применил AI-промпт "Валидатор идеи" к своей бизнес-идее и получил структурированный результат (Score жизнеспособности + Top-3 риска + рекомендации). Это конкретное событие `prompt_result_viewed` с prompt_name = "idea_validator".

**Обоснование через core job:**
- **Non-Technical Founders** (core job: понять что строить и в каком порядке) — за 5 минут получили структурированный анализ своей идеи, который раньше требовал недель размышлений или дорогого ментора. Момент перехода от неопределённости к ясности.
- **Solopreneurs** (core job: быстро понять стоит ли идея времени) — моментально видят Score жизнеспособности и конкретные риски. "За 5 минут я понял, стоит ли тратить вечера на эту идею."
- **AI-Era Career Builders** (core job: освоить AI для продуктов + иметь framework) — впервые видят, как AI + framework дают структурированный продуктовый анализ. "Я могу так анализировать любой продукт!"
- **AI Skills Seekers** (core job: практические навыки с AI) — впервые видят, что AI-промпт даёт конкретный бизнес-результат, а не generic ответ. "Это совсем другой уровень использования AI!"

**Составное событие Aha-момента:** `aha_moment_reached` — трекается когда выполняются ОБА условия: (1) пользователь завершил Exercise 1 (описал свой продукт через Jobs) И (2) применил промпт "Валидатор идеи" и провёл > 30 секунд на странице результата.

**Стратегия:** Aha-момент сдвинут максимально влево — в бесплатный Module 1. Пользователь испытывает ценность ДО оплаты.

**Шаги активации:**
1. Начал Module 1 (`module_started`, module_number = 1)
2. Посмотрел первый видеоурок (`video_watched`, lesson_id = "1.1")
3. Начал упражнение (`exercise_started`, exercise_id = "describe_product_jobs")
4. Завершил упражнение (`exercise_completed`, exercise_id = "describe_product_jobs")
5. Скопировал AI-промпт (`prompt_copied`, prompt_name = "idea_validator")
6. Сохранил результат промпта (`prompt_result_saved`, prompt_name = "idea_validator")
7. **Достиг Aha-момента** (`aha_moment_reached`)

**Как определить в аналитике:** воронка signup_completed -> aha_moment_reached, с замером time_to_aha. Target: < 90 мин от регистрации.

#### Revenue — момент оплаты

Пользователь видит paywall после завершения Module 1 при попытке открыть Module 2. Paywall контекстный: показывает конкретную ценность следующих модулей через Jobs ("В Module 2 ты узнаешь, кто твой идеальный клиент — не по демографии, а по работам").

**Шаги:**
1. Завершил Module 1 (`module_completed`, module_number = 1)
2. Увидел CTA на покупку (`paywall_shown`, trigger = "module_1_completed")
3. Кликнул "Upgrade" / "Get Full Course" (`purchase_initiated`)
4. Завершил оплату (`purchase_completed`)

**Как определить в аналитике:** конверсия module_1_completed -> purchase_completed по когортам, сегментам, каналам привлечения. Target: CR aha -> purchase = 15%.

#### Retention — что означает "вернулся"

Для recorded-курса "вернулся" означает **продолжил прохождение курса** (начал новый урок, выполнил упражнение, использовал AI-промпт). Ключевое окно: **неделя** (weekly retention).

**Почему неделя:**
- Курс self-paced — студенты проходят в своём темпе, часто по выходным
- Email-nurturing рассчитан на D+1, D+3, D+7 — недельная каденция
- Solopreneurs работают по вечерам/выходным — 5-10 часов в неделю

**Retention-действия (любое из):**
- Начал/продолжил урок (`video_watched`)
- Выполнил упражнение (`exercise_completed`)
- Использовал AI-промпт (`prompt_copied` или `prompt_result_saved`)
- Зашёл в community (`community_action`)

**Как определить в аналитике:** когортная таблица, ось X — недели после signup (для free) / purchase (для paid), ячейка — % пользователей с хотя бы одним retention-действием.

#### Referral — как привести других

- Пользователь делится AI-промптом "Валидатор идеи" в соцсетях (промпт сам по себе ценен и может быть viral)
- Реферальная ссылка в dashboard ("Invite a friend — get 20% off next course")
- Шеринг результата промпта ("I just validated my idea in 5 minutes with this framework!")
- Community-driven: рекомендации в Discord

**Шаги:**
1. Поделился ссылкой/промптом (`referral_sent`, share_type: social/copy/email)
2. Реферал перешёл по ссылке (`referral_link_clicked`)
3. Реферал зарегистрировался (`referral_signup_completed`)
4. Реферал купил курс (`referral_converted`)

---

### Особенности воронки по сегментам

#### Сегмент 1: Non-Technical Founders (0->1) — Приоритетный

| Шаг AARRR | Специфика сегмента | Ключевая метрика |
|---|---|---|
| Acquisition | SEO: "how to build first product", "product thinking for founders", paid ads: "turn idea into product without coding" | CAC < $40 |
| Activation | Aha = описал продукт через Jobs + получил RAT-анализ. Высокий риск застревания на формулировке Jobs (непривычный фреймворк) | Time to Aha < 90 мин, Exercise 1 Completion > 50% |
| Revenue | Paywall на Module 2. Сегмент готов платить $199-399 (для них это дёшево vs $5-20K на MVP). Нужен social proof | Free-to-Paid > 12% |
| Retention | Возвращаются для: следующих модулей, применения промптов. Ожидаемый цикл: 1-2 урока в неделю | W1 > 60%, W4 > 35% |
| Referral | Делятся в founder-сообществах (Reddit r/startups, Twitter, ProductHunt) | Referral rate > 8% |

#### Сегмент 2: Solopreneurs / Side-Hustlers — Приоритетный

| Шаг AARRR | Специфика сегмента | Ключевая метрика |
|---|---|---|
| Acquisition | SEO: "validate startup idea fast", "side project framework", контент: Indie Hackers, HackerNews | CAC < $35 |
| Activation | Aha = Score жизнеспособности идеи за 5 минут. Мотивация: не тратить вечера впустую. Более быстрая активация (привычны к инструментам) | Time to Aha < 60 мин, Prompt Copy Rate > 70% |
| Revenue | Самый готовый к оплате сегмент — ценят экономию времени. $199 = стоимость нескольких вечеров их работы | Free-to-Paid > 15% |
| Retention | Возвращаются для: быстрого прохождения (хотят компактно). Более высокий completion rate | W1 > 65%, W4 > 40% |
| Referral | Делятся в Indie Hackers, Twitter. AI-промпты как viral-контент | Referral rate > 10% |

#### Сегмент 3: AI-Era Career Builders — Вторичный

| Шаг AARRR | Специфика сегмента | Ключевая метрика |
|---|---|---|
| Acquisition | SEO: "product management AI skills", "AI tools for PMs", контент: LinkedIn | CAC < $50 |
| Activation | Aha = впервые провёл структурированный анализ продукта через AURA. Важен portfolio-кейс | Time to Aha < 90 мин, Exercise 1 Completion > 40% |
| Revenue | Менее готовы платить (инвестиция в карьеру, не в бизнес). Чувствительны к social proof и сертификации | Free-to-Paid > 8% |
| Retention | Проходят методично. Retention через portfolio-задания | W1 > 50%, W4 > 30% |
| Referral | Рекомендуют коллегам. LinkedIn-посты про курс | Referral rate > 5% |

#### Сегмент 4: AI Skills Seekers — Вторичный

| Шаг AARRR | Специфика сегмента | Ключевая метрика |
|---|---|---|
| Acquisition | SEO: "learn Claude Code", "AI prompts for business", контент: YouTube, Twitter | CAC < $30 |
| Activation | Aha = первый работающий AI-промпт с конкретным бизнес-результатом. Быстрая активация (tech-curious) | Time to Aha < 45 мин, Prompt Copy Rate > 80% |
| Revenue | Ценят практические инструменты. Готовы платить за промпты и skills, менее — за теорию | Free-to-Paid > 10% |
| Retention | Возвращаются за промптами. Риск "cherry-picking" — берут промпты, пропускают теорию | W1 > 55%, W4 > 25% |
| Referral | Активно шерят промпты и результаты в соцсетях | Referral rate > 12% |

---

## 2. Полный план событий

### Acquisition Events

| Название события | Описание | Когда трекать | Properties | Тип |
|---|---|---|---|---|
| `page_viewed` | Просмотр страницы | При загрузке каждой страницы | `page_name`, `referrer`, `utm_source`, `utm_medium`, `utm_campaign`, `utm_content`, `utm_term`, `device_type` | funnel |
| `cta_clicked` | Клик на CTA-кнопку | При клике на любой CTA | `cta_name`, `cta_location`, `page_name`, `variant` (для A/B) | funnel |
| `signup_started` | Начал процесс регистрации | При открытии формы/модалки регистрации | `method` (email/google/github), `referrer`, `utm_source` | funnel |
| `signup_completed` | Завершил регистрацию | При успешном создании аккаунта | `method`, `referrer`, `utm_source`, `utm_medium`, `utm_campaign`, `device_type` | funnel, cohort |

### Onboarding & Activation Events

| Название события | Описание | Когда трекать | Properties | Тип |
|---|---|---|---|---|
| `onboarding_question_answered` | Ответил на вопрос онбординга ("What describes you best?") | При выборе ответа | `question`, `answer`, `segment_assigned` | funnel, cohort |
| `module_started` | Начал модуль курса | При первом открытии модуля | `module_number`, `module_name`, `is_free`, `days_since_signup` | funnel |
| `module_completed` | Завершил модуль курса | При завершении всех уроков и упражнений модуля | `module_number`, `module_name`, `time_spent_total_seconds`, `lessons_completed`, `exercises_completed`, `prompts_copied` | funnel, cohort |
| `aha_moment_reached` | Достиг Aha-момента | При выполнении обоих условий: exercise_completed (describe_product_jobs) + prompt_result_saved (idea_validator) + > 30 сек на результате | `segment`, `time_from_signup_seconds`, `trigger_exercise`, `trigger_prompt` | funnel, cohort |

### Course Content Events — Видеоуроки

| Название события | Описание | Когда трекать | Properties | Тип |
|---|---|---|---|---|
| `video_started` | Начал просмотр видеоурока | При нажатии play | `lesson_id`, `lesson_name`, `module_number`, `video_duration_seconds` | funnel |
| `video_watched` | Просмотрел видеоурок (> 80% длительности) | При достижении 80% прогресса | `lesson_id`, `lesson_name`, `module_number`, `watch_duration_seconds`, `completion_percent`, `playback_speed`, `subtitles_enabled` | funnel, cohort |
| `video_paused` | Поставил видео на паузу | При паузе | `lesson_id`, `module_number`, `pause_at_seconds`, `pause_count` | cohort |
| `video_speed_changed` | Изменил скорость воспроизведения | При смене скорости | `lesson_id`, `module_number`, `from_speed`, `to_speed` | cohort |
| `video_seeked` | Перемотал видео | При перемотке | `lesson_id`, `module_number`, `from_seconds`, `to_seconds`, `direction` (forward/backward) | cohort |

### Course Content Events — Упражнения

| Название события | Описание | Когда трекать | Properties | Тип |
|---|---|---|---|---|
| `exercise_started` | Начал практическое упражнение | При открытии формы упражнения | `exercise_id`, `exercise_name`, `module_number`, `is_first_attempt` | funnel |
| `exercise_completed` | Завершил упражнение | При нажатии "Complete" / "Submit" | `exercise_id`, `exercise_name`, `module_number`, `time_spent_seconds`, `input_length_chars`, `attempt_number` | funnel, cohort |
| `exercise_saved_draft` | Сохранил черновик упражнения | При автосохранении или ручном сохранении | `exercise_id`, `module_number`, `input_length_chars` | cohort |

### Course Content Events — AI-промпты

| Название события | Описание | Когда трекать | Properties | Тип |
|---|---|---|---|---|
| `prompt_viewed` | Открыл страницу AI-промпта | При просмотре промпта | `prompt_id`, `prompt_name`, `module_number` | funnel |
| `prompt_copied` | Скопировал AI-промпт | При клике "Copy Prompt" | `prompt_id`, `prompt_name`, `module_number`, `copy_count` | funnel, cohort |
| `prompt_result_saved` | Сохранил результат применения промпта | При вставке результата обратно в платформу | `prompt_id`, `prompt_name`, `module_number`, `result_length_chars` | funnel, cohort |
| `prompt_result_viewed` | Просмотрел страницу с сохранённым результатом | При открытии результата | `prompt_id`, `prompt_name`, `module_number`, `view_duration_seconds` | cohort |
| `skill_downloaded` | Скачал Claude Code skill | При скачивании файла skill | `skill_id`, `skill_name`, `module_number` | funnel |
| `skill_instruction_viewed` | Открыл инструкцию по установке skill | При просмотре инструкции | `skill_id`, `skill_name`, `time_spent_seconds` | cohort |

### Revenue Events

| Название события | Описание | Когда трекать | Properties | Тип |
|---|---|---|---|---|
| `paywall_shown` | Показан paywall | При попытке открыть платный модуль | `trigger` (module_2_click/module_3_click/cta_after_module_1), `module_attempted`, `segment` | funnel, revenue |
| `paywall_dismissed` | Закрыл paywall без действия | При закрытии paywall | `trigger`, `time_on_paywall_seconds` | funnel |
| `purchase_initiated` | Начал процесс оплаты | При переходе на Stripe Checkout | `price`, `currency`, `plan` (standard/premium), `coupon_code`, `segment` | funnel, revenue |
| `purchase_completed` | Оплата прошла успешно | При получении webhook от Stripe | `price`, `currency`, `payment_method`, `plan`, `coupon_code`, `time_from_signup_days`, `time_from_aha_days`, `module_1_completed`, `segment`, `utm_source_first`, `utm_campaign_first` | funnel, revenue, cohort |
| `checkout_abandoned` | Начал оплату, но не завершил | Когда purchase_initiated есть, а purchase_completed нет в течение 30 минут | `price`, `step_abandoned`, `time_in_checkout_seconds` | revenue |
| `refund_requested` | Запросил возврат (14 дней money-back) | При запросе возврата | `days_since_purchase`, `modules_completed`, `reason` | revenue, churn |
| `refund_completed` | Возврат выполнен | При подтверждении возврата | `price`, `days_since_purchase`, `reason` | revenue |

### Session & Retention Events

| Название события | Описание | Когда трекать | Properties | Тип |
|---|---|---|---|---|
| `session_started` | Начал сессию | При загрузке приложения (если > 30 мин с последней активности) | `session_number`, `days_since_signup`, `days_since_last_session`, `is_paid_user` | cohort |
| `session_ended` | Завершил сессию | При закрытии/неактивности 30 мин | `session_duration_seconds`, `actions_count`, `lessons_watched`, `exercises_done` | cohort |
| `feature_used` | Использовал фичу платформы | При использовании ключевых фич | `feature_name` (progress_bar/community_link/prompt_library/speed_control), `usage_count_total` | cohort |
| `progress_milestone_reached` | Достиг вехи прогресса | При достижении 25%/50%/75%/100% курса | `milestone_percent`, `modules_completed`, `days_since_signup`, `days_since_purchase` | cohort |
| `course_completed` | Завершил весь курс (6 модулей) | При завершении Module 6 | `total_days`, `total_sessions`, `exercises_completed_count`, `prompts_used_count`, `skills_downloaded_count`, `segment` | funnel, cohort |

### Churn & Risk Events

| Название события | Описание | Когда трекать | Properties | Тип |
|---|---|---|---|---|
| `churn_risk_detected` | Сигнал оттока | При обнаружении паттерна оттока (серверный cron) | `days_inactive`, `last_action`, `is_paid`, `modules_completed`, `progress_percent`, `risk_score`, `segment` | churn |
| `drop_off_detected` | Пользователь бросил конкретный модуль | Когда module_started есть, а video_watched нет в течение 7 дней | `module_number`, `last_lesson_watched`, `last_exercise_done`, `days_since_last_activity` | churn |

### Referral Events

| Название события | Описание | Когда трекать | Properties | Тип |
|---|---|---|---|---|
| `referral_sent` | Поделился ссылкой/промптом | При клике "Share" | `share_type` (twitter/linkedin/copy/email/whatsapp), `share_content` (course_link/prompt/result), `context` (dashboard/lesson/prompt_result) | referral |
| `referral_link_clicked` | Кто-то перешёл по реферальной ссылке | При переходе по ref-ссылке | `referrer_user_id`, `source` (social/direct/community) | referral |
| `referral_signup_completed` | Реферал зарегистрировался | При signup через ref-ссылку | `referrer_user_id`, `source` | referral |
| `referral_converted` | Реферал купил курс | При purchase_completed через ref | `referrer_user_id`, `source`, `revenue` | referral, revenue |

### Email & Nurture Events

| Название события | Описание | Когда трекать | Properties | Тип |
|---|---|---|---|---|
| `email_sent` | Отправлен автоматический email | При отправке | `email_type` (welcome/d1_continue/d3_nudge/d7_remind/paywall_follow_up/churn_risk/nps_survey), `user_segment` | cohort |
| `email_opened` | Email открыт | При трекинге открытия | `email_type` | cohort |
| `email_clicked` | Кликнул ссылку в email | При клике | `email_type`, `link_name` | cohort |
| `email_unsubscribed` | Отписался от рассылки | При клике "Unsubscribe" | `email_type` | churn |

### Community Events

| Название события | Описание | Когда трекать | Properties | Тип |
|---|---|---|---|---|
| `community_joined` | Присоединился к Discord | При использовании invite-ссылки после оплаты | `days_since_purchase`, `module_current` | cohort |
| `community_action` | Активность в community | При взаимодействии (трекинг через Discord bot) | `action_type` (message/reaction/thread), `channel` | cohort |

### NPS & Feedback Events

| Название события | Описание | Когда трекать | Properties | Тип |
|---|---|---|---|---|
| `nps_survey_shown` | Показан NPS-опрос | После Module 1 complete или Course complete | `trigger` (module_1_complete/course_complete), `segment` | cohort |
| `nps_survey_completed` | Заполнил NPS | При отправке ответа | `score`, `comment`, `trigger`, `segment` | cohort |

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

// === Utility: Get device type ===
function getDeviceType(): 'mobile' | 'tablet' | 'desktop' {
  const width = window.innerWidth
  if (width < 768) return 'mobile'
  if (width < 1024) return 'tablet'
  return 'desktop'
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

// === Utility: Store signup timestamp for time_from_signup calculations ===
function getTimeFromSignupSeconds(): number | null {
  const signupTimestamp = localStorage.getItem('signup_timestamp')
  if (!signupTimestamp) return null
  return Math.round((Date.now() - parseInt(signupTimestamp)) / 1000)
}

function getTimeFromSignupDays(): number | null {
  const seconds = getTimeFromSignupSeconds()
  if (seconds === null) return null
  return Math.round(seconds / 86400)
}
```

### Identify — пользовательские свойства

```typescript
// === User Identification ===
// Вызывать при signup_completed и при каждом логине
function identifyUser(
  userId: string,
  properties: {
    email: string
    name: string
    signupMethod: 'email' | 'google' | 'github'
    segment: string
    signupDate: string
    utmSource?: string | null
    utmMedium?: string | null
    utmCampaign?: string | null
  }
): void {
  posthog.identify(userId, {
    email: properties.email,
    name: properties.name,
    signup_method: properties.signupMethod,
    segment: properties.segment,
    signup_date: properties.signupDate,
    plan: 'free', // free | paid
    is_paid: false,
    modules_completed: 0,
    current_module: 0,
    exercises_completed: 0,
    prompts_copied: 0,
    prompts_results_saved: 0,
    skills_downloaded: 0,
    aha_moment_reached: false,
    course_completed: false,
    community_joined: false,
    nps_score: null,
    utm_source_first: properties.utmSource,
    utm_medium_first: properties.utmMedium,
    utm_campaign_first: properties.utmCampaign,
  })

  // Сохраняем timestamp для расчёта time_from_signup
  localStorage.setItem('signup_timestamp', Date.now().toString())
}

// === Update user properties ===
// Вызывать при изменении состояния пользователя
function updateUserProperties(properties: Record<string, any>): void {
  posthog.people.set(properties)
}

// Примеры обновлений:

// При завершении модуля:
// updateUserProperties({
//   modules_completed: 1,
//   current_module: 2,
//   module_1_completed_at: new Date().toISOString()
// })

// При покупке:
// updateUserProperties({
//   plan: 'paid',
//   is_paid: true,
//   purchase_date: new Date().toISOString(),
//   purchase_price: 199,
//   purchase_currency: 'USD'
// })

// При Aha-моменте:
// updateUserProperties({
//   aha_moment_reached: true,
//   aha_moment_at: new Date().toISOString()
// })

// При NPS:
// updateUserProperties({ nps_score: 9 })
```

### Acquisition Events

```typescript
// === page_viewed ===
// Вызывать при загрузке каждой страницы (роутер / layout)
function trackPageViewed(pageName: string): void {
  const utmParams = getUtmParams()
  posthog.capture('page_viewed', {
    page_name: pageName, // 'landing' | 'signup' | 'dashboard' | 'module_1' | 'module_2' | ...
    referrer: document.referrer,
    device_type: getDeviceType(),
    ...utmParams,
  })
}

// === cta_clicked ===
// Вызывать при клике на CTA-кнопку
function trackCtaClicked(ctaName: string, ctaLocation: string, pageName: string, variant?: string): void {
  posthog.capture('cta_clicked', {
    cta_name: ctaName, // 'start_free_module' | 'get_full_course' | 'copy_prompt' | ...
    cta_location: ctaLocation, // 'hero' | 'after_module_1' | 'pricing_section' | 'navbar' | ...
    page_name: pageName,
    variant: variant ?? null, // для A/B тестов лендинга
  })
}

// === signup_started ===
// Вызывать при открытии формы регистрации
function trackSignupStarted(method: 'email' | 'google' | 'github'): void {
  const utmParams = getUtmParams()
  timeTracker.start('signup')

  posthog.capture('signup_started', {
    method,
    referrer: document.referrer,
    utm_source: utmParams.utm_source,
  })
}

// === signup_completed ===
// Вызывать при успешном создании аккаунта
function trackSignupCompleted(method: 'email' | 'google' | 'github'): void {
  const utmParams = getUtmParams()
  const signupDuration = timeTracker.stop('signup')

  posthog.capture('signup_completed', {
    method,
    referrer: document.referrer,
    device_type: getDeviceType(),
    signup_duration_seconds: signupDuration,
    ...utmParams,
  })
}
```

### Onboarding & Activation Events

```typescript
// === onboarding_question_answered ===
// Вызывать при ответе на вопрос "What describes you best?"
function trackOnboardingAnswer(question: string, answer: string, segmentAssigned: string): void {
  posthog.capture('onboarding_question_answered', {
    question, // 'what_describes_you' | 'main_goal' | ...
    answer, // 'founder' | 'solopreneur' | 'career_builder' | 'ai_seeker'
    segment_assigned: segmentAssigned,
  })

  // Обновляем свойство пользователя
  updateUserProperties({ segment: segmentAssigned })
}

// === module_started ===
// Вызывать при первом открытии модуля
function trackModuleStarted(moduleNumber: number, moduleName: string): void {
  timeTracker.start(`module_${moduleNumber}`)

  posthog.capture('module_started', {
    module_number: moduleNumber, // 1-6
    module_name: moduleName, // 'what_is_value' | 'segmentation' | 'positioning' | 'value_creation' | 'communication' | 'funnel'
    is_free: moduleNumber === 1,
    days_since_signup: getTimeFromSignupDays(),
  })

  updateUserProperties({ current_module: moduleNumber })
}

// === module_completed ===
// Вызывать при завершении всех уроков и упражнений модуля
function trackModuleCompleted(
  moduleNumber: number,
  moduleName: string,
  stats: {
    lessonsCompleted: number
    exercisesCompleted: number
    promptsCopied: number
  }
): void {
  const timeSpent = timeTracker.stop(`module_${moduleNumber}`)

  posthog.capture('module_completed', {
    module_number: moduleNumber,
    module_name: moduleName,
    time_spent_total_seconds: timeSpent,
    lessons_completed: stats.lessonsCompleted,
    exercises_completed: stats.exercisesCompleted,
    prompts_copied: stats.promptsCopied,
    days_since_signup: getTimeFromSignupDays(),
  })

  updateUserProperties({
    modules_completed: moduleNumber,
    [`module_${moduleNumber}_completed_at`]: new Date().toISOString(),
  })
}

// === aha_moment_reached ===
// Вызывать когда ОБА условия выполнены:
// 1) exercise_completed с exercise_id = "describe_product_jobs"
// 2) prompt_result_saved с prompt_name = "idea_validator" + > 30 сек на результате
function trackAhaMomentReached(segment: string): void {
  posthog.capture('aha_moment_reached', {
    segment,
    time_from_signup_seconds: getTimeFromSignupSeconds(),
    trigger_exercise: 'describe_product_jobs',
    trigger_prompt: 'idea_validator',
  })

  updateUserProperties({
    aha_moment_reached: true,
    aha_moment_at: new Date().toISOString(),
  })
}
```

### Course Content Events — Видеоуроки

```typescript
// === video_started ===
// Вызывать при нажатии play
function trackVideoStarted(lessonId: string, lessonName: string, moduleNumber: number, videoDuration: number): void {
  timeTracker.start(`video_${lessonId}`)

  posthog.capture('video_started', {
    lesson_id: lessonId, // '1.1' | '1.2' | '2.1' | ...
    lesson_name: lessonName, // 'what_is_value_theory' | 'jobs_to_be_done' | ...
    module_number: moduleNumber,
    video_duration_seconds: videoDuration,
  })
}

// === video_watched ===
// Вызывать при достижении 80% прогресса
function trackVideoWatched(
  lessonId: string,
  lessonName: string,
  moduleNumber: number,
  completionPercent: number,
  playbackSpeed: number,
  subtitlesEnabled: boolean
): void {
  const watchDuration = timeTracker.stop(`video_${lessonId}`)

  posthog.capture('video_watched', {
    lesson_id: lessonId,
    lesson_name: lessonName,
    module_number: moduleNumber,
    watch_duration_seconds: watchDuration,
    completion_percent: completionPercent,
    playback_speed: playbackSpeed, // 0.5 | 0.75 | 1 | 1.25 | 1.5 | 2
    subtitles_enabled: subtitlesEnabled,
  })
}

// === video_paused ===
function trackVideoPaused(lessonId: string, moduleNumber: number, pauseAtSeconds: number, pauseCount: number): void {
  posthog.capture('video_paused', {
    lesson_id: lessonId,
    module_number: moduleNumber,
    pause_at_seconds: pauseAtSeconds,
    pause_count: pauseCount,
  })
}

// === video_speed_changed ===
function trackVideoSpeedChanged(lessonId: string, moduleNumber: number, fromSpeed: number, toSpeed: number): void {
  posthog.capture('video_speed_changed', {
    lesson_id: lessonId,
    module_number: moduleNumber,
    from_speed: fromSpeed,
    to_speed: toSpeed,
  })
}

// === video_seeked ===
function trackVideoSeeked(lessonId: string, moduleNumber: number, fromSeconds: number, toSeconds: number): void {
  posthog.capture('video_seeked', {
    lesson_id: lessonId,
    module_number: moduleNumber,
    from_seconds: fromSeconds,
    to_seconds: toSeconds,
    direction: toSeconds > fromSeconds ? 'forward' : 'backward',
  })
}
```

### Course Content Events — Упражнения

```typescript
// === exercise_started ===
// Вызывать при открытии формы упражнения
function trackExerciseStarted(exerciseId: string, exerciseName: string, moduleNumber: number, isFirstAttempt: boolean): void {
  timeTracker.start(`exercise_${exerciseId}`)

  posthog.capture('exercise_started', {
    exercise_id: exerciseId,
    // Список ID упражнений:
    // 'describe_product_jobs' (Module 1)
    // 'choose_focus_segment' (Module 2)
    // 'write_one_liner' (Module 3)
    // 'apply_5_mechanics' (Module 4)
    // 'write_landing_copy' (Module 5)
    // 'build_funnel' (Module 6)
    exercise_name: exerciseName,
    module_number: moduleNumber,
    is_first_attempt: isFirstAttempt,
  })
}

// === exercise_completed ===
// Вызывать при нажатии "Complete" / "Submit"
function trackExerciseCompleted(
  exerciseId: string,
  exerciseName: string,
  moduleNumber: number,
  inputLengthChars: number,
  attemptNumber: number
): void {
  const timeSpent = timeTracker.stop(`exercise_${exerciseId}`)

  posthog.capture('exercise_completed', {
    exercise_id: exerciseId,
    exercise_name: exerciseName,
    module_number: moduleNumber,
    time_spent_seconds: timeSpent,
    input_length_chars: inputLengthChars,
    attempt_number: attemptNumber,
  })

  // Обновляем счётчик
  posthog.people.set_once({ first_exercise_completed_at: new Date().toISOString() })
  posthog.people.increment('exercises_completed', 1)
}

// === exercise_saved_draft ===
function trackExerciseSavedDraft(exerciseId: string, moduleNumber: number, inputLengthChars: number): void {
  posthog.capture('exercise_saved_draft', {
    exercise_id: exerciseId,
    module_number: moduleNumber,
    input_length_chars: inputLengthChars,
  })
}
```

### Course Content Events — AI-промпты

```typescript
// === prompt_viewed ===
// Вызывать при просмотре страницы AI-промпта
function trackPromptViewed(promptId: string, promptName: string, moduleNumber: number): void {
  timeTracker.start(`prompt_view_${promptId}`)

  posthog.capture('prompt_viewed', {
    prompt_id: promptId,
    // Список prompt_name:
    // 'idea_validator' (Module 1) — Валидатор идеи
    // 'segment_generator' (Module 2) — Генератор сегментов
    // 'ajtbd_interview_guide' (Module 2) — AJTBD-интервью гайд
    // 'positioning_generator' (Module 3) — Генератор позиционирования
    // 'job_graph_generator' (Module 4) — Генератор графа работ
    // 'value_hypothesis_generator' (Module 4) — Генератор гипотез ценности
    // 'landing_generator' (Module 5) — Генератор лендинга
    // 'funnel_generator' (Module 6) — Генератор воронки
    // 'unit_economics_calculator' (Module 6) — Калькулятор юнит-экономики
    prompt_name: promptName,
    module_number: moduleNumber,
  })
}

// === prompt_copied ===
// Вызывать при клике "Copy Prompt"
function trackPromptCopied(promptId: string, promptName: string, moduleNumber: number, copyCount: number): void {
  posthog.capture('prompt_copied', {
    prompt_id: promptId,
    prompt_name: promptName,
    module_number: moduleNumber,
    copy_count: copyCount, // Сколько раз скопирован этот промпт данным пользователем
  })

  posthog.people.increment('prompts_copied', 1)
}

// === prompt_result_saved ===
// Вызывать при вставке результата обратно в платформу
function trackPromptResultSaved(promptId: string, promptName: string, moduleNumber: number, resultLengthChars: number): void {
  posthog.capture('prompt_result_saved', {
    prompt_id: promptId,
    prompt_name: promptName,
    module_number: moduleNumber,
    result_length_chars: resultLengthChars,
  })

  posthog.people.increment('prompts_results_saved', 1)
}

// === prompt_result_viewed ===
// Вызывать при просмотре сохранённого результата
function trackPromptResultViewed(promptId: string, promptName: string, moduleNumber: number): void {
  const viewDuration = timeTracker.stop(`prompt_view_${promptId}`)

  posthog.capture('prompt_result_viewed', {
    prompt_id: promptId,
    prompt_name: promptName,
    module_number: moduleNumber,
    view_duration_seconds: viewDuration,
  })
}

// === skill_downloaded ===
// Вызывать при скачивании Claude Code skill
function trackSkillDownloaded(skillId: string, skillName: string, moduleNumber: number): void {
  posthog.capture('skill_downloaded', {
    skill_id: skillId,
    // Список skill_name:
    // 'landing_from_prd' (Module 5) — Лендинг из PRD
    // 'prd_from_interview' (Module 6) — PRD из интервью
    skill_name: skillName,
    module_number: moduleNumber,
  })

  posthog.people.increment('skills_downloaded', 1)
}

// === skill_instruction_viewed ===
function trackSkillInstructionViewed(skillId: string, skillName: string): void {
  timeTracker.start(`skill_instruction_${skillId}`)

  posthog.capture('skill_instruction_viewed', {
    skill_id: skillId,
    skill_name: skillName,
  })
}
```

### Revenue Events

```typescript
// === paywall_shown ===
// Вызывать при попытке открыть платный модуль
function trackPaywallShown(trigger: string, moduleAttempted: number, segment: string): void {
  timeTracker.start('paywall')

  posthog.capture('paywall_shown', {
    trigger, // 'module_2_click' | 'module_3_click' | 'cta_after_module_1' | 'cta_in_lesson'
    module_attempted: moduleAttempted,
    segment,
  })
}

// === paywall_dismissed ===
function trackPaywallDismissed(trigger: string): void {
  const timeOnPaywall = timeTracker.stop('paywall')

  posthog.capture('paywall_dismissed', {
    trigger,
    time_on_paywall_seconds: timeOnPaywall,
  })
}

// === purchase_initiated ===
// Вызывать при переходе на Stripe Checkout
function trackPurchaseInitiated(price: number, currency: string, plan: string, couponCode: string | null, segment: string): void {
  posthog.capture('purchase_initiated', {
    price, // 199 | 399
    currency, // 'USD'
    plan, // 'standard' | 'premium'
    coupon_code: couponCode,
    segment,
  })
}

// === purchase_completed ===
// Вызывать при получении webhook от Stripe (серверная сторона, но также клиент при redirect)
function trackPurchaseCompleted(
  price: number,
  currency: string,
  paymentMethod: string,
  plan: string,
  couponCode: string | null,
  segment: string,
  utmSourceFirst: string | null,
  utmCampaignFirst: string | null
): void {
  posthog.capture('purchase_completed', {
    price,
    currency,
    payment_method: paymentMethod,
    plan,
    coupon_code: couponCode,
    time_from_signup_days: getTimeFromSignupDays(),
    module_1_completed: true, // всегда true — покупка после Module 1
    segment,
    utm_source_first: utmSourceFirst,
    utm_campaign_first: utmCampaignFirst,
    // PostHog revenue tracking
    $set: { plan: 'paid', is_paid: true },
  })

  updateUserProperties({
    plan: 'paid',
    is_paid: true,
    purchase_date: new Date().toISOString(),
    purchase_price: price,
    purchase_currency: currency,
    purchase_plan: plan,
  })
}

// === checkout_abandoned ===
// Серверная сторона: cron каждые 30 минут проверяет purchase_initiated без purchase_completed
function trackCheckoutAbandoned(price: number, stepAbandoned: string, timeInCheckoutSeconds: number): void {
  posthog.capture('checkout_abandoned', {
    price,
    step_abandoned: stepAbandoned, // 'payment_form' | 'processing' | '3ds'
    time_in_checkout_seconds: timeInCheckoutSeconds,
  })
}

// === refund_requested ===
function trackRefundRequested(daysSincePurchase: number, modulesCompleted: number, reason: string): void {
  posthog.capture('refund_requested', {
    days_since_purchase: daysSincePurchase,
    modules_completed: modulesCompleted,
    reason,
  })
}

// === refund_completed ===
function trackRefundCompleted(price: number, daysSincePurchase: number, reason: string): void {
  posthog.capture('refund_completed', {
    price,
    days_since_purchase: daysSincePurchase,
    reason,
  })

  updateUserProperties({
    plan: 'refunded',
    is_paid: false,
    refund_date: new Date().toISOString(),
    refund_reason: reason,
  })
}
```

### Session & Retention Events

```typescript
// === session_started ===
// Вызывать при загрузке приложения (если > 30 мин с последней активности)
function trackSessionStarted(sessionNumber: number, isPaidUser: boolean): void {
  const daysSinceLastSession = parseInt(localStorage.getItem('days_since_last_session') || '0')

  posthog.capture('session_started', {
    session_number: sessionNumber,
    days_since_signup: getTimeFromSignupDays(),
    days_since_last_session: daysSinceLastSession,
    is_paid_user: isPaidUser,
  })

  timeTracker.start('session')
  localStorage.setItem('last_session_timestamp', Date.now().toString())
}

// === session_ended ===
// Вызывать при закрытии/неактивности 30 мин
function trackSessionEnded(actionsCount: number, lessonsWatched: number, exercisesDone: number): void {
  const sessionDuration = timeTracker.stop('session')

  posthog.capture('session_ended', {
    session_duration_seconds: sessionDuration,
    actions_count: actionsCount,
    lessons_watched: lessonsWatched,
    exercises_done: exercisesDone,
  })
}

// === feature_used ===
function trackFeatureUsed(featureName: string, usageCountTotal: number): void {
  posthog.capture('feature_used', {
    feature_name: featureName,
    // 'progress_bar' | 'community_link' | 'prompt_library' | 'speed_control' |
    // 'subtitles' | 'exercise_autosave' | 'dark_mode'
    usage_count_total: usageCountTotal,
  })
}

// === progress_milestone_reached ===
function trackProgressMilestoneReached(milestonePercent: number, modulesCompleted: number): void {
  posthog.capture('progress_milestone_reached', {
    milestone_percent: milestonePercent, // 25 | 50 | 75 | 100
    modules_completed: modulesCompleted,
    days_since_signup: getTimeFromSignupDays(),
  })
}

// === course_completed ===
function trackCourseCompleted(
  stats: {
    totalSessions: number
    exercisesCompletedCount: number
    promptsUsedCount: number
    skillsDownloadedCount: number
    segment: string
  }
): void {
  posthog.capture('course_completed', {
    total_days: getTimeFromSignupDays(),
    total_sessions: stats.totalSessions,
    exercises_completed_count: stats.exercisesCompletedCount,
    prompts_used_count: stats.promptsUsedCount,
    skills_downloaded_count: stats.skillsDownloadedCount,
    segment: stats.segment,
  })

  updateUserProperties({
    course_completed: true,
    course_completed_at: new Date().toISOString(),
  })
}
```

### Churn & Risk Events

```typescript
// === churn_risk_detected ===
// Серверная сторона: cron ежедневно проверяет паттерны оттока
function trackChurnRiskDetected(
  userId: string,
  daysInactive: number,
  lastAction: string,
  isPaid: boolean,
  modulesCompleted: number,
  progressPercent: number,
  riskScore: number,
  segment: string
): void {
  // Серверный вызов через PostHog API
  posthog.capture('churn_risk_detected', {
    distinct_id: userId,
    days_inactive: daysInactive,
    last_action: lastAction,
    is_paid: isPaid,
    modules_completed: modulesCompleted,
    progress_percent: progressPercent,
    risk_score: riskScore, // 0-100, чем выше — тем больше риск
    segment,
  })
}

// === drop_off_detected ===
// Серверная сторона: когда module_started есть, а video_watched нет в течение 7 дней
function trackDropOffDetected(
  userId: string,
  moduleNumber: number,
  lastLessonWatched: string | null,
  lastExerciseDone: string | null,
  daysSinceLastActivity: number
): void {
  posthog.capture('drop_off_detected', {
    distinct_id: userId,
    module_number: moduleNumber,
    last_lesson_watched: lastLessonWatched,
    last_exercise_done: lastExerciseDone,
    days_since_last_activity: daysSinceLastActivity,
  })
}
```

### Referral Events

```typescript
// === referral_sent ===
function trackReferralSent(shareType: string, shareContent: string, context: string): void {
  posthog.capture('referral_sent', {
    share_type: shareType, // 'twitter' | 'linkedin' | 'copy' | 'email' | 'whatsapp'
    share_content: shareContent, // 'course_link' | 'prompt' | 'result' | 'certificate'
    context, // 'dashboard' | 'lesson' | 'prompt_result' | 'course_complete'
  })
}

// === referral_link_clicked ===
function trackReferralLinkClicked(referrerUserId: string, source: string): void {
  posthog.capture('referral_link_clicked', {
    referrer_user_id: referrerUserId,
    source, // 'social' | 'direct' | 'community' | 'email'
  })
}

// === referral_signup_completed ===
function trackReferralSignupCompleted(referrerUserId: string, source: string): void {
  posthog.capture('referral_signup_completed', {
    referrer_user_id: referrerUserId,
    source,
  })
}

// === referral_converted ===
function trackReferralConverted(referrerUserId: string, source: string, revenue: number): void {
  posthog.capture('referral_converted', {
    referrer_user_id: referrerUserId,
    source,
    revenue,
  })
}
```

### Email & Nurture Events

```typescript
// === email_sent ===
// Серверная сторона: при отправке любого автоматического email
function trackEmailSent(emailType: string, userSegment: string): void {
  posthog.capture('email_sent', {
    email_type: emailType,
    // Типы писем:
    // 'welcome' — сразу после регистрации
    // 'd1_continue_module_1' — через 1 день: "Ты начал Module 1, продолжи!"
    // 'd3_nudge_exercise' — через 3 дня: "Ты ещё не сделал упражнение — попробуй!"
    // 'd7_remind_prompt' — через 7 дней: "Попробуй Валидатор идеи для своего продукта"
    // 'module_1_completed_upsell' — после Module 1: "Ты описал Jobs — теперь найди сегмент в Module 2"
    // 'paywall_follow_up' — через 2 дня после paywall: "Ты видел Module 2 — вот что внутри..."
    // 'churn_risk_free' — неактивный free user
    // 'churn_risk_paid' — неактивный paid user
    // 'nps_survey' — NPS-опрос
    // 'course_completed_referral' — после завершения курса: "Порекомендуй другу"
    user_segment: userSegment,
  })
}

// === email_opened ===
function trackEmailOpened(emailType: string): void {
  posthog.capture('email_opened', {
    email_type: emailType,
  })
}

// === email_clicked ===
function trackEmailClicked(emailType: string, linkName: string): void {
  posthog.capture('email_clicked', {
    email_type: emailType,
    link_name: linkName, // 'continue_module' | 'try_prompt' | 'upgrade' | 'view_results'
  })
}

// === email_unsubscribed ===
function trackEmailUnsubscribed(emailType: string): void {
  posthog.capture('email_unsubscribed', {
    email_type: emailType,
  })
}
```

### Community Events

```typescript
// === community_joined ===
// Вызывать при использовании invite-ссылки после оплаты
function trackCommunityJoined(daysSincePurchase: number, moduleCurrent: number): void {
  posthog.capture('community_joined', {
    days_since_purchase: daysSincePurchase,
    module_current: moduleCurrent,
  })

  updateUserProperties({ community_joined: true, community_joined_at: new Date().toISOString() })
}

// === community_action ===
// Серверная сторона: Discord bot трекает активность
function trackCommunityAction(actionType: string, channel: string): void {
  posthog.capture('community_action', {
    action_type: actionType, // 'message' | 'reaction' | 'thread' | 'voice_join'
    channel, // 'questions' | 'projects' | 'prompts' | 'general'
  })
}
```

### NPS & Feedback Events

```typescript
// === nps_survey_shown ===
// Вызывать после Module 1 complete или Course complete
function trackNpsSurveyShown(trigger: string, segment: string): void {
  posthog.capture('nps_survey_shown', {
    trigger, // 'module_1_complete' | 'course_complete'
    segment,
  })
}

// === nps_survey_completed ===
function trackNpsSurveyCompleted(score: number, comment: string | null, trigger: string, segment: string): void {
  posthog.capture('nps_survey_completed', {
    score, // 0-10
    comment,
    trigger,
    segment,
  })

  updateUserProperties({ nps_score: score })
}
```

---

## 4. Дашборды

### Дашборд 1: Воронка активации

**Цель:** Видеть конверсию на каждом шаге от лендинга до Aha-момента. Находить узкие места.

**Графики:**

1. **Funnel: Landing -> Aha** (PostHog Funnel Insight)
   - Шаги: `page_viewed` (landing) -> `cta_clicked` (start_free) -> `signup_completed` -> `module_started` (1) -> `video_watched` (1.1) -> `exercise_completed` (describe_product_jobs) -> `prompt_copied` (idea_validator) -> `aha_moment_reached`
   - Группировка: по неделям
   - Фильтры: сегмент, utm_source, device_type

2. **Conversion Rate по шагам** (PostHog Trends)
   - Метрики: CR каждого шага воронки (% от предыдущего)
   - Группировка: по неделям, с трендом
   - Target-линии: signup 20%, module_start 70%, video_1 90%, exercise_1 50%, prompt_copy 60%, aha 40%

3. **Time to Aha** (PostHog Trends)
   - Метрика: медиана и P90 `time_from_signup_seconds` из `aha_moment_reached`
   - Группировка: по сегментам
   - Target-линия: 90 мин

4. **Drop-off Analysis** (PostHog Funnel, breakdown)
   - Куда уходят на каждом шаге: показать top-3 точки потерь
   - Breakdown по: сегмент, device_type, utm_source

5. **Module 1 Completion Funnel** (детальный)
   - Шаги внутри Module 1: video_1.1 -> video_1.2 -> exercise_1 -> video_1.3 (RAT) -> prompt_1 (validator) -> CTA

### Дашборд 2: Когортный анализ retention

**Цель:** Понять, как часто студенты возвращаются к курсу. Определить retention-кривую.

**Графики:**

1. **Cohort Retention Table — Free users** (PostHog Retention)
   - Начальное событие: `signup_completed`
   - Возвратное событие: `session_started`
   - Период: неделя
   - Когорты: по неделе регистрации

2. **Cohort Retention Table — Paid users** (PostHog Retention)
   - Начальное событие: `purchase_completed`
   - Возвратное событие: `session_started` (с любым retention-действием)
   - Период: неделя
   - Когорты: по неделе покупки

3. **Completion Rate по когортам** (PostHog Trends)
   - Метрика: % paid users, достигших `course_completed`
   - Группировка: по когорте покупки (неделя)
   - Target-линия: 35%

4. **Module-to-Module Retention** (PostHog Funnel)
   - Шаги: module_completed(1) -> module_completed(2) -> ... -> module_completed(6)
   - Только для paid users

5. **Activity Heatmap** (PostHog Trends)
   - Метрика: session_started по дням недели и часам
   - Инсайт: когда студенты учатся (оптимальное время для email-nurturing)

### Дашборд 3: Юнит-экономика по когортам

**Цель:** Считать CAC, LTV, ROI по когортам и каналам привлечения.

**Графики:**

1. **Revenue по когортам** (PostHog Trends)
   - Метрика: сумма `price` из `purchase_completed`
   - Группировка: по когорте (неделя signup)
   - Кумулятивно

2. **CAC по каналам** (PostHog Trends + внешние данные)
   - Метрика: Marketing Spend / purchase_completed (по utm_source)
   - Каналы: organic, google_ads, meta_ads, linkedin_ads, content, referral
   - Target-линия: CAC < $50

3. **LTV** (PostHog Trends)
   - Метрика: средний purchase_completed.price по когортам
   - Для v1 (one-time purchase): LTV = цена курса + potential upsell
   - В будущем: + advanced course, + community subscription

4. **LTV/CAC Ratio** (PostHog Trends)
   - Метрика: LTV / CAC по каналам
   - Target-линия: > 4
   - Breakdown по utm_source

5. **Payback Period** (одно число)
   - Для one-time purchase: 0 дней (оплата сразу)
   - Но с учётом refund rate: effective payback = (days_to_refund_window * refund_rate)

6. **Refund Rate по когортам** (PostHog Trends)
   - Метрика: refund_completed / purchase_completed
   - Группировка: по когорте
   - Target: < 5%

### Дашборд 4: Конверсия по сегментам

**Цель:** Сравнить поведение сегментов на каждом шаге воронки. Определить самый ценный сегмент.

**Графики:**

1. **Funnel Conversion by Segment** (PostHog Funnel)
   - Полная воронка: signup -> module_1 -> aha -> purchase -> course_complete
   - Breakdown по `segment` (founder/solopreneur/career_builder/ai_seeker)

2. **Segment Distribution** (PostHog Trends, pie chart)
   - Метрика: signup_completed, breakdown по segment
   - Показать: распределение сегментов среди free users vs paid users

3. **Time to Aha by Segment** (PostHog Trends)
   - Медиана time_from_signup_seconds из aha_moment_reached
   - По каждому сегменту

4. **Free-to-Paid CR by Segment** (PostHog Trends)
   - purchase_completed / signup_completed по сегментам
   - По неделям, с трендом

5. **Completion Rate by Segment** (PostHog Trends)
   - course_completed / purchase_completed по сегментам
   - Target: founder 35%, solopreneur 40%, career_builder 30%, ai_seeker 25%

6. **Revenue by Segment** (PostHog Trends, stacked bar)
   - Суммарный revenue (purchase_completed.price) по сегментам
   - По месяцам

### Дашборд 5: Revenue Breakdown

**Цель:** Полная картина revenue: откуда деньги, тренд, средний чек.

**Графики:**

1. **Total Revenue** (PostHog Trends, big number)
   - Кумулятивный revenue из purchase_completed.price
   - Target: $199K-$399K в год

2. **Paid Students Count** (PostHog Trends, big number)
   - Кумулятивный count purchase_completed
   - Target: 1000 в год

3. **Revenue по неделям** (PostHog Trends, bar chart)
   - Сумма purchase_completed.price по неделям
   - С трендом

4. **Average Revenue Per User (ARPU)** (PostHog Trends)
   - Средний purchase_completed.price
   - По неделям (тренд цены — standard vs premium)

5. **Revenue by Plan** (PostHog Trends, stacked bar)
   - Standard ($199) vs Premium ($399)
   - По месяцам

6. **Revenue by Channel** (PostHog Trends, stacked bar)
   - purchase_completed, breakdown по utm_source_first
   - Определяет самый revenue-эффективный канал

7. **Checkout Conversion** (PostHog Funnel)
   - purchase_initiated -> purchase_completed
   - Drop-off: checkout_abandoned по step_abandoned

8. **Refund Trend** (PostHog Trends)
   - refund_completed count и сумма по неделям
   - + refund rate (refund_completed / purchase_completed)

### Дашборд 6: Aha-момент анализ

**Цель:** Глубокий анализ Aha-момента: кто достигает, что влияет, как оптимизировать.

**Графики:**

1. **Aha-момент Funnel** (PostHog Funnel)
   - Шаги: signup -> exercise_started (describe_product_jobs) -> exercise_completed -> prompt_copied (idea_validator) -> prompt_result_saved -> aha_moment_reached
   - Drop-off на каждом шаге

2. **Aha Rate by Segment** (PostHog Trends)
   - % пользователей, достигших aha_moment_reached, по сегментам
   - Target: 40% от зарегистрировавшихся

3. **Aha -> Purchase Correlation** (PostHog Trends)
   - Два графика: purchase_completed у тех, кто достиг Aha vs кто не достиг
   - Гипотеза: Aha -> 3-5x выше конверсия в покупку

4. **Time to Aha Distribution** (PostHog Trends, histogram)
   - Распределение time_from_signup_seconds для aha_moment_reached
   - Медиана, P25, P75, P90

5. **Exercise 1 Completion Analysis** (PostHog Funnel)
   - exercise_started -> exercise_completed для describe_product_jobs
   - Breakdown по сегменту и device_type
   - input_length_chars distribution (короткие ответы = low engagement)

6. **Prompt Adoption Funnel** (PostHog Funnel)
   - prompt_viewed -> prompt_copied -> prompt_result_saved
   - Для каждого из 9 промптов
   - Какой промпт самый "конвертирующий"

### Дашборд 7: Каналы привлечения

**Цель:** Определить самые эффективные каналы. Оптимизировать маркетинговый бюджет.

**Графики:**

1. **Traffic by Channel** (PostHog Trends, stacked area)
   - page_viewed (landing), breakdown по utm_source
   - Каналы: organic, google_ads, meta_ads, linkedin, twitter, youtube, referral, direct

2. **Signup CR by Channel** (PostHog Trends)
   - signup_completed / page_viewed (landing) по utm_source
   - Показывает качество трафика

3. **Aha CR by Channel** (PostHog Trends)
   - aha_moment_reached / signup_completed по utm_source
   - Показывает качество привлечённых пользователей

4. **Purchase CR by Channel** (PostHog Trends)
   - purchase_completed / signup_completed по utm_source
   - End-to-end конверсия по каналам

5. **CAC by Channel** (PostHog Trends + внешние данные)
   - Marketing Spend / purchase_completed по каналам
   - Требует интеграции данных о расходах

6. **Channel Efficiency Matrix** (таблица)
   - Для каждого канала: Traffic, Signup CR, Aha CR, Purchase CR, CAC, Revenue, ROI
   - Помогает перераспределить бюджет

7. **Landing Page A/B Test Results** (PostHog Experiments)
   - CR по вариантам лендинга (заголовок, CTA, структура)
   - Breakdown по сегментам

---

## 5. Триггеры для автоматических коммуникаций

### Онбординг-триггеры

| # | Триггер | Условие | Действие | Канал | Задержка |
|---|---------|---------|----------|-------|----------|
| O1 | Welcome | `signup_completed` | Приветственное письмо: "Добро пожаловать! Начни Module 1 — ты узнаешь, что такое ценность и опишешь свой продукт через Jobs" | Email | 0 мин |
| O2 | Не начал Module 1 | `signup_completed` + НЕТ `module_started` (1) через 24 часа | "Ты зарегистрировался, но ещё не начал. Module 1 — бесплатный, 60 минут. Первый урок — про то, как Uber и ChatGPT создают ценность" | Email | D+1 |
| O3 | Начал, но не закончил видео 1 | `video_started` (1.1) + НЕТ `video_watched` (1.1) через 48 часов | "Ты начал урок о ценности. Продолжи — через 15 минут ты узнаешь формулу описания Jobs" | Email | D+2 |
| O4 | Посмотрел видео, не сделал упражнение | `video_watched` (1.2) + НЕТ `exercise_started` через 72 часа | "Ты посмотрел уроки — теперь попробуй описать свой продукт через Jobs. Это займёт 10 минут и изменит то, как ты думаешь о продукте" | Email | D+3 |
| O5 | Сделал упражнение, не скопировал промпт | `exercise_completed` + НЕТ `prompt_copied` (idea_validator) через 48 часов | "Ты описал Jobs — отлично! Теперь проверь свою идею за 5 минут: скопируй промпт 'Валидатор идеи' и вставь в Claude/ChatGPT" | Email | D+2 от exercise |
| O6 | Quick win | `exercise_completed` (describe_product_jobs) | In-app сообщение: "Ты описал свой продукт через Jobs. Это больше, чем делают 90% founders. Продолжай!" | In-app | 0 сек |

### Retention-триггеры

| # | Триггер | Условие | Действие | Канал | Задержка |
|---|---------|---------|----------|-------|----------|
| R1 | Неактивный free user (7 дней) | `signup_completed` + НЕТ `session_started` за 7 дней | "Ты начинал Module 1. Следующий шаг — описать работы своего клиента. Это займёт 15 минут" | Email | D+7 |
| R2 | Неактивный paid user (5 дней) | `purchase_completed` + НЕТ `session_started` за 5 дней | "Ты купил курс — в Module [X] тебя ждёт [конкретная ценность]. Продолжи прохождение" | Email | D+5 от последней сессии |
| R3 | Бросил модуль | `drop_off_detected` | "Ты остановился на Module [X]. [Конкретная ценность следующего урока]. Это займёт всего 20 минут" | Email | D+3 от drop_off |
| R4 | Завершил модуль, не начал следующий | `module_completed` (N) + НЕТ `module_started` (N+1) через 5 дней | "Ты прошёл [Module N]. В Module [N+1] ты научишься [конкретная ценность]. Начни сейчас" | Email | D+5 |
| R5 | Завершил половину курса | `progress_milestone_reached` (50%) | In-app: "Ты на полпути! У тебя уже есть [список артефактов]. Осталось 3 модуля до полной системы" | In-app + Email | 0 сек |
| R6 | Высокий риск оттока | `churn_risk_detected` (risk_score > 70) | Персональное письмо: "Мы заметили, что ты давно не заходил. Есть ли сложности? Вот самые полезные материалы из курса: [top-3 промпта]" | Email | 0 мин |

### Upsell-триггеры (Free -> Paid)

| # | Триггер | Условие | Действие | Канал | Задержка |
|---|---------|---------|----------|-------|----------|
| U1 | Aha-момент достигнут | `aha_moment_reached` | In-app CTA: "Ты описал свой продукт и оценил риски. Получи все инструменты: 8 промптов + 2 skills + 5 модулей" | In-app | 0 сек |
| U2 | Module 1 завершён | `module_completed` (1) | Email: "Ты прошёл Module 1 — знаешь про ценность, Jobs и RAT. Module 2 научит найти идеального клиента. $199 — 14 дней money-back" | Email | D+1 |
| U3 | Paywall viewed, но не купил | `paywall_dismissed` | Email: "Ты пытался открыть Module [X]. Вот что внутри: [3 конкретные ценности]. $199 с 14-дневным возвратом" | Email | D+2 |
| U4 | Повторный paywall | `paywall_shown` 3+ раз | In-app: Более сильный CTA + скидка 10% (limited time) | In-app | 0 сек |
| U5 | Использовал 2+ промпта (free) | `prompt_copied` count >= 2 + is_paid = false | Email: "Тебе понравились промпты Module 1. В полном курсе ещё 8 промптов + 2 Claude Code skills для создания лендинга и PRD" | Email | D+1 |
| U6 | Email nurturing — серия | `signup_completed` + is_paid = false | Серия из 5 писем с дополнительной ценностью: D+3 (кейс студента), D+7 (бесплатный мини-урок), D+10 (social proof), D+14 (скидка), D+21 (last chance) | Email | Серия |

### Referral-триггеры

| # | Триггер | Условие | Действие | Канал | Задержка |
|---|---------|---------|----------|-------|----------|
| Ref1 | Высокий NPS | `nps_survey_completed` (score >= 9) | "Рад, что тебе нравится! Поделись с другом — получи 20% скидку на следующий курс" | Email + In-app | D+1 |
| Ref2 | Курс завершён | `course_completed` | "Поздравляем! Ты прошёл весь курс. Поделись результатом в LinkedIn/Twitter. Вот шаблон поста" | Email | D+1 |
| Ref3 | Промпт дал отличный результат | `prompt_result_saved` + высокий input_length (> 500 chars) | In-app: "Отличный результат! Поделись промптом с коллегами" + кнопка Share | In-app | 0 сек |

### Расчёт churn_risk_score (серверная логика)

```typescript
// === Churn Risk Score Calculator ===
// Запускается ежедневным cron-ом для каждого пользователя

interface UserActivity {
  daysSinceLastSession: number
  isPaid: boolean
  modulesCompleted: number
  totalModules: number
  exercisesCompleted: number
  promptsCopied: number
  ahaReached: boolean
  communityJoined: boolean
  emailsOpened: number
  emailsSent: number
}

function calculateChurnRiskScore(activity: UserActivity): number {
  let score = 0

  // Фактор 1: Дни неактивности (0-40 баллов)
  if (activity.daysSinceLastSession > 30) score += 40
  else if (activity.daysSinceLastSession > 14) score += 30
  else if (activity.daysSinceLastSession > 7) score += 20
  else if (activity.daysSinceLastSession > 3) score += 10

  // Фактор 2: Прогресс (0-25 баллов, больше = меньше риск)
  const progressRatio = activity.modulesCompleted / activity.totalModules
  if (progressRatio === 0) score += 25
  else if (progressRatio < 0.25) score += 15
  else if (progressRatio < 0.5) score += 10
  // > 50% прогресс = 0 баллов риска

  // Фактор 3: Engagement (0-20 баллов)
  if (activity.exercisesCompleted === 0 && activity.promptsCopied === 0) score += 20
  else if (activity.exercisesCompleted === 0 || activity.promptsCopied === 0) score += 10

  // Фактор 4: Aha-момент (0-10 баллов)
  if (!activity.ahaReached) score += 10

  // Фактор 5: Email engagement (0-5 баллов)
  if (activity.emailsSent > 0 && activity.emailsOpened === 0) score += 5

  return Math.min(score, 100)
}

// Пороги:
// 0-30: Низкий риск — нет действий
// 31-60: Средний риск — мягкий nudge email
// 61-80: Высокий риск — персональное письмо + in-app notification
// 81-100: Критический — агрессивная реактивация + special offer
```

---

## 6. Приложение: Маппинг событий на воронку

### Полная воронка с Target CR

```
Landing Page Visit (page_viewed, landing)
  |
  ├── CR: 20% ─────> Signup (signup_completed)
  |                      |
  |                      ├── CR: 70% ───> Module 1 Started (module_started, 1)
  |                      |                    |
  |                      |                    ├── CR: 90% ───> Video 1.1 Watched
  |                      |                    |                    |
  |                      |                    |                    ├── CR: 85% ──> Video 1.2 Watched
  |                      |                    |                    |                   |
  |                      |                    |                    |                   ├── CR: 50% ──> Exercise 1 Done
  |                      |                    |                    |                   |                  |
  |                      |                    |                    |                   |                  ├── CR: 70% ──> Prompt Copied
  |                      |                    |                    |                   |                  |                 |
  |                      |                    |                    |                   |                  |                 ├── CR: 80% ──> Aha Reached
  |                      |                    |                    |                   |                  |                 |                 |
  |                      |                    |                    |                   |                  |                 |                 ├── CR: 60% ──> Module 1 Complete
  |                      |                    |                    |                   |                  |                 |                 |                  |
  |                      |                    |                    |                   |                  |                 |                 |                  ├── CR: 15% ──> Purchase
  |                      |                    |                    |                   |                  |                 |                 |                  |               |
  |                      |                    |                    |                   |                  |                 |                 |                  |               ├── CR: 35% ──> Course Complete
```

### End-to-end метрики (Target Year 1)

| Метрика | Target | Формула |
|---------|--------|---------|
| Landing visitors | 50,000+ | page_viewed (landing) |
| Signups | 10,000+ | signup_completed (CR 20%) |
| Module 1 Started | 7,000+ | module_started (CR 70%) |
| Aha Reached | 2,100+ | aha_moment_reached (CR 30% от signup) |
| Module 1 Completed | 3,500+ | module_completed (CR 50% от started) |
| Purchases | 1,000+ | purchase_completed (CR 10% от signup) |
| Course Completed | 350+ | course_completed (CR 35% от purchase) |
| Revenue | $199K-$399K | 1000 x $199-399 |
| CAC | < $50 | marketing_spend / purchases |
| LTV/CAC | > 4 | $199-399 / $50 |
| NPS (Module 1) | > 40 | nps_survey_completed |
| NPS (Full Course) | > 50 | nps_survey_completed |
| Referral Rate | > 10% | referral_sent / course_completed |

### North Star Metric

**Количество студентов, завершивших курс И применивших frameworks к своему продукту.**

Прокси-метрика в PostHog: `course_completed` WHERE `exercises_completed_count >= 4` AND `prompts_used_count >= 3`

Target: 250+ в первый год (из 350+ завершивших, 70% применили на практике).
