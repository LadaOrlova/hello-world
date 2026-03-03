# Надёжная доставка критичных событий

> Часть архитектуры Zamesin IS.
> Основной документ: [PLAN.md](../PLAN.md) | Архитектура: [02-architecture.md](02-architecture.md) | Edge cases: [06-edge-cases.md](06-edge-cases.md)
> Исходный анализ рисков: [docs/OLD/RISKS-2026-02-16.md](OLD/RISKS-2026-02-16.md)

---

## 17.1 Зачем этот документ

Три конкретные проблемы, универсальные для любого критичного события (`payment.success`, `refund.initiated`, `cohort.completed` и т.д.):

| ID | Проблема | Суть |
|----|----------|------|
| A | Crash после бизнес-записи, до jobs | Бизнес-операция выполнена, но последующие шаги не запущены |
| B | Частично выполненные handlers | Один handler упал — остальные не отработали и не будут повторены |
| C | Job сделал side effect, но step не обновился | При retry — дубль side effect |

Payment — наиболее яркий пример (деньги получены, онбординг не запустился), но риски идентичны для любого критичного пути.

**Ключевой принцип решения**: не добавлять новые слои абстракций, а использовать то, что уже есть — pg-boss работает в той же PostgreSQL, что и бизнес-данные.

---

## 17.2 Почему НЕ нужен отдельный Outbox/Inbox

### pg-boss уже является outbox

pg-boss хранит jobs в таблице `pgboss.job` в той же PostgreSQL. Если мы можем вставить job-запись **в той же транзакции**, что и бизнес-изменения — это и есть transactional outbox, только бесплатно:

```
Классический Outbox:
  TX: Payment + Order + OutboxEvent  →  Dispatcher  →  pg-boss  →  Worker

pg-boss-as-outbox:
  TX: Payment + Order + pg-boss job  →  Worker
```

Вместо 3 шагов — 1. Меньше кода, меньше точек отказа, меньше таблиц.

### Inbox (EventHandlerDelivery) избыточен на MVP

Inbox нужен, когда:
- Много handlers на одно событие, и каждый может упасть независимо.
- Нужна гарантия, что каждый handler отработает ровно один раз.

В нашем случае:
- Сейчас один handler на `payment.success`.
- «Много handlers» — это на самом деле **шаги Process** (grant_lms, assign_curator, send_welcome), и у каждого уже есть свой pg-boss job с retry.
- Process.steps уже трекает статус каждого шага.

**Process + pg-boss jobs — это и есть inbox.** Отдельная таблица `EventHandlerDelivery` дублирует эту функциональность.

---

## 17.3 Решение: 3 конкретных изменения

### Изменение 1: Атомарная транзакция webhook → jobs

**Закрывает риск A.**

Проблема: сейчас webhook handler делает `emit("payment.success")` → handler создаёт Process → отдельно ставит jobs. Crash между commit Process и `boss.send()` теряет jobs.

Решение: одна транзакция, включающая и бизнес-запись, и постановку jobs.

**Как поставить pg-boss job внутри Prisma-транзакции:**

pg-boss хранит jobs в `pgboss.job`. Мы можем вставить туда запись через `$queryRawUnsafe` внутри `$transaction`:

```ts
// src/server/worker/send-in-transaction.ts

import type { PrismaClient } from "@prisma/client";

type TxClient = Parameters<Parameters<PrismaClient["$transaction"]>[0]>[0];

/**
 * Ставит pg-boss job внутри Prisma-транзакции.
 * Job не будет виден pg-boss worker-у до commit транзакции.
 */
export async function sendJobInTransaction(
  tx: TxClient,
  queue: string,
  data: object,
  options: {
    singletonKey?: string;
    retryLimit?: number;
    retryBackoff?: boolean;
    expireInSeconds?: number;
    startAfter?: Date;
  } = {}
) {
  const schema = process.env.PG_BOSS_SCHEMA ?? "pgboss";
  const retryLimit = options.retryLimit ?? 5;
  const retryBackoff = options.retryBackoff ?? true;
  const expireInSeconds = options.expireInSeconds ?? 1800;

  const startAfter = options.startAfter ?? new Date();

  // pg-boss v12: expire_seconds (integer), state = 'created'
  const result = await tx.$queryRawUnsafe<{ id: string }[]>(
    `INSERT INTO "${schema}"."job" (
      name, data, singleton_key,
      retry_limit, retry_backoff,
      expire_seconds, start_after, state
    ) VALUES (
      $1, $2::jsonb, $3,
      $4, $5,
      $6, $7, 'created'
    )
    ON CONFLICT DO NOTHING
    RETURNING id`,
    queue,
    JSON.stringify(data),
    options.singletonKey ?? null,
    retryLimit,
    retryBackoff,
    expireInSeconds,
    startAfter
  );

  return result[0]?.id ?? null;
}
```

**Webhook handler (целевой вид):**

```ts
// Весь критичный путь — в одной транзакции
await db.$transaction(async (tx) => {
  // 1. WebhookLog
  await tx.webhookLog.create({ data: { source: "yookassa", rawPayload } });

  // 2. Idempotency check + Payment/Order update
  const payment = await upsertPaymentFromWebhook(tx, payload);
  await markOrderPaid(tx, payment.orderId);

  // 3. Event запись (для аналитики)
  await tx.event.create({
    data: {
      eventType: "payment.success",
      source: "webhook",
      userId: payment.userId,
      eventData: { orderId: payment.orderId, amount: payment.amount },
    },
  });

  // 4. Process + Jobs — всё в той же транзакции
  const process = await tx.process.create({
    data: {
      type: "onboarding",
      entityType: "order",
      entityId: payment.orderId,
      status: "running",
      steps: initialSteps,
    },
    select: { id: true },
  });

  // 5. Jobs в pg-boss — через raw insert в той же TX
  for (const step of steps) {
    await sendJobInTransaction(tx, step.queue, {
      processId: process.id,
      stepIndex: step.index,
      stepName: step.name,
      entityType: "order",
      entityId: payment.orderId,
      payload: step.payload,
    }, {
      singletonKey: `${step.queue}:order:${payment.orderId}:${step.name}`,
      retryLimit: 5,
      retryBackoff: true,
      expireInSeconds: 1800,
    });
  }
});

// Транзакция закоммичена. pg-boss увидит jobs при следующем poll.
return 200;
```

**Свойство**: если crash до commit — ничего не произошло (ни Payment, ни jobs). Если commit прошёл — и Payment, и jobs гарантированно существуют. Окна потери нет.

---

### Изменение 2: Заменить цепочку emit-handlers на явный orchestration

**Закрывает риск B.**

Проблема: цепочка handlers (ранее через EventEmitter) могла привести к частичному выполнению при crash.

Решение: для критичного пути `payment.success` — один явный orchestration-блок в транзакции, включающий бизнес-записи + Event-запись + pg-boss jobs.

> **Историческая справка:** EventEmitter (Domain Events) был удалён из архитектуры. Сервисы теперь вызывают друг друга напрямую, Event-записи создаются через `db.event.create()`, а pg-boss jobs ставятся через `sendJobInTransaction()` — всё в одной транзакции.

**Правило: если потеря действия означает потерю денег или неоказание услуги — используй явную транзакцию с `sendJobInTransaction()`.**

Для `payment.success` это значит:

| Действие | Было (handler chain) | Стало (explicit TX) |
|----------|---------------------|---------------------|
| WebhookLog, Payment, Order | В webhook handler | В TX |
| Event запись (analytics) | analytics handler | В TX |
| Process + Jobs (onboarding) | onboarding handler | В TX |
| Lead.status → converted | crm handler | Отдельный pg-boss job в TX |
| Бонус реферера | promo handler | Отдельный pg-boss job в TX |

Каждое действие, которое может упасть независимо, становится отдельным job с собственным retry. Нет цепочки handlers, нет проблемы частичного выполнения.

---

### Изменение 3: Идемпотентность каждого job handler

**Закрывает риск C.**

Это не архитектурное изменение, а дисциплина кода. Каждый handler при retry должен быть no-op, если side effect уже выполнен.

**Практические правила:**

```
DB-операции:
  ✅ upsert вместо create
  ✅ createMany({ skipDuplicates: true })
  ✅ уникальные индексы на бизнес-ключах

Внешние API (Telegram, Mailgun, Calendar):
  ✅ idempotency_key при вызове API (если поддерживает)
  ✅ проверка «уже сделано?» перед вызовом
  ✅ guard: если ChatMembership.status === 'joined', не приглашать повторно
```

**Конкретные handlers онбординга:**

| Job | Идемпотентность |
|-----|-----------------|
| `grant_lms` | `Progress @@unique([enrollmentId, lessonId])` — createMany skipDuplicates |
| `create_onboarding_page` | `ChatMembership @@unique([userId, telegramChatId])` — upsert |
| `assign_curator` | Проверить `CuratorGroup WHERE enrollmentId` перед назначением |
| `subscribe_calendar` | Хранить `calendar_invite_sent_at` в Enrollment — skip если not null |
| `send_welcome` | `Notification @@unique([userId, type, referenceId])` — skip если exists |

**Про обновление Process.steps (риск C конкретно):**

Текущий `executor.ts` делает handler → отдельный update step. При crash между ними — retry вызовет handler повторно. Если handler идемпотентен — повторный вызов = no-op → step обновится → всё ok.

Можно ли сделать handler + step update в одной транзакции? Да, для DB-only шагов:

```ts
// Для DB-only шагов (grant_lms, create_onboarding_page)
await db.$transaction(async (tx) => {
  await handler(tx, payload);  // DB-операции через tx
  await updateProcessStepStatus(tx, { processId, stepIndex, status: "completed" });
});
```

Для шагов с внешними API (send_welcome, subscribe_calendar) — это невозможно, и идемпотентность handler-а является единственной защитой. Это нормально и достаточно.

---

## 17.4 Что остаётся как есть

| Компонент | Почему не трогаем |
|-----------|-------------------|
| `db.event.create()` | Прямая запись Event-аналитики в транзакции сервиса |
| `Process` + `steps` JSON | Уже трекает состояние. Отдельная таблица ProcessStep не нужна |
| pg-boss retry/backoff/dead jobs | Уже есть, покрывает retry |
| `Payment.providerPaymentId @unique` | Идемпотентность webhook уже есть |
| `WebhookLog` | Аудит уже есть |

---

## 17.5 Что меняется

| Что | Было | Стало |
|-----|------|-------|
| Webhook → jobs | emit → handler → createProcess → boss.send (3 фазы, 2 точки crash) | Одна $transaction (0 точек crash) |
| payment.success orchestration | Цепочка Domain Event handlers | Явный код в транзакции + отдельные jobs |
| Job handlers | Нет требования к идемпотентности | Обязательная идемпотентность (upsert/skipDuplicates/guard) |
| DB-only job steps | handler() → update step (2 фазы) | Опционально: handler + step в одной TX |
| Новые Prisma-модели | — | Не нужны. Без OutboxEvent, без EventHandlerDelivery |

---

## 17.6 `sendJobInTransaction` — ключевой контракт

### Почему это работает

1. pg-boss хранит jobs в `pgboss.job` в той же PostgreSQL.
2. `INSERT INTO pgboss.job` внутри Prisma `$transaction` — запись видна pg-boss только после commit.
3. pg-boss worker polling (`SELECT ... FOR UPDATE SKIP LOCKED`) подхватит job при следующем цикле (по умолчанию каждые 2 секунды).
4. `ON CONFLICT DO NOTHING` + `singletonKey` защищает от дублей при повторном webhook.

### Ограничения

- Привязка к внутренней структуре таблицы pg-boss — при мажорном обновлении pg-boss может сломаться. Митигация: закрепить версию pg-boss, добавить интеграционный тест на insert.
- Raw SQL вместо `boss.send()` — менее читаемо. Митигация: обёрнуто в единственную функцию `sendJobInTransaction`, используется только для критичных путей.

### Альтернатива без raw SQL

Если привязка к внутренней таблице pg-boss кажется хрупкой, можно использовать минимальный outbox:

```ts
// Вместо raw INSERT в pgboss.job — запись в свою таблицу
await tx.pendingJob.create({
  data: { queue, payload, singletonKey, status: "pending" }
});

// Отдельный cron (раз в 5 сек) подхватывает и вызывает boss.send()
```

Это добавляет одну таблицу и один cron, но убирает зависимость от internal schema pg-boss. Для MVP с ~10-20 платежами в день — overkill, но опция есть.

---

## 17.7 Обновление документации

### `docs/06-edge-cases.md` — строка 370

Сейчас написано: «Worker обновляет в одной транзакции» — это **не соответствует коду**. `executor.ts` делает handler и step update как два отдельных вызова.

Исправить на: «Worker обновляет step после handler. Для DB-only шагов можно объединить в транзакцию. Для API-шагов защита — идемпотентность handler.»

### `docs/02-architecture.md` — строка 253

Сейчас написано: «emit — синхронный. Все handlers выполняются в той же транзакции (если нужно)» — вводит в заблуждение, потому что handlers не оборачиваются в транзакцию автоматически.

Обновлено: EventEmitter удалён. Для всех путей используется явная транзакция с `sendJobInTransaction()`.

---

## 17.8 Порядок внедрения

```
1. [P0] sendJobInTransaction()
   - Функция raw insert в pgboss.job внутри Prisma TX
   - Интеграционный тест: job появляется после commit, не появляется после rollback

2. [P0] Рефакторинг webhook handler payment.success
   - Одна транзакция: WebhookLog + Payment + Order + Event + Process + Jobs
   - Прямой вызов сервиса вместо emit (уже сделано)
   - Event запись — в той же TX (не через handler)

3. [P0] Идемпотентность каждого onboarding job handler
   - grant_lms: createMany skipDuplicates
   - create_onboarding_page: upsert ChatMembership
   - assign_curator: guard check
   - subscribe_calendar: guard + idempotency_key
   - send_welcome: unique Notification key

4. [P1] DB-only steps в одной транзакции с handler
   - executor.ts: опциональная обёртка handler + step update в $transaction
   - Только для handlers, принимающих tx-клиент

5. [P1] Интеграционные тесты на отказные сценарии
   - Crash между Payment commit и job pickup
   - Повторный webhook (idempotency)
   - Job retry после partial side effect

6. [P1] Обновить docs/02 и docs/06
   - Убрать формулировки, выглядящие как реализованные гарантии
```

---

## 17.9 Сравнение подходов

| Критерий | Outbox + Inbox (предыдущий doc-17) | pg-boss-in-TX (этот документ) |
|----------|-------------------------------------|-------------------------------|
| Новые Prisma-модели | 2 (OutboxEvent, EventHandlerDelivery) | 0 |
| Новые enum-ы | 2 (OutboxStatus, DeliveryStatus) | 0 |
| Новые workers/cron | 2 (outbox.dispatch, inbox.process.*) | 0 |
| Точки отказа | outbox → dispatcher → inbox → handler | TX commit → handler |
| Гарантия доставки | at-least-once через dispatcher | at-least-once через pg-boss retry |
| Независимый retry handlers | Да (per-delivery) | Да (per-job, уже есть) |
| Наблюдаемость | Свои метрики outbox/inbox | pg-boss dead jobs dashboard (уже есть) |
| Масштабируемость | Готов к multi-handler | Handlers = jobs, масштабируется через pg-boss |
| Сложность внедрения | ~3-4 дня | ~1-2 дня |
| Привязка к pg-boss internals | Нет | Да (raw insert в pgboss.job) |

**Вывод**: для текущего масштаба (~3000 студентов/год, ~10-20 платежей/день) подход pg-boss-in-TX даёт те же гарантии при вдвое меньшей сложности. Outbox + Inbox оправдан при переходе на несколько consumer-сервисов или внешний брокер — но это Phase 3+.

---

## 17.10 Когда переходить на полноценный Outbox

Триггеры для пересмотра:
- Появляются >5 handlers на одно событие с разными SLA.
- Нужна доставка событий во внешние системы (другой сервис, Kafka).
- pg-boss обновляется мажорно и ломает schema — тогда outbox-таблица выгоднее raw insert.
- Нагрузка вырастает до уровня, где polling outbox + inbox эффективнее прямых jobs.

До этого момента — pg-boss-in-TX закрывает все три риска (A, B, C) без дополнительной инфраструктуры.
