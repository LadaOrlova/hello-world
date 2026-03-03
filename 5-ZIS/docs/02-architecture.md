# Высокоуровневая архитектура системы

> Часть архитектуры Zamesin IS.
> Основной документ: [PLAN.md](../PLAN.md) | Доменная модель: [01-domain-model.md](01-domain-model.md)

---

## Общая схема

```
┌─────────────────────────────────────────────────────────────────────┐
│                        КЛИЕНТЫ (Consumers)                         │
│                                                                     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐              │
│  │  Web App      │  │  TG Bot       │  │  MCP / CLI   │              │
│  │  (Next.js)    │  │  (grammY)     │  │  (будущее)   │              │
│  │              │  │              │  │              │              │
│  │  Студент:    │  │  Уведомления │  │  AI-агенты,  │              │
│  │  - LMS       │  │  студентам,  │  │  автоматиза- │              │
│  │  - прогресс  │  │  сбор ОС,    │  │  ции, батчи  │              │
│  │  - ДЗ        │  │  онбординг,  │  │              │              │
│  │              │  │  прогрев,    │  │              │              │
│  │  Менеджер:   │  │  контроль    │  │              │              │
│  │  - дэшборд   │  │  доступа     │  │              │              │
│  │  - CRM       │  │              │  │              │              │
│  │  - биллинг   │  │              │  │              │              │
│  │  - контент   │  │              │  │              │              │
│  │              │  │              │  │              │              │
│  │  B2B-кабинет:│  │              │  │              │              │
│  │  - счета     │  │              │  │              │              │
│  │  - сотрудники│  │              │  │              │              │
│  │              │  │              │  │              │              │
│  │  Куратор:    │  │              │  │              │              │
│  │  - прогресс  │  │              │  │              │              │
│  │  - ДЗ        │  │              │  │              │              │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘              │
│         │                 │                 │                       │
└─────────┼─────────────────┼─────────────────┼───────────────────────┘
          │                 │                 │
          ▼                 ▼                 ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     API LAYER (tRPC + Prisma)                      │
│                                                                     │
│  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐      │
│  │ users      │ │ billing    │ │ lms        │ │ telegram   │      │
│  │ (auth,     │ │ (orders,   │ │ (modules,  │ │ (chats,    │      │
│  │  profiles, │ │  payments, │ │  lessons,  │ │  members,  │      │
│  │  companies)│ │  invoices, │ │  progress, │ │  bot)      │      │
│  │            │ │  promos)   │ │  homework) │ │            │      │
│  └────────────┘ └────────────┘ └────────────┘ └────────────┘      │
│  ┌────────────┐ ┌────────────┐ ┌────────────┐ ┌────────────┐      │
│  │ crm        │ │ analytics  │ │ content    │ │ webhooks   │      │
│  │ (leads,    │ │ (events,   │ │ (editor,   │ │ (ЮKassa,   │      │
│  │  pipeline) │ │  dashboards│ │  templates)│ │  TypeForm, │      │
│  │            │ │  reports)  │ │            │ │  Kinescope)│      │
│  └────────────┘ └────────────┘ └────────────┘ └────────────┘      │
│                                                                     │
│  API выполняет:                                                     │
│  1. Синхронную бизнес-логику (CRUD, валидация) → 200 OK            │
│  2. Ставит фоновые задачи в pg-boss для тяжёлых/внешних операций  │
│     → 202 Accepted + { process_id } для отслеживания               │
│  3. Записывает Event в таблицу events при каждом действии          │
│  4. Webhook acknowledgment → 200 OK (синхронная обработка)         │
│                                                                     │
└──────────────────────────┬──────────────────────────────────────────┘
                           │
                    ┌──────┴──────┐
                    │  pg-boss    │
                    │  (Job Queue │
                    │  в PostgreSQL)
                    └──────┬──────┘
                           │
                           ▼
                  ┌──────────────────┐
                  │  Worker          │
                  │  (один процесс)  │
                  │                  │
                  │  Обрабатывает    │
                  │  все очереди:    │
                  │  - onboarding.*  │
                  │  - payment.*     │
                  │  - notification.*│
                  │  - schedule.*    │
                  │  - feedback.*    │
                  │  - certificate.* │
                  │  - access.*      │
                  │  - homework.*    │
                  │  - lms.inactive.*│
                  └──────┬──────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     ИНФРАСТРУКТУРА                                  │
│                                                                     │
│  ┌──────────────────┐  ┌──────────────────────────────────────┐    │
│  │  PostgreSQL       │  │  Внешние сервисы                     │    │
│  │                  │  │                                      │    │
│  │  - Данные        │  │  ЮKassa, Т-Банк, Stripe (будущее),  │    │
│  │  - Jobs (pg-boss)│  │  Telegram API (grammY),              │    │
│  │  - Processes     │  │  Zoom API, Google Calendar,          │    │
│  │  - Events        │  │  Kinescope, Mailgun,                 │    │
│  │  - AuditLog      │  │  LLM API, S3 (Yandex Object Storage)│    │
│  │  - WebhookLog    │  │                                      │    │
│  └──────────────────┘  └──────────────────────────────────────┘    │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │  Логирование: Pino (structured JSON logs → stdout)           │   │
│  │  trace_id привязывает логи к process_id / job_id       │   │
│  └──────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

## Модульный монолит — структура

Каждый модуль = папка со своими tRPC-роутерами и сервисами. Модули вызывают сервисы друг друга напрямую, а асинхронную работу ставят через pg-boss jobs в транзакции.

```
src/
├── server/
│   ├── db/                 # Prisma schema, migrations
│   ├── trpc/routers/       # tRPC роутеры по модулям
│   │   ├── users.ts
│   │   ├── billing.ts
│   │   ├── lms.ts
│   │   ├── telegram.ts
│   │   ├── crm.ts
│   │   ├── analytics.ts
│   │   └── content.ts
│   ├── services/           # Бизнес-логика по модулям
│   │   ├── users/
│   │   ├── billing/
│   │   ├── lms/
│   │   ├── telegram/
│   │   ├── crm/
│   │   └── analytics/
│   └── integrations/       # Обёртки внешних API
│       ├── yookassa/
│       ├── tbank/
│       ├── mailgun/
│       ├── kinescope/
│       ├── zoom/
│       └── telegram/
├── bot/                    # Telegram bot (grammY)
│   ├── index.ts
│   ├── commands/
│   ├── conversations/      # Воронки (прогрев, онбординг)
│   └── middleware/
├── app/                    # Next.js pages (App Router)
│   ├── (student)/          # LMS для студентов
│   ├── (admin)/            # Админка для менеджеров
│   ├── (auth)/             # OTP-авторизация
│   ├── (onboarding)/       # Онбординг-страница после оплаты
│   ├── (company)/          # B2B-кабинет компании
│   └── api/                # API endpoints (tRPC, webhooks)
└── shared/                 # Общие типы, утилиты
```

## DTO и границы слоёв

Чтобы не протекала внутренняя модель БД в API и интеграции, используем явные DTO-контракты.

**Правила:**

1. Внешний вход (Web App, Bot, Webhook, CLI/agent) валидируется через transport DTO-схемы в `src/server/dto/trpc/*` (или профильном DTO-файле transport-слоя).
2. tRPC-роутер принимает `Input DTO`, передаёт в сервис только типизированные данные (без `unknown`/raw payload).
3. Сервис работает с `Command DTO`/`Query DTO` и не зависит от transport-слоя (tRPC/HTTP/Telegram).
4. Prisma-модели не возвращаются клиенту напрямую; наружу отдаётся `Response DTO` (явный `select` + mapper).
5. Чувствительные поля (`token`, `password`, `secret`, `raw_payload`) редактируются в DTO для логов/Audit/Event.

**Текущая реализация (WP-001..WP-005):**

```
src/server/dto/trpc/{module}.ts      # Input/Output DTO для transport-границы
src/server/dto/events.ts             # DTO payload для Event-записей в БД
src/server/dto/worker.ts             # DTO envelope для worker jobs
```

**Целевая структура для доменных модулей (Phase 1+):**

```
src/server/dto/trpc/{module}.ts        # Zod input/output DTO transport-слоя
src/server/services/{module}/dto.ts   # Command/Query DTO для сервиса
src/server/services/{module}/mappers.ts # Prisma -> Response DTO
```

**Поток данных:**

```
Client -> Input DTO (Zod) -> Router -> Service DTO -> Prisma
Prisma result -> Mapper -> Response DTO -> Client
```

### Naming conventions

| Артефакт | Паттерн | Пример |
|---|---|---|
| Transport input | `{Entity}{Action}RequestDtoSchema` | `UserCreateRequestDtoSchema` |
| Transport output | `{Entity}ResponseDtoSchema` | `UserResponseDtoSchema` |
| Service command | `{Action}{Entity}CommandSchema` | `CreateUserCommandSchema` |
| Service query | `{Action}{Entity}QuerySchema` | `ListUsersQuerySchema` |
| Worker payload | `{Queue}PayloadSchema` | `OnboardingGrantLmsPayloadSchema` |
| Event payload | `{Event}EventDtoSchema` | `PaymentSuccessEventDtoSchema` |
| Inferred type | Без `Schema` | `UserResponseDto` |
| Mapper function | `to{Entity}ResponseDto` | `toUserResponseDto` |
| Prisma select | `{entity}ResponseSelect` | `userResponseSelect` |

### Guard rails

1. **Каждый tRPC procedure обязан иметь `.output()`** — runtime-валидация ответа
2. **Prisma-запросы всегда с `select`** — использовать `{entity}ResponseSelect` из mappers
3. **Router-файлы не импортируют `@prisma/client` напрямую** — только через dto/ и services/
4. **Shared-enum sync** — compile-time type assertions в `src/server/dto/shared.ts` (`AssertEqual<PrismaEnum, ZodInferred>`)
5. **Worker payloads** — каждая очередь обязана иметь зарегистрированную payload-схему в `src/server/dto/worker.ts`

---

## Как модули общаются — сервисы + pg-boss в транзакции

### Принцип работы

Сервисы вызывают друг друга напрямую (через import). Асинхронная работа ставится через `sendJobInTransaction()` / `createProcessWithJobsInTransaction()` в той же БД-транзакции, что и бизнес-записи. Аналитические Event-записи создаются через прямой `db.event.create()` внутри транзакции.

```
┌──────────────┐     $transaction:                 ┌──────────────────────────┐
│ billing      │ ──→ 1. Бизнес-записи (Payment,   │  pg-boss Worker          │
│ service      │      Order, Enrollment)            │  (подхватывает после     │
└──────────────┘     2. db.event.create() —         │   commit)                │
                        аналитика                   │                          │
                     3. sendJobInTransaction() ──→  │  onboarding.grant_lms    │
                        pg-boss jobs                │  onboarding.send_welcome │
                     → return 200 / 202             │  и т.д.                  │
                                                    └──────────────────────────┘
```

### Правила

1. **Всё критичное — в одной транзакции**. Бизнес-записи, Event-запись и постановка pg-boss jobs выполняются в одном `$transaction`. Нет окна потери между commit и jobs.
2. **Тяжёлая работа — через pg-boss**. Сервис не отправляет email и не вызывает внешние API напрямую. Вместо этого ставит Job в pg-boss через `sendJobInTransaction()`.
3. **Event-запись — прямой INSERT**. Для аналитики сервис делает `db.event.create()` внутри транзакции. Без прослоек.
4. **Типизация**. Все типы Event payload описаны в `src/server/dto/events.ts`. Zod-схемы валидируют payload при записи.
5. **При необходимости декаплинга** (рост до нескольких команд) можно добавить event bus на уровне pg-boss или внешнего брокера.

### Реализация

```
src/server/
├── dto/events.ts                    # Zod-схемы payload для Event-записей
├── services/billing/
│   └── handle-payment-success.ts    # Обработка payment.success (транзакция)
├── worker/
│   ├── send-in-transaction.ts       # sendJobInTransaction — raw INSERT в pgboss.job
│   ├── process.ts                   # createProcessWithJobsInTransaction
│   └── cron.ts                      # Cron-задачи (прямой db.event.create)
```

### Каталог событий (Event-записи в таблице Event)

#### Billing (модуль billing)

| Событие                | Payload                                            | Кто эмитит               | Обработчики                                                                                                                | Этап |
| ---------------------- | -------------------------------------------------- | ------------------------ | -------------------------------------------------------------------------------------------------------------------------- | ---- |
| `payment.success`      | `{ orderId, paymentId, userId, amount, currency }` | webhook handler (ЮKassa) | analytics: Event запись; crm: Lead.status → converted; onboarding: создать Process + Jobs; promo: начислить бонус рефереру | 1    |
| `payment.failed`       | `{ orderId, paymentId, reason }`                   | webhook handler          | analytics: Event запись; notification: уведомить менеджера                                                                 | 1    |
| `order.created`        | `{ orderId, userId, productId, tierId }`           | billing service          | analytics: Event запись                                                                                                    | 1    |
| `refund.initiated`     | `{ orderId, paymentId, amount }`                   | billing service          | analytics: Event; onboarding: запустить Process "rollback_onboarding"                                                      | 2    |
| `upgrade.completed`    | `{ enrollmentId, oldTierId, newTierId }`           | billing service          | analytics: Event; telegram: пересчёт ChatMembership                                                                        | 2    |
| `subscription.charged` | `{ subscriptionId, paymentId }`                    | cron job (pg-boss)       | analytics: Event                                                                                                           | 3    |
| `subscription.failed`  | `{ subscriptionId, reason }`                       | cron job                 | analytics: Event; notification: уведомить студента                                                                         | 3    |

#### CRM (модуль crm)

| Событие               | Payload                            | Кто эмитит            | Обработчики                                         | Этап |
| --------------------- | ---------------------------------- | --------------------- | --------------------------------------------------- | ---- |
| `lead.created`        | `{ leadId, source, email }`        | crm service / webhook | analytics: Event; notification: уведомить менеджера | 1    |
| `lead.status_changed` | `{ leadId, oldStatus, newStatus }` | crm service           | analytics: Event                                    | 1    |
| `lead.converted`      | `{ leadId, userId, orderId }`      | crm service           | analytics: Event                                    | 1    |

#### LMS (модуль lms)

| Событие                  | Payload                                      | Кто эмитит  | Обработчики                                                             | Этап |
| ------------------------ | -------------------------------------------- | ----------- | ----------------------------------------------------------------------- | ---- |
| `lesson.completed`       | `{ enrollmentId, lessonId, userId }`         | lms service | analytics: Event                                                        | 1    |
| `lesson.opened`          | `{ enrollmentId, lessonId, userId }`         | lms service | analytics: Event                                                        | 1    |
| `lesson.content_updated` | `{ lessonId, revisionId, editorId }`         | lms service | analytics: Event; content: пометить CohortContent.is_synced → false [2] | 1    |
| `homework.submitted`     | `{ submissionId, enrollmentId, homeworkId }` | lms service | analytics: Event; notification: уведомить куратора                      | 2    |
| `homework.reviewed`      | `{ submissionId, status, reviewerId }`       | lms service | analytics: Event; notification: уведомить студента                      | 2    |

#### Onboarding (модуль onboarding / enrollment)

| Событие                  | Payload                                      | Кто эмитит         | Обработчики                                         | Этап |
| ------------------------ | -------------------------------------------- | ------------------ | --------------------------------------------------- | ---- |
| `enrollment.created`     | `{ enrollmentId, userId, cohortId, tierId }` | enrollment service | analytics: Event                                    | 1    |
| `onboarding.completed`   | `{ enrollmentId, processId }`                | worker (Process)   | analytics: Event; notification: уведомить менеджера | 1    |
| `onboarding.step_failed` | `{ enrollmentId, stepName, error }`          | worker (Job)       | analytics: Event; notification: алерт менеджеру     | 1    |

#### Telegram (модуль telegram)

| Событие       | Payload                      | Кто эмитит              | Обработчики                                                  | Этап |
| ------------- | ---------------------------- | ----------------------- | ------------------------------------------------------------ | ---- |
| `chat.joined` | `{ userId, chatId }`         | bot (chat_member event) | analytics: Event; onboarding: обновить ChatMembership.status | 1    |
| `chat.left`   | `{ userId, chatId }`         | bot (chat_member event) | analytics: Event; crm: обновить ChatMembership.status        | 1    |
| `bot.started` | `{ telegramUserId, userId }` | bot (/start)            | analytics: Event                                             | 1    |

#### Auth (модуль auth)

| Событие           | Payload                 | Кто эмитит         | Обработчики      | Этап |
| ----------------- | ----------------------- | ------------------ | ---------------- | ---- |
| `user.registered` | `{ userId, email }`     | better-auth (hook) | analytics: Event | 1    |
| `user.logged_in`  | `{ userId, sessionId }` | better-auth (hook) | analytics: Event | 1    |

#### Schedule (модуль schedule) [этап 2]

| Событие                | Payload                                | Кто эмитит       | Обработчики                                                       | Этап |
| ---------------------- | -------------------------------------- | ---------------- | ----------------------------------------------------------------- | ---- |
| `schedule.created`     | `{ scheduleId, cohortId }`             | schedule service | analytics: Event; notification: запустить Process уведомлений     | 2    |
| `schedule.rescheduled` | `{ scheduleId, oldTime, newTime }`     | schedule service | analytics: Event; notification: запустить Process переуведомлений | 2    |
| `attendance.recorded`  | `{ scheduleId, enrollmentId, status }` | schedule service | analytics: Event                                                  | 2    |

#### Feedback (модуль feedback) [этап 3]

| Событие                       | Payload                                  | Кто эмитит       | Обработчики                                     | Этап |
| ----------------------------- | ---------------------------------------- | ---------------- | ----------------------------------------------- | ---- |
| `feedback.response_received`  | `{ campaignId, enrollmentId, npsScore }` | feedback service | analytics: Event; ai: запустить суммаризацию    | 3    |
| `feedback.campaign_completed` | `{ campaignId, responseRate }`           | cron job         | analytics: Event; notification: отчёт менеджеру | 3    |

#### Cohort lifecycle

| Событие            | Payload        | Кто эмитит   | Обработчики                                          | Этап |
| ------------------ | -------------- | ------------ | ---------------------------------------------------- | ---- |
| `cohort.started`   | `{ cohortId }` | admin action | analytics: Event; content: fork CohortContent [2]    | 1    |
| `cohort.completed` | `{ cohortId }` | admin action | analytics: Event; offboarding: запустить Process [3] | 3    |

#### Student Activity (модуль lms) [этап 2]

| Событие            | Payload                                                      | Кто эмитит        | Обработчики                                             | Этап |
| ------------------ | ------------------------------------------------------------ | ----------------- | ------------------------------------------------------- | ---- |
| `student.inactive` | `{ enrollmentId, userId, daysSinceLastActivity, curatorId }` | cron job (INT.15) | analytics: Event; notification: TG-уведомление куратору | 2    |

### Пример: полный цикл payment.success

```
ЮKassa webhook → POST /api/webhooks/yookassa
    │
    ▼
webhook handler → $transaction:
    1. Записать WebhookLog (DB.27)
    2. Проверить idempotency (provider_payment_id UNIQUE)
    3. Обновить Payment.status → success (DB.5)
    4. Обновить Order.status → paid (DB.4)
    5. db.event.create({ eventType: "payment.success", ... })  ← аналитика
    6. createProcessWithJobsInTransaction(tx, { type: "onboarding", steps: [...] })
       └── 5 Jobs в pg-boss (grant_lms, onboarding_page, calendar, curator, welcome)
    → commit → return 200 OK

[Worker подхватывает Jobs после commit]
    │
    ├── onboarding.grant_lms → LMS.1 → Process.steps[0].status = "completed"
    ├── onboarding.create_onboarding_page → TG.2 + EMAIL.1 → Process.steps[1]
    ├── onboarding.subscribe_calendar → GCAL.3 → Process.steps[2]
    ├── onboarding.assign_curator → INT.2 → Process.steps[3]
    └── onboarding.send_welcome (chain) → TG.1 + EMAIL.1 → Process.status = "completed"
```

### Синхронное vs асинхронное: когда что

```
Синхронно в транзакции сервиса             pg-boss (асинхронный, Job Queue)
──────────────────────────────             ──────────────────────────────────
Записать Event в БД (db.event.create)      Отправить email / TG
Обновить статус сущности                   Вызвать внешнее API (ЮKassa, Zoom, Calendar)
Поставить Jobs в pg-boss                   Генерация PDF (сертификат, счёт)
Быстрая бизнес-логика                      AI-суммаризация
                                           Cron-задачи (access check, content sync)
                                           Любая операция > 100ms
```

## Cron-задачи (pg-boss schedules): управление

Cron-задачи — это такой же production-контракт, как и API: они должны быть идемпотентными, наблюдаемыми и управляемыми.

**Базовые правила:**

1. Все cron-регистрации централизованы в одном месте (`src/server/worker/cron.ts`), без «скрытых» schedule в модулях.
2. Имя cron фиксировано и доменно (`access.check_memberships`, `content.auto_sync`, `billing.subscription_charge`).
3. Cron не выполняет тяжёлую бизнес-логику: только вычисляет набор работ и ставит jobs в pg-boss.
4. Успех cron = успешная постановка jobs (`enqueued_count`), а не завершение downstream-обработки.
5. Каждый запуск пишет структурированный лог с `cron_name`, `job_id`, `trace_id`, `started_at`, `duration_ms`, `status`.
6. Любой cron-обработчик идемпотентен: повторный запуск не ломает состояние и не создаёт дубли.
7. Для задач с риском дублей используем `singletonKey` и/или DB-ограничения (unique + upsert).
8. Ошибки cron не теряются: retry с backoff, после исчерпания — `failed/expired` + dead job в дэшборде.
9. Тяжёлый объём cron разбивается на fan-out Jobs (чанки), а не выполняется в cron-процессе.
10. Каждый cron имеет runbook: цель, расписание, side effects, idempotency-стратегия, как безопасно ретраить вручную.

**Минимальный реестр cron (MVP):**

- `access.check_memberships` — ежедневно, пересчёт доступа к чатам.
- `lms.check_inactive_students` — ежедневно, детект неактивных студентов.
- `content.auto_sync` — ежедневно, синхронизация контента SoK -> CohortContent.

**Что считать инцидентом cron:**

- пропущен запуск по расписанию;
- queue lag выше порога для cron-очереди;
- повторяющиеся `failed/expired` jobs по одному `cron_name`.

## Один worker — почему и когда масштабировать

**Почему один процесс достаточно:**

- ~3000 студентов/год = ~10-20 фоновых задач в день (онбординг, уведомления)
- pg-boss может обрабатывать тысячи задач/минуту на одном процессе
- Простота деплоя и отладки: один процесс, один лог

**Когда разделять на несколько worker'ов:**

- Если время ожидания в очереди вырастет > 1 минуты для критичных задач
- Запуск второго экземпляра того же worker'а — pg-boss автоматически балансирует через FOR UPDATE SKIP LOCKED
- При необходимости приоритетов — разделить на отдельные named queues с разными worker'ами

---

## Пример: как работает онбординг после оплаты

```
Студент оплачивает курс → ЮKassa webhook → payment.success
        │
        ▼
Webhook handler → $transaction:
        │
        ├── Создать Enrollment + Order.status → paid
        ├── db.event.create({ eventType: "payment.success" }) — аналитика
        ├── createProcessWithJobsInTransaction(tx, {
        │     type: "onboarding", entity: enrollment:123,
        │     steps: [{name: "grant_lms", status: "pending"},
        │             {name: "create_onboarding_page", status: "pending"},
        │             {name: "subscribe_calendar", status: "pending"},
        │             {name: "assign_curator", status: "pending"},
        │             {name: "send_welcome", status: "pending"}]
        │   })  ← Process + 5 Jobs в pg-boss — всё в одной TX
        │
        └── commit → return 200 OK (webhook acknowledgement)

[Worker подхватывает Jobs из очереди]

        Worker: onboarding.grant_lms
            ├── Выдать доступ к LMS (создать Progress записи)
            └── Обновить Process.steps[0].status → "completed"

        Worker: onboarding.create_onboarding_page
            ├── Определить чаты: Tier.telegram_chats[] + фильтр по потоку (cohort_id)
            ├── Создать ChatMembership записи (should_be_member: true, status: pending)
            ├── Отправить ссылку на онбординг-страницу студенту (email + TG)
            └── Онбординг-страница показывает:
                ├── Чат "КДП Поток 14" — [Вступить] / [Вступил ✓]
                ├── Канал "КДП Записи" — [Вступить] / [Вступил ✓]
                └── Чат "Воркшопы" — [Вступить] / [Вступил ✓]
                    (бот отслеживает вступления через chat_member events)

        Worker: onboarding.assign_curator
            ├── Назначить в группу куратора (round-robin по загрузке)
            └── Обновить Process.steps[3].status → "completed"

        Worker: onboarding.send_welcome (chain: после остальных)
            ├── Email: приветственное письмо + инструкции
            ├── TG: "Добро пожаловать! Начните с LMS: [ссылка]"
            └── Process.status → "completed"

[Web App: дэшборд менеджера]

        Процесс #456: Онбординг студента Мария Петрова
        ┌────────────────────────┬──────────┐
        │ Шаг                    │ Статус   │
        ├────────────────────────┼──────────┤
        │ Доступ к LMS           │ Done     │
        │ Онбординг-страница     │ Done     │
        │ Подписка на календарь  │ Done     │
        │ Назначение куратора    │ Done     │
        │ Приветственное сообщ.  │ Done     │
        └────────────────────────┴──────────┘
```

## Как Process и Job связаны

```
Process — бизнес-уровень (видим менеджеру в дэшборде)
    │
    ├── steps: JSON-массив с именами шагов и их статусами
    │   Обновляется worker'ом при завершении каждого Job
    │
    └── Каждый Job при создании получает process_id в data
        Worker после выполнения Job → обновляет соответствующий step
        Если все steps completed → Process.status = "completed"
        Если хотя бы один step failed (после всех retry) → Process.status = "partially_failed"
```

**Упрощение по сравнению с DAG**: шаги выполняются параллельно (pg-boss сам разбирает из очереди). Если нужна последовательность — Job ставит следующий Job в очередь при завершении (chain). Нет явных `depends_on[]`, нет отдельной таблицы ProcessStep.

## Telegram Bot — архитектура (grammY)

```
grammY Bot (webhook mode)
    │
    ├── Middleware: auth (связать telegram_user_id → User)
    ├── Middleware: logging (все сообщения → Event)
    │
    ├── Commands:
    │   ├── /start → привязка TG аккаунта к профилю
    │   └── /help → информация
    │
    ├── Event Handlers:
    │   ├── chat_member → обновить ChatMembership.status
    │   └── message → обработка входящих (FAQ-бот, будущее)
    │
    ├── Conversations (grammY plugin):
    │   ├── warmup_funnel → прогрев (замена BotHelp, этап 2)
    │   └── feedback_form → сбор NPS (этап 3)
    │
    └── Notifications (исходящие, через pg-boss Job):
        ├── Напоминания о вебинарах
        ├── Результаты проверки ДЗ
        ├── Новый контент в LMS
        └── Кросс-продуктовые предложения
```
