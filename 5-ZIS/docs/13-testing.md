# Стратегия тестирования

> Часть архитектуры Zamesin IS.
> Основной документ: [PLAN.md](../PLAN.md) | Атомарные операции: [05-atomic-operations.md](05-atomic-operations.md)
> Edge cases: [06-edge-cases.md](06-edge-cases.md) | Архитектура: [02-architecture.md](02-architecture.md)
> ROADMAP: [ROADMAP.md](../ROADMAP.md)

Минимально-необходимый набор тестов для MVP — без избыточного покрытия, с фокусом на критичных путях.

---

## 13.1 Принципы

### MVP-фокус

- **Приоритет**: стабильность критичного пути (оплата, онбординг, LMS, RBAC), не полное покрытие
- **Нет целевого coverage %** — тестируем то, что ломается дороже всего
- **Быстрые тесты** — unit + integration должны выполняться за < 30 сек

### Стек

- **Unit + Integration**: Vitest (совместим с Next.js, Vite, быстрый)
- **E2E**: Playwright (кросс-браузер, стабильный)
- **Моки**: внешние API — ЮKassa, Mailgun, Telegram, Zoom, Kinescope

### Тестовая БД

- Отдельная схема PostgreSQL для тестов (или `test` database)
- `prisma migrate deploy` перед integration/E2E
- Seed-данные для тестовых сценариев

---

## 13.2 Пирамида тестирования (минимальная)

```
         E2E (5–7 сценариев)
        /                   \
   Integration (критичные модули)
  /______________________________\
 Unit (критичная логика, edge cases)
```

---

## 13.3 Unit-тесты

### Что тестировать

**DTO-контракты границ (обязательно):**

- tRPC/API boundary: schema validation для `input/output` DTO.
- Event payload boundary: валидация DTO перед `db.event.create()`.
- Worker boundary: валидация envelope DTO перед вызовом handler.

**Внутренняя логика (INT.\*)** — чистая логика без side effects:

| Операция | Файл/сервис                  | Что проверять                                                                      |
| -------- | ---------------------------- | ---------------------------------------------------------------------------------- |
| INT.1    | `check_cohort_capacity`      | Места есть / нет, граничные значения                                               |
| INT.2    | `assign_curator_round_robin` | Round-robin по загрузке                                                            |
| INT.3    | `dedup_lead`                 | Дедупликация по hash(email + phone)                                                |
| INT.5    | `check_rbac`                 | Роли: admin, manager, curator, student; forbidden для чужих данных                 |
| INT.7    | `validate_promo_code`        | Срок, лимит, продукт                                                               |
| INT.9    | `calculate_upgrade_price`    | Доплата = разница тарифов                                                          |
| INT.10   | `calculate_should_be_member` | Enrollment.status, support_expires_at, Tier.telegram_chats, TelegramChat.cohort_id |

**Edge cases** из [06-edge-cases.md](06-edge-cases.md):

- **Идемпотентность оплат** (6.1): повторный webhook с тем же `provider_payment_id` → no-op
- **RBAC** (6.4): curator не видит чужие потоки, student не видит админку
- **OTP** (6.3): rate limiting, TTL — лучше через integration с better-auth

### Где размещать

```
src/
├── server/
│   ├── services/
│   │   ├── billing/
│   │   │   └── __tests__/
│   │   ├── crm/
│   │   │   └── __tests__/
│   │   └── lms/
│   │       └── __tests__/
└── shared/
    └── lib/
        └── __tests__/
```

### Пример (INT.1)

```typescript
// src/server/services/billing/__tests__/capacity.test.ts
import { describe, it, expect, beforeEach } from "vitest";
import { checkCohortCapacity } from "../capacity";

describe("checkCohortCapacity", () => {
  it("вернёт true когда enrolled_count < max_students", () => {
    expect(checkCohortCapacity(50, 60)).toBe(true);
  });
  it("вернёт false когда места заняты", () => {
    expect(checkCohortCapacity(60, 60)).toBe(false);
  });
});
```

---

## 13.4 Интеграционные тесты

### Транзакционные flow

- **payment.success**: при обработке webhook в одной транзакции создаётся Enrollment, Event-запись, Process, Jobs в pg-boss
- **db.event.create()**: каждое бизнес-действие записывает Event в БД (DB.26)
- **Lead.status → converted**: при payment.success в транзакции

### Payment webhook (PAY.2)

- **Идемпотентность**: два одинаковых webhook'а → второй 200 OK, без дубля Payment
- **provider_payment_id UNIQUE**: constraint violation → catch → 200 OK
- **WebhookLog**: каждый webhook сохраняется в сыром виде (DB.27)

### pg-boss Job handlers

- **onboarding.\***: mock интеграций (Mailgun, Telegram, Zoom) → проверка Process.steps
- **onboarding.grant_lms**: создаются Progress записи
- **onboarding.send_welcome**: mock TG.1 + EMAIL.1 → Process.status = completed

### Топ-5 критичных операций

| ID     | Операция                 | Тип теста                        |
| ------ | ------------------------ | -------------------------------- |
| INT.5  | check_rbac               | Unit                             |
| DB.25  | write_audit_log          | Integration (middleware)         |
| INT.11 | write_event              | Integration (транзакционный flow)    |
| PAY.2  | process_yookassa_webhook | Integration                      |
| INT.4  | create_process_with_jobs | Integration (onboarding handler) |

---

## 13.5 E2E (сквозные потоки)

Привязка к [ROADMAP.md](../ROADMAP.md) WP-023.

### Сценарии

1. **Lead → Order → Payment → Enrollment → Onboarding**
   - Менеджер создаёт заказ
   - Симуляция webhook ЮKassa (success)
   - Проверка: Enrollment создан, Process onboarding, Jobs в очереди

2. **Студент: OTP → LMS → прогресс**
   - Запрос OTP → вход
   - Открытие урока → отметка "Изучено"
   - Проверка: Progress обновлён

3. **Менеджер: дэшборд, CRM, создание заказа**
   - Login как manager
   - Просмотр дэшборда
   - Создание Order + payment link

4. **Куратор: прогресс группы**
   - Login как curator
   - Просмотр таблицы студент × урок
   - (этап 2) Проверка ДЗ

5. **Webhook acknowledgement**
   - POST /api/webhooks/yookassa с валидным payload
   - 200 OK в течение 1–2 сек

### Запуск

- Playwright, один тестовый инстанс (Next.js + Worker + PostgreSQL)
- Или: отдельный CI job с `docker compose up` для E2E

---

## 13.6 Моки и изоляция

### integrations/

Обёртки над внешними API должны допускать инъекцию mock'а:

```typescript
// src/server/integrations/mailgun.ts
export function createMailgunClient(config?: MailgunConfig) {
  const client = config?.mock ?? new RealMailgunClient(config);
  return client;
}
```

### Рекомендации по мокам

| Сервис    | В unit/integration                                                 | В E2E           |
| --------- | ------------------------------------------------------------------ | --------------- |
| ЮKassa    | Mock: возврат фиксированного payment_url, webhook — локальный POST | Sandbox         |
| Mailgun   | No-op или mock (запись в memory)                                   | Sandbox / no-op |
| Telegram  | grammY mock, не отправлять реальные сообщения                      | Sandbox / no-op |
| Zoom      | Mock API responses                                                 | Sandbox         |
| Kinescope | Mock embed URL                                                     | Sandbox         |

---

## 13.7 CI и критерии

- **Unit + Integration**: запуск в каждом PR
- **E2E**: на merge в main или nightly (если долго)
- **Порядок**: `npm run test:unit` → `npm run test:integration` → `npm run test:e2e`

Команды (предполагаемые):

```bash
npm run test          # unit + integration
npm run test:unit
npm run test:integration
npm run test:e2e
```

---

## 13.8 Ссылки

- [05-atomic-operations.md](05-atomic-operations.md) — матрица операций, что тестировать
- [06-edge-cases.md](06-edge-cases.md) — паттерны идемпотентности, RBAC, edge cases
- [02-architecture.md](02-architecture.md) — Worker, pg-boss, транзакционная оркестрация
- [ROADMAP.md](../ROADMAP.md) — WP-023 E2E тесты
