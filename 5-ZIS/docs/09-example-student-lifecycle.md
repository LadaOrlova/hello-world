# Пример: полный жизненный цикл студента

> Часть архитектуры Zamesin IS.
> Основной документ: [PLAN.md](../PLAN.md) | Доменная модель: [01-domain-model.md](01-domain-model.md)
> Data Flows: [03-data-flows.md](03-data-flows.md) | Архитектура: [02-architecture.md](02-architecture.md)

Выдуманный, но реалистичный пример прохождения студентом всего пути — от первого визита на сайт до завершения курса. Для каждого этапа указаны действия системы и их статус, как менеджер увидит это в бэк-офисе.

---

### Студент: Мария Петрова, курс "Как делать продукт", Поток 14

---

#### Этап 1: Заявка (День 0)

```
10:32  Мария заходит на zamesin.ru/producthowto, заполняет TypeForm
       |
       v
       Система: получен webhook от TypeForm
       +-- WebhookLog: сохранён сырой payload
       +-- Создан Lead #847
       |   +-- name: "Мария Петрова"
       |   +-- email: "maria.petrova@gmail.com"
       |   +-- phone: "+7 916 123-45-67"
       |   +-- telegram_username: "@mpetrova"
       |   +-- source: typeform
       |   +-- product_interest: "Как делать продукт"
       |   +-- status: new
       |
       +-- Дедупликация: dedup_key (email) проверен -- новый лид (дублей нет)
       |
       +-- Автоназначение: менеджер Ольга (round-robin)
       |   +-- Lead.assigned_manager_id -- User #12 (Ольга)
       |
       +-- Event: { type: "lead_created", payload: { lead_id: 847, source: "typeform" } }
```

**В бэк-офисе (дэшборд менеджера Ольги):**

```
+-----------------------------------------------------+
| Новый лид: Мария Петрова                             |
| Источник: TypeForm | Курс: Как делать продукт       |
| Email: maria.petrova@gmail.com | TG: @mpetrova      |
| Статус: Новый | Назначен: Ольга                      |
+-----------------------------------------------------+
```

---

#### Этап 2: Квалификация и продажа (Дни 1-3)

```
День 1, 11:00  Ольга связывается с Марией через Telegram
               Lead.status: new -- contacted
               Event: { type: "lead_status_changed", payload: { lead_id: 847, status: "contacted" } }

День 2, 14:30  Мария выбирает тариф "Продвинутый" (25 000 руб.)
               Lead.status: contacted -- qualified

День 3, 10:15  Мария готова оплатить
               |
               v
               tRPC: billing.createOrder
               +-- Проверка: Cohort #14 enrolled_count (47) < max_students (60) -- OK
               |
               +-- Создан Order #780
               |   +-- user_id: -- создан User #892 (из данных Lead)
               |   +-- cohort_id: 14 ("Поток 14")
               |   +-- tier_id: 3 ("Продвинутый")
               |   +-- amount: 25000, currency: RUB
               |   +-- status: pending
               |
               +-- Создан Enrollment #1203
               |   +-- order_id: 780
               |   +-- user_id: 892
               |   +-- cohort_id: 14
               |   +-- tier_id: 3 ("Продвинутый")
               |   +-- price_snapshot: 25000
               |   +-- status: pending (место зарезервировано)
               |
               +-- Создан Payment #3456
               |   +-- order_id: 780
               |   +-- amount: 25000, currency: RUB
               |   +-- provider: yookassa
               |   +-- idempotency_key: "pay_uuid_abc123"
               |   +-- status: pending
               |
               +-- ЮKassa API: создана ссылка на оплату
               |   +-- Редирект -- Мария оплачивает
               |
               +-- Lead.status: qualified -- converted
               |   Lead.converted_to_user_id -- User #892
               |
               +-- Event: { type: "order_created", payload: { order_id: 780 } }
```

```
День 3, 10:18  Webhook от ЮKassa: платёж подтверждён
               |
               v
               Система: обработка webhook
               +-- WebhookLog: сохранён сырой payload
               +-- Payment #3456: provider_payment_id = "yk_29f8a..." (UNIQUE check -- OK, не дубль)
               +-- Payment.status: pending -- success
               +-- Order.status: pending -- paid
               +-- Enrollment.status: pending -- active
               |
               +-- Event: { type: "payment_success", payload: { order_id: 780, amount: 25000 } }
               +-- Триггер: сервис в транзакции -- запуск Process #501 (type: "onboarding")
```

**В бэк-офисе:**

```
+-----------------------------------------------------+
| Оплата подтверждена                                  |
| Студент: Мария Петрова | Сумма: 25 000 руб.         |
| Заказ: #780 | Курс: КДП | Поток 14 | Продвинутый   |
| Способ: ЮKassa | ID: yk_29f8a...                     |
|                                                      |
| Онбординг запущен (Process #501)                     |
+-----------------------------------------------------+
```

---

#### Этап 3: Онбординг (День 3, автоматически)

```
Process #501: Онбординг студента Мария Петрова
===================================================

10:18:01  Job 1: grant_lms_access
          +-- Создание Progress записей для всех уроков Потока 14 (на момент зачисления)
          |   При добавлении новых уроков позже — Progress создаётся для всех active Enrollments
          |   (см. docs/10-example-manager-day.md, docs/06-edge-cases.md §6.25)
          |   +-- Module "Введение" (4 урока) -- 4 Progress (status: not_started)
          |   +-- Module "Юнит-экономика" (3 урока) -- 3 Progress
          |   +-- Module "Исследования" (5 уроков) -- 5 Progress
          |   +-- ... всего 24 Progress записи
          +-- Enrollment.lms_access_granted = true
          +-- OK completed (1.4s)

10:18:01  Job 2: create_onboarding_page (параллельно с Job 1)
          +-- Определение чатов: Tier #3 (Продвинутый).telegram_chats[] ∩ поток 14:
          |   (cohort_id IS NULL или cohort_id = 14)
          |   +-- TelegramChat #10: "КДП Поток 14" (cohort_id=14, основной чат)
          |   +-- TelegramChat #11: "КДП Записи" (cohort_id=null, канал)
          |   +-- TelegramChat #12: "КДП Воркшопы" (cohort_id=null, чат для продвинутых)
          |
          +-- Создание ChatMembership для каждого чата:
          |   +-- ChatMembership { user: 892, chat: 10, should_be_member: true, status: pending }
          |   +-- ChatMembership { user: 892, chat: 11, should_be_member: true, status: pending }
          |   +-- ChatMembership { user: 892, chat: 12, should_be_member: true, status: pending }
          |
          +-- Генерация уникальной ссылки: /onboarding/abc123xyz
          +-- Email + TG: отправлена ссылка на онбординг-страницу
          +-- OK completed (0.8s)

          Онбординг-страница (веб) — Мария открывает ссылку:
          +-----------------------------------------------+
          | Добро пожаловать на курс "Как делать продукт"! |
          |                                                |
          | Вступите в чаты курса:                         |
          |                                                |
          | [ ] Чат "КДП Поток 14"         [Вступить]     |
          | [ ] Канал "КДП Записи"         [Вступить]     |
          | [ ] Чат "КДП Воркшопы"         [Вступить]     |
          |                                                |
          | (бот отслеживает вступления в реальном времени)|
          +-----------------------------------------------+

10:18:01  Job 3: subscribe_calendar (параллельно)
          +-- Google Calendar API: отправлена ссылка на подписку
          +-- Enrollment.calendar_subscribed = true
          +-- OK completed (0.9s)

10:18:01  Job 4: assign_curator (параллельно)
          +-- Свободные кураторы в Потоке 14:
          |   - Алексей (5/6 студентов)
          |   - Дарья (4/6 студентов) <-- наименее загружена
          +-- Мария -- CuratorGroup куратора Дарья
          +-- OK completed (0.1s)

10:18:03  Job 5: send_welcome_msg (chain: после Jobs 1-4)
          +-- Все предыдущие шаги completed
          +-- Email: приветственное письмо с инструкциями
          +-- TG: "Добро пожаловать на курс! Пройдите онбординг: /onboarding/abc123xyz"
          +-- OK completed (0.5s)

10:18:04  Process #501: OK completed
          Общее время: 3.0s | Retries: 0
```

```
10:25  Мария открывает онбординг-страницу, нажимает "Вступить" для каждого чата

10:26  Мария вступила в чат "КДП Поток 14"
       +-- Бот (grammY): получен chat_member event
       +-- TelegramAccount привязан: User #892 <-> telegram_user_id: 5839271
       +-- ChatMembership { chat: 10 }: status: pending -- joined
       +-- Онбординг-страница обновляется: [v] КДП Поток 14

10:27  Мария вступила в канал "КДП Записи"
       +-- ChatMembership { chat: 11 }: status: pending -- joined
       +-- Онбординг-страница: [v] КДП Записи

10:27  Мария вступила в чат "КДП Воркшопы"
       +-- ChatMembership { chat: 12 }: status: pending -- joined
       +-- Онбординг-страница: [v] КДП Воркшопы

       Все чаты -- [v] -- кнопка "Перейти к LMS" стала активной
       Мария нажимает "Перейти к LMS" -- открывается LMS-интерфейс
```

**В бэк-офисе (карточка студента):**

```
+-----------------------------------------------------+
| Мария Петрова | Поток 14 | Продвинутый               |
|                                                      |
| Онбординг:                    Статус                 |
| +-- Доступ к LMS              [v] Выдан              |
| +-- Чат "КДП Поток 14"       [v] Вступила           |
| +-- Канал "КДП Записи"       [v] Вступила           |
| +-- Чат "КДП Воркшопы"       [v] Вступила           |
| +-- Календарь                 [v] Подписана          |
| +-- Куратор                   [v] Дарья              |
| +-- Приветствие               [v] Отправлено         |
|                                                      |
| Все шаги онбординга выполнены [v]                    |
+-----------------------------------------------------+
```

---

#### Этап 4: Обучение (Недели 1-6)

##### Неделя 1: LMS и первое занятие

```
Пн, 10:00    Мария открывает LMS
             |
             v
             LMS отображает модули курса:
             +-----------------------------------------------+
             | Как делать продукт -- Поток 14                 |
             |                                                |
             | Модуль 1: Введение (4 урока)        0/4       |
             | +-- Урок 1: Что такое продукт       [ ]       |
             | +-- Урок 2: Роль продакт-менеджера  [ ]       |
             | +-- Урок 3: Продуктовый подход      [ ]       |
             | +-- Урок 4: Фреймворки              [ ]       |
             |                                                |
             | Модуль 2: Юнит-экономика (3 урока)  0/3       |
             | ...                                            |
             +-----------------------------------------------+

Пн, 10:05    Мария открывает Урок 1: "Что такое продукт"
             +-- Lesson #201 (type: text_video)
             |   +-- content: markdown-текст с теорией
             |   +-- video_url: Kinescope embed (запись лекции)
             +-- Progress: status: not_started -- in_progress
             +-- Event: { type: "lesson_opened", payload: { lesson_id: 201, enrollment_id: 1203 } }

Пн, 10:45    Мария дочитала и посмотрела видео, нажимает "Изучено"
             +-- Progress: status: in_progress -- completed
             +-- Progress.completed_at = 2026-02-24T10:45:00Z
             +-- Event: { type: "lesson_completed", payload: { lesson_id: 201, enrollment_id: 1203 } }
```

```
Пн, 19:00    Schedule #78: Воркшоп "Введение в продуктовый подход"
             |
             +-- Schedule создан менеджером заранее:
             |   +-- Process "schedule_setup":
             |   |   +-- Job: create_zoom_meeting -- OK (Zoom ID: 847293...)
             |   |   +-- Job: create_breakout_rooms -- OK (5 комнат для кураторов)
             |   |   +-- Job: create_calendar_event -- OK
             |   |   +-- Job: notify_students_tg -- OK (48 уведомлений)
             |   +-- Process: OK completed
             |
             +-- [19:00-21:00] Воркшоп проведён
             |
             +-- Attendance (по данным Zoom API):
             |   +-- Мария Петрова: present (joined 18:57, left 21:02)
             |   +-- ...47 других студентов...
             |   +-- Иван Сидоров: absent
             |
             +-- Запись загружена в Kinescope
                 +-- Lesson #78 (LMS): video_url обновлён (запись воркшопа)
                 +-- TG: "Запись занятия 'Введение...' доступна"
```

##### Неделя 2: Домашнее задание

```
Вт           Мария видит ДЗ к уроку 4 "Фреймворки":
             |
             v
             Homework #15
             +-- lesson_id: 204 (Урок 4: Фреймворки)
             +-- title: "Выберите фреймворк для своего продукта"
             +-- description: "Опишите, какой фреймворк подходит..."
             +-- deadline_days: 7 (от момента зачисления)

Ср           Мария сдаёт ДЗ:
             +-- HomeworkSubmission #340
             |   +-- homework_id: 15
             |   +-- enrollment_id: 1203
             |   +-- answer: { text: "Я выбрала Jobs-to-be-Done..." }
             |   +-- status: submitted
             |   +-- submitted_at: 2026-02-26T14:30:00Z
             +-- Event: { type: "homework_submitted", payload: { submission_id: 340 } }

Чт           Куратор Дарья проверяет ДЗ Марии:
             +-- HomeworkSubmission #340: status: submitted -- accepted
             +-- HomeworkSubmission.feedback: "Отличный выбор фреймворка!..."
             +-- HomeworkSubmission.reviewed_by: User #45 (Дарья)
             +-- Event: { type: "homework_reviewed", payload: { submission_id: 340, result: "accepted" } }
             |
             +-- [Job] TG-уведомление Марии:
                 "Ваше ДЗ 'Выберите фреймворк' проверено: Принято!
                  Комментарий куратора: 'Отличный выбор фреймворка!...'"
```

**В бэк-офисе (дэшборд куратора Дарьи):**

```
+-----------------------------------------------------+
| Мои студенты | Поток 14 | Группа Дарьи (5 студентов) |
|                                                      |
| Прогресс по урокам:                                  |
|           | У1 | У2 | У3 | У4 | У5 | У6 | ...       |
| Петрова М.| ++ | ++ | ++ | ++ | .. | -- | ...       |
| Козлов А. | ++ | ++ | .. | -- | -- | -- | ...       |
| Волкова Е.| ++ | ++ | ++ | ++ | ++ | .. | ...       |
| ...                                                  |
|                                                      |
| ++  completed   ..  in_progress   --  not_started    |
|                                                      |
| ДЗ на проверку: 2 (Козлов А., Волкова Е.)           |
+-----------------------------------------------------+
```

##### Недели 3-5: Основное обучение

```
Неделя 3          Мария посещает 5 из 6 воркшопов (пропустила один по болезни)
                  Attendance: 83.3% посещаемость
                  LMS Progress: 18/24 уроков пройдено (75%)

Неделя 4          FeedbackCampaign #45 (trigger: after_lesson, Занятие 3)
                  |
                  +-- 48 запросов отправлено (TG + email)
                  |
                  +-- Мария ответила через TG-бот:
                  |   +-- NPS: 9
                  |   +-- Комментарий: "Очень полезно, хочу больше примеров"
                  |
                  +-- [+24ч] 12 студентов не ответили -- напоминание
                  |
                  +-- Итого: 44/48 ответили (91.7%)
                      +-- Средний NPS: 8.6
                      +-- AI-summary: "Основные темы: хотят больше практических
                          примеров (18 упоминаний), темп комфортный (12),
                          куратор Дарья -- отличные отзывы (8)"

Неделя 5          Мария завершает все 24 урока и 6 ДЗ
                  LMS Progress: 24/24 (100%)
                  Homework: 6/6 accepted
```

**В бэк-офисе (дэшборд обратной связи):**

```
+-----------------------------------------------------+
| Обратная связь: Поток 14, Занятие 3                  |
|                                                      |
| Ответили: 44/48 (91.7%)  |  NPS: 8.6                |
|                                                      |
| AI-инсайты:                                          |
| - Запрос на больше практических примеров (18 упом.)  |
| - Комфортный темп (12 упом.)                         |
| - Положительные отзывы о кураторе Дарье (8 упом.)   |
|                                                      |
| Не ответили: Сидоров И., Козлова А., Михайлов П.,   |
|              Новикова Е.                              |
+-----------------------------------------------------+
```

---

#### Этап 5: Завершение курса (Неделя 6)

```
Неделя 6, Пт     Последний воркшоп проведён
                  |
                  +-- Финальная FeedbackCampaign #52 (trigger: end_course)
                  |   +-- Мария: NPS 10, "Курс изменил мой подход к продукту"
                  |   +-- Итого: 46/48 (95.8%), NPS: 9.1
                  |
                  +-- Менеджер Ольга нажимает "Завершить поток"
                      |
                      v
                      tRPC: cohort.complete({ cohort_id: 14 })
                      |
                      +-- Проверка: все Enrollments resolved? -- OK
                      |   (46 active -- completed, 2 refunded ранее)
                      |
                      +-- Process #612 (type: "offboarding")
                          запущен для 46 студентов
```

```
Process #612: Offboarding Потока 14

Для Мария Петрова (Enrollment #1203):
=====================================

  Job 1: check_completion_criteria
         +-- Уроки пройдены: 24/24 (100%)
         +-- ДЗ сданы: 6/6, все accepted
         +-- Посещаемость: 83.3% (выше минимума 70%)
         +-- Статус: допущена к сертификату
         +-- OK completed

  Job 2: generate_certificate
         +-- Certificate #cert_uuid_789xyz
         +-- Шаблон: "Как делать продукт - Продвинутый"
         +-- PDF сгенерирован
         +-- QR-код -- https://zamesin.ru/verify/cert_uuid_789xyz
         +-- Enrollment.certificate_id = cert_uuid_789xyz
         +-- OK completed (2.1s)

  Job 3: send_certificate
         +-- Email: PDF-сертификат отправлен
         +-- TG: "Поздравляем! Ваш сертификат готов"
         +-- OK completed (0.8s)

  Job 4: setup_makers_subscription
         +-- Проверка: активная подписка Makers? -- Нет
         +-- TG-сообщение: "Хотите вступить в сообщество Makers?
         |   Первый месяц бесплатно, далее 990 руб./мес"
         +-- [Мария нажала "Да, хочу"]
         +-- Subscription #234 создана
         |   +-- plan: maker
         |   +-- source: post_course
         |   +-- source_order_id: 780
         |   +-- next_payment_date: 2026-04-20
         +-- OK completed

  Job 5: add_to_alumni_chats
         +-- ChatMembership создана для чата "Замесим Product Club"
         |   +-- should_be_member: true, status: pending
         +-- TG: инвайт отправлен
         +-- Мария вступила -- ChatMembership.status: joined
         +-- OK completed

  Job 6: update_enrollment_status
         +-- Enrollment.status: active -- completed
         +-- Enrollment.completed_at: 2026-03-20T16:00:00Z
         +-- (is_alumni теперь вычисляется: EXISTS(Enrollment WHERE status = 'completed'))
         +-- Event: { type: "enrollment_completed", payload: { enrollment_id: 1203 } }
         +-- OK completed

  Process #612 (для Марии): OK completed
  Общее время: 4.2s | Retries: 0
```

**В бэк-офисе (итоговая карточка студента):**

```
+-------------------------------------------------------------+
| Мария Петрова                          Alumni [v]            |
| Курс: Как делать продукт | Поток 14 | Тариф: Продвинутый   |
|                                                              |
| === ХРОНОЛОГИЯ ===                                           |
|                                                              |
| 20 фев  Заявка (TypeForm)                        [v]        |
| 22 фев  Квалификация (менеджер Ольга)            [v]        |
| 23 фев  Заказ #780: 25 000 руб. (ЮKassa)        [v]        |
| 23 фев  Онбординг (3.0s, 0 retries)             [v]        |
|          +-- LMS [v] TG-чаты (3/3) [v] Календарь [v]       |
|          +-- Куратор: Дарья                                  |
| 24 фев  Начало обучения                          [v]        |
|          +-- Уроки: 24/24 (100%)                             |
|          +-- ДЗ: 6/6 (accepted)                              |
|          +-- Посещаемость: 10/12 (83.3%)                     |
|          +-- NPS после занятия 3: 9                          |
|          +-- NPS финальный: 10                               |
| 20 мар  Завершение курса                          [v]        |
|          +-- Сертификат: cert_uuid_789xyz                    |
|          +-- Подписка Makers: активна                        |
|                                                              |
| === ТЕКУЩИЙ СТАТУС ===                                       |
| Enrollment: Completed [v]                                    |
| Makers: Активна (след. оплата: 20 апр)                      |
| Сертификат: Выдан [v]                                        |
| TG-чаты: Поток 14 (3/3) + Product Club (1/1)               |
+-------------------------------------------------------------+
```
