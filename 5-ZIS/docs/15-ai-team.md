# AI-команда разработки: Workflow v1 (superpowers + Backlog.md)

> Этот документ описывает design-time workflow AI-разработки.
> Runtime-агенты системы описаны в [08-mcp-cli-agents.md](08-mcp-cli-agents.md).

## 15.1 Цель

Собрать единый, понятный и современный процесс, который:

- прост для онбординга новых разработчиков;
- сохраняет архитектурную целостность из `PLAN.md`;
- использует `superpowers` как execution methodology;
- использует `Backlog.md` как source of truth по задачам.

## 15.2 Source of truth

1. `PLAN.md` — архитектурные инварианты и границы.
2. `ROADMAP.md` — контекст фаз и направлений.
3. `backlog/tasks/*`, `backlog/drafts/*` — единственный исполняемый source of truth.

Правило: если есть конфликт между roadmap-контекстом и backlog-задачей, приоритет у backlog-задачи.

## 15.3 Инструменты

- `superpowers` — процесс выполнения (brainstorm, plan, execute, review, finish).
- `Backlog.md` (MCP/CLI) — фиксация задач, статусов, AC/DoD, final summary.
- `Context7` — актуальная документация библиотек.
- `postgres_zis` (MCP, read-only) — оперативная диагностика данных и аномалий в локальной БД.
- Git + PR + CI — обязательные quality gates.

### 15.3.1 Дисциплина схем БД

- Доменная схема приложения: `public` (источник модели — `prisma/schema.prisma`).
- Очереди и служебные таблицы pg-boss: отдельная схема `pgboss`.
- Правило: не смешивать доменные данные и queue-данные между схемами.

## 15.4 Единый pipeline

### Фаза A: Plan Mode (интерактивная, обязательная)

Цель: за один проход пройти intake + brainstorm + выбор подхода + постановку задачи.

Human in the loop: обязательно.

Результат фазы:

- создан/обновлён `Draft` или `Task`;
- зафиксированы `Scope`, `Acceptance Criteria`, `Definition of Done`, `Plan`, `Test Strategy`, `Risks`;
- получено явное подтверждение пользователя на старт реализации.

### Фаза B: Delivery Mode

Цель: реализация строго в рамках утверждённого scope.

Правила:

- без scope drift;
- изменения в scope только через обновление задачи в Backlog;
- реализация маленькими шагами с тестами по уровню риска.

Внутри Delivery обязательны validation/review-гейты перед передачей в UAT:

- `npm run typecheck`
- `npm run lint`
- релевантные тесты (unit/integration/e2e)
- code review по дефектам/регрессиям
- security review (если затронуты auth/RBAC/validation/integrations)

### Фаза C: UAT Gate (ручная проверка пользователем)

Система передаёт функционал на ручную проверку.

Пользователь выбирает один из статусов:

- `approve`
- `approve_with_followups`
- `reject`

Правило:

- `approve` или `approve_with_followups` -> финализация;
- `reject` -> возврат в `In Progress` с фиксацией замечаний в задаче.

### Фаза D: Finalization

- заполнить `final summary` в задаче;
- обновить `CHANGELOG.md` для code/runtime (если был код);
- обновить `docs/CHANGELOG.md` для docs/process/architecture;
- перевести задачу в `Done`.

## 15.5 Task Cookie Cutter (Plan Mode)

Ниже каноничный интерактивный шаблон, который агент проходит с пользователем.

### Блок 1: Цель и ценность

- Какую проблему решаем?
- Для какой роли/сегмента?
- Что считается успехом?

### Блок 2: Scope

- In scope (что делаем в этой задаче)?
- Out of scope (что явно не делаем)?
- Что откладываем на follow-up?

### Блок 3: Ограничения и инварианты

- Архитектурные ограничения из `PLAN.md`.
- Ограничения по сроку/риску/совместимости.
- Нельзя добавлять новые инфраструктурные компоненты без отдельного решения.

### Блок 4: Варианты решения

- Вариант 1: кратко + trade-offs.
- Вариант 2: кратко + trade-offs.
- Рекомендованный вариант и почему.
- Явный выбор пользователя.

### Блок 5: Контракты и данные

- Какие API/DTO/сущности затрагиваются?
- Какие события/джобы/права доступа меняются?
- Нужны ли миграции или data backfill?

### Блок 6: Acceptance Criteria

- AC-1: функциональный результат.
- AC-2: граничные сценарии/ошибки.
- AC-3: права доступа/безопасность (если применимо).
- AC-4: наблюдаемость/логирование (если применимо).

### Блок 7: Definition of Done

- Реализация завершена в рамках scope.
- Пройдены typecheck/lint/релевантные тесты.
- Проведены review-гейты.
- Пройден UAT gate.
- Заполнен final summary и обновлён changelog.

### Блок 8: План реализации

- Шаг 1: подготовка контрактов.
- Шаг 2: backend.
- Шаг 3: frontend/integration.
- Шаг 4: тесты и проверки.
- Шаг 5: UAT и финализация.

### Блок 9: Риски

- Технические риски.
- Продуктовые риски.
- План отката/смягчения.

### Выход Plan Mode (обязателен)

Перед стартом реализации задача в Backlog должна содержать:

- `Description`
- `Scope (In/Out)`
- `Acceptance Criteria`
- `Definition of Done`
- `Implementation Plan`
- `Test Strategy`
- `Risks`
- `References/Documentation`

И после этого должно быть явное подтверждение пользователя: `план согласован, можно реализовывать`.

## 15.6 Роли в delivery

- Architect: держит границы и архитектурную корректность.
- Backend: реализует API/service/worker-часть.
- Frontend: реализует UI и интеграцию с контрактами.
- QA: проверяет AC/регрессии.
- Security: проверяет auth/RBAC/validation/integrations.
- Code Review: финальная проверка дефектов и рисков.

Один человек может совмещать роли, но quality gates остаются обязательными.

## 15.7 Анти-паттерны

- Старт реализации без завершённого Plan Mode.
- Закрытие задачи без UAT подтверждения.
- Расширение scope без обновления задачи в Backlog.
- Выполнение только “по памяти” без фиксации AC/DoD.
- Merge/Done без финальных проверок и summary.

## 15.8 Короткие триггеры работы

- `Спланируем задачу ...` -> запуск Plan Mode по cookie cutter.
- `Берём ZIS-XXX в работу` -> Delivery Mode.
- `Готово к UAT` -> ручная проверка пользователя.
- `Подтверждаю UAT, финализируй` -> Finalization и `Done`.

## 15.9 Ссылки

- [PLAN.md](../PLAN.md)
- [ROADMAP.md](../ROADMAP.md)
- [13-testing.md](13-testing.md)
- [14-nfr.md](14-nfr.md)
- [16-frontend.md](16-frontend.md)
- [17-reliable-events.md](17-reliable-events.md)
