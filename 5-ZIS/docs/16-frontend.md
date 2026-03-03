# Frontend Architecture & Practices

> Часть архитектуры Zamesin IS.
> Основной документ: [PLAN.md](../PLAN.md) | Архитектура: [02-architecture.md](02-architecture.md)
> UX-сценарии: [09-example-student-lifecycle.md](09-example-student-lifecycle.md), [10-example-manager-day.md](10-example-manager-day.md), [12-lms-module.md](12-lms-module.md)

Документ фиксирует единые правила разработки фронтенда: структура, принципы компонентной архитектуры, работа с Tailwind CSS 4.1, контракты с backend и критерии качества.

---

## 16.1 Цель

- Сделать фронтенд предсказуемым для команды и AI-агентов.
- Обеспечить безопасное масштабирование UI без хаотичного дублирования.
- Зафиксировать единый путь: `UX scenario -> route -> component -> contract -> tests`.

---

## 16.2 Инварианты фронтенда

- Framework: Next.js App Router.
- UI-стили: Tailwind CSS 4.1 (`tailwindcss` + `@tailwindcss/postcss`).
- Типизация: TypeScript strict.
- Контракты данных: только типизированные boundary (`tRPC DTO`, `better-auth client`), без `any`.
- RBAC на UI не заменяет backend RBAC, а только отражает разрешённые действия.

---

## 16.3 Структура каталогов

Базовый принцип: **сначала route-level co-location, потом выделение в shared**.
Дополнительный инвариант: **1 компонент = 1 директория**.

```
src/
├── app/
│   ├── (route-group)/...          # страницы и route-level UI
│   │   ├── page.tsx               # Server Component по умолчанию
│   │   ├── loading.tsx            # Suspense fallback (App Router convention)
│   │   ├── error.tsx              # Error boundary (App Router convention)
│   │   ├── not-found.tsx          # 404 UI (App Router convention)
│   │   └── _components/           # private folder — route-level компоненты
│   │       └── SignOut/
│   │           ├── index.tsx
│   │           ├── styles.module.css   # опционально
│   │           ├── types.ts            # опционально
│   │           └── index.test.tsx      # опционально
│   ├── auth/
│   │   ├── login/page.tsx
│   │   └── verify/page.tsx
│   ├── api/                       # route handlers
│   ├── _components/               # app-shell/общие layout-компоненты (если нужны)
│   └── globals.css                # @import tailwindcss + @theme (design tokens)
├── shared/
│   ├── ui/                        # переиспользуемые UI primitives
│   │   └── Button/
│   │       ├── index.tsx
│   │       ├── styles.module.css       # опционально
│   │       ├── types.ts                # опционально
│   │       └── index.test.tsx          # опционально
│   ├── trpc-client.ts             # tRPC client + React Query provider (будущее)
│   ├── auth-client.ts             # better-auth client
│   ├── auth-redirect.ts           # чистые UI/domain утилиты
│   └── index.ts
```

Конвенция `_components/`:

- `_components/` — Next.js private folder (не создаёт route segment).
- Это единственный паттерн для route-level компонентов: `src/app/<route>/_components/<ComponentName>/index.tsx`.
- В директории компонента можно хранить всё специфичное для него (стили, словари, локальные типы, тесты).

Правило выделения:

- Если компонент используется в одной странице/секции: хранить рядом с маршрутом в `_components/`.
- Если компонент используется в 2+ независимых фичах: переносить в `src/shared/ui`.
- И в обоих случаях сохранять directory-based формат:
  - `.../_components/SignOut/index.tsx`
  - `src/shared/ui/SignOut/index.tsx`

### Почему directory-based компонент

- Упрощает развитие компонента без переименований файлов.
- Позволяет безопасно добавлять co-located артефакты:
  - `styles.module.css`
  - `types.ts`
  - `index.test.tsx`
- Снижает вероятность конфликтов и хаотичного роста “плоской” структуры файлов.

### Локализация компонентов

- На текущем этапе в проекте **нет** централизованного i18n-механизма (locale negotiation, provider, message loading).
- До появления такого механизма агентам **запрещено** создавать `_messages/*.json`, `lang.ts`, `messages.ts` и прочие псевдо-i18n структуры.
- Пока используем локальные строковые константы внутри `index.tsx`.
- `_messages/<locale>.json` можно вводить только после отдельного архитектурного решения и обновления этого документа.

---

## 16.4 Server/Client граница

- По умолчанию компоненты в App Router — Server Components.
- `\"use client\"` добавляется только если нужны:
  - обработчики событий (`onClick`, `onSubmit`);
  - хуки состояния (`useState`, `useEffect`);
  - browser APIs.
- Нельзя без необходимости “поднимать” весь route в client mode.

Decision rule:

1. Сначала server page/layout.
2. Интерактивные островки выносить в отдельные client-компоненты.

---

## 16.5 Принципы компонентной архитектуры

### Уровни компонентов

1. `Primitives` (shared/ui): кнопка, input, card, badge.
2. `Compositions` (route-level or shared): `AuthForm`, `OrderSummary`.
3. `Page sections` (route-level): блоки конкретного сценария страницы.
4. `Page` (route): только оркестрация секций и загрузки данных.

### Контракт компонента

Каждый компонент должен иметь:

- явные `props` (тип + обязательность);
- прогнозируемые состояния (`loading`, `error`, `empty` при необходимости);
- отсутствие скрытых side-effect на уровне рендера.

---

## 16.6 Tailwind CSS 4.1 policy

### Базовые правила

- Используем utility-first подход по умолчанию.
- `globals.css` содержит:
  - `@import "tailwindcss";`
  - только действительно глобальные стили (body/font/background/theme tokens).
- Не возвращаемся к "таблицам" кастомных классов под каждую страницу.

### Цветовая палитра

- Используем стандартную палитру Tailwind без кастомизации.
- Семантическое назначение цветов (convention, не конфиг):
  - `cyan-700` / `cyan-800` — primary actions (кнопки, ссылки);
  - `slate-*` — текст, borders, фоны;
  - `emerald-*` — success-состояния;
  - `rose-*` — error-состояния;
  - `amber-*` — warning-состояния.
- Кастомные design tokens добавляются при необходимости через `@theme` в `globals.css`.

### Когда выделять переиспользуемый UI-компонент

Выделять в `src/shared/ui`, если одновременно:

1. Повторяется одинаковая структура + классы в 2+ местах.
2. Повторяется одинаковое поведение (variant/size/loading/disabled).
3. Есть риск рассинхронизации дизайна.

### Variants

- Варианты (`primary`, `secondary`, `danger`) фиксируются через typed props.
- Нельзя размазывать variant-логику через условные строки по страницам.

---

## 16.7 Работа с данными и контрактами

- Данные для UI приходят только через typed контракты:
  - tRPC outputs;
  - `authClient`/better-auth responses.
- На границе UI валидируем только пользовательский input (формы).
- Не использовать raw Prisma-модели и server-only типы во frontend-слое.

### 16.7.1 tRPC на фронтенде

tRPC-клиент подключается через `@trpc/tanstack-react-query` (уже в зависимостях).

Паттерны вызова:

1. **Client Components** — через React Query hooks:

   ```tsx
   const { data, isLoading, error } = trpc.health.check.useQuery();
   const mutation = trpc.someModule.create.useMutation();
   ```

2. **Server Components** — через server-side caller (без React Query):
   ```tsx
   // в page.tsx (Server Component)
   const result = await trpcCaller.health.check();
   ```

Правила:

- Provider (`TRPCProvider`) оборачивает app в `layout.tsx` — добавляется при реализации первого tRPC-вызова из UI.
- Файл `src/shared/trpc-client.ts` — единственная точка создания tRPC client.
- Не вызывать tRPC напрямую через `fetch` — только через типизированный client.

### 16.7.2 State management

- **Серверное состояние**: TanStack Query (через tRPC hooks) — единственный механизм. Без Redux, Zustand и аналогов.
- **UI-состояние**: `useState` / `useReducer` для локальных интерактивных компонентов.
- **URL-состояние**: `searchParams` для фильтров, пагинации, табов — всё, что должно быть shareable/bookmarkable.
- **React Context**: допустим только для сквозных UI-concerns (тема, sidebar state). Не для данных с сервера.

### 16.7.3 Cursor Pagination Pattern (Admin Lists)

Базовый шаблон для админ-списков:

- API использует общий DTO-контракт: `pagination?: { cursor?: string; limit?: number }` -> `pagination: { hasMore, nextCursor }`.
- Фильтры страницы хранятся в URL (`searchParams`) и считаются source of truth.
- При изменении filter key пагинация сбрасывается к первой странице.
- UX по умолчанию: кнопка `Load more` (без infinite scroll и без numbered pages).

Размещение переиспользуемых сущностей:

- `src/shared/hooks/use-cursor-pagination.ts` — общий hook для cursor-пагинации.
- `src/shared/ui/PaginationControls/index.tsx` — общий компонент контролов пагинации.

Pilot-реализация:

- `src/app/admin/events/events-admin-client.tsx`.

---

## 16.8 Формы и UX-состояния

### Формы

Для каждой формы обязательны:

- `idle` состояние;
- `submitting` состояние (блокировка submit + явный текст);
- `success` и `error` сообщения;
- корректная обработка сетевых ошибок.

Подход к реализации форм:

- **Простые формы** (1-3 поля, линейный флоу): `useState` — как в auth/, auth/verify.
- **Сложные формы** (много полей, вложенная валидация): допустимо добавить `react-hook-form` при появлении реальной потребности. Не добавлять заранее.
- Валидация input — на клиенте (UX), но backend всегда перевалидирует через DTO.

### Page-level состояния (App Router conventions)

Для страниц с загрузкой данных используются встроенные App Router file conventions:

- `loading.tsx` — Suspense fallback на уровне route (скелетон/спиннер);
- `error.tsx` — Error boundary на уровне route (`"use client"`, получает `error` + `reset`);
- `not-found.tsx` — 404 UI на уровне route.

Для компонентного уровня — состояния передаются через props/state (`isLoading`, `error`, `isEmpty`).

Также обязательны:

- `empty` состояние (нет данных);
- `forbidden`/`unauthorized` UX согласно RBAC-потоку.

---

## 16.9 RBAC на фронтенде

- UI проверяет role только для отображения/навигации.
- Backend middleware (`isAuthenticated`, `requireRole`, `requireCompanyAccess`) остаётся единственным источником авторизации.
- Любая критичная операция должна считаться потенциально “forbidden” даже если UI её не показал.

---

## 16.10 Naming conventions

- Компоненты: `PascalCase` (`AuthCard.tsx`, `RoleBadge.tsx`).
- Директории компонентов: `PascalCase` (`SignOut`, `AuthCard`, `RoleBadge`).
- Хуки: `useXxx`.
- Пропсы: `type XxxProps = { ... }`.
- Утилиты: `camelCase`.
- Файлы route-level компонентов:
  - `src/app/<route>/_components/<ComponentName>/index.tsx` (если компонент не shared).

---

## 16.11 Эволюционный процесс (как масштабируем)

1. Реализуем фичу минимально в route-level.
2. После появления повторов выделяем primitives в `src/shared/ui`.
3. После стабилизации UX добавляем тесты и docs-пример.
4. Обновляем `docs/16-frontend.md` при изменении подхода.

Это защищает от premature abstraction и от хаотичного копипаста.

---

## 16.12 Тестирование фронтенда

Минимум для новых UI-флоу:

- typecheck + lint обязательно;
- smoke e2e/интеграция на критичный путь (по мере появления Playwright-сценариев);
- для сложной UI-логики — unit тесты utility/mapper функций.

Playwright добавляется в devDependencies при появлении первого E2E-сценария (не заранее).

Ссылка: [13-testing.md](13-testing.md).

---

## 16.13 Анти-паттерны

- Большие page-файлы с mixed business/UI/network логикой.
- Нестрогие пропсы (`any`, `unknown as ...`) без boundary-обоснования.
- Дублирование одинаковых Tailwind-строк в 3+ местах без выделения компонента.
- "Скрытые" RBAC-правила только во frontend без backend-проверки.
- Массовые глобальные стили, которые ломают локальную изоляцию компонентов.
- Использование Redux/Zustand/MobX при наличии TanStack Query через tRPC.
- Прямые `fetch()` вызовы к tRPC endpoint вместо типизированного client.
- Добавление `react-hook-form` / Playwright / других библиотек "на будущее" до реальной потребности.

---

## 16.14 Checklist для PR (frontend)

- [ ] Компоненты размещены по правилам (`route-level _components/` vs `shared/ui`)
- [ ] `"use client"` только там, где нужен
- [ ] Есть состояния `loading/error/empty` (если релевантно)
- [ ] Page-level: `loading.tsx` / `error.tsx` добавлены при необходимости
- [ ] Данные получены через tRPC hooks или server caller (не raw fetch)
- [ ] Контракты backend/frontend типобезопасны
- [ ] RBAC-видимость в UI не конфликтует с backend
- [ ] `npm run typecheck`
- [ ] `npm run lint`
- [ ] `npm run format:check`
- [ ] Обновлена документация при изменении паттерна
