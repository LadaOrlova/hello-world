# Архитектурные решения для edge-кейсов

> Часть архитектуры Zamesin IS.
> Основной документ: [PLAN.md](../PLAN.md) | Доменная модель: [01-domain-model.md](01-domain-model.md)
> Архитектура: [02-architecture.md](02-architecture.md)

Разделены на две группы: **реализовать сразу** (дёшево и важно) и **реализовать позже** (сложно или некритично на старте). Единый формат каждой секции: **Проблема** — описание; **Решение** — описание (при необходимости с примером реализации).

---

# РЕАЛИЗОВАТЬ СРАЗУ

## 6.1 Идемпотентность оплат

**Проблема:** Двойная оплата при повторном webhook от ЮKassa или при двойном нажатии «Оплатить» пользователем.

**Решение:**

1. `provider_payment_id` — UNIQUE constraint в таблице Payment. Повторный webhook → constraint violation → catch → 200 OK (no-op).
2. `idempotency_key` — UUID от фронтенда при нажатии «Оплатить», передаётся в ЮKassa API. Повторное нажатие = тот же ключ = тот же платёж.
3. WebhookLog — каждый входящий webhook сохраняется в сыром виде. Если формат изменился → webhook сохранён, алерт команде, перепарсить позже.

```
// Пример: webhook handler
try {
  await prisma.payment.create({ data: { ... } });
} catch (e) {
  if (e.code === 'P2002') return res.status(200).end(); // UNIQUE violation
  throw e;
}
```

## 6.2 Резервирование мест

**Проблема:** Как не oversell (продать больше мест, чем есть) и как освобождать неоплаченные резервы.

**Решение:** При создании Order: проверка `Cohort.enrolled_count < max_students`, создание Enrollment со status='pending'. Если оплата не пришла — менеджер вручную удаляет/помечает expired. Без автоматического TTL Job на этапе 1 (при 10 зачислениях в день race маловероятен). Race при параллельных заявках — см. 6.28.3.

```
// Проверка при создании Order
const cohort = await prisma.cohort.findUnique({ where: { id } });
if (cohort.enrolled_count >= cohort.max_students) throw new Error('Места заняты');
```

## 6.3 OTP-аутентификация (better-auth)

**Проблема:** Безопасная аутентификация без паролей, защита от brute-force, rate limiting, управление сессиями.

**Решение:** better-auth + Email OTP plugin. OTP: 6 цифр, TTL 5 мин, макс. 5 попыток; код через Mailgun. Verification (better-auth) — автоочистка expired. Сессии в PostgreSQL — отзыв, импersonation, аудит. Admin plugin: роли, бан, импersonation. Bearer plugin — API для ботов. Конфиг: `otpLength: 6`, `expiresIn: 300`, `allowedAttempts: 5`.

## 6.4 RBAC (4 роли + доступ по связи)

**Проблема:** Разграничение доступа: кто что видит и что может делать. B2B — не роль, а связь с компанией.

**Решение:** Роли: admin (всё), manager (кроме системных настроек), curator (свой поток, ДЗ), student (LMS, личный кабинет). B2B: доступ по `Company.contact_person_id = user.id`. tRPC middleware `requireRole()`, для куратора — проверка cohort_id + curator_group, для B2B — `requireCompanyAccess()`. Безопасность: ключи в env, Prisma (параметризованные запросы), sanitization JSON-полей.

```
// Пример middleware
if (!['admin', 'manager'].includes(ctx.user.role)) throw new TRPCError({ code: 'FORBIDDEN' });
```

## 6.5 ChatMembership синхронизация

**Проблема:** Студент должен быть в нужных TG-чатах по тарифу и потоку; при истечении доступа — удалён. Бот должен знать, кто «должен» быть участником.

**Решение:** `should_be_member` = (Enrollment.status=active) AND (support_expires_at не истекло) AND (Tier.telegram_chats включает чат) AND (chat.cohort_id IS NULL OR = cohort_id). Онбординг: создаём ChatMembership (should_be_member: true, status: pending), бот по chat_member → joined. Ежедневный cron: пересчёт should_be_member, предупреждение за 3 и 1 день, удаление, уведомление команде.

## 6.6 Price snapshots и целостность данных

**Проблема:** Изменение тарифа не должно влиять на уже зачисленных. Корректные доплаты и возвраты при смене валюты. Невозможность завершить когорту с активными студентами.

**Решение:** `Enrollment.price_snapshot` + `price_snapshot_currency` фиксируют цену на момент зачисления. Cohort.status → completed блокируется, если есть Enrollment со status='active' (application logic, см. 6.30.6). Product.is_active = false → нельзя создать Cohort, существующие работают. Currency: "RUB" | "USD".

## 6.7 Soft delete и retention

**Проблема:** Удаление без потери истории; восстановление; очистка старых данных.

**Решение:** Soft delete: `deleted_at` для User, Product, Cohort, Company. Prisma middleware — фильтр `deleted_at IS NULL`. Восстановление — обнулить deleted_at. Retention: pg-boss archiveCompletedAfterSeconds; AuditLog — 2 года, затем архив (cron); Event — хранить всё; Verification — better-auth очищает.

## 6.8 Доступ к материалам с истечением

**Проблема:** Два разных срока: доступ к записям (может быть вечным) и доступ к куратору/обновлениям (1 год).

**Решение:** `materials_access_expires_at` — доступ к записям (null = вечный). `support_expires_at` — куратор и обновления (1 год с enrolled_at). При истечении support — записи остаются. Middleware при запросе к LMS проверяет оба поля.

---

# РЕАЛИЗОВАТЬ ПОЗЖЕ (этап 2+)

## 6.9 Откат онбординга при возврате

**Проблема:** При возврате средств нужно отозвать доступ к LMS, удалить из TG-чатов, отписать от календаря.

**Решение:** [Этап 2] Process(type: "rollback_onboarding"): Job 1 — revoke_lms_access, Job 2 — remove_from_tg_chats, Job 3 — unsubscribe_calendar, Job 4 — Enrollment.status → refunded, Job 5 — Order.status → refunded. Каждый шаг проверяет состояние — no-op если уже откатан. На этапе 1: менеджер вручную отзывает доступы.

## 6.10 Telegram: устойчивость к недоступности

**Проблема:** Студент заблокировал бота или не привязал TG — уведомления не доходят.

**Решение:** [Этап 2] Если `!user.telegram_user_id` или `tg_bot_status == 'blocked'` → отправить email, лог "TG unavailable, email fallback". При 403 от TG API → пометить TelegramAccount deleted/blocked, далее fallback на email. На этапе 1: Job failed → менеджер видит в дэшборде, решает вручную.

## 6.11 Rate limiting к внешним API

**Проблема:** Внешние API (Telegram, Zoom) имеют лимиты запросов. Превышение → 429, блокировка.

**Решение:** [Этап 2] In-memory Map в worker: Telegram max 30 msg/sec, Zoom max 10 req/sec. При превышении — setTimeout перед следующим запросом. Один worker — достаточно. Несколько worker'ов — счётчик в PostgreSQL (см. 6.30.4).

## 6.12 Расписание: целостность

**Проблема:** Два занятия в одно время; при переносе — синхронизация Zoom, Calendar, уведомлений.

**Решение:** [Этап 2] При создании/обновлении Schedule — проверка пересечений по (cohort_id, scheduled_at, duration_minutes). Конфликт → 409 Conflict. Перенос: Process("schedule_reschedule") — Job 1: update_calendar_event, Job 2: update_zoom_meeting, Job 3: notify_students (за 1 день, 1 час, 15 мин).

## 6.13 Посещаемость

**Проблема:** Сопоставить участников Zoom с Enrollments для отметки посещаемости.

**Решение:** [Этап 2] Матчинг: 1) по email (Zoom participant = User.email), 2) по имени (display name ~ User.name), 3) нераспознанные — ручная привязка менеджером. Автоотметка present: joined и > 50% времени занятия.

## 6.14 Рассрочки Т-Банк

**Проблема:** Дефолт по рассрочке — нужно знать и реагировать.

**Решение:** [Этап 2] Payment.installment_status: active | defaulted | cancelled. Webhook от Т-Банк при дефолте → installment_status = 'defaulted', уведомление менеджеру. Менеджер решает: связаться или suspend enrollment. Этап 1: вручную.

## 6.15 Домашние задания: дедлайны

**Проблема:** Дедлайн ДЗ, напоминания, учёт просроченных сдач.

**Решение:** [Этап 2] Homework.deadline_days — дней после enrolled_at. Cron: за 1 день — TG студенту; просрочено — HomeworkSubmission.overdue = true. Куратор решает, принимать ли просроченное. Дедлайн = `enrolled_at + deadline_days`.

## 6.16 Обратная связь

**Проблема:** Кому слать запрос ОС; как валидировать ответы; не включать невалидные в аналитику.

**Решение:** [Этап 3] Таргет: enrollment.status IN ('active', 'completed'), исключать refunded, suspended, pending. NPS: 0–10. Свободный текст: принимать всё, is_valid=false при < 3 символов. Невалидные не включать в AI-суммаризацию.

## 6.17 Warmup-бот (замена BotHelp)

**Проблема:** Прогрев лидов через TG-воронку (замена BotHelp).

**Решение:** [Будущая фаза] grammY Conversations: воронка (вебинар → контент → покупка), сбор email/телефона → привязка к User, цепочки по расписанию, все шаги → Event. Этап 1: BotHelp продолжает работать.

## 6.18 FAQ-бот

**Проблема:** Автоответы на вопросы о курсе без галлюцинаций; контроль качества.

**Решение:** [Будущая фаза] System prompt: «Отвечай ТОЛЬКО о курсе [название]. Если не уверен — "Уточните у куратора"». temperature: 0.3, контекст — материалы + FAQ. Логирование ответов. Кнопка «Ответ неверный» → при 3+ жалобах автоотключение и alert куратору.

## 6.19 Мониторинг

**Проблема:** Видеть застрявшие Jobs, зависшие оплаты, расхождения ChatMembership; оперативно реагировать.

**Решение:** [Этап 2] Дэшборд: Dead Jobs, Pending Payments > 30 мин, расхождения should_be_member ≠ status, pg-boss stats. Алерты в TG: dead jobs > 5, payment > 1 ч, расхождения > 10. Этап 1: только дэшборд, без алертов.

## 6.20 Апгрейд тарифа

**Проблема:** Студент хочет перейти на более высокий тариф; доплата, смена чатов.

**Решение:** [Этап 2] Доплата = новая цена − price_snapshot. Новый Order → оплата → Enrollment.tier_id обновлён, пересчёт ChatMembership, добавление в новые чаты, удаление из старых (если не пересекаются). Tier.upgrade_to_tier_id — подсказка UI.

## 6.21 Кросс-продуктовые бонусы

**Проблема:** Автоматическое начисление бонуса (Maker, AURA) при покупке КДП/BOOST.

**Решение:** [Этап 3] Event handler на payment.success: проверка Product.bonus_config → создание Subscription (source: "bonus", source_order_id), без запроса согласия. Уведомление: «Вам начислена подписка Maker на N мес.».

## 6.24 Обнаружение неактивных студентов

**Проблема:** Студент давно не заходил — куратор должен знать и связаться.

**Решение:** [Этап 2] Cron "lms.check_inactive_students": для каждого active Enrollment считаем days_inactive = NOW() − MAX(last_event, last_progress). Порог: курсы 7 дней, интенсивы 3 дня (по duration_days). При превышении → Event student_inactive, TG куратору. Куратор может пометить «уведомлён» — не слать повторно.

## 6.23 Объединение профилей (merge_users)

**Проблема:** Один человек зарегистрировался под разными email — дубликаты, неполный LTV.

**Решение:** [Этап 2] merge*users(primary_id, duplicate_id): валидация (duplicate не admin) → перенос всех FK на primary (Enrollment, Order, Lead, ChatMembership, TelegramAccount, Company.contact_person_id, с проверкой UNIQUE) → мерж пустых полей (phone, telegram*\*) → deleted_at дубликата → AuditLog + Event. Требует preview + confirm. Необратимо.

## 6.22 Скидка выпускникам

**Проблема:** Выпускникам — автоматическая скидка при повторной покупке.

**Решение:** [Этап 2] is_alumni = EXISTS(Enrollment WHERE user_id = ? AND status = 'completed'). При создании Order — скидка 20%, кросс-продуктовая (КДП↔BOOST). Совместима с промокодами — применяется лучшая скидка.

## 6.25 Добавление урока во время активного потока

**Проблема:** Курс начался с 10 уроками, к концу — 15. Нужны Progress для новых уроков у уже зачисленных.

**Решение:** [Этап 1] При онбординге — Progress только для существующих уроков. При lms.lessons.create — Lesson + LessonRevision; Progress автоматически создаётся для всех active Enrollments потоков того же продукта (status: not_started). CohortContent (этап 2): fallback — Lesson.current_revision_id.

---

# ОРКЕСТРАЦИЯ И ПРОЦЕСС

## 6.26 Оркестрация pg-boss jobs — вопросы и риски

**Проблема:** Сложность отладки, потеря Jobs, двойные webhook'и, риски (зависание, неверный payload).

**Решение:** Отладка — trace_id + Process.steps, логи по trace_id, dead jobs в дэшборде. Job падает — retry с backoff, затем менеджер вручную. Jobs не теряются (pg-boss jobs ставятся в той же транзакции через `sendJobInTransaction`, PostgreSQL ACID). Двойной webhook — идемпотентность (6.1). Строгая типизация + Zod валидация payload. Каталог событий в 02-architecture.md. Демо: happy path, дэшборд Process, сценарий отказа.

---

## 6.27 Процесс тестирования и доработки по edge-кейсам

**Проблема:** Как итерировать по edge-кейсам: реестр, приоритизация, репродукция, SLA. Новые кейсы обнаруживаются в проде.

**Решение:** Реестр «Обнаруженные в проде» (6.33). Приоритизация: вероятность × влияние. Репродукция — шаги или ссылка на тест. SLA (MVP): critical 24ч, high 1 неделя. Фаза 0.5: каждый «реализовать сразу» → тест; E2E happy path + повторный webhook. Фаза 1+: обнаружен → реестр → приоритет → тест → фикс или backlog; ревью раз в 2 недели.

---

# НЕПОКРЫТЫЕ EDGE-КЕЙСЫ (с решениями)

## 6.28 Критичные

### 6.28.1 Webhook timeout (ЮKassa повторяет при таймауте)

**Проблема:** Handler > 30 сек → ЮKassa считает неудачу, шлёт повторно.

**Решение:** Webhook handler отвечает < 5 сек. Только: validate → WebhookLog → проверка idempotency → emit → 200 OK. Вся тяжёлая работа — в pg-boss Jobs. Повторный webhook — идемпотентность (6.1) защищает.

### 6.28.2 Одновременная оплата двух заказов одним пользователем

**Проблема:** Два webhook'а почти одновременно. Race на Enrollment?

**Решение:** Разные provider_payment_id → разные Payment. UNIQUE(user_id, cohort_id) — второй Enrollment в тот же cohort = constraint violation. Разные cohorts — оба Enrollment создаются. Race невозможен. Пример: каждый webhook в своей транзакции, constraint ловит дубль.

### 6.28.3 Когорта заполнена между проверкой и созданием Enrollment

**Проблема:** check-then-act race. Проверили — места есть. Создали — уже нет.

**Решение:** Атомарная операция в одной транзакции: `UPDATE cohort SET enrolled_count = enrolled_count + 1 WHERE id = ? AND enrolled_count < max_students RETURNING *`. Если 0 rows — места нет, откат. Альтернатива: SELECT FOR UPDATE на Cohort перед созданием Enrollment.

```sql
UPDATE cohort SET enrolled_count = enrolled_count + 1
WHERE id = $1 AND enrolled_count < max_students
RETURNING *;
```

### 6.28.4 Частичный онбординг (LMS есть, чатов нет)

**Проблема:** Студент оплатил, не вступил в чаты. Что через 30 дней? Через год?

**Решение:** Этап 1: ручная работа менеджера (дэшборд «не вступил»). Этап 2: Cron — если Process completed, но ChatMembership status != joined и > 7 дней → напоминание по email. Онбординг-страница остаётся доступной, ссылки не expire.

### 6.28.5 Дубликаты Lead/User после миграции AirTable

**Проблема:** Дедупликация при импорте есть. Дубликат создан вручную после импорта?

**Решение:** merge_users (6.23) — этап 2. Этап 1: ручная дедупликация при импорте (07). После — менеджер использует merge_users или вручную объединяет данные.

---

## 6.29 Средние

### 6.29.1 Студент сменил email после оплаты

**Проблема:** OTP и уведомления — куда отправлять после смены email?

**Решение:** better-auth: обновление email с подтверждением на новый. После User.email — все уведомления на новый. При смене — подтверждение на старый (если доступен) или через менеджера (impersonation).

### 6.29.2 Отмена заказа до оплаты

**Проблема:** Order.status = cancelled. Нужно ли освобождать зарезервированное место?

**Решение:** При cancelled — Enrollment (pending) помечается expired или удаляется. Cron: pending без оплаты > 48ч → auto-expire. Ручная отмена — мгновенно. Освобождение места — автоматически при expired.

### 6.29.3 Промокод истёк между корзиной и оплатой

**Проблема:** Order создан со скидкой. Оплата через 2 дня — промокод истёк.

**Решение:** При создании payment link (PAY.1) — проверка PromoCode.valid_until и usage_count. Если истёк — 400 «Промокод истёк. Оформите заказ заново». Order.amount фиксирует сумму на момент создания ссылки. Пример: `if (promo.valid_until < now) throw new Error('PROMO_EXPIRED')`.

### 6.29.4 Менеджер изменил состав групп куратора во время онбординга

**Проблема:** assign_curator выполнен. Студент в группе A. Менеджер переместил в B.

**Решение:** Функция «Переместить студента в группу» (M.21) обновляет CuratorGroup. Последнее действие менеджера имеет приоритет. Cron access.check_memberships не трогает группы. Ручное перемещение — ок.

### 6.29.5 Подписка AURA: студент отменил карту до списания

**Проблема:** Когда отключаем доступ к чатам после неудачного списания?

**Решение:** Grace period (7 дней — PLAN.md). После неудачного списания: уведомление, Subscription.status = grace_period. Cron через 7 дней: status = cancelled → Job удаляет из чатов Makers. Доступ отзывается после grace period.

### 6.29.6 B2B: компания купила 10 мест, зачислили 8, 2 истекли

**Проблема:** Резервирование мест. TTL для неиспользованных?

**Решение:** B2B Order: N placeholder Enrollments (pending, company_id) или ReservedSlot. TTL 30 дней — если не привязан User, освобождение. Или менеджер вручную отменяет. Уточнить у заказчика: авто-TTL.

### 6.29.7 Два потока одного продукта с пересекающимися датами

**Проблема:** Студент в потоке 14. Хочет в поток 15. Можно ли?

**Решение:** UNIQUE(user_id, cohort_id) — разные cohorts разрешены. Ограничение «один active на продукт» — опционально. Если да: проверка при Order — `EXISTS(Enrollment WHERE user_id = ? AND product_id = ? AND status = 'active')`. Уточнить у заказчика.

### 6.29.8 B2C: пользователь вернулся в checkout после незавершённой оплаты

**Проблема:** При повторном входе в checkout у пользователя уже может существовать `Order.status='pending'` на тот же поток. Блокировка такого кейса приводит к потере оплаты, а старая payment-ссылка может быть уже невалидной у провайдера.

**Решение:** Не создавать новый `Order`, а переиспользовать текущий pending-order по `(buyer, cohort)`:
- если есть валидный pending payment attempt — вернуть его для продолжения оплаты;
- если attempt устарел/невалиден — создать новый payment attempt для того же order;
- `Enrollment` по-прежнему создаётся только после `Payment.status='success'`;
- второй `payment.succeeded` webhook для уже оплаченного order обрабатывается как no-op (инвариант `single-success` на order).

---

## 6.30 Низкие (этап 2+)

### 6.30.1 GDPR / запрос на удаление данных

**Проблема:** Полное удаление User и всех связанных данных по запросу.

**Решение:** [Этап 2+] Операция «Полное удаление пользователя»: каскад анонимизации/удаления (Enrollment, Order, Lead, Event). AuditLog фиксирует удаление. Требует подтверждения (admin impersonation).

### 6.30.2 Разные валюты в одном заказе

**Проблема:** order.currency vs tier.price_rub vs tier.price_usd — смешение валют.

**Решение:** Order.currency определяет валюту заказа. Enrollment.price_snapshot_currency = Order.currency. Один Order — одна валюта.

### 6.30.3 Изменение цены тарифа во время оформления

**Проблема:** Order создан, оплата через 2 дня — цена тарифа изменилась.

**Решение:** Order.amount фиксируется при создании payment link. Payment link TTL 24–48ч. Истёк — пересоздать Order с актуальной ценой. При оплате — ЮKassa возвращает сумму; при расхождении — уточнить поведение webhook.

### 6.30.4 Telegram API rate limit (429) при нескольких worker'ах

**Проблема:** 6.11 — in-memory в одном worker. Несколько worker'ов — счётчик не общий.

**Решение:** Rate limit в PostgreSQL: таблица RateLimitBucket или использование pg-boss heartbeat. Альтернатива: один выделенный worker для notification.\* очередей.

### 6.30.5 Студент в нескольких потоках одного продукта

**Проблема:** Повторная покупка (выпускник) — тот же продукт, другой поток.

**Решение:** UNIQUE(user_id, cohort_id) — разные cohorts разрешены. Выпускник КДП → КДП поток 20 — новый Enrollment. Ограничение «один active на продукт» — опционально.

### 6.30.6 Cohort completed с active enrollments

**Проблема:** 6.6 — «Cohort не может стать completed». Кто проверяет?

**Решение:** Application logic при смене Cohort.status: блокировать completed, если `EXISTS(Enrollment WHERE cohort_id = ? AND status = 'active')`. 409 Conflict. Опционально: DB trigger.

```typescript
if (newStatus === "completed") {
  const active = await prisma.enrollment.count({
    where: { cohortId, status: "active" },
  });
  if (active > 0)
    throw new TRPCError({
      code: "CONFLICT",
      message: "Есть активные студенты",
    });
}
```

---

# РИСКИ ВЫКАТКИ И РЕКОМЕНДАЦИИ ДЛЯ ДЕМО

## 6.31 Риски по категориям

**Проблема:** Риски выкатки: PostgreSQL, pg-boss, внешние API, миграция, команда, ожидания, оркестрация.

**Решение:**

| Категория       | Риск                              | Митигация                                             |
| --------------- | --------------------------------- | ----------------------------------------------------- |
| Технические     | PostgreSQL недоступен             | Managed DB, backup, health check                      |
| Технические     | pg-boss job застрял               | Dead job дэшборд, алерт в TG, ручной retry            |
| Технические     | Внешний API недоступен            | Retry в pg-boss, fallback (6.10)                      |
| Технические     | Миграция AirTable — ошибки        | Dry-run, валидация, откат (07)                        |
| Организационные | Команда не готова                 | Обучение, read-only AirTable                          |
| Организационные | Ожидание 100% edge cases          | Реестр, приоритизация. MVP — критичные пути           |
| Оркестрация     | Частичный онбординг               | Process.status = partially_failed, менеджер повторяет |
| Оркестрация     | Job выполнен, Process не обновлён | Worker обновляет step после handler. Для DB-only шагов можно объединить в транзакцию. Для API-шагов защита — идемпотентность handler (см. [17-reliable-events.md](17-reliable-events.md)). |

## 6.32 Рекомендации для прототипа (демонстрация)

**Проблема:** Что показать заказчику для убеждения; чего избегать на первом демо.

**Решение:** Показать: happy path, повторный webhook (идемпотентность), дэшборд Process, список edge cases с покрытием тестами. Не показывать: возврат, B2B, подписки, AI-агенты. Метрики: Webhook < 2 сек, тесты < 30 сек, E2E < 2 мин, критические edge cases — 100% с тестами.

---

## 6.33 Обнаруженные в проде (реестр)

**Проблема:** Новые edge cases обнаруживаются после выкатки. Нужен реестр для итерации.

**Решение:** Новые кейсы добавляются сюда. Формат: дата, описание, приоритет, решение/статус.

---

## 6.34 Атомарность критичного пути payment → onboarding

**Проблема:** Три риска оркестрации для критичных бизнес-путей:

| ID | Риск | Суть |
|----|------|------|
| A | Crash после бизнес-записи, до jobs | Payment/Order записаны, но onboarding jobs не поставлены — деньги получены, студент не зачислен |
| B | Частично выполненные handlers | Один handler упал в цепочке `emit()` — остальные не выполнены и не будут повторены |
| C | Job сделал side effect, но step не обновился | При retry — дублирование побочного эффекта (двойной доступ, двойное уведомление) |

**Решение:** pg-boss-in-TX — один `$transaction` блок, включающий бизнес-запись и raw INSERT в `pgboss.job`. Подробное описание, SQL, код и порядок внедрения — в [docs/17-reliable-events.md](17-reliable-events.md).
