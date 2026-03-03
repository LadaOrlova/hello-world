# Доменная модель (Domain Model)

> Часть архитектуры Zamesin IS.
> Основной документ: [PLAN.md](../PLAN.md) | Архитектура: [02-architecture.md](02-architecture.md)

Все таблицы создаются сразу (Prisma migrate). Бизнес-логика и API реализуются поэтапно.
Этап реализации указан в скобках: **[1]** — ядро, **[2]** — автоматизация, **[3]** — аналитика, **[F]** — будущая фаза.

---

## Люди и организации

### Аутентификация: better-auth

Аутентификация реализована через библиотеку [better-auth](https://www.better-auth.com/) с плагинами:

- **Email OTP** — вход по email + 6-значный код (без паролей)
- **Admin** — управление ролями, бан, импersonation
- **Bearer** — API-аутентификация через токен (для ботов/агентов)

better-auth управляет 4 таблицами (`user`, `session`, `account`, `verification`).
Наши кастомные поля добавляются в `user` через `additionalFields`.

```
User (Пользователь — better-auth + кастомные поля) [1]
├── id (string, PK — генерируется better-auth)
├── name, email (unique)
├── emailVerified (boolean — better-auth)
├── image (nullable — better-auth)
├── role: admin | manager | curator | student (better-auth admin plugin)
├── banned, banReason, banExpires (better-auth admin plugin)
├── phone (кастомное)
├── telegram_user_id (числовой, стабильный — не username!)
├── telegram_username (отображаемый, может меняться)
├── preferred_channel: telegram | email
├── timezone (напр. "Europe/Moscow")
├── (is_alumni — вычисляется: EXISTS(Enrollment WHERE user_id = ? AND status = 'completed'))
└── created_at, updated_at, deleted_at (soft delete — единственный индикатор деактивации)

Session (Сессия — better-auth) [1]
├── id (string, PK)
├── userId (FK → User)
├── token (unique)
├── expiresAt
├── ipAddress, userAgent (nullable)
├── impersonatedBy (string, nullable — admin plugin: кто имперсонирует)
└── createdAt, updatedAt
│
│   better-auth хранит сессии в БД (не stateless JWT).
│   Преимущества: отзыв сессий, импersonation, аудит активных сессий.
│   При деактивации User (deleted_at IS NOT NULL) или бане — сессии отзываются.

Account (Аккаунт провайдера — better-auth) [1]
├── id (string, PK)
├── userId (FK → User)
├── accountId, providerId (для email OTP: providerId = "email-otp")
├── accessToken, refreshToken (nullable)
├── accessTokenExpiresAt, refreshTokenExpiresAt (nullable)
├── scope, idToken, password (nullable)
└── createdAt, updatedAt
│
│   Для email OTP: одна запись на пользователя с providerId = "email-otp".
│   В будущем можно добавить OAuth-провайдеры (Google, GitHub) без миграций.

Verification (Верификация / OTP-коды — better-auth) [1]
├── id (string, PK)
├── identifier (email)
├── value (OTP-код или токен)
├── expiresAt
└── createdAt, updatedAt
│
│   Заменяет бывшую таблицу OtpCode.
│   better-auth управляет созданием, проверкой, TTL и rate limiting.
│   Настройки: otpLength=6, expiresIn=300с, allowedAttempts=5.

Company (Компания B2B) [1]
├── id, name, inn, kpp
├── legal_name, legal_address
├── contact_person_id (FK → User, любая роль — HR, руководитель, студент)
├── account_manager_id (FK → User, менеджер со стороны Замесина)
├── billing_info (реквизиты для выставления счетов)
└── created_at, updated_at, deleted_at (soft delete)
│
│   Доступ к B2B-кабинету: не по роли, а по связи Company.contact_person_id = user.id
│   Контактное лицо может одновременно быть студентом (роль student)
│   В Lead-first flow карточка Company создаётся только после approve B2B Lead
│   (на этапе заявки хранится только Lead source=b2b + b2bApplication payload)
│   Компания владеет кадровым контуром через CompanyEmployee и заявками
│   на обучение через CompanyRequest.
│
CompanyEmployee (Сотрудник компании B2B) [NEW]
├── id, company_id, user_id (nullable)
├── full_name, corporate_email, phone, position
├── metadata (JSON), deleted_at
└── UNIQUE(company_id, corporate_email)
│
│   user_id = null для сотрудников, ещё не зарегистрированных в системе.
│   После массового создания пользователей user_id заполняется.
```

## Продукты и обучение

```
Product (Продукт / Курс) [1]
├── id, title, slug, description
├── landing_url
├── type: course | subscription   (intensive = course с коротким duration_days)
├── duration_days (длительность в днях — универсальная единица, отображение в UI)
└── deleted_at (soft delete — единственный индикатор деактивации)

Tier (Тариф) [1]
├── id, product_id, title, price_rub
├── price_usd (nullable, для валютных платежей — будущее)
├── tier_type: standard | advanced | with_author | team
├── features[] — что входит (JSON)
├── upgrade_to_tier_id (FK → Tier, nullable — для апгрейдов)
├── telegram_chats[] — в какие чаты добавлять (JSON: массив TelegramChat ID; при резолве — фильтр по cohort_id: см. 03-data-flows)
├── max_students (для командного тарифа)
└── deleted_at (soft delete)

Cohort (Поток) [1]
├── id, product_id, title (напр. "Поток 12")
├── number (номер потока)
├── start_date, end_date
├── status: planned | enrolling | active | completed
├── max_students
└── deleted_at (soft delete)

Enrollment (Зачисление) [1]
├── id, user_id (student), cohort_id, tier_id
├── order_id (FK → Order, обязательно)
├── company_id (nullable — для B2B)
├── status: pending | active | upgraded | completed | refunded | suspended
├── enrolled_at, completed_at
├── price_snapshot (цена на момент зачисления — защита от изменения тарифов)
├── price_snapshot_currency (валюта: "RUB" | "USD", default "RUB")
├── materials_access_expires_at (доступ к материалам: null = вечный к записям потока)
├── support_expires_at (доступ к куратору и обновлениям: 1 год с enrolled_at)
├── lms_access_granted, tg_added, calendar_subscribed
├── certificate_id (FK → Certificate, nullable)
└── UNIQUE(user_id, cohort_id) — нельзя зачислить дважды в один поток
│
│   Инвариант: Enrollment создаётся только после подтверждённой оплаты
│   (B2C: Payment.status=success; B2B: Invoice.status=paid + linked Order.status=paid).
```

## LMS (контент и обучение)

```
Module (Модуль курса) [1]
├── id, product_id, title
├── position (порядок — для drag-and-drop)
├── type: main | workshop | interview | demo | case
└── deleted_at (soft delete)

Lesson (Урок / Материал — метаданные) [1]
├── id, module_id, title
├── type: text | video | text_video
├── current_revision_id (FK → LessonRevision — указатель на SoK, текущая версия контента)
├── position (порядок внутри модуля)
├── deadline_at (опциональный дедлайн)
├── is_new (метка "новый контент")
├── available_for_tiers[] — для каких тарифов доступно (JSON)
└── deleted_at (soft delete)
│
│   content, video_url, duration_minutes переехали в LessonRevision.
│   Lesson хранит метаданные, LessonRevision — контент.
│   См. docs/11-content-versioning.md

LessonRevision (Ревизия урока — хранит контент) [1]
├── id, lesson_id (FK → Lesson)
├── revision_number (auto-increment per lesson)
├── content (markdown)
├── video_url (Kinescope embed)
├── duration_minutes
├── change_summary (что изменилось — для diff-лога)
├── created_by (FK → User)
├── created_at
└── UNIQUE(lesson_id, revision_number)
│
│   Каждое редактирование урока создаёт новую ревизию.
│   Lesson.current_revision_id → актуальная версия (SoK).
│   Ревизии не удаляются (append-only, как git commits).

CohortContent (Снимок контента потока — fork SoK) [2]
├── id, cohort_id (FK → Cohort), lesson_id (FK → Lesson)
├── pinned_revision_id (FK → LessonRevision)
├── is_synced (boolean — совпадает ли с Lesson.current_revision_id)
├── synced_at
└── UNIQUE(cohort_id, lesson_id)
│
│   При создании потока → fork: CohortContent для каждого урока.
│   Студент видит pinned_revision_id своего потока.
│   Auto-sync: pg-boss cron обновляет eligible потоки.
│   Менеджер может: sync вручную, откатить на предыдущую ревизию.
│   См. docs/11-content-versioning.md

Progress (Прогресс студента) [1]
├── id, enrollment_id, lesson_id
├── status: not_started | in_progress | completed
├── completed_at
├── time_spent_seconds
└── UNIQUE(enrollment_id, lesson_id)
│
│   Связь со студентом — через enrollment_id (→ Enrollment.user_id).
│   Дизайн: прогресс привязан к зачислению, а не к User, т.к.
│   студент может проходить курс повторно в другом потоке.

Homework (Домашнее задание) [2]
├── id, lesson_id, title, description
├── deadline_days (дней после открытия доступа)
└── deleted_at (soft delete)

HomeworkSubmission (Сдача ДЗ) [2]
├── id, homework_id, enrollment_id
├── content (текст ответа)
├── status: submitted | reviewed | revision_needed | accepted
├── reviewer_id (FK → User, куратор)
├── feedback (текст обратной связи от куратора)
├── submitted_at, reviewed_at
└── UNIQUE(homework_id, enrollment_id) — одна сдача на ДЗ на студента
│
│   Связь со студентом — через enrollment_id (→ Enrollment.user_id).
│   Аналогично Progress: привязка к зачислению обеспечивает
│   корректную работу при повторном прохождении курса.
```

## Расписание и занятия

```
Schedule (Занятие-воркшоп / Zoom-встреча) [2]
├── id, cohort_id, title, description
├── lesson_type: lecture | workshop | elective | qa_session
├── scheduled_at, duration_minutes
├── zoom_meeting_id, zoom_join_url
├── recording_url (kinescope)
├── calendar_event_id
└── available_for_tiers[] — для каких тарифов доступно (JSON)

CuratorGroup (Группа куратора) [2]
├── id, cohort_id, curator_id (FK → User)
└── students[] → Enrollment[]

Attendance (Посещение) [2]
├── id, schedule_id, enrollment_id
├── status: present | absent | late
└── recorded_at
```

## CRM (продажи)

```
Lead (Лид / Сделка — объединённая сущность) [1]
├── id, name, email, phone, telegram
├── company_name (для B2B-лидов)
├── source: typeform | website | instagram | partner | referral | telegram_bot | diagnostic | manual
├── product_id (интересующий продукт)
├── tier_id (FK → Tier, nullable — конкретный тариф, для B2B/переговоров)
├── amount (nullable — сумма сделки, для B2B/переговоров)
├── status: new | qualified | negotiation | proposal | converted | lost | reject
├── close_probability (nullable, % вероятности — для B2B)
├── expected_close_date (nullable — для B2B)
├── assigned_manager_id (FK → User)
├── converted_to_user_id (FK → User, nullable)
├── dedup_key (hash от нормализованного email+phone)
├── notes, utm_tags (JSON: {source, medium, campaign, content, term})
├── ym_client_id (nullable — Яндекс Метрика _ym_uid, для сквозной аналитики) [2]
├── yclid (nullable — Яндекс Директ click ID, для Offline Conversions) [2]
├── last_contacted_at
├── created_at, updated_at
└── При деактивации менеджера → auto-reassign на admin
│
│   Объединяет бывшие Lead и Deal в одну сущность (CHG-016).
│   Для B2B воронка: new → qualified → negotiation → proposal.
│   Решение модерации: converted (одобрено) или reject (отклонено менеджером).
│   Для B2C лид может идти напрямую: qualified → converted.
│   Поля tier_id, amount, close_probability, expected_close_date обычно
│   заполняются на этапах negotiation/proposal.
```

## Финансы и биллинг

```
Order (Заказ / Покупка) [1]
├── id, user_id, product_id, tier_id, cohort_id
├── type: b2c | b2b
├── company_id (FK → Company, для B2B)
├── amount_rub, currency
├── payment_method: card | installment | invoice | stripe
├── status: pending | paid | refunded | cancelled
├── paid_at
└── created_at, updated_at

Payment (Платёж) [1]
├── id, order_id (FK → Order)
├── provider: yookassa | tbank | stripe
├── provider_payment_id (UNIQUE — дедупликация webhook'ов)
├── amount, currency
├── status: pending | success | failed | refunded
├── idempotency_key (защита от двойного нажатия "Оплатить")
├── receipt_url (ссылка на фискальный чек — 54-ФЗ, приходит от провайдера)
├── metadata (JSON)
└── created_at
│
│   receipt_url: ссылка на онлайн-чек (ОФД), обязательна по 54-ФЗ.
│   Приходит в webhook от ЮKassa/Т-Банк после фискализации.
│   Хранится для: переотправки клиенту, бухгалтерского учёта, аудита.

Invoice (Счёт для B2B) [1]
├── id, company_id, contract_id (FK → Contract, required)
├── invoice_number
├── amount, vat_amount, total_amount
├── document_url (PDF)
├── status: draft | sent | paid | overdue | cancelled
├── sent_at, paid_at, due_date
└── paid_amount (для отслеживания частичных оплат)
│
│   Счет всегда создается на основании конкретного договора (contract-first).
│   Для batch B2B связь с заказами через Order.invoice_id (1 invoice → N order).
│
CompanyRequest (Заявка компании на обучение) [NEW]
├── id, company_id, invoice_id (FK, required, UNIQUE)
├── product_id, cohort_id
├── unit_price, employees_count, discount_amount, total_amount, currency
├── status:
│   draft | submitted | invoiced | paid | users_created |
│   enrollments_started | fulfilled | cancelled | failed
├── override_allowed, override_by_id, override_at
├── created_by_id, submitted_at, paid_at, fulfilled_at
├── notes, metadata
└── created_at, updated_at
│
│   Header заявки: операционный контур исполнения, не заменяет Invoice.
│   Invoice отвечает за юридико-финансовый статус оплаты и связан с Contract.
│
CompanyRequestEmployee (Строка заявки компании) [NEW]
├── id, request_id, company_employee_id
├── full_name_snapshot, corporate_email_snapshot, phone_snapshot
├── status: selected | user_created | order_created | enrolled | skipped | failed
├── user_id, order_id, enrollment_id (nullable FK)
├── error_reason, metadata
└── UNIQUE(request_id, company_employee_id)

Contract (Договор для B2B) [2]
├── id, company_id (FK → Company)
├── order_id (FK → Order, nullable — может быть рамочный без заказа)
├── contract_number
├── type: service | framework (разовый или рамочный)
├── subject (предмет договора: описание услуг)
├── amount, currency
├── document_url (PDF — сгенерированный или загруженный из ЭДО)
├── external_doc_id (nullable — ID документа во внешней системе ЭДО, если договоры ведутся вне системы)
├── status: draft | sent | signed | active | expired | cancelled
├── signed_at, valid_from, valid_until
└── created_at, updated_at
│
│   ⚠️ Уточнить у заказчика: договоры формируются в системе (PDF-генерация)
│   или во внешней системе ЭДО? Если ЭДО — сущность хранит ссылку
│   (external_doc_id + document_url) и отслеживает статус.

Act (Акт выполненных работ) [3]
├── id, invoice_id (UNIQUE)
├── document_url (PDF)
├── status: draft | signed
└── generated_at
│
│   Инвариант: 1 Invoice -> 1 Act.
│   Акт закрывает весь оплаченный счет как единый отчетный документ.

PromoCode (Промокод) [2]
├── id, code (UNIQUE)
├── type: discount_percent | discount_fixed | bonus_subscription
├── value (скидка или кол-во месяцев подписки)
├── referrer_user_id (FK → User, кто получает бонус, nullable)
├── referrer_bonus_type, referrer_bonus_value
├── product_id (для какого продукта, null = все)
├── usage_limit, usage_count
├── valid_from, valid_until
├── deleted_at (soft delete)
└── applicable_tiers[] (JSON)

Subscription (Подписка AURA/Maker) [3]
├── id, user_id
├── plan: maker | founder
├── status: active | paused | cancelled | expired
├── source: purchase | bonus | post_course
├── source_order_id (FK → Order, nullable)
├── started_at, next_payment_date, expires_at
├── is_recurring (boolean)
├── payment_method
├── consent_given_at (обязательное явное согласие)
├── price_at_subscription (цена на момент оформления)
└── UNIQUE(user_id) при status IN ('active', 'paused') — только одна активная подписка
```

## Telegram-интеграция

```
TelegramChat (Telegram чат/канал) [1]
├── id, telegram_chat_id (Telegram ID чата)
├── type: chat | channel
├── name, invite_link (постоянная)
├── product_id (FK → Product, nullable)
├── cohort_id (FK → Cohort, nullable)
├── purpose: general | workshop | premium | base_channel | premium_channel | alumni | respondents
└── deleted_at (soft delete)

TelegramAccount (Telegram аккаунт пользователя) [1]
├── id, user_id (FK → User)
├── telegram_user_id (числовой Telegram ID)
├── username
└── linked_at

ChatMembership (Членство в чате) [1]
├── id, user_id (FK → User), telegram_chat_id (FK → TelegramChat)
├── status: pending | joined | left | kicked
├── should_be_member (boolean — рассчитывается из enrollment + tier)
├── joined_at, left_at
└── UNIQUE(user_id, telegram_chat_id)
```

## Обратная связь

```
FeedbackCampaign (Кампания сбора ОС) [3]
├── id, cohort_id, title
├── trigger: after_lesson | mid_course | end_course | manual
├── target_lesson_id (nullable)
├── questions[] (JSON — вопросы анкеты, включая NPS)
├── send_via: telegram | email | both
├── status: draft | scheduled | active | completed
└── scheduled_at

FeedbackResponse (Ответ на ОС) [3]
├── id, campaign_id, enrollment_id
├── UNIQUE(campaign_id, enrollment_id)
├── answers (JSON), nps_score
├── ai_summary (nullable — graceful degradation при недоступности LLM)
└── submitted_at
```

## Сертификаты

```
Certificate (Сертификат) [3]
├── id, enrollment_id, user_id
├── certificate_number (UUID)
├── template_id
├── document_url (PDF)
├── qr_code_url (для верификации)
├── issued_at
└── verification_url
```

## Событийная аналитика

```
Event (Событие) [1]
├── id, user_id (nullable — для системных событий)
├── event_type (строка: "lesson_completed", "payment_success", "chat_joined" и т.д.)
├── event_data (JSON — произвольные данные события)
├── product_id, cohort_id (контекст, nullable)
├── source: lms | bot | landing | payment | agent | system
├── session_id (nullable)
└── created_at

Категории событий:
  LMS:      lesson_opened, lesson_completed, video_watched, homework_submitted, homework_reviewed
  Billing:  order_created, payment_success, payment_failed, refund_initiated, upgrade_completed
  Telegram: chat_joined, chat_left, chat_kicked, onboarding_started, onboarding_completed
  CRM:      lead_created, lead_contacted, lead_converted, lead_lost
  Auth:     user_registered, user_logged_in, otp_sent
  Bot:      bot_started, bot_message_received, warmup_funnel_step
  Agent:    agent_action_completed, agent_error
```

## Очередь задач и системные

```
Job (Задача в очереди) [1]
├── Управляется pg-boss (таблица создаётся автоматически)
├── name (тип задачи: "onboarding.grant_lms", "payment.process_webhook" и т.д.)
├── data (JSON — входные данные)
├── state: created | active | completed | failed | expired
├── retry_count, retry_limit
├── expire_in (timeout — если задача зависла)
├── start_after (для отложенных задач)
├── completed_on, started_on, created_on
└── output (JSON — результат или ошибка)
│
│   pg-boss из коробки обеспечивает:
│   - Идемпотентность через singletonKey
│   - Retry с экспоненциальным backoff
│   - Dead letter (expired jobs)
│   - Distributed lock (FOR UPDATE SKIP LOCKED)
│   - Cron-задачи (schedules)
└── Не нужно реализовывать вручную: heartbeat, watchdog, приоритеты

Process (Бизнес-процесс) [1]
├── id, type: onboarding | offboarding | feedback_collection | payment_flow | lesson_setup
├── entity_type, entity_id (напр. "enrollment", 123)
├── status: running | completed | failed | partially_failed
├── steps (JSON — упорядоченный массив шагов с их статусами)
│   └── [{name: "grant_lms", status: "completed", job_id: "...", error: null}, ...]
├── started_at, completed_at
├── initiated_by (User ID)
└── metadata (JSON)

Notification (Уведомление) [2] — реализуется как Job
├── id, user_id, channel: telegram | email
├── type: onboarding | reminder | feedback_request | payment | certificate | homework
├── content, status: queued | sent | delivered | failed
└── sent_at

AuditLog (Журнал действий) [1]
├── id, user_id, action, entity_type, entity_id
├── changes (JSON diff)
├── source: web | api_token | system | agent
└── created_at

WebhookLog (Журнал входящих webhook'ов) [1]
├── id, source: yookassa | typeform | tbank | stripe | kinescope
├── raw_payload (JSON)
├── processed_at
└── error (nullable)

ApiToken (API-токен для агентов) [F]
├── id, user_id, name, token_hash
├── scopes (JSON), expires_at
├── last_used_at
└── deleted_at (soft delete)
```

### Что НЕ хранится в БД

**Операционные логи** (application logs) — вместо таблицы в PostgreSQL используются структурированные логи через Pino:

- JSON-формат с `trace_id` (= process_id или job_id)
- Уровни: debug, info, warn, error
- Пишутся в stdout → агрегируются через файл/Datadog/Loki
- Добавить OpenTelemetry позже — без миграции БД

> AuditLog — это журнал аудита (кто что изменил), а не операционные логи. Он хранится в БД.

---

### Принципы работы очереди задач (pg-boss)

**Идемпотентность**: pg-boss поддерживает `singletonKey` — если задача с таким ключом уже существует (в любом состоянии), дубль не создаётся:

- `onboarding.grant_lms:enrollment:123` — если уже выполнена, повторная → no-op
- `payment.create_zoom:lesson:456` — если встреча уже создана, возвращаем существующий ID

**Retry с экспоненциальным backoff**:

- pg-boss поддерживает `retryLimit` + `retryBackoff: true`
- По умолчанию: 5 попыток с экспоненциальным backoff
- После исчерпания попыток → задача в state `expired` (dead letter)

**Dead Jobs**: Задачи в state `expired` или `failed` — аналог dead letter queue.
Менеджер/админ в дэшборде может: посмотреть ошибку, ретраить вручную, пометить как resolved.

**Timeout**: `expireInMinutes` вместо heartbeat — если задача не завершилась за N минут, pg-boss автоматически переводит её в failed и ретраит.

---

### Связь Event ↔ AuditLog

- **Event** — событийная аналитика (для дашбордов, метрик, воронок). Пишется автоматически при каждом действии. Не удаляется. На этапе роста можно вынести в ClickHouse/TimescaleDB.
- **AuditLog** — журнал действий пользователей (кто что изменил). Для аудита и отладки. Содержит JSON diff изменений.

Оба пишутся параллельно, но для разных целей.
