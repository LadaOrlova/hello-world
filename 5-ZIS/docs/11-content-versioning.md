# Версионирование контента (Source of Knowledge)

> Часть архитектуры Zamesin IS.
> Основной документ: [PLAN.md](../PLAN.md) | Доменная модель: [01-domain-model.md](01-domain-model.md)
> Data Flows: [03-data-flows.md](03-data-flows.md) | Модули: [04-modules-priorities.md](04-modules-priorities.md)

---

## Проблема

Сейчас `Lesson.content` и `Lesson.video_url` — единственная версия без истории. Все потоки одного продукта видят одни и те же данные. Если менеджер обновляет урок — изменение немедленно видят все, включая завершённые потоки. Нет контроля, нет возможности выборочно обновить контент старого потока, нет истории изменений.

## Концепция: Source of Knowledge (SoK)

SoK — "git для контента":

- **SoK = master** — живая база знаний продукта, постоянно обновляется менеджером
- **Fork** — при старте потока создаётся снимок (snapshot) текущего состояния SoK
- **Sync** — обновление SoK автоматически синхронизируется в активные потоки + лог изменений + возможность отката

Реализация в два этапа:

- **Этап 1**: LessonRevision — история контента (версии уроков)
- **Этап 2**: CohortContent — fork контента для потоков + auto-sync

---

## Новые сущности

### LessonRevision (этап 1)

Хранит контент урока. Каждое редактирование создаёт новую ревизию. Lesson.current_revision_id указывает на актуальную версию (SoK).

```
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
```

### CohortContent (этап 2)

Снимок контента потока — "fork" SoK. Определяет, какую ревизию урока видят студенты конкретного потока.

```
CohortContent (Снимок контента потока — fork SoK) [2]
├── id, cohort_id (FK → Cohort), lesson_id (FK → Lesson)
├── pinned_revision_id (FK → LessonRevision)
├── is_synced (boolean — совпадает ли с Lesson.current_revision_id)
├── synced_at
└── UNIQUE(cohort_id, lesson_id)
```

### Изменения в Lesson (этап 1)

Поля `content`, `video_url`, `duration_minutes` переезжают в LessonRevision. В Lesson остаются метаданные + указатель на текущую ревизию.

```
Lesson (метаданные урока) [1]
├── id, module_id, title
├── type: text | video | text_video
├── position, is_new, available_for_tiers[], is_active
├── deadline_at
└── current_revision_id (FK → LessonRevision) — указатель на SoK
    (content, video_url, duration_minutes — теперь в LessonRevision)
```

---

## Логика работы

### Этап 1: LessonRevision (история контента)

```
[Менеджер редактирует урок]
        │
        ▼
  Создаётся новая LessonRevision
  (revision_number = prev + 1,
   change_summary = "что изменилось")
        │
        ▼
  Lesson.current_revision_id → новая ревизия
        │
        ▼
  Event: lesson_content_updated
        │
        ▼
  Все студенты видят текущую ревизию
  через Lesson.current_revision_id
  (как сейчас, но с историей)

[Менеджер — история изменений]
  Список ревизий урока:
  ┌──────┬────────────────────────┬──────────────┬───────────┐
  │ Rev# │ Что изменилось         │ Автор        │ Дата      │
  ├──────┼────────────────────────┼──────────────┼───────────┤
  │ 3    │ Обновлён пример в п.2  │ Алёна        │ 15 янв    │
  │ 2    │ Добавлено видео        │ Иван         │ 10 янв    │
  │ 1    │ Создан урок            │ Иван         │ 5 янв     │
  └──────┴────────────────────────┴──────────────┴───────────┘
```

**Атомарная операция** (DB.33 create_lesson_revision):

1. Создать LessonRevision с данными из формы
2. Обновить Lesson.current_revision_id
3. Если есть CohortContent → пометить is_synced = false (этап 2)

### Этап 2: CohortContent (fork + sync)

#### Fork: при создании потока

```
[Менеджер создаёт Cohort]
        │
        ▼
  Cohort.status → planned
        │
        ▼
  [Job] fork_cohort_content:
  Для каждого Lesson продукта (Product → Module → Lesson):
        │
        ├──→ CohortContent(
        │      cohort_id = новый поток,
        │      lesson_id = урок,
        │      pinned_revision_id = Lesson.current_revision_id,
        │      is_synced = true,
        │      synced_at = now
        │    )
        │
        └──→ Event: cohort_content_forked
```

**Атомарная операция** (DB.34 fork_cohort_content):

1. Для каждого активного Lesson продукта
2. Создать CohortContent(pinned = current_revision_id, is_synced = true)

#### Что видит студент

```
Студент (Enrollment в Cohort 12)
        │
        ▼
  Открывает урок → система определяет ревизию:
        │
        ├── Если есть CohortContent для (cohort_id, lesson_id):
        │   └── Показать CohortContent.pinned_revision_id
        │
        └── Если нет CohortContent (fallback):
            └── Показать Lesson.current_revision_id (SoK)
```

#### Auto-sync: обновление контента в потоках

```
[pg-boss cron: "content.auto_sync" — ежедневно]
        │
        ▼
  Найти CohortContent WHERE is_synced = false
        │
        ├── Для каждого → проверить поток:
        │   │
        │   ├── Cohort.status IN (enrolling, active)?
        │   │
        │   ├── Есть хотя бы один Enrollment
        │   │   с status = active
        │   │   и support_expires_at > now()?
        │   │
        │   └── Cohort НЕ заблокирован для auto-sync?
        │       (Cohort.auto_sync_disabled = false, default)
        │
        ├── Если eligible:
        │   ├── CohortContent.pinned_revision_id → Lesson.current_revision_id
        │   ├── CohortContent.is_synced → true
        │   ├── CohortContent.synced_at → now
        │   └── Event: cohort_content_synced
        │
        └── Если не eligible:
            └── Остаётся is_synced = false (ждёт ручного sync или auto-sync disabled)
```

**Атомарная операция** (DB.35 sync_cohort_content):

1. Обновить CohortContent.pinned_revision_id → Lesson.current_revision_id
2. Установить is_synced = true, synced_at = now
3. Записать Event

#### Ручной sync

Менеджер может синхронизировать любой поток вручную — даже с истёкшим support:

```
[Менеджер — дэшборд потока]
  Список несинхронизированных уроков:
  ┌────────────────────┬─────────────────────────┬───────────┐
  │ Урок               │ Что изменилось (SoK)    │ Действие  │
  ├────────────────────┼─────────────────────────┼───────────┤
  │ Урок 3: Интервью   │ Обновлён пример в п.2   │ [Sync]    │
  │ Урок 7: Метрики    │ Добавлено видео          │ [Sync]    │
  │ Урок 12: CustDev   │ Исправлена ошибка        │ [Sync]    │
  └────────────────────┴─────────────────────────┴───────────┘
  [Синхронизировать все]
```

#### Откат

Менеджер может вернуть pinned_revision_id на любую предыдущую ревизию для конкретного урока в конкретном потоке:

```
[Менеджер — урок в потоке]
  Текущая ревизия: Rev 3 (от 15 янв)

  Доступные ревизии:
  ├── Rev 3: Обновлён пример в п.2 (15 янв) ← текущая
  ├── Rev 2: Добавлено видео (10 янв)
  └── Rev 1: Создан урок (5 янв)

  [Откатить на Rev 2]
  → CohortContent.pinned_revision_id → Rev 2
  → CohortContent.is_synced → false
```

---

## Индикаторы в дэшборде менеджера

При is_synced = false менеджер видит:

```
[Дэшборд — Потоки]
┌──────────────┬──────────┬───────────────────────────────┐
│ Поток        │ Статус   │ Контент                       │
├──────────────┼──────────┼───────────────────────────────┤
│ КДП Поток 14 │ active   │ ✅ Синхронизирован             │
│ КДП Поток 13 │ active   │ ⚠️ 3 урока обновлены в SoK    │
│ КДП Поток 12 │ completed│ ⚠️ 5 уроков обновлены в SoK   │
└──────────────┴──────────┴───────────────────────────────┘
```

---

## Правила

1. **Создание урока** → автоматически создаётся первая LessonRevision (revision_number = 1)
2. **Редактирование урока** → новая LessonRevision, обновление current_revision_id, пометка is_synced = false для всех CohortContent этого урока
3. **Создание потока** → fork: CohortContent для каждого активного урока продукта
4. **Auto-sync** работает только для eligible потоков (active + есть active enrollment с valid support)
5. **Менеджер может**: синхронизировать вручную любой поток, откатить на любую ревизию, заблокировать auto-sync для потока
6. **Fallback**: если CohortContent не существует для пары (cohort, lesson) — показывать Lesson.current_revision_id
7. **Удаление ревизий**: ревизии не удаляются (append-only, как git commits)

---

## Связанные документы

- [01-domain-model.md](01-domain-model.md) — схема LessonRevision, CohortContent, изменения в Lesson
- [03-data-flows.md](03-data-flows.md) — секция 3.13: обновление контента, fork, sync
- [05-atomic-operations.md](05-atomic-operations.md) — DB.33, DB.34, DB.35
