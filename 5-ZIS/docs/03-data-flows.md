# Процессы обмена информацией (Data Flows)

> Часть архитектуры Zamesin IS.
> Основной документ: [PLAN.md](../PLAN.md) | Доменная модель: [01-domain-model.md](01-domain-model.md)

---

## 3.1 Воронка продаж (Lead → Order → Enrollment)

```
[Внешние каналы]                [Система]
                                     │
TypeForm ──────┐                     │
Лендинг ───────┤                     │
Instagram ─────┼──→ Lead (создание) ─┤
Реферал ───────┤        │            │
TG-бот ────────┤        ▼            │
Диагностика ───┘   Менеджер          │
                   (назначение)      │
                        │            │
                        ▼            │
                   Квалификация      │
                   (общение с лидом) │
                        │            │
                   ┌────┴────┐       │
                   │         │       │
                B2C:       B2B:      │
             qualified   negotiation │  [этап 2: расширенные
                │        → proposal  │   статусы Lead для B2B]
                │        → contract  │
                │        → invoice   │
                │         │          │
                └────┬────┘          │
                     ▼               │
                   Order ────────────┼──→ ЮKassa (B2C)
                   (создание)        ├──→ Т-Банк (рассрочка)
                        │            ├──→ Invoice + PDF (B2B)
                        ▼            │
                   Payment ──────────┤
                   (подтверждение)   │
                        │            │
                        ▼            │
                   Lead.status ──────┤──→ converted
                   → converted       │
                        │            │
                   Enrollment ───────┼──→ Event: payment.success
                   (зачисление)      ├──→ pg-boss jobs: запуск онбординга (в транзакции)
                                     └──→ Event: запись в аналитику
```

Инвариант потока: до подтверждения оплаты (`Payment.status=success` для B2C, `Invoice.status=paid` для B2B) `Enrollment` не создаётся.

## 3.2 Онбординг студента (веб-страница + чаты)

```
Event: payment.success → Process (type: "onboarding")
        │
        │   Worker выполняет шаги параллельно (pg-boss):
        │
        ├──→ [Job] grant_lms_access
        │         ├── Создать Progress записи для всех уроков
        │         └── Enrollment.lms_access_granted = true
        │
        ├──→ [Job] create_onboarding_page
        │         ├── Определить чаты: Tier.telegram_chats[] ∩ (cohort_id IS NULL OR cohort_id = Enrollment.cohort_id)
        │         │   (тариф задаёт набор чатов; поток фильтрует cohort-specific чаты)
        │         ├── Создать ChatMembership (should_be_member: true, status: pending)
        │         ├── Сгенерировать уникальную ссылку на онбординг-страницу
        │         └── Отправить ссылку студенту (email + TG)
        │
        │         Онбординг-страница (веб):
        │         ┌─────────────────────────────────────────┐
        │         │ Добро пожаловать! Вступите в чаты:       │
        │         │                                         │
        │         │ ☐ Чат "КДП Поток 14"    [Вступить]     │
        │         │ ☐ Канал "Записи"         [Вступить]     │
        │         │ ☐ Чат "Воркшопы"        [Вступить]     │
        │         │                                         │
        │         │ (бот отслеживает вступления real-time)  │
        │         │ (чекбоксы загораются зелёным ✓)         │
        │         │                                         │
        │         │ [Все чаты зелёные → Перейти к LMS]      │
        │         └─────────────────────────────────────────┘
        │
        ├──→ [Job] subscribe_calendar
        │         └── Google Calendar API: отправить ссылку на подписку
        │
        ├──→ [Job] assign_curator
        │         └── Назначить в группу куратора (round-robin по загрузке)
        │
        └──→ [Job] send_welcome_msg (chain: после остальных)
                  └── Email + TG: приветственное сообщение + инструкции

Обновление статуса:
  - Каждый Job обновляет Process.steps[N].status
  - Бот: при chat_member event → обновить ChatMembership.status → joined
  - Enrollment: lms_access_granted ✓, tg_added ✓, calendar_subscribed ✓
  - Если Job провалился после всех retry → менеджер видит ошибку, может повторить
```

## 3.3 LMS: контент и прогресс

> Версионирование контента (SoK): [docs/11-content-versioning.md](11-content-versioning.md)

```
[Менеджер — Контент-админка]              [Студент — LMS]
        │                                       │
  Создаёт Module ──→ Product.modules[]          │
        │                                       │
  Создаёт Lesson ──→ Module.lessons[]           │
        │   ├── type: text | video | text_video  │
        │   └── deadline_at                      │
        │                                       │
  Редактирует контент:                          │
        │   → LessonRevision (новая ревизия)    │
        │   → Lesson.current_revision_id (SoK)  │
        │                                       │
  (drag-and-drop для порядка)                   │
        │                                       │
        │                                 Открывает урок
        │                                       │
        │                                 (контент из LessonRevision
        │                                  через CohortContent [2]
        │                                  или Lesson.current_revision_id)
        │                                       │
        │                                 Event: lesson_opened
        │                                       │
        │                                 Изучает материал
        │                                       │
        │                                 Нажимает "Изучено" ✓
        │                                       │
        │                                 Progress.status → completed
        │                                 Event: lesson_completed
        │                                       │
[Куратор — Дэшборд]                           │
        │                                       │
  Видит таблицу "студент × урок"               │
  с цветовой индикацией:                        │
  🟢 completed  🟡 in_progress  ⚪ not_started  │
```

## 3.4 Домашние задания [этап 2]

```
[Менеджер]              [Студент]                [Куратор]
     │                       │                        │
Создаёт Homework       Видит ДЗ в LMS               │
(привязка к Lesson)          │                        │
     │                  Сдаёт ответ                   │
     │                       │                        │
     │              HomeworkSubmission                 │
     │              (status: submitted)                │
     │                       │                        │
     │              Event: homework_submitted     Видит в дэшборде
     │                       │                        │
     │                       │                  Рецензирует:
     │                       │                  ├── accepted ✓
     │                       │                  ├── revision_needed
     │                       │                  └── feedback (текст)
     │                       │                        │
     │              Event: homework_reviewed           │
     │                       │                        │
     │              [Job] TG: уведомление студенту    │
     │              "Ваше ДЗ проверено: [статус]"     │
```

## 3.5 Учебный цикл (расписание + воркшопы) [этап 2]

```
[Менеджер]                          [Система]                    [Внешние сервисы]
        │                                │
  Создаёт Schedule ──────────────→ Schedule
        │                                │
        │                                ├──→ [Job] Zoom API: создать встречу
        │                                │    └── + breakout rooms для кураторов
        │                                │
        │                                ├──→ [Job] Google Calendar API:
        │                                │    создать/обновить событие
        │                                │
        │                                └──→ [Job] TG Bot: уведомить студентов
        │                                     (за 1 день + за 1 час + за 15 мин)
        │
  [День занятия]                         │
        │                                │
  Проводится воркшоп ←──── Zoom ─────────┤
        │                                │
        │                          Attendance: фиксация
        │                          (ручная отметка менеджером
        │                          или авто из Zoom API)
        │                                │
  Загрузка записи ──────────────→ Kinescope
        │                                │
        │                          Lesson.video_url обновлён
        │                                │
        │                          [Job] TG Bot: "Запись занятия доступна"
```

## 3.6 CRM Pipeline (Lead) [этап 1-2]

```
Lead создан → Менеджер квалифицирует
        │
        ├── status: new → contacted → qualified
        │   └── B2C: квалифицирован → создать Order → converted
        │
        ├── status: negotiation (B2B / сложные сделки)
        │   └── Менеджер обсуждает условия, заполняет tier_id, amount
        │
        ├── status: proposal
        │   └── Менеджер отправляет КП
        │
        ├── status: contract (для B2B)
        │   └── Подписание договора
        │
        ├── status: invoice (для B2B)
        │   └── Выставлен счёт
        │
        ├── status: converted
        │   └── Оплата получена → Event: lead_converted
        │       └── Автоматическое создание Order + Enrollment
        │
        └── status: lost
            └── Event: lead_lost

[Kanban-доска в Web App — фильтр по статусам]
┌──────┬───────────┬──────────┬────────────┬────────────┬────────────┬──────┬───────────┐
│ Новые│ Контакт   │ Квалиф.  │ Переговоры │ КП         │ Договор    │ Счёт │ Оплачено  │
│      │           │          │            │            │            │      │           │
│ ┌──┐ │ ┌───────┐ │ ┌──────┐ │ ┌────────┐ │ ┌────────┐ │      │            │ ┌───────┐ │
│ │5 │ │ │Иванов │ │ │Сидор.│ │ │ ООО X  │ │ │ ООО Z  │ │      │            │ │Петров │ │
│ └──┘ │ └───────┘ │ └──────┘ │ │ 180к ₽ │ │ │ 250к ₽ │ │      │            │ │ 25к ₽ │ │
│      │           │          │ └────────┘ │ └────────┘ │      │            │ └───────┘ │
└──────┴───────────┴──────────┴────────────┴────────────┴────────────┴──────┴───────────┘

Этап 1: статусы new → contacted → qualified → converted → lost (базовая воронка).
Этап 2: статусы negotiation → proposal → contract → invoice → converted (B2B pipeline).
```

## 3.7 B2B заявка на обучение и документооборот

```
Lead (source=b2b) → approve
        │
        ▼
Company (active) + CompanyEmployee (кадровый список)
        │
        ▼
CompanyRequest (header + lines)
        │
        ├── выбор Contract
        ├── выбор Product/Cohort
        ├── выбор CompanyEmployee[]
        └── расчет суммы (unit * employees - discount)
             │
             ▼
Contract + Invoice
        │
        ├── Invoice.contract_id (required) → Contract.id
        ├── Invoice.status: draft → sent → paid
        ├── CompanyRequest.status: submitted → invoiced → paid
        └── override-флаг (admin/manager) допустим для DEMO
             │
             ▼
Операционка после оплаты
        │
        ├── [Admin] Создать пользователей для CompanyEmployee с user_id=NULL
        ├── [Admin] Создать Order (type=b2b) по каждой строке заявки
        ├── [System] Для каждого Order гарантировать Enrollment + onboarding process
        ├── [System] Сформировать Act по Invoice (идемпотентно)
        └── CompanyRequest.status: users_created → enrollments_started → fulfilled
             │
             ▼
Act (закрывающие документы)
        └── один Act на один Invoice (1:1)

Принцип: Order-first для обучения сохраняется.
Invoice/Contract/Act — документный и финансовый контур,
Order/Enrollment — контур фактического доступа к обучению.
```

## 3.8 Сбор обратной связи [этап 3]

```
FeedbackCampaign (активация)
        │
        ├──→ Определить целевых студентов
        │    (Enrollment в Cohort WHERE status IN ('active', 'completed'))
        │
        ├──→ [Job] Отправка запросов
        │    ├── Telegram: сообщение с ссылкой на форму
        │    └── Email: письмо со ссылкой на форму
        │
        ├──→ [Scheduled Job, через 24ч] Напоминание неответившим
        │
        ├──→ Сбор FeedbackResponse
        │    └── Сохранение ответов, NPS score
        │
        └──→ [Job] AI-анализ (если доступен LLM API)
             ├── Суммаризация свободных ответов
             └── Запись ai_summary в FeedbackResponse

[Дэшборд]
├── % ответивших по кампании
├── Средний NPS (по потоку, по продукту, тренд)
└── Список студентов: кто ответил, кто нет
```

## 3.9 Завершение обучения (Offboarding) [этап 3]

```
Cohort.status → completed → Process (type: "offboarding")
        │
        ├──→ Для каждого Enrollment (status = active):
        │    │
        │    ├──→ [Job] Проверка критериев завершения
        │    │    ├── Все обязательные уроки пройдены?
        │    │    ├── Все ДЗ сданы и приняты?
        │    │    └── Посещаемость выше минимума?
        │    │
        │    ├──→ [Job] Генерация Certificate (если критерии пройдены)
        │    │    ├── Уникальный номер (UUID)
        │    │    ├── PDF по шаблону
        │    │    ├── QR-код для верификации
        │    │    └── Отправка студенту (Email + TG)
        │    │
        │    ├──→ Enrollment.status → completed
        │    │    (is_alumni вычисляется автоматически из наличия completed enrollments)
        │    │
        │    ├──→ [Job] Предложение подписки Makers (TG-сообщение)
        │    │    └── Если студент согласен → Subscription (source: post_course)
        │    │
        │    └──→ [Job] Добавление в чаты выпускников
        │         ├── "Замесим Product Club"
        │         └── "Респондентошная"
        │
        ├──→ [Job] Act → PDF для B2B-студентов (если есть Invoice)
        │
        └──→ [Job] Финальная FeedbackCampaign (end_course)
```

## 3.10 Telegram: контроль доступа [Cron Job, ежедневно]

```
[pg-boss cron: "access.check_memberships" — ежедневно]
        │
        ├──→ Cron вычисляет список ChatMembership для проверки
        │
        ├──→ Cron ставит fan-out jobs в pg-boss:
        │    queue: access.check_memberships.process
        │    result: enqueued_count = N
        │
        ├──→ Worker обрабатывает каждую запись:
        │    │
        │            ├── Рассчитать should_be_member:
        │    │   ├── Enrollment.status == active?
        │    │   ├── Enrollment.support_expires_at не истекло?
        │    │   ├── Tier включает этот чат (Tier.telegram_chats[])?
        │    │   └── Чат относится к потоку (TelegramChat.cohort_id IS NULL OR = Enrollment.cohort_id)?
        │    │
        │    ├── should_be_member = true, status != joined:
        │    │   └── Если pending > 2 дней → уведомить менеджера
        │    │
        │    └── should_be_member = false, status == joined:
        │        ├── Предупреждение за 3 дня
        │        ├── Предупреждение за 1 день
        │        └── Удаление из чата → ChatMembership.status = kicked
        │
        └──→ [Job] Уведомление команде в служебный TG-чат:
             "Удалены: 3 студента | Предупреждены: 5 | Не вступили: 2"

Важно:
  - Успех cron = jobs поставлены в очередь.
  - Бизнес-результат формируется downstream jobs в worker.
```

## 3.11 Управление подпиской AURA/Maker [этап 3]

```
[Ежемесячно — Cron Job через pg-boss]
        │
        ├──→ Cron выбирает Subscription (status = active, is_recurring = true)
        │
        ├──→ Cron ставит jobs в pg-boss:
        │    queue: billing.subscription.charge
        │    result: enqueued_count = N
        │
        ├──→ Worker по каждой подписке:
        │    ├── [Job] Попытка списания → ЮKassa
        │    ├── Успех → продлить next_payment_date
        │    └── Неудача → уведомление + grace period → cancel
        │
        └──→ [Job] Проверка доступа к TG-чатам Makers
             ├── Активная подписка → OK
             └── Нет подписки → предупреждение → удаление

Кросс-продуктовые бонусы:
  - Покупка КДП → автоматическая подписка Maker на N месяцев
  - Покупка BOOST → автоматическая подписка AURA
  - Subscription.source = "bonus", source_order_id = Order.id

Важно:
  - Cron не ждёт выполнения списаний; он только оркестрирует постановку jobs.
```

## 3.15 Сквозная аналитика: лендинг → Lead [этап 2]

```
Задача: связать визит на лендинг с Lead для расчёта конверсии по каналам.

[Лендинг (landing_url)]
        │
        ├── UTM-метки в URL: ?utm_source=...&utm_medium=...&utm_campaign=...
        │
        ├── Яндекс Метрика: _ym_uid (cookie) + yclid (Яндекс Директ)
        │
        └── Заявка (TypeForm / форма на лендинге)
               │
               ├── Передаёт hidden fields:
               │   ├── utm_source, utm_medium, utm_campaign, utm_content, utm_term
               │   ├── yclid (если пришёл из Яндекс Директ)
               │   └── _ym_uid (Яндекс Метрика client ID)
               │
               └── Zamesin IS: webhook / API
                      │
                      ├── Создать Lead (DB.2)
                      ├── Lead.utm_tags = { source, medium, campaign, content, term }
                      ├── Lead.ym_client_id = _ym_uid (для сквозной аналитики)
                      ├── Lead.yclid = yclid (для связи с Яндекс Директ)
                      └── Event: lead_created (с UTM в event_data)

Дэшборд аналитики [этап 3]:
  ├── Конверсия по utm_source: лендинг → заявка → оплата
  ├── CAC по каналам (если добавить расходы на рекламу)
  ├── Яндекс Метрика Offline Conversions API:
  │   при payment_success → POST в Метрику (yclid + revenue)
  │   → Яндекс видит конверсию в рекламном кабинете
  └── ROI по кампаниям

⚠️ Уточнить у заказчика:
  - Используется ли Яндекс Директ? Если да — yclid обязателен
  - Нужна ли интеграция с Offline Conversions API Яндекс Метрики?
  - Какие ещё рекламные каналы (VK Ads, Google Ads)?
```

## 3.14 Временная интеграция с BotHelp [этап 1]

> На этапе 1 BotHelp продолжает работать для прогрева лидов.
> На этапе 2 BotHelp заменяется собственным warmup-ботом (grammY Conversations).

```
Задача: связать BotHelp-пользователя с User/Lead в Zamesin IS.

Вариант A: Webhook из BotHelp (рекомендуется)
  BotHelp → webhook при событии (подписка, тег, завершение воронки)
     │
     ├── Payload: { email, phone, telegram_id, tag, event }
     │
     └── Zamesin IS: POST /api/webhooks/bothelp
            │
            ├── Поиск Lead по email/phone (INT.3 dedup)
            ├── Если нет → создать Lead (source: "telegram_bot")
            ├── Обновить Lead.notes += "[BotHelp] тег: {tag}"
            ├── Если есть User с таким email → связать Lead.converted_to_user_id
            └── WebhookLog + Event

Вариант B: Ручной периодический импорт
  BotHelp → экспорт CSV (подписчики, теги)
     │
     └── Менеджер загружает CSV в Zamesin IS
            │
            ├── Скрипт: match по email/phone → создать/обновить Lead
            └── Реже, но проще в реализации

⚠️ Уточнить у заказчика:
  - BotHelp поддерживает webhook'и?
  - Какие данные собирает BotHelp (email, phone, telegram_id)?
  - Какие воронки активны и какие теги используются?
```

## 3.12 Событийная аналитика

```
КАЖДОЕ действие в системе → Event запись

Примеры:
  Студент открыл урок     → Event(lesson_opened, {lesson_id, enrollment_id})
  Оплата успешна          → Event(payment_success, {order_id, amount})
  Студент вступил в чат   → Event(chat_joined, {chat_id, user_id})
  Агент выполнил действие → Event(agent_action_completed, {agent, action})

Event пишется параллельно с основным действием (не блокирует).
На этапе роста можно вынести в ClickHouse/TimescaleDB.

[Дэшборды — этап 3]
├── Воронка: лендинг → заявка → оплата → онбординг → прохождение → сертификат
├── Конверсии по сегментам (B2B vs B2C, тарифы, источники)
├── Retention: сколько выпускников покупают другие продукты
├── LTV по сегментам
└── Операционные метрики: время на процессы, нагрузка на кураторов
```

## 3.13 Версионирование контента (Source of Knowledge)

> Подробная концепция: [docs/11-content-versioning.md](11-content-versioning.md)

### Этап 1: Редактирование урока → LessonRevision [1]

```
[Менеджер редактирует урок]
        │
        ▼
  Создаётся новая LessonRevision
  (revision_number = prev + 1,
   change_summary = "описание изменений")
        │
        ▼
  Lesson.current_revision_id → новая ревизия
        │
        ├──→ Event: lesson_content_updated
        │
        └──→ Все CohortContent этого урока:
             is_synced → false (этап 2)
```

### Этап 2: Fork контента при создании потока [2]

```
[Менеджер создаёт Cohort]
        │
        ▼
  [Job] fork_cohort_content (DB.34):
  Для каждого активного Lesson продукта:
        │
        └──→ CohortContent(
               cohort_id, lesson_id,
               pinned_revision_id = Lesson.current_revision_id,
               is_synced = true
             )
```

### Этап 2: Auto-sync контента [2]

```
[pg-boss cron: "content.auto_sync" — ежедневно]
        │
        ├──→ Cron выбирает CohortContent WHERE is_synced = false
        │
        ├──→ Cron ставит jobs:
        │    queue: content.auto_sync.process
        │    result: enqueued_count = N
        │
        └──→ Worker для каждого CohortContent:
             │
             ├── Поток eligible?
             │   (active + enrollment с valid support_expires_at
             │    + auto_sync не заблокирован)
             │
             ├── Да → sync: pinned → current, is_synced → true
             │         Event: cohort_content_synced
             │
             └── Нет → остаётся is_synced = false
                  (ждёт ручного sync от менеджера)

Важно:
  - Cron завершает работу после постановки jobs.
  - Реальное обновление контента происходит в worker jobs.

[Менеджер — ручной sync / откат]
        │
        ├── Sync: pinned → current (для любого потока)
        └── Откат: pinned → предыдущая ревизия
```

### Что видит студент

```
Студент открывает урок
        │
        ├── Есть CohortContent(cohort_id, lesson_id)?
        │   └── Да → показать LessonRevision по pinned_revision_id
        │
        └── Нет (fallback) → показать LessonRevision по Lesson.current_revision_id
```
