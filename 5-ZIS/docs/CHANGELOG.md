# Changelog — архитектурные решения

Журнал архитектурных изменений относительно исходного PRD заказчика.
Формат: дата, что изменено, было → стало, обоснование.

---

## 2026-03-03 — ZIS-054: публичные лендинги продуктов + поддержка архивного отображения

### CHG-083: Публичный `/products` и `/products/[slug]` больше не завязаны на наличие открытого набора

- **Было**:
  - каталог и лендинг фактически были ориентированы на products с open enrollment;
  - для части сценариев продукт без активного набора приводил к скрытию/404 вместо информативного archive-state.
- **Стало**:
  - каталог отображает все неудалённые продукты; enrolling-потоки остаются только для purchase-блока;
  - лендинг открывается для любого неудалённого продукта по `slug`, даже без tiers/cohorts;
  - если набор не ведётся (нет доступной связки `tiers/cohorts`), UI явно показывает архивный state:
    `В настоящий момент набор на этот курс не ведётся.`
- **Почему**: требование demo и бизнес-кейса COURSE-01 включает публичную витрину продукта не только в период активного набора, но и как постоянную продуктовую страницу.
- **Затронуто**: `src/server/trpc/routers/products.ts`, `src/app/products/page`-flow, `src/app/products/[slug]/page.tsx`, `src/app/products/[slug]/product-landing-client.tsx`, `src/app/products/products-catalog-client.tsx`.

---

## 2026-02-27 — ZIS-048: операционный recovery прав для MCP read-only пользователя

### CHG-082: Зафиксирован обязательный post-reset шаг восстановления grants для `mcp_readonly`

- **Было**:
  - после `prisma migrate reset` права `mcp_readonly` на `public` могли исчезать;
  - диагностика через MCP `postgres_zis` падала с `permission denied for schema public`.
- **Стало**:
  - в репозитории добавлен стандартный recovery-путь `npm run db:grant-mcp`;
  - grants и default privileges на `public`/`pgboss` теперь восстанавливаются идемпотентно одним скриптом;
  - шаг запуска recovery-скрипта зафиксирован в `README` как часть операционного dev-процесса после reset/migrate.
- **Почему**: гарантировать стабильный read-only доступ MCP к доменной схеме `public` и избежать повторяющихся инцидентов диагностики.
- **Затронуто**: `scripts/db/grant-mcp-readonly.sql`, `scripts/db/grant-mcp-readonly.sh`, `README.md`.

---

## 2026-02-27 — ZIS-047: retry-политика B2C checkout для pending заказа

### CHG-081: Повторный вход в checkout не создаёт блокировку при незавершённой оплате

- **Было**:
  - повторный `checkout.start` при `Order.status in ('pending','paid')` для того же buyer+cohort блокировался;
  - сообщение «Пользователь уже зачислен...» использовалось и для кейса `pending` заказа;
  - для retry-платежей не было явной политики reuse/refresh payment attempt.
- **Стало**:
  - в B2C checkout закреплена retry-модель: один `pending` order на доступ, повторный checkout переиспользует order;
  - при валидном pending attempt возвращается текущая ссылка, при устаревшем attempt создаётся новый payment attempt для того же order;
  - доменная семантика разделена: «уже зачислен» только для enrollment-кейса, «оплаченный заказ уже есть» отдельно;
  - webhook `payment.succeeded` для уже оплаченного order обрабатывается как `noop` (`order_already_paid`) для сохранения инварианта single-success.
- **Почему**: убрать ложные блокировки при возврате пользователя к оплате, не нарушая инварианты `single-payment per access` и `enrollment only after paid`.
- **Затронуто**: `docs/06-edge-cases.md`, `src/server/trpc/routers/billing.ts`, `src/server/services/billing/process-yookassa-webhook.ts`.

---

## 2026-02-27 — ZIS-046: единая финализация paid-invoice и инвариант `1 invoice -> 1 act`

### CHG-080: B2B закрывающие документы упрощены до одного акта на счет

- **Было**:
  - модель допускала несколько `Act` на один `Invoice` (через `enrollmentId`);
  - финализация paid invoice была размазана по двум роутерам с дублирующейся бизнес-логикой.
- **Стало**:
  - введён единый service-level use-case `finalizePaidInvoice`, который используют:
    - `billing.confirmInvoicePaid`
    - `companies.markCompanyRequestPaid`;
  - закреплён инвариант `Act(invoiceId UNIQUE)` — один акт на один счет;
  - акт формируется идемпотентно при финализации оплаты и может быть дособран вручную из `/admin/companies/[companyId]/invoices` (с confirm modal).
- **Почему**: для текущего B2B-контура это более прозрачная и юридически ожидаемая модель закрывающего документа; она уменьшает хаос и исключает дубли.
- **Затронуто**: `docs/01-domain-model.md`, `docs/03-data-flows.md`, `docs/GLOSSARY.md`, `DEMO.md`.

---

## 2026-02-26 — ZIS-044: clean-slate billing architecture (invoice/manual + unified paid-flow)

### CHG-079: Упрощён payment-домен и зафиксирован единый атомарный путь активации после оплаты

- **Было**:
  - B2B invoice batch использовал отдельную join-сущность `InvoiceOrder`;
  - paid-поведение было распределено по нескольким веткам роутеров и webhook-обработке;
  - ручной emergency-path не имел жёсткого требования обязательного комментария.
- **Стало**:
  - `InvoiceOrder` удалён, связь счёта с заказами переведена на `Order.invoiceId`;
  - в `PaymentProvider` добавлены `invoice` и `manual`, введён `Payment.invoiceId` для трассировки invoice-платежей;
  - добавлен единый use-case `applyPaymentSuccess`, и на него переведены все ключевые paid-entrypoints:
    - `billing.confirmInvoicePaid`
    - `billing.confirmOrderPaidManually`
    - `companies.markCompanyRequestPaid`
    - `processYooKassaWebhook` (ветка `payment.succeeded`);
  - для manual override комментарий сделан обязательным полем DTO/UI.
- **Почему**: убрать архитектурную двусмысленность paid-flow, сократить количество связей и зафиксировать единый предсказуемый процесс оплаты -> активации доступа.
- **Затронуто**: prisma/schema.prisma, prisma/migrations/20260226163000_clean_slate_payment_and_company_request/migration.sql, src/server/services/billing/apply-payment-success.ts, src/server/trpc/routers/billing.ts, src/server/trpc/routers/companies.ts, src/server/services/billing/process-yookassa-webhook.ts, src/server/dto/trpc/billing.ts

---

## 2026-02-26 — Guard от двойной оплаты и унификация запуска onboarding

### CHG-078: Зафиксирована политика single-payment per access и общий helper onboarding-start

- **Было**:
  - запуск onboarding выполнялся несколькими локальными блоками в разных paid-flow;
  - invoice-path и card-path могли пересекаться операционно (недостаточно жёсткие guard’ы);
  - guest checkout не имел симметричного антидубль-контроля как admin `createOrder`.
- **Стало**:
  - введён единый helper `startOnboardingIfMissing` для идемпотентного старта onboarding-process;
  - `billing.getPaymentLink` запрещён для invoice/B2B заказов;
  - `billing.confirmInvoicePaid` блокируется при наличии успешного non-manual платежа по order;
  - `billing.checkout.start` блокирует повторный pending/paid заказ для того же email/user и cohort.
  - добавлены DB-level partial unique constraints для инвариантов single-access/single-payment:
    - `Order(userId, cohortId)` при `status in ('pending','paid')`;
    - `Order(lower(guestEmail), cohortId)` при `status in ('pending','paid')`;
    - `Payment(orderId)` при `status='success'`;
    - `Process(entityType, entityId)` при `type='onboarding'`.
- **Почему**: исключить двойную монетизацию одного и того же доступа и снизить риск расхождения поведения paid-flow.
- **Затронуто**: src/server/services/enrollments/start-onboarding.ts, src/server/trpc/routers/billing.ts, src/server/services/billing/process-yookassa-webhook.ts, src/server/trpc/routers/__tests__/billing-router.test.ts, src/server/services/billing/__tests__/process-yookassa-webhook.test.ts

---

## 2026-02-26 — Ручная фиксация оплаты order и guard для installment

### CHG-077: Добавлен операционный путь manual payment для pending order без ослабления инварианта Enrollment

- **Было**:
  - после ужесточения правила `Enrollment` (только после оплаты) отсутствовал прикладной путь ручной фиксации оплаты заказа;
  - `installment` отображался в UI как рабочая опция при отсутствии реализованного backend-flow.
- **Стало**:
  - добавлена мутация ручного подтверждения оплаты order (`billing.confirmOrderPaidManually`) для admin/manager;
  - ручное подтверждение создаёт payment trace, переводит order в `paid` и запускает тот же paid-path создания enrollment;
  - в UI `installment` остаётся видимым, но помечен как не реализованный и недоступен к выбору; сервер возвращает явную ошибку при попытке использовать этот метод.
- **Почему**: сохранить инвариант «без оплаты нет enrollment» и вернуть необходимый операционный сценарий (наличные/внепровайдерная оплата).
- **Затронуто**: src/server/trpc/routers/billing.ts, src/server/dto/trpc/billing.ts, src/app/admin/billing/billing-admin-client.tsx, src/server/trpc/routers/__tests__/billing-router.test.ts

---

## 2026-02-26 — Enrollment только после оплаты (Order-Centric целостность)

### CHG-076: `Enrollment` создаётся только из оплаченного заказа и всегда имеет обязательный `orderId`

- **Было**:
  - в отдельных API-потоках `Enrollment` создавался до оплаты;
  - в runtime/DTO допускалась nullable-семантика `Enrollment.orderId`.
- **Стало**:
  - закреплён инвариант: `Enrollment` создаётся только после подтверждённой оплаты
    (`Payment.status=success` для B2C, `Invoice.status=paid` для B2B);
  - `Enrollment.orderId` переведён в обязательный FK;
  - ручные и batch-потоки зачисления теперь требуют существующий `Order.status=paid`.
- **Почему**: устранить нарушение целостности и зафиксировать правило «нельзя быть зачисленным без оплаты».
- **Затронуто**: prisma/schema.prisma, src/server/trpc/routers/billing.ts, src/server/trpc/routers/enrollments.ts, src/server/trpc/routers/companies.ts, docs/01-domain-model.md, docs/03-data-flows.md, docs/GLOSSARY.md

---

## 2026-02-26 — Contract-first привязка счета к договору в B2B request flow

### CHG-075: Юридический контур B2B зафиксирован через обязательный `Invoice.contractId`

- **Было**:
  - B2B заявка на обучение не требовала явного выбора договора в пользовательском UX;
  - связь счета с договором могла быть неявной в отдельных ветках.
- **Стало**:
  - закреплено правило: каждый `Invoice` обязан ссылаться на `Contract` (`Invoice.contractId`);
  - в `/company` добавлен read-only блок договоров и обязательный выбор договора перед формированием заявки;
  - `CompanyRequest` остаётся операционным header, а юридическая трассировка выполняется через `Invoice -> Contract`;
  - добавлен read-only админ-раздел `/admin/companies/[companyId]/contracts`.
- **Почему**: повысить прозрачность юридической базы для клиента и менеджера, исключить счета без договорного основания.
- **Затронуто**: docs/01-domain-model.md, docs/03-data-flows.md, docs/GLOSSARY.md, docs/CHANGELOG.md

---

## 2026-02-25 — Lead-First B2B: удаление Company.status и модерация через Lead

### CHG-074: Упрощён lifecycle компании в B2B flow

- **Было**:
  - в схеме присутствовал `Company.status (pending|active|rejected)`, что дублировало pre-approval состояние заявки;
  - B2B flow имел риск рассинхрона между `Lead.status` и `Company.status`.
- **Стало**:
  - lifecycle pre-approval закреплён только за `Lead` (`source=b2b`);
  - `Company.status` удалён из runtime-модели; доступ к B2B-company определяется по связи `Company.contact_person_id` и `deleted_at IS NULL`;
  - в `docs/01-domain-model.md` зафиксировано правило Lead-first: Company создаётся только на approve B2B lead.
- **Почему**: исключить дублирующие источники состояния и упростить модерацию/операционку B2B сценария.
- **Затронуто**: docs/01-domain-model.md, docs/CHANGELOG.md

---

## 2026-02-25 — B2C Act I demo flow (products/checkout/otp-gated onboarding)

### CHG-073: Закреплён guest-first сценарий покупки с отложенной активацией доступа после email verification

- **Было**:
  - B2C путь не покрывал полный self-service сценарий гостя;
  - onboarding/LMS могли открываться без явного шага подтверждения владения email в кабинете;
  - не было явного проектного инварианта о создании/применении миграций только через Prisma CLI.
- **Стало**:
  - реализован целевой демо-поток: `/products -> /checkout (guest) -> mock payment -> auto sign-in -> /student -> OTP verification -> auto onboarding activation -> LMS`;
  - для guest checkout зафиксирована модель заказа `userId? + guestEmail` с DB-инвариантом «хотя бы один идентификатор покупателя»;
  - UI кабинета студента блокирует действия до подтверждения email; LMS для студента доступен только после старта onboarding;
  - после подтверждения email активация onboarding выполняется автоматически (без ручного действия);
  - в `PLAN.md` добавлен инвариант: любые schema-изменения и миграции выполняются только через Prisma (`npx prisma ...`).
- **Почему**: повысить конверсию в демо-сценарии за счёт guest-first покупки, одновременно сохранив безопасную верификацию email перед полноценной активацией обучения и уведомлений.
- **Затронуто**: PLAN.md, DEMO.md, prisma/schema.prisma, prisma/migrations/20260225060000_guest_checkout_orders/migration.sql, src/app/products/*, src/app/checkout/*, src/app/student/student-hub-client.tsx, src/server/trpc/routers/billing.ts, src/server/trpc/routers/lms.ts, src/server/trpc/routers/student.ts, docs/CHANGELOG.md

---

## 2026-02-25 — Wave 1: синхронизация AC и тестового покрытия

### CHG-072: Уточнён redirect-контракт и расширено regression-покрытие Wave 1

- **Было**:
  - redirect helper `getRoleRedirectPath` для `admin|manager` возвращал `/admin`, что расходилось с AC `ZIS-024` (`/admin/dashboard`);
  - не было изолированных тестов для `student.myEnrollments` и `curator.myGroups`, а также unit-покрытия redirect mapping.
- **Стало**:
  - `getRoleRedirectPath` приведён к AC: `admin|manager -> /admin/dashboard`;
  - добавлены тесты:
    - `src/shared/auth-redirect.test.ts`
    - `src/server/trpc/routers/__tests__/student-router.test.ts`
    - `src/server/trpc/routers/__tests__/curator-router.test.ts`
  - обновлён ожидаемый redirect в `impersonation-router.test.ts` под новый контракт.
- **Почему**: закрыть разрыв между acceptance criteria и фактическим поведением, а также зафиксировать регрессионную защиту Wave 1.
- **Затронуто**: src/shared/auth-redirect.ts, src/shared/auth-redirect.test.ts, src/server/trpc/routers/__tests__/student-router.test.ts, src/server/trpc/routers/__tests__/curator-router.test.ts, src/server/trpc/routers/__tests__/impersonation-router.test.ts, docs/CHANGELOG.md

---

## 2026-02-25 — Impersonation MVP: дизайн и delivery-задача

### CHG-071: Зафиксирован дизайн impersonation и выполнена реализация `ZIS-035`

- **Было**:
  - в process-документах и backlog не было формализованного MVP-решения по impersonation с обязательным reason, UI-banner и audit policy.
- **Стало**:
  - создан дизайн-документ `docs/plans/2026-02-25-impersonation-design.md` с выбранным подходом `tRPC orchestration + better-auth admin impersonation`;
  - задача `ZIS-035` переведена из draft в delivery и доведена до UAT `approve`;
  - зафиксированы policy-ограничения MVP:
    - start только для `admin`;
    - target только `manager|curator|student`;
    - banned/deactivated target блокируется;
    - reason обязателен;
    - global impersonation banner + stop action.
- **Почему**: стандартизировать безопасный support-flow «посмотреть глазами пользователя» без отхода от auth-инвариантов.
- **Затронуто**: `docs/plans/2026-02-25-impersonation-design.md`, `backlog/tasks/zis-035 - Impersonation-в-админке-вход-от-лица-пользователя-MVP.md`, `docs/CHANGELOG.md`

---

## 2026-02-25 — Wave 1: Мультиролевые личные кабинеты (дизайн + план)

### CHG-070: Дизайн-документ и план реализации мультиролевого демо

- **Было**: демо-сценарий проводился от одного пользователя (admin); остальные роли не имели собственных layout/hub.
- **Стало**: создан дизайн-документ и план реализации Wave 1 (9 задач); DEMO.md переписан для 5-браузерной мультиролевой демонстрации.
- **Почему**: для демонстрации инвесторам/команде нужен наглядный мультиролевой сценарий с переключением между браузерами.
- **Затронуто**: `docs/plans/2026-02-24-multi-role-demo-design.md`, `docs/plans/2026-02-24-wave1-personal-dashboards.md`, `DEMO.md`

---

## 2026-02-20 — Документирован шаблон cursor-пагинации для админ-списков

### CHG-069: В `docs/16-frontend.md` добавлен стандарт `Cursor Pagination Pattern (Admin Lists)`

- **Было**:
  - в frontend-практиках не было отдельного каноничного паттерна для cursor-пагинации в админских таблицах.
- **Стало**:
  - добавлен раздел `16.7.3 Cursor Pagination Pattern (Admin Lists)`:
    - общий API-контракт пагинации (`pagination` input/meta output),
    - URL как source of truth для фильтров,
    - обязательный reset пагинации при изменении filter key,
    - базовый UX `Load more`,
    - стандартизированы пути shared сущностей (`use-cursor-pagination`, `PaginationControls`) и pilot-пример `/admin/events`.
- **Почему**: закрепить переиспользуемый, единообразный и предсказуемый паттерн пагинации для последующего тиражирования на другие админ-страницы.
- **Затронуто**: docs/16-frontend.md, docs/CHANGELOG.md

---

## 2026-02-20 — Восстановлен `AGENTS.md` и синхронизированы `PLAN.md`/`ROADMAP.md`

### CHG-068: Startup contract возвращён, процесс закреплён в ключевых индексах

- **Было**:
  - после workflow reset отсутствовал корневой `AGENTS.md`, что ухудшало bootstrap новых чатов;
  - `PLAN.md` и `ROADMAP.md` не содержали явной фиксации `Plan Mode`/`UAT Gate` как обязательных process-gates.
- **Стало**:
  - восстановлен `AGENTS.md` как короткий operational contract для новых чатов;
  - в `PLAN.md` добавлен раздел `Workflow v1 (superpowers + Backlog.md)` со ссылками на process-docs и правилом старта реализации только после согласованного Plan Mode;
  - в `ROADMAP.md` добавлены ссылки на `docs/15-ai-team.md` и `AGENTS.md`, а также явно зафиксированы обязательные `Plan Mode` и `UAT Gate`.
  - `ROADMAP.md` переведён с WP-терминологии на ID backlog (`ZIS-*` / `DRAFT-*`) в таблицах и примечаниях.
  - в `README.md` добавлен раздел со стандартным агентским workflow и рабочими триггерами процесса.
  - добавлен `WORKFLOW.MD` в корне проекта с живым end-to-end примером применения Workflow v1 (промпты пользователя + этапы + UAT ветки).
  - в `CLAUDE.md` добавлен явный раздел `Workflow v1`, синхронизированный с `AGENTS.md`.
  - в `AGENTS.md`, `CLAUDE.md`, `docs/15-ai-team.md` и `WORKFLOW.md` добавлены правила использования MCP `postgres_zis` и явное разделение схем: `public` (Prisma domain) и `pgboss` (queue).
  - добавлен `docs/GLOSSARY.md` с глоссарием сущностей на уровне моделей Prisma и их назначением.
  - формулировки pipeline упрощены до `Plan Mode -> Delivery -> UAT -> Finalization` (validation/review встроены в Delivery).
  - удалён `RESUME.md` как legacy-документ старого workflow, не используемый в новом процессе.
- **Почему**: сохранить “точку входа” для нового чата и снизить риск расхождения между архитектурным/плановым контекстом и фактическим workflow.
- **Затронуто**: AGENTS.md, CLAUDE.md, PLAN.md, ROADMAP.md, README.md, WORKFLOW.md, docs/15-ai-team.md, docs/GLOSSARY.md, RESUME.md (deleted), docs/CHANGELOG.md

---

## 2026-02-20 — Workflow reset: superpowers + Backlog.md (точка 0)

### CHG-067: Пересобран process-docs с нуля вокруг Plan Mode + Task Cookie Cutter

- **Было**:
  - процесс опирался на набор legacy-артефактов (`AGENTS.md`, `WORKFLOW.md`, `docs/agents/*`, `backlog/agent/*`);
  - этапы intake/brainstorm/выбор подхода были разнесены по нескольким операционным документам и скриптам.
- **Стало**:
  - удалены legacy-артефакты workflow: `WORKFLOW.md`, `docs/agents/*`, `backlog/agent/*`;
  - удалены legacy workflow-скрипты: `scripts/agents/*`;
  - `docs/15-ai-team.md` переписан как единый стандарт `superpowers + Backlog.md`;
  - добавлен каноничный `Task Cookie Cutter` для интерактивного Plan Mode с обязательным human approval перед реализацией;
  - зафиксированы этапы: `Plan Mode -> Delivery -> UAT -> Finalization` с внутренними validation/review гейтами в Delivery.
- **Почему**: упростить онбординг и снизить process-friction, сохранив строгие quality gates и понятный human-in-the-loop.
- **Затронуто**: docs/15-ai-team.md, docs/CHANGELOG.md, WORKFLOW.md (deleted), docs/agents/* (deleted), backlog/agent/* (deleted), scripts/agents/* (deleted)

---

## 2026-02-19 — Agent artifacts переехали в `backlog/agent/*`

### CHG-066: Убран split между Backlog и `docs/agents/tasks` для рабочих артефактов

- **Было**:
  - task/draft source of truth находился в `backlog/*`, но операционные артефакты (`task-card`, `state`, handoff, retrospective, KPI) создавались в `docs/agents/tasks/*`.
- **Стало**:
  - все новые операционные артефакты создаются рядом с backlog в `backlog/agent/{zis-xxx|draft-xxx}/*`;
  - `take-task/validate-task/plan-draft` переведены на новый путь;
  - шаблоны и skill-инструкции обновлены на новую структуру.
- **Почему**: убрать путаницу между двумя директориями и закрепить единый домен артефактов в `backlog/*`.
- **Затронуто**: scripts/agents/take-task.sh, scripts/agents/validate-task.sh, scripts/agents/plan-draft.sh, docs/agents/task-card-template.md, docs/agents/task-state-template.yaml, docs/agents/templates/handoff-template.md, docs/agents/templates/retrospective-template.md, docs/agents/templates/wp-kpi-template.yaml, docs/agents/README.md, .agents/skills/*/SKILL.md, CHANGELOG.md, docs/CHANGELOG.md

---

## 2026-02-19 — Формализован Draft Plan entrypoint (`plan-draft.sh`)

### CHG-065: Добавлен отдельный скрипт для планирования `DRAFT-*` и обновлены workflow-инструкции

- **Было**:
  - для доработки draft использовался только текстовый триггер, без стандартизированного preflight-скрипта.
- **Стало**:
  - добавлен `scripts/agents/plan-draft.sh DRAFT-XXX [--dry-run]`;
  - скрипт проверяет draft в `backlog/drafts/*` и подготавливает planning card в `backlog/agent/draft-xxx/plan.md`;
  - обновлены workflow-документы с явной командой для Draft Plan Mode.
- **Почему**: снизить рассинхрон между агентами и сделать этап доработки черновиков воспроизводимым.
- **Затронуто**: scripts/agents/plan-draft.sh, docs/agents/README.md, docs/15-ai-team.md, WORKFLOW.md, docs/CHANGELOG.md

---

## 2026-02-19 — Команды take/validate переведены на task-only (`ZIS-*`)

### CHG-064: Переход с `take-wp/validate-wp` на `take-task/validate-task` и унификация триггеров

- **Было**:
  - рабочие команды были ориентированы на `WP-*` и допускали mixed режим (tasks/drafts).
  - в playbook оставались формулировки «Берём `WP-XXX`...».
- **Стало**:
  - введены команды `scripts/agents/take-task.sh ZIS-XXX` и `scripts/agents/validate-task.sh ZIS-XXX`.
  - take/validate теперь работают только с `backlog/tasks/*` (task-only), а `DRAFT-*` явно вынесен в Plan Mode.
  - `scripts/agents/take-wp.sh` и `scripts/agents/validate-wp.sh` оставлены как deprecated wrappers с подсказкой новых команд.
  - `docs/agents/README.md` и `.agents/skills/architect-wp-orchestrator-skill/SKILL.md` синхронизированы с новыми командами/триггерами.
- **Почему**: устранить путаницу между `WP-*` и backlog IDs, привести команды к фактическому source of truth (задачи `ZIS-*`).
- **Затронуто**: scripts/agents/take-task.sh, scripts/agents/validate-task.sh, scripts/agents/take-wp.sh, scripts/agents/validate-wp.sh, docs/agents/README.md, .agents/skills/architect-wp-orchestrator-skill/SKILL.md, docs/CHANGELOG.md

---

## 2026-02-19 — Backlog-first формулировки в `docs/agents/README.md`

### CHG-063: Убрана привязка `take-wp` к ROADMAP в тексте playbook

- **Было**:
  - в `docs/agents/README.md` запуск цикла был описан как «Берём `WP-XXX` из `ROADMAP.md`».
- **Стало**:
  - формулировка обновлена до «Берём `WP-XXX` из Backlog».
  - цель playbook уточнена как Backlog-first (`WP` берётся из backlog, а не из roadmap-индекса).
- **Почему**: синхронизировать документацию с текущим source of truth (`backlog/tasks/*`, `backlog/drafts/*`) и поведением automation-скриптов.
- **Затронуто**: docs/agents/README.md, docs/CHANGELOG.md

---

## 2026-02-19 — Усилен `WORKFLOW.md`: Plan Mode + конкретные промпты

### CHG-062: Мини-сценарий в `WORKFLOW.md` заменён на практический end-to-end runbook

- **Было**:
  - пример в `WORKFLOW.md` был слишком абстрактным и не задавал явный формат взаимодействия user ↔ agent на этапе детализации.
- **Стало**:
  - добавлен отдельный раздел про ожидаемое поведение агента в Plan Mode (уточняющие вопросы, baseline, подтверждение перед реализацией);
  - добавлен конкретный сценарий с готовыми промптами пользователя и ожидаемыми действиями агента на каждом шаге (A-E).
- **Почему**: сделать workflow пригодным для ежедневной практики без неоднозначной трактовки.
- **Затронуто**: WORKFLOW.md, docs/CHANGELOG.md

---

## 2026-02-19 — Добавлен операционный quick-reference `WORKFLOW.md`

### CHG-061: Создан `WORKFLOW.md` с пошаговой инструкцией и примером применения

- **Было**:
  - процесс был описан в архитектурной документации, но не было короткой «рабочей памятки» в корне репозитория.
- **Стало**:
  - добавлен `WORKFLOW.md` в корень проекта;
  - зафиксированы: source of truth, триггеры, pipeline, quality gates, CLI-команды и мини-сценарий применения.
- **Почему**: дать быстрый и единый reference для ежедневной работы по Backlog-first процессу.
- **Затронуто**: WORKFLOW.md, docs/CHANGELOG.md

---

## 2026-02-19 — Объединение `docs/15` и `docs/18` в единый процесс

### CHG-060: Delivery workflow встроен в `docs/15-ai-team.md`, отдельный `docs/18-ai-delivery-workflow.md` удалён

- **Было**:
  - процесс ролей AI-команды и delivery pipeline были разнесены по двум файлам (`docs/15-ai-team.md` и `docs/18-ai-delivery-workflow.md`), что создавало лишнюю навигацию и риск рассинхрона.
- **Стало**:
  - `docs/15-ai-team.md` стал единым документом: роли + source of truth + триггеры + pipeline + quality gates + DoD + CLI-команды;
  - `docs/18-ai-delivery-workflow.md` удалён;
  - ссылки в `PLAN.md` и `ROADMAP.md` переведены на `docs/15-ai-team.md`.
- **Почему**: уменьшить путаницу и оставить один каноничный документ для процесса AI-разработки.
- **Затронуто**: docs/15-ai-team.md, docs/18-ai-delivery-workflow.md (deleted), PLAN.md, ROADMAP.md, docs/CHANGELOG.md

---

## 2026-02-19 — Синхронизация `docs/15-ai-team.md` с Backlog-first процессом

### CHG-059: `docs/15-ai-team.md` переведён в role-map + ссылки на каноничный workflow

- **Было**:
  - `docs/15-ai-team.md` частично дублировал/конфликтовал с новым процессом из `docs/18-ai-delivery-workflow.md` (упор на `ROADMAP` и устаревшие формулировки).
  - Cookie cutter ссылался на roadmap-формулировки и legacy путь `src/server/events/types.ts`.
- **Стало**:
  - `docs/15-ai-team.md` актуализирован как документ про роли AI-команды (Architect, Backend, Frontend, QA, Security, Code Review) и карту чтения документов.
  - Явно зафиксировано:
    - source of truth для реализации — `backlog/tasks/*` и `backlog/drafts/*`;
    - `ROADMAP.md` используется только как контекст/навигация;
    - каноничный delivery pipeline — `docs/18-ai-delivery-workflow.md`.
  - Секция Cookie Cutter теперь ссылается на каноничный раздел в `PLAN.md`.
  - Обновлены правила по changelog discipline (корневой `CHANGELOG.md` и `docs/CHANGELOG.md`).
- **Почему**: убрать рассинхрон между документами и обеспечить единый процесс разработки через Backlog-first workflow.
- **Затронуто**: docs/15-ai-team.md, docs/CHANGELOG.md

---

## 2026-02-19 — Backlog-first AI delivery workflow: регламент и шаблоны

### CHG-058: Формализован единый pipeline работы AI-команды и добавлены шаблоны Draft/Task

- **Было**:
  - процесс обсуждался устно/в диалогах, но не был зафиксирован как единый операционный стандарт с обязательными quality gates и changelog discipline;
  - не было централизованных шаблонов для Draft/Task в backlog.
- **Стало**:
  - добавлен документ `docs/18-ai-delivery-workflow.md` с полным циклом: intake → planning → draft/task → multi-agent delivery → QA/Security/Code Review → finalization;
  - в `AGENTS.md` добавлены:
    - операционный цикл (`4.1`);
    - базовый триггер запуска реализации: `Берём ZIS-XXX из Backlog`;
    - обязательные проверки перед завершением (включая тесты нового/изменённого функционала);
    - changelog discipline (`CHANGELOG.md` + `docs/CHANGELOG.md`);
  - добавлены рабочие шаблоны:
    - `backlog/docs/draft-template.md`
    - `backlog/docs/task-template.md`;
  - `PLAN.md` дополнен ссылкой на новый workflow-документ в навигации.
- **Почему**: закрепить воспроизводимый процесс масштабирования разработки через Backlog-first подход и multi-agent роли, снизить scope drift и сделать качество/документирование обязательной частью delivery.
- **Затронуто**: AGENTS.md, PLAN.md, docs/18-ai-delivery-workflow.md, backlog/docs/draft-template.md, backlog/docs/task-template.md, docs/CHANGELOG.md

---

## 2026-02-19 — ROADMAP упрощён до индекса backlog, cookie cutter закреплён в PLAN

### CHG-057: Перенос детальных WP-описаний из `ROADMAP.md` в backlog-ссылки + канонизация шаблона модулей в `PLAN.md`

- **Было**:
  - `ROADMAP.md` содержал развёрнутые текстовые описания WP.
  - После перехода на backlog-first формат существовал риск потерять видимость секции "cookie cutter" из roadmap.
- **Стало**:
  - `ROADMAP.md` упрощён до фазового индекса с ссылками на файлы `backlog/tasks/*` и `backlog/drafts/*`.
  - Шаблон разработки нового модуля (cookie cutter) закреплён в `PLAN.md` как самостоятельный каноничный раздел.
  - В `ROADMAP.md` добавлена явная ссылка на cookie cutter раздел в `PLAN.md`.
- **Почему**: сохранить roadmap как навигационный документ (а не дублирующий task-body) и одновременно не потерять инженерный стандарт для единообразной разработки модулей.
- **Затронуто**: ROADMAP.md, PLAN.md, docs/CHANGELOG.md

---

## 2026-02-16 — Удаление Domain Events (EventEmitter) из архитектуры

### CHG-056: Удалён EventEmitter, переход на прямые вызовы сервисов + pg-boss в транзакции

- **Было**: Два параллельных механизма событий — EventEmitter (`src/server/events/`) и pg-boss. Webhook вызывал `domainEvents.emit("payment.success")`, цепочка handlers ставила pg-boss jobs.
- **Стало**:
  - Удалена директория `src/server/events/` (emitter.ts, types.ts, handlers/, тесты)
  - Сервисы вызывают друг друга напрямую
  - Event-записи создаются через `db.event.create()` внутри транзакции
  - pg-boss jobs ставятся через `sendJobInTransaction()` / `createProcessWithJobsInTransaction()`
  - DTO payload-схемы остались в `src/server/dto/events.ts` (переименованы: `EventTypeName`, `EventPayloadMap`, `EventRecord` и т.д.)
  - `handlePaymentSuccess` перемещён в `src/server/services/billing/handle-payment-success.ts`
  - `cron.ts` использует `db.event.create()` вместо `domainEvents.emit()`
- **Почему**: Для масштаба ~3000 студентов/год, 1 разработчик, монолит — два механизма событий создают лишнюю сложность. Один механизм (прямые вызовы + pg-boss в транзакции) проще, прозрачнее, транзакционно безопаснее.
- **Затронуто**: src/server/events/ (удалено), src/server/dto/events.ts, src/server/services/billing/handle-payment-success.ts (new), src/server/worker/cron.ts, src/server/worker/README.md, PLAN.md, CLAUDE.md, README.md, ROADMAP.md, CHANGELOG.md, docs/CHANGELOG.md, docs/02-architecture.md, docs/03-data-flows.md, docs/06-edge-cases.md, docs/09-example-student-lifecycle.md, docs/10-example-manager-day.md, docs/13-testing.md, docs/14-nfr.md, docs/15-ai-team.md, docs/17-reliable-events.md, docs/08-mcp-cli-agents.md, docs/agents/tasks/wp-003.md, docs/agents/tasks/wp-004.md

---

## 2026-02-16 — Надёжная доставка критичных событий: документация + код

### CHG-055: Рефакторинг doc-17, перенос рисков, sendJobInTransaction

- **Было**:
  - `docs/17-queue-inbox-outbox.md` — заголовок и содержание привязаны к payment, SQL-ошибка (`expire_in interval` вместо `expire_seconds int`).
  - Риски A/B/C описаны в отдельном `RISKS.md`, не интегрированы в реестр edge-cases.
  - `docs/06-edge-cases.md:370` — неточность «Worker обновляет в одной транзакции».
  - `docs/02-architecture.md:253` — вводящая в заблуждение формулировка о транзакционности handlers.
  - В коде нет функции для raw INSERT в `pgboss.job` внутри Prisma `$transaction`.
- **Стало**:
  - Файл переименован `docs/17-queue-inbox-outbox.md` → `docs/17-reliable-events.md`, обобщён на все критичные события.
  - SQL исправлен: `expire_seconds` (integer), `state = 'created'`.
  - `RISKS.md` перемещён в `docs/OLD/RISKS-2026-02-16.md`.
  - Добавлена секция `6.34 Атомарность критичного пути payment → onboarding` в `docs/06-edge-cases.md`.
  - Исправлены неточности в `docs/06-edge-cases.md` и `docs/02-architecture.md`.
  - Ссылки обновлены в `PLAN.md` и `docs/CHANGELOG.md`.
  - Реализован `sendJobInTransaction()` в `src/server/worker/send-in-transaction.ts`.
  - Реализован `createProcessWithJobsInTransaction()` в `src/server/worker/process.ts`.
  - Рефакторинг `handlePaymentSuccess` — использует transactional создание Process + Jobs.
  - Тесты для `sendJobInTransaction` и `createProcessWithJobsInTransaction`.
- **Почему**: закрыть gap между декларациями архитектуры и реальными runtime-гарантиями; дать команде рабочий код для атомарной постановки pg-boss jobs.
- **Затронуто**: docs/17-reliable-events.md, docs/06-edge-cases.md, docs/02-architecture.md, PLAN.md, docs/CHANGELOG.md, RISKS.md → docs/OLD/, src/server/worker/send-in-transaction.ts (new), src/server/worker/process.ts, src/server/worker/index.ts, src/server/events/handlers/payment-success.ts, tests

---

## 2026-02-16 — Терминология: Domain Events как каноничное название

### CHG-054: Унифицирована терминология событийного слоя во всей активной документации

- **Было**: в документации параллельно использовались термины `Event Bus`, `EventBus` и `Domain Events`, что создавало риск неверной интерпретации как внешней message bus-инфраструктуры (Kafka/RabbitMQ/EventBridge).
- **Стало**:
  - каноничный термин: `Domain Events`;
  - во всех ключевых документах обновлены формулировки (`PLAN.md`, `ROADMAP.md`, `README.md`, `docs/02-architecture.md`, `docs/06-edge-cases.md`, `docs/13-testing.md`, `docs/14-nfr.md`, `docs/15-ai-team.md`, task-cards WP);
  - сохранён явный технический контекст: текущая реализация — внутренний in-process typed EventEmitter, а надёжность тяжёлых/асинхронных операций обеспечивается через `pg-boss`.
- **Почему**: зафиксировать однозначный фундаментный словарь проекта и убрать терминологическую двусмысленность для новых разработчиков.
- **Затронуто**: PLAN.md, ROADMAP.md, README.md, CHANGELOG.md, CLAUDE.md, RESUME.md, docs/02-architecture.md, docs/03-data-flows.md, docs/06-edge-cases.md, docs/08-mcp-cli-agents.md, docs/09-example-student-lifecycle.md, docs/10-example-manager-day.md, docs/13-testing.md, docs/14-nfr.md, docs/15-ai-team.md, docs/agents/tasks/wp-003.md, docs/agents/tasks/wp-004.md

---

## 2026-02-16 — Outbox/Inbox reliability blueprint for critical events

### CHG-052: Добавлен отдельный архитектурный стандарт для queue-надежности (`docs/17-reliable-events.md`)

- **Было**: Риски потери/частичной обработки критичных событий (payment/onboarding) были описаны в edge-cases и в ad-hoc анализе, но без единого детального implementation blueprint по transactional outbox + inbox delivery state.
- **Стало**:
  - Добавлен новый документ `docs/17-reliable-events.md` (ранее `docs/17-queue-inbox-outbox.md`) с полным контрактом:
    - цели и scope для критичных сценариев (`payment.success`);
    - модель данных `outbox_events` и `event_handler_deliveries`;
    - пошаговые flow'ы: webhook transaction, dispatcher, inbox processor;
    - отказные сценарии (crash/retry) и их детерминированное поведение;
    - правила идемпотентности handler'ов (DB + external API);
    - observability-метрики, alerting, тестовые критерии и порядок внедрения.
  - В `PLAN.md` добавлен новый пункт навигации: `17. Надёжная доставка критичных Domain Events`.
- **Почему**: убрать неоднозначность между декларациями архитектуры и требуемыми runtime-гарантиями для критичных бизнес-операций; дать команде чёткий пошаговый план внедрения.
- **Затронуто**: docs/17-reliable-events.md (new), PLAN.md, docs/CHANGELOG.md

### CHG-053: `docs/17-reliable-events.md` (ранее `17-queue-inbox-outbox.md`) адаптирован под текущий runtime-стек (Prisma-first)

- **Было**: секция модели данных и часть примеров были описаны SQL-терминами (`CREATE TABLE`, snake_case table names).
- **Стало**:
  - модель данных переписана как Prisma schema (`OutboxEvent`, `EventHandlerDelivery`, enum-ы `OutboxStatus`, `DeliveryStatus`);
  - примеры dispatcher/inbox processor переписаны на Prisma API (`findMany`, `upsert`, `updateMany`, `update`, `db.$transaction`);
  - рекомендации по идемпотентности приведены к Prisma-практикам (`upsert`, `createMany(..., skipDuplicates: true)`).
- **Почему**: документ должен быть directly actionable для текущего кода проекта (TypeScript + Prisma), без лишнего SQL-слоя.
- **Затронуто**: docs/17-reliable-events.md, docs/CHANGELOG.md

---

## 2026-02-16 — WP-008 Improvement: глобальный отказ от isActive

### CHG-050: Замена `is_active` на `deleted_at` во всех моделях

- **Было**: Часть моделей использовала двойной механизм soft delete (`isActive` + `deletedAt`), часть — только `isActive` без `deletedAt`. Непоследовательный паттерн.
- **Стало**: Единый паттерн soft delete через `deletedAt DateTime?` (null = активна, non-null = деактивирована). Поле `isActive` удалено из всех моделей: User, Product, Tier, Module, Lesson, Homework, PromoCode, TelegramChat, ApiToken. Для моделей, где `deletedAt` не было — добавлено.
- **Почему**: Единообразие, устранение дублирования состояния, упрощение WHERE-фильтров (`deletedAt IS NULL` вместо двойной проверки).
- **Затронуто**: docs/01-domain-model.md, prisma/schema.prisma, src/server/dto/trpc/users.ts, src/server/dto/trpc/companies.ts, src/server/dto/trpc/auth-context.ts, src/server/services/users/mappers.ts, src/server/services/users/dto.ts, src/server/trpc/routers/users.ts, src/server/trpc/routers/companies.ts, src/server/auth.ts, prisma/seed.ts, src/app/admin/users/users-admin-client.tsx

### CHG-051: Инфраструктурные улучшения WP-008

- **Было**: Локальные `normalizeText` в каждом роутере; `UserIdSchema` вместо `CuidSchema`; `*MutationOutputDtoSchema` naming; inline auth guard в admin-страницах; vanilla fetch вместо React Query; sequential DB queries в `assertAssignableUserIds`; self-deactivation guard только для admin.
- **Стало**:
  - `normalizeText` вынесен в `src/server/lib/text.ts`
  - `CuidSchema` из `@/server/dto/shared` вместо локального `UserIdSchema`
  - `*MutationOutputDtoSchema` → `*OutputDtoSchema`
  - `src/server/lib/require-admin-session.ts` — общая утилита auth guard
  - `@trpc/tanstack-react-query` + `@tanstack/react-query` — провайдеры, хуки, invalidation
  - `assertAssignableUserIds` — один `findMany` вместо цикла `findFirst`
  - Self-deactivation запрещена для всех ролей, не только admin
  - Тесты расширены: явный поиск по ID, cursor pagination, новые кейсы
- **Почему**: Повышение качества reference-кода (Phase 0.5 образец для команды).
- **Затронуто**: src/server/lib/text.ts (new), src/server/lib/require-admin-session.ts (new), src/app/_providers.tsx (new), src/shared/trpc-client.ts, src/app/layout.tsx, src/app/admin/users/page.tsx, src/app/admin/companies/page.tsx, src/app/admin/users/users-admin-client.tsx, src/app/admin/companies/companies-admin-client.tsx, src/server/trpc/routers/users.ts, src/server/trpc/routers/companies.ts, src/server/dto/trpc/users.ts, src/server/dto/trpc/companies.ts, tests

---

## 2026-02-16 — Консолидация role-документации в skills

### CHG-049: `docs/agents/role-*` переведены в role-index, source of truth по ролям закреплён в `SKILL.md`

- **Было**: role-файлы в `docs/agents/role-*` дублировали workflow и checkpoints, которые уже были описаны в `.agents/skills/*/SKILL.md`.
- **Стало**:
  - `docs/agents/role-architect.md`
  - `docs/agents/role-backend.md`
  - `docs/agents/role-frontend.md`
  - `docs/agents/role-qa.md`
  - `docs/agents/role-security.md`

  переведены в короткие role-index документы с ссылкой на canonical source: соответствующий `SKILL.md`.
  - В `docs/agents/README.md` добавлено явное правило: role-files = navigation index, canonical role behavior = `.agents/skills/*/SKILL.md`.
- **Почему**: убрать дублирование и риск рассинхронизации между docs и skills, сохранив удобную навигацию для людей.
- **Затронуто**: docs/agents/role-*.md, docs/agents/README.md, docs/CHANGELOG.md

---

## 2026-02-14 — Автономный контур AI-команды (без CI/CD части)

### CHG-048: Введён autonomous-by-default workflow для WP с machine-readable state, handoff, retrospective и KPI

- **Было**: Процесс команды уже включал planning-gate, task-card и formal Security/QA, но оставался в основном markdown-first и с ручными точками синхронизации между ролями.
- **Стало**:
  - Добавлены policy-файлы:
    - `docs/agents/policies/autonomy-policy.yaml` (risk classes, stop-conditions, completion requirements)
    - `docs/agents/policies/model-routing.yaml` (routing моделей по этапам, escalation policy)
    - `docs/agents/policies/ops-boundaries.md` (разделение dev-автономии и prod-операций)
  - Добавлен machine-readable шаблон состояния WP:
    - `docs/agents/task-state-template.yaml`
  - Расширен `docs/agents/task-card-template.md`:
    - секция `Autonomy Contract`
    - обязательные handoff/retrospective/KPI артефакты в DoD
  - Добавлены шаблоны операционных артефактов:
    - `docs/agents/templates/handoff-template.md`
    - `docs/agents/templates/retrospective-template.md`
    - `docs/agents/templates/wp-kpi-template.yaml`
  - Добавлен eval-набор для регресса автономии:
    - `docs/agents/evals/README.md`
    - `docs/agents/evals/scenarios.yaml`
  - Добавлены локальные orchestration-скрипты:
    - `scripts/agents/take-wp.sh` (единый вход “Берём WP-XXX”)
    - `scripts/agents/validate-wp.sh` (проверка обязательных артефактов без CI/CD)
  - Обновлены playbook/роли/skills под новый autonomous workflow:
    - `docs/agents/README.md`
    - `docs/agents/role-*.md`
    - `.agents/skills/*/SKILL.md`
- **Почему**: перейти к модели, где пользователь задаёт только WP из `ROADMAP.md`, а команда выполняет цикл максимально автономно с явными точками эскалации и измеримыми метриками.
- **Затронуто**: docs/agents/\*, .agents/skills/\*, scripts/agents/\*, docs/CHANGELOG.md

---

## 2026-02-13 — Frontend architecture standardization

### CHG-047: Расширен frontend-стандарт (tRPC client, state management, App Router conventions, design tokens)

- **Было**: `docs/16-frontend.md` покрывал базовую структуру, Tailwind policy и RBAC, но не описывал tRPC client setup, стратегию state management, App Router file conventions (`loading.tsx`/`error.tsx`/`not-found.tsx`), позицию по библиотеке форм и цветовую палитру.
- **Стало**:
  - Добавлен раздел **16.7.1 tRPC на фронтенде** — паттерны вызова (client hooks vs server caller), правила создания provider.
  - Добавлен раздел **16.7.2 State management** — TanStack Query как единственный механизм серверного состояния, без Redux/Zustand.
  - Раздел 16.8 расширен: App Router file conventions (`loading.tsx`, `error.tsx`, `not-found.tsx`), позиция по формам (`useState` для простых, `react-hook-form` при реальной потребности).
  - Раздел 16.6 расширен: зафиксирована цветовая палитра (cyan = primary, slate = neutral, emerald = success, rose = error, amber = warning).
  - Раздел 16.3 расширен: уточнена конвенция `_components/` как private folder.
  - Раздел 16.12: уточнено что Playwright добавляется при первом E2E-сценарии.
  - Раздел 16.13: добавлены анти-паттерны (Redux при наличии TanStack Query, raw fetch к tRPC, premature dependencies).
  - Раздел 16.14: добавлены пункты checklist (`format:check`, `loading.tsx`/`error.tsx`, tRPC hooks).
- **Почему**: устранение пробелов в frontend-стандарте, которые привели бы к неоднозначным решениям при реализации dashboard/CRM/LMS страниц.
- **Затронуто**: docs/16-frontend.md, docs/CHANGELOG.md

### CHG-046: Введён единый frontend-стандарт (структура, компоненты, Tailwind 4.1 policy)

- **Было**: frontend-подход был зафиксирован фрагментарно (через отдельные WP/изменения), без единого документа по структуре каталогов, правилам выделения компонентов и поддерживаемому стилевому стандарту.
- **Стало**:
  - добавлен `docs/16-frontend.md` с формализованными правилами:
    - структура frontend-слоя (`route-level` co-location, `shared/ui`);
    - границы Server/Client компонентов в App Router;
    - policy для Tailwind CSS 4.1;
    - правила выделения reusable UI-компонентов;
    - contract-first подход к данным, RBAC-UI принципы, checklist для PR.
  - в `PLAN.md` добавлен новый раздел навигации по документации: `16. Frontend Architecture & Practices`.
  - в `PLAN.md` и `docs/15-ai-team.md` обновлена карта файлов для LLM/AI-агентов (добавлена ссылка на frontend-стандарт).
- **Почему**: чтобы frontend развивался системно и предсказуемо, без дублирования паттернов и с едиными правилами масштабирования UI.
- **Затронуто**: docs/16-frontend.md, PLAN.md, docs/15-ai-team.md

---

## 2026-02-13 — WP-006: Pino logging + error handling

### CHG-045: Уточнён operational-подход к логированию tRPC ошибок и app-level error mapping

- **Было**: в фундаменте был базовый Pino-логгер и request logger, но не было формализованного глобального логирования tRPC-ошибок в route handler и явного app-level error hierarchy.
- **Стало**:
  - В runtime-коде реализован расширенный Pino-конфиг (ISO timestamp + redaction чувствительных полей)
  - Для tRPC request-level logger зафиксированы поля `trace_id`, `user_id`
  - Ошибки tRPC централизованно пишутся в `fetchRequestHandler(... onError ...)` на API-границе
  - Добавлены `AppError`, `NotFoundError`, `ConflictError` и mapping `toTRPCError()`
  - Добавлен formal task-card `docs/agents/tasks/wp-006.md`
- **Почему**: Улучшение наблюдаемости и управляемости ошибок без нарушения текущих границ модульного монолита и без добавления внешней observability-инфраструктуры.
- **Затронуто**: docs/agents/tasks/wp-006.md

---

## 2026-02-13 — Комплексный DTO-слой с guard rails

### CHG-043: Комплексный DTO-слой: shared-примитивы, worker payloads, mappers, guard rails

- **Было**: DTO baseline покрывал 3 файла (transport health, event payloads, worker envelope). Prisma enum дублировались через `z.enum()` в каждом файле. Worker payloads не типизированы. Нет паттерна response mapper. `WorkerJobData` дублирован в process.ts.
- **Стало**:
  - `src/server/dto/shared.ts` — зеркала всех 37 Prisma enum как Zod-схемы с compile-time guard (`AssertEqual`), общие примитивы (`CuidSchema`, `EmailSchema`, `AmountSchema`, `JsonValueSchema`), pagination, sort, date range
  - `src/server/dto/trpc/health.ts` — рефакторинг: `UserRoleSchema` из shared вместо дублирования
  - `src/server/dto/worker.ts` — per-job payload schemas (5 очередей), реестр `workerJobPayloadSchemas`, `parseWorkerJobPayload()`
  - `src/server/worker/process.ts` — `WorkerJobData` → re-export `WorkerJobEnvelopeDto`
  - `src/server/worker/executor.ts` — валидация payload через зарегистрированные схемы
  - `src/server/worker/registry.ts` — `registerTypedHandler<J>()` с типизацией payload по имени очереди
  - `src/server/services/users/mappers.ts` — reference-паттерн: `UserResponseDtoSchema`, `userResponseSelect`, `toUserResponseDto()`
  - `src/server/services/users/dto.ts` — command/query DTOs: `CreateUserCommandSchema`, `UpdateUserCommandSchema`, `BanUserCommandSchema`, `ListUsersQuerySchema`
  - Тесты: 52 новых (shared: 46, mappers: 6), всего 72 теста
  - `docs/02-architecture.md` — naming conventions + guard rails
- **Почему**: Предотвратить утечку Prisma-моделей в API, устранить дублирование типов, создать guard rails и reference-паттерн для всех будущих модулей Phase 1
- **Затронуто**: src/server/dto/shared.ts, src/server/dto/worker.ts, src/server/dto/trpc/health.ts, src/server/worker/process.ts, src/server/worker/executor.ts, src/server/worker/registry.ts, src/server/services/users/mappers.ts, src/server/services/users/dto.ts, docs/02-architecture.md, package.json

---

## 2026-02-13 — Дополнения архитектурных контрактов и реализация WP-004

### CHG-042: Удалены остатки legacy DTO-описаний из активного workflow

- **Было**: в части активной документации оставались legacy-формулировки про `src/shared/schemas/*` и старый шаблон `роутер + сервис + zod-схема`
- **Стало**:
  - `docs/02-architecture.md` переведён на актуальный DTO baseline (`src/server/dto/trpc/*`)
  - `ROADMAP.md` (структура и cookie-cutter разделы) синхронизирован с текущим DTO-подходом
- **Почему**: чтобы исключить двойные трактовки и закрепить единый рабочий путь без legacy-слоя
- **Затронуто**: docs/02-architecture.md, ROADMAP.md

### CHG-041: В workflow создания модулей DTO закреплены как обязательный шаг

- **Было**: DTO-принципы были зафиксированы в архитектуре, но в операционных инструкциях по созданию модулей (cookie cutter/agent workflow) требование не было явно обязательным
- **Стало**:
  - в `ROADMAP.md` (cookie cutter) добавлены обязательные шаги по transport/service DTO, mapper и DTO для event/worker payload
  - в `docs/15-ai-team.md` обновлён шаблон нового модуля и правила типизации/валидации
  - в `docs/agents/README.md` добавлено явное обязательное правило DTO для каждого нового модуля
  - в `docs/agents/task-card-template.md` добавлен DoD пункт про DTO-контракты
  - в `docs/agents/role-backend.md` добавлены шаг и checkpoint по DTO
- **Почему**: Сделать требование DTO не рекомендацией, а частью формального процесса разработки и приёмки
- **Затронуто**: ROADMAP.md, docs/15-ai-team.md, docs/agents/README.md, docs/agents/task-card-template.md, docs/agents/role-backend.md

### CHG-040: DTO retrofit для WP-001..WP-005 зафиксирован в коде и документации

- **Было**: DTO-требования были задокументированы, но фундаментные реализации (tRPC/Domain Events/Worker) покрывали их неполно и не везде имели runtime-валидацию payload на границах
- **Стало**:
  - добавлен DTO baseline в коде:
    - `src/server/dto/trpc/health.ts` (transport DTO для API/tRPC)
    - `src/server/dto/events.ts` (domain event payload DTO)
    - `src/server/dto/worker.ts` (worker job envelope DTO)
  - `health` router переведён на явные input/output DTO-схемы
  - Domain Events валидирует payload через DTO перед persist/handler dispatch
  - Worker executor валидирует envelope DTO перед обработкой job
  - обновлены документы: `PLAN.md`, `ROADMAP.md`, `README.md`, `docs/02-architecture.md`, `docs/13-testing.md`
- **Почему**: На этапе проектирования/масштабирования важнее зафиксировать строгие границы модулей сейчас, чем накапливать неявные контракты
- **Затронуто**: PLAN.md, ROADMAP.md, README.md, docs/02-architecture.md, docs/13-testing.md, src/server/dto/\*

### CHG-039: Документированы DTO-контракты и operational-подход к cron-задачам

- **Было**: DTO-слой и правила управления cron-задачами были описаны фрагментарно (через отдельные примеры), без явного архитектурного контракта и NFR-критериев наблюдаемости
- **Стало**:
  - в `docs/02-architecture.md` добавлены разделы:
    - `DTO и границы слоёв` (Input/Command/Response DTO, mapper `Prisma -> DTO`, запрет на утечку raw Prisma-моделей наружу)
    - `Cron-задачи (pg-boss schedules): управление` (единый cron-реестр, idempotency, singleton/DB constraints, incident criteria)
  - в `docs/03-data-flows.md` уточнены cron-флоу: cron только вычисляет объём и ставит jobs (`enqueued_count`), тяжёлая обработка выполняется downstream worker jobs
  - в `docs/14-nfr.md` добавлен раздел `Наблюдаемость cron-задач` (обязательные поля логов, метрики, MVP-алерты)
  - в `PLAN.md` обновлены принципы и карта файлов (явные ссылки на DTO + cron policy)
  - в `ROADMAP.md` уточнены ожидания для WP-003/WP-005 по DTO и cron governance
- **Почему**: Чтобы снизить риски production-инцидентов (дубли, пропуски cron, деградация отладки) и сделать API/сервисные контракты единообразными для команды
- **Затронуто**: PLAN.md, ROADMAP.md, docs/02-architecture.md, docs/03-data-flows.md, docs/14-nfr.md

### CHG-037: Добавлен формальный task-card WP-004 и зафиксирован результат закрытия

- **Было**: отсутствовала карточка `WP-004` с formal Security/QA секциями и evidence
- **Стало**: добавлен `docs/agents/tasks/wp-004.md` со статусом `Done`, заполненными секциями `Security Review (Formal)` и `QA Checklist (Formal)`, command evidence и метриками качества
- **Почему**: для нового workflow обязательно формальное закрытие каждого WP
- **Затронуто**: docs/agents/tasks/wp-004.md

### CHG-038: Добавлен формальный task-card WP-005 и зафиксирован результат закрытия

- **Было**: отсутствовала карточка `WP-005` с formal Security/QA секциями и evidence
- **Стало**: добавлен `docs/agents/tasks/wp-005.md` со статусом `Done`, заполненными секциями `Security Review (Formal)` и `QA Checklist (Formal)`, command evidence и метриками качества
- **Почему**: продолжение обязательного workflow формального закрытия каждого WP
- **Затронуто**: docs/agents/tasks/wp-005.md

## 2026-02-13 — Формализация workflow Security/QA

### CHG-036: Security/QA review сделан обязательным шагом закрытия WP

- **Было**: Security-review и QA-checklist были в DoD, но без жёсткого требования формального заполнения секций с evidence перед переводом WP в `Done`
- **Стало**:
  - В `docs/agents/task-card-template.md` добавлены обязательные секции:
    - `Security Review (Formal)` (scope/checks/findings/decision)
    - `QA Checklist (Formal)` (functional checks/command evidence/decision)
  - В `docs/agents/README.md` закреплено правило:
    - WP нельзя закрыть в `Done` без заполненных формальных секций Security/QA и command evidence (`test`, `typecheck`, `lint`)
  - Для `docs/agents/tasks/wp-003.md` выполнен и зафиксирован формальный PASS по Security и QA
- **Почему**: Сделать поведение единообразным по умолчанию в workflow команды и исключить “неформальное” закрытие WP
- **Затронуто**: docs/agents/task-card-template.md, docs/agents/README.md, docs/agents/tasks/wp-003.md

## 2026-02-11 — Расширение документации (testing, NFR, AI-team)

### CHG-035: Приведение docs/06-edge-cases.md к единому формату

- **Было**: Разные форматы в секциях: code blocks, таблицы, списки, без явной структуры «Проблема / Решение»
- **Стало**: Единый формат: **Проблема:** описание; **Решение:** описание (с примерами кода там, где уместно). Для непокрытых кейсов (6.28–6.30) добавлены примеры SQL/TypeScript
- **Почему**: Лучшая читаемость и сканируемость; единый шаблон для добавления новых edge cases
- **Затронуто**: docs/06-edge-cases.md

### CHG-034: Перенос содержимого docs/16-weak-points.md в docs/06-edge-cases.md

- **Было**: Отдельный файл docs/16-weak-points.md с Domain Events, процессом тестирования, непокрытыми edge-кейсами
- **Стало**: Содержимое перенесено в docs/06-edge-cases.md. Добавлены разделы:
  - 6.26 Domain Events и оркестрация — FAQ, риски, демонстрация
  - 6.27 Процесс тестирования и доработки по edge-кейсам
  - 6.28–6.30 Непокрытые edge-кейсы (W1–W18) **с решениями** для каждого
  - 6.31 Риски выкатки, 6.32 Рекомендации для прототипа, 6.33 Реестр «Обнаруженные в проде»
- **Почему**: Объединение в один файл по edge-кейсам. Добавлены конкретные решения для каждого непокрытого кейса
- **Затронуто**: docs/06-edge-cases.md, docs/16-weak-points.md (удалён), PLAN.md, CLAUDE.md

### CHG-033: Документирование добавления урока во время активного потока

- **Было**: Сценарий «10 уроков на старте → 15 к концу» не описан; неясно, создаётся ли Progress для новых уроков
- **Стало**: Edge case 6.25 — при создании урока Progress автоматически создаётся для всех active Enrollments; примечание в 09-example-student-lifecycle
- **Почему**: Логика уже описана в 10-example-manager-day, но отсутствовала в edge cases и основном сценарии студента
- **Затронуто**: docs/06-edge-cases.md, docs/09-example-student-lifecycle.md

### CHG-032: Исправление Kanban CRM — добавлена колонка «Счёт» (invoice)

- **Было**: Kanban-доска CRM имела 7 колонок (Договор → Оплачено), колонка invoice отсутствовала
- **Стало**: Добавлена колонка «Счёт» между «Договор» и «Оплачено»; этап 2: contract → invoice → converted
- **Почему**: Lead.status включает invoice (счёт выставлен) как отдельный этап B2B-воронки
- **Затронуто**: docs/03-data-flows.md

### CHG-031: Уточнение логики определения чатов: тариф + поток

- **Было**: В онбординге и cron job чаты определялись только из Tier.telegram_chats[]
- **Стало**: Чаты = Tier.telegram_chats[] ∩ (TelegramChat.cohort_id IS NULL OR cohort_id = Enrollment.cohort_id). Тариф задаёт набор; cohort-specific чаты фильтруются по потоку студента
- **Почему**: TelegramChat имеет cohort_id — чат может быть привязан к потоку. Студент потока 15 не должен получать инвайт в чат "КДП Поток 14"
- **Затронуто**: docs/01-domain-model.md, docs/03-data-flows.md, docs/06-edge-cases.md, docs/02-architecture.md, docs/09-example-student-lifecycle.md, docs/05-atomic-operations.md, docs/13-testing.md

### CHG-030: Уточнение разницы между логами и AuditLog

- **Было**: В секции «Что НЕ хранится в БД» использовался термин «Логи» без пояснения, что AuditLog — это не то же самое и хранится в БД
- **Стало**: «Операционные логи» (application logs) — чёткое наименование; добавлено примечание, что AuditLog — журнал аудита и хранится в БД
- **Почему**: Избежать путаницы: операционные логи (Pino) не в БД, AuditLog (журнал действий) — в БД
- **Затронуто**: docs/01-domain-model.md

### CHG-029: Переименование correlation_id → trace_id

- **Было**: В логах и документации использовался термин `correlation_id` для привязки логов к process_id / job_id
- **Стало**: Везде используется `trace_id` — более привычная терминология для трассировки
- **Почему**: trace_id — устоявшийся термин в экосистеме (OpenTelemetry, Jaeger, Datadog)
- **Затронуто**: docs/01-domain-model.md, docs/02-architecture.md, docs/14-nfr.md, PLAN.md, PRESENTATION_TECHNICAL.md, ROADMAP.md

### CHG-028: Добавление docs/13-testing.md, docs/14-nfr.md, docs/15-ai-team.md

- **Было**: Документация не включала стратегию тестирования, нефункциональные требования (масштабирование, наблюдаемость), описание AI-агентов для разработки (Cursor, Claude, вайб-кодинг)
- **Стало**: Добавлены три документа:
  - docs/13-testing.md — стратегия тестирования (Vitest + Playwright), unit/integration/E2E, моки, CI, привязка к атомарным операциям и edge cases
  - docs/14-nfr.md — NFR: масштабируемость (триггеры worker, PostgreSQL), наблюдаемость (Pino, correlation_id, health checks), производительность, доступность, безопасность
  - docs/15-ai-team.md — AI-агенты для разработки (отличие от runtime-агентов docs/08), команда агентов, карта файлов, best practices, MCP-инструменты
- **Почему**: Закрыть пробелы: тестирование модулей и атомарных функций, системный дизайн NFR, best practices для AI-разработки в эпоху вайб-кодинга
- **Затронуто**: docs/13-testing.md (новый), docs/14-nfr.md (новый), docs/15-ai-team.md (новый), PLAN.md (навигация + карта файлов), CLAUDE.md (структура документации)

---

## 2026-02-11 — Аудит синхронизации документации

### CHG-027: Аудит синхронизации всех документов — исправление 12 несоответствий

- **Было**: Накопленные рассинхронизации между файлами после CHG-001..CHG-026:
  - 01-domain-model: Event categories содержали удалённые `deal_created, deal_won, deal_lost`
  - 03-data-flows (3.10): устаревшее имя `Enrollment.access_expires_at`
  - 06-edge-cases (6.5): устаревшее имя `Enrollment.access_expires_at`
  - 05-atomic-operations: неверная статистика (67 оп. вместо 80, 44 функции вместо 48, INT=15 вместо 14, B=3 вместо 4)
  - 08-mcp-cli-agents: MCP Tools маппинги ссылались на несуществующие AT.1 и DB.16, содержали неверные ссылки на атомарные операции (DB.15 вместо DB.5 и т.д.), неверные ссылки на функции менеджера (M.9→M.10, M.10→M.11, M.13→M.16, M.15→M.17, M.18→M.20)
  - 09-example-student-lifecycle: Payment.status "completed" вместо "success", прямая установка User.is_alumni вместо вычисляемого значения
  - 10-example-manager-day: Payment.status "completed" вместо "success"
  - PRESENTATION_TECHNICAL.md: устаревшая статистика (67/44 вместо 80/48)
  - CLAUDE.md: отсутствовал ROADMAP.md в структуре файлов
  - ROADMAP.md WP-002: отсутствовал Contract в списке таблиц
- **Стало**: Все файлы синхронизированы:
  - Event categories: `lead_converted, lead_lost` вместо `deal_*`
  - Имя поля: `support_expires_at` везде
  - Статистика: 80 операций, 48 функций, INT=14, B=4
  - MCP Tools: все маппинги соответствуют 05-atomic-operations.md
  - Payment.status: `success` везде (по 01-domain-model)
  - is_alumni: вычисляемое значение
  - CLAUDE.md: добавлен ROADMAP.md
  - ROADMAP.md: добавлен Contract
- **Почему**: Плановый аудит синхронизации всей документации
- **Затронуто**: docs/01-domain-model.md, docs/03-data-flows.md, docs/05-atomic-operations.md, docs/06-edge-cases.md, docs/07-migration-strategy.md, docs/08-mcp-cli-agents.md, docs/09-example-student-lifecycle.md, docs/10-example-manager-day.md, PRESENTATION_TECHNICAL.md, CLAUDE.md, ROADMAP.md

---

## 2026-02-11 — Доработки по анализу требований (TODO.md)

### CHG-026: Синхронизация презентаций с актуальной архитектурой (v2)

- **Было**: PRESENTATION.md не упоминал: Contract, merge_users, inactive detection, массовые рассылки, заливщик контента, BotHelp, AURA, UTM-аналитику. PRESENTATION_TECHNICAL.md содержал устаревшие данные: JWT вместо better-auth сессий, «двойная запись» AirTable, LMS как внешний сервис, external_payment_id, REST API в описании, 64 операции / 41 функция, неактуальные фазы roadmap
- **Стало**: PRESENTATION.md: Фаза 2 расширена (+7 пунктов), раздел AirTable → «Текущие системы» (AirTable + AURA + BotHelp), путь студента — добавлен контроль вовлечённости, вопросы обновлены. PRESENTATION_TECHNICAL.md: better-auth вместо JWT, однократный импорт AirTable, Contract в финансах, Lead с B2B pipeline и UTM-полями, Payment с provider_payment_id и receipt_url, pg-boss singletonKey, Job с актуальными очередями, фазы roadmap (0/0.5/1/2/3), цифры (67 операций, 44 функции, 12+ интеграций), открытые вопросы обновлены
- **Почему**: Презентации накопили расхождения после CHG-018..CHG-025 (Contract, merge_users, inactive detection, массовые рассылки, заливщик контента, BotHelp, AURA, UTM)
- **Затронуто**: PRESENTATION.md, PRESENTATION_TECHNICAL.md

### CHG-025: Миграция AURA Framework — описание стратегии

- **Было**: docs/07-migration-strategy.md описывал только миграцию из AirTable. AURA не упоминался
- **Стало**: Добавлен раздел «Миграция AURA Framework»: маппинг данных (aura_user → User, aura_subscription → Subscription), два варианта (однократный импорт / периодическая синхронизация), шаги импорта. Рекомендация: вариант B (периодическая sync)
- **Почему**: AURA — отдельное приложение с подписчиками. Без миграции нет единого профиля студента, невозможны кросс-продуктовые бонусы и единый LTV
- **Затронуто**: docs/07-migration-strategy.md, PLAN.md (открытые вопросы)

### CHG-024: Сквозная аналитика лендинг → Lead (UTM + Яндекс Метрика)

- **Было**: `Lead.utm_tags` сохраняет UTM-метки, но нет описания механизма связи лендинг → Lead и интеграции с Яндекс Метрикой
- **Стало**: Описан полный поток: лендинг → UTM → TypeForm hidden fields → Lead. Добавлены поля `Lead.ym_client_id` (Яндекс Метрика \_ym_uid) и `Lead.yclid` (Яндекс Директ click ID) для сквозной аналитики. Описана интеграция с Offline Conversions API Яндекс Метрики
- **Почему**: Без связки лендинг → Lead невозможно посчитать конверсию по рекламным каналам и ROI кампаний
- **Затронуто**: docs/01-domain-model.md (Lead), docs/03-data-flows.md (+3.15), PLAN.md (открытые вопросы)

### CHG-023: Временная интеграция с BotHelp (этап 1)

- **Было**: Нет описания связи BotHelp-пользователя с User/Lead в системе. BotHelp «висит в воздухе»
- **Стало**: Описаны два варианта интеграции: A) webhook из BotHelp (создание/обновление Lead), B) ручной CSV-импорт. Описаны данные для передачи (email, phone, telegram_id, теги)
- **Почему**: На этапе 1 BotHelp продолжает работать для прогрева лидов, нужна связь с CRM
- **Затронуто**: docs/03-data-flows.md (+3.14)

### CHG-022: Массовые email-рассылки (EMAIL.2)

- **Было**: Только транзакционная email-отправка (EMAIL.1 — OTP, уведомления, документы)
- **Стало**: Добавлена операция `EMAIL.2 send_bulk_email` — массовая рассылка через Mailgun с сегментацией (product, cohort, alumni, subscription). Функция менеджера `M.27 Массовая email-рассылка`. Отправка через pg-boss чанками по 100
- **Почему**: Маркетинговые рассылки (новый продукт, анонсы выпускникам) — необходимая функция, отсутствовала в операциях
- **Затронуто**: docs/05-atomic-operations.md (EMAIL.2, M.27)

### CHG-021: Обнаружение неактивных студентов (inactive detection)

- **Было**: Нет механизма отслеживания «студент не заходил N дней»
- **Стало**: Добавлена операция `INT.15 check_inactive_students` — cron job, проверяет активность по Event/Progress. При неактивности > N дней → событие `student.inactive` → TG-уведомление куратору. Порог: 7 дней для курсов, 3 дня для интенсивов (по duration_days)
- **Почему**: Раннее обнаружение = вовремя связаться = удержание студента. Критично для кураторов
- **Затронуто**: docs/05-atomic-operations.md (INT.15), docs/02-architecture.md (Domain Events, Worker), docs/06-edge-cases.md (+6.24)

### CHG-020: Объединение профилей (merge_users)

- **Было**: Дедупликация при импорте из AirTable (docs/07), но нет операции для мёрджа в рантайме
- **Стало**: Добавлена операция `INT.14 merge_users` и функция `M.26 Объединить профили`. Алгоритм: перенос всех FK (Enrollment, Order, Payment, Lead, ChatMembership, TelegramAccount) на primary User, деактивация дубликата (soft delete). Деструктивная операция с подтверждением
- **Почему**: Один человек может покупать под разными email. Без merge — дублированные данные, неполный LTV
- **Затронуто**: docs/05-atomic-operations.md (INT.14, M.26), docs/06-edge-cases.md (+6.23)

### CHG-019: Сущность Contract (договор для B2B)

- **Было**: Есть Invoice (счёт) и Act (акт), но нет Contract (договор) — обязательного документа для B2B
- **Стало**: Добавлена сущность `Contract` [2] — привязка к Company и Order, типы service/framework, статусы (draft → signed → active). Поле `external_doc_id` для интеграции с ЭДО. Операция `DOC.5 generate_contract_pdf`, `DB.36 create_update_contract`, функция `M.25 Подготовить договор B2B`
- **Почему**: B2B = 30-40% выручки, договор — юридическая необходимость. Поле external_doc_id даёт гибкость: генерировать внутри или хранить ссылку на ЭДО
- **Затронуто**: docs/01-domain-model.md (+Contract), docs/03-data-flows.md (3.7), docs/05-atomic-operations.md (DB.36, DOC.5, M.25)

### CHG-018: Заливщик контента перенесён из Phase F в Этап 2

- **Было**: Агент «Заливщик контента» — Phase F (полный автомат через AI-агента)
- **Стало**: Этап 2 — полуавтоматический процесс: webhook из Kinescope → предзаполнение урока (видео, название), менеджер подтверждает и привязывает к модулю/потоку. Полный автомат остаётся как будущая эволюция
- **Почему**: Боль #2 заказчика (ручная заливка лекций) — приоритет «Высокий». Полуавтомат закрывает боль без сложности полного агента
- **Затронуто**: docs/04-modules-priorities.md (+п.32\*), docs/08-mcp-cli-agents.md (фаза F→2), ROADMAP.md (+WP-043)

---

## 2026-02-10 — Синхронизация презентации

### CHG-017: Синхронизация PRESENTATION.md с актуальной архитектурой

- **Было**: Фазы в презентации не соответствовали docs/04: LMS, Telegram, онбординг, дэшборд отсутствовали в Фазе 1; онбординг ошибочно отнесён к Фазе 2; Фаза 2 не упоминала ДЗ, CRM B2B, промокоды, апгрейды/возвраты. Раздел AirTable описывал "двойную запись" (отвергнуто в docs/07). Онбординг описывался как "добавление в чат" вместо онбординг-страницы.
- **Стало**: Фазы соответствуют docs/04-modules-priorities.md. Раздел AirTable описывает однократный импорт (docs/07). Онбординг описывает онбординг-страницу (docs/02). Путь студента: LMS вместо зум-ссылок в онбординге.
- **Почему**: Презентация накопила расхождения после CHG-013..CHG-016 (SoK, better-auth, объединение Lead+Deal, новый ROADMAP).
- **Затронуто**: PRESENTATION.md

---

## 2026-02-10 — better-auth и объединение Lead+Deal

### CHG-016: Объединение Lead и Deal в одну сущность

- **Было**: `Lead` [1] (квалификация) и `Deal` [2] (воронка сделки) — две отдельные таблицы, связь Lead → Deal (1:many)
- **Стало**: Единый `Lead` [1] с расширенными статусами: `new | contacted | qualified | negotiation | proposal | contract | invoice | converted | lost`. Поля из Deal (`tier_id`, `amount`, `close_probability`, `expected_close_date`) перенесены в Lead как nullable.
- **Почему**: При ~3000 студентов/год сценарий "один человек — несколько параллельных сделок" — редкость. Повторная покупка — это уже User. Для B2C основной поток: Lead → Order напрямую (без Deal). Для B2B: расширенные статусы Lead покрывают воронку сделки. Принцип проекта: меньше сущностей. При необходимости Deal можно выделить обратно.
- **Удалённые операции**: DB.16 create_update_deal
- **Обновлённые функции**: M.14 (CRM/Deals → CRM/Leads pipeline), M.2 (расширение)
- **Затронуто**: 01-domain-model, 03-data-flows (3.6), 05-atomic-operations (DB.16, M.14), 06-edge-cases, ROADMAP.md

### CHG-015: Аутентификация через better-auth (вместо самописного OTP + JWT)

- **Было**: Самописная OTP-авторизация: таблица `OtpCode`, ручная генерация/проверка кодов, JWT (1ч access + 30д refresh, stateless), ручной rate limiting
- **Стало**: Библиотека [better-auth](https://www.better-auth.com/) с плагинами:
  - **Email OTP** — вход по email + 6-значный код (без паролей), управление TTL/attempts/rate limiting из коробки
  - **Admin** — роли (`role` поле в User), бан, импersonation
  - **Bearer** — API-аутентификация токеном (для ботов/агентов)
  - 4 таблицы better-auth: `user` (расширяется кастомными полями), `session`, `account`, `verification`
  - Сессии хранятся в БД (не stateless JWT) — можно отзывать, аудитировать, имперсонировать
- **Почему**: Не изобретать велосипед для auth. better-auth: Prisma adapter, Next.js integration, OTP из коробки, RBAC, session management. Экономия ~3-4 дней разработки Auth + меньше surface area для ошибок безопасности.
- **Удалённые сущности**: `OtpCode` (заменена `Verification` от better-auth)
- **Удалённые операции**: DB.31 create_otp_code, DB.32 verify_otp_code
- **Новые сущности**: `Session`, `Account`, `Verification` (управляются better-auth)
- **Изменён User**: добавлены поля better-auth (`emailVerified`, `image`, `banned`, `banReason`, `banExpires`), `id` теперь string
- **Затронуто**: 01-domain-model, 02-architecture, 05-atomic-operations, 06-edge-cases (6.3, 6.4), PLAN.md, ROADMAP.md

---

## 2026-02-10 — LMS-модуль и обновление презентаций

### CHG-014: Добавлен docs/12-lms-module.md и обновлены презентации

- **Было**: Информация о LMS разбросана по 01-domain-model, 03-data-flows, 05-atomic-operations. Презентации не учитывали SoK и LessonRevision. PRESENTATION_TECHNICAL.md путала Lesson (урок LMS) с Schedule (занятие-воркшоп).
- **Стало**:
  - `docs/12-lms-module.md` — консолидированное описание LMS: сущности, процессы, UX для менеджера (контент-админка, SoK), студента (навигация, прогресс, ДЗ) и куратора (дэшборд прогресса)
  - PRESENTATION.md — добавлено обновление материалов (SoK в нетехнических терминах) + контроль версий в фазе 2
  - PRESENTATION_TECHNICAL.md — секция "LMS и контент" (Module, Lesson, LessonRevision, CohortContent, Progress), секция 4.6 Source of Knowledge, разделены Lesson и Schedule, обновлены цифры (64 операции, 41 функция)
- **Почему**: Консолидация для удобства реализации LMS-модуля. Исправление ошибки в презентации (Lesson ≠ Schedule).
- **Затронуто**: +docs/12-lms-module.md, PRESENTATION.md, PRESENTATION_TECHNICAL.md, PLAN.md (+12), CLAUDE.md

---

## 2026-02-10 — Source of Knowledge (версионирование контента)

### CHG-013: Source of Knowledge — версионирование контента LMS

- **Было**: `Lesson.content` и `Lesson.video_url` — единственная версия без истории. Все потоки видят одни и те же данные. Изменение менеджером немедленно видно всем, включая завершённые потоки.
- **Стало**: SoK ("git для контента"):
  - `Lesson` хранит только метаданные + `current_revision_id` (указатель на SoK)
  - `LessonRevision` [1] — хранит контент (content, video_url, duration_minutes), история ревизий (append-only)
  - `CohortContent` [2] — снимок контента для потока (fork SoK при создании потока)
  - Auto-sync: pg-boss cron обновляет eligible потоки (active + valid support_expires_at)
  - Ручной sync / откат на предыдущую ревизию для любого потока
- **Почему**: Контроль над тем, какой контент видят студенты разных потоков. История изменений. Возможность выборочного обновления. Защита завершённых потоков от непреднамеренных изменений.
- **Новые операции**: DB.33 create_lesson_revision [1], DB.34 fork_cohort_content [2], DB.35 sync_cohort_content [2]
- **Новые функции менеджера**: M.23 sync контента потока [2], M.24 откат контента потока [2]
- **Затронуто**: 01-domain-model (Lesson, +LessonRevision, +CohortContent), 03-data-flows (+3.13), 04-modules-priorities (+5, +23), 05-atomic-operations (+DB.33-35, +M.23-24), PLAN.md (+11), +docs/11-content-versioning.md

---

## 2026-02-10 — Ревизия доменной модели (v2)

### CHG-001: Удалено поле `is_alumni` из таблицы User

- **Было**: `User.is_alumni` (boolean) — устанавливалось вручную при завершении курса (INT.12)
- **Стало**: Вычисляемое значение через запрос `EXISTS (Enrollment WHERE user_id = ? AND status = 'completed')`
- **Почему**: Хранимое поле создаёт риск рассинхронизации. При ~3000 студентов/год запрос с EXISTS по индексированному `(user_id, status)` выполняется за микросекунды. Убираем атомарную операцию INT.12 и необходимость синхронизации.
- **Затронуто**: 01-domain-model, 03-data-flows (offboarding), 05-atomic-operations (INT.12), 06-edge-cases (6.22)

### CHG-002: Удалена роль `company` из User.role

- **Было**: `User.role: admin | manager | curator | student | company` (5 ролей)
- **Стало**: `User.role: admin | manager | curator | student` (4 роли)
- **Почему**: `company` — не роль пользователя, а отношение к юрлицу. Представитель компании (HR) может не быть студентом, а студент может стать представителем компании. Смешение ролей и отношений создаёт путаницу и ограничивает гибкость.
- **Как теперь**: Доступ к B2B-кабинету определяется наличием связи `Company.contact_person_id = user.id`. tRPC middleware `requireCompanyAccess()` проверяет эту связь, а не роль.
- **Затронуто**: 01-domain-model, 02-architecture, 05-atomic-operations, 06-edge-cases (RBAC), PLAN.md, PRESENTATION_TECHNICAL.md

### CHG-003: Расширена модель Company.contact_person

- **Было**: `Company.contact_person_id` → User с ролью `company`
- **Стало**: `Company.contact_person_id` → User с любой ролью (admin, manager, curator, student)
- **Почему**: Контактное лицо компании (HR, руководитель) может не проходить обучение. Если позже решит стать студентом — не нужно менять роль. Связь с компанией и роль в системе — ортогональные понятия.
- **Будущее**: Таблица `CompanyMember` (Phase F) для нескольких представителей одной компании.
- **Затронуто**: 01-domain-model, 06-edge-cases (RBAC)

### CHG-004: Объединены типы `course` и `intensive` в Product

- **Было**: `Product.type: course | intensive | subscription`
- **Стало**: `Product.type: course | subscription`
- **Почему**: Единственное отличие course от intensive — длительность, которая уже выражена через `duration_days` (см. CHG-010). Subscription принципиально отличается (рекуррентный биллинг). Меньше типов — стабильнее система, проще понимание.
- **Затронуто**: 01-domain-model, PLAN.md, PRESENTATION_TECHNICAL.md

### CHG-005: Добавлена валюта к price_snapshot в Enrollment

- **Было**: `Enrollment.price_snapshot` (число, без валюты)
- **Стало**: `Enrollment.price_snapshot` (число) + `Enrollment.price_snapshot_currency` (строка, default "RUB")
- **Почему**: При наличии `Tier.price_usd` и `Order.currency` Enrollment должен знать, в какой валюте зафиксирована цена. Без этого невозможно корректно рассчитать доплату при апгрейде или возврат для валютных платежей.
- **Затронуто**: 01-domain-model, 06-edge-cases (6.6, 6.20)

### CHG-006: Переименованы поля expires_at в Enrollment для ясности

- **Было**: `access_expires_at` и `curator_access_expires_at`
- **Стало**: `materials_access_expires_at` и `support_expires_at`
- **Почему**: Исходные имена не объясняли разницу. Новые имена явно выражают: `materials_access_expires_at` — доступ к записям и материалам курса (null = вечный), `support_expires_at` — доступ к куратору и обновлениям (1 год). После истечения support студент сохраняет доступ к записям своего потока.
- **Затронуто**: 01-domain-model, 06-edge-cases (6.8)

### CHG-007: Добавлено пояснение о связи Progress/HomeworkSubmission со студентом

- **Было**: Неявная связь через `enrollment_id`
- **Стало**: То же (enrollment_id), но добавлен пояснительный комментарий
- **Почему**: Дизайн корректный — прогресс привязан к зачислению (студент + поток), а не к студенту напрямую. Один студент может проходить курс дважды в разных потоках. Добавлен комментарий для ясности.
- **Затронуто**: 01-domain-model

### CHG-008: HTTP 202 Accepted для асинхронных операций

- **Было**: Неопределённый HTTP-код при постановке задач в очередь
- **Стало**: Явное правило: `200 OK` для синхронных операций и webhook acknowledgment, `202 Accepted` для операций, ставящих задачу в очередь (возвращают `process_id`)
- **Почему**: Семантически корректный HTTP: 202 означает "запрос принят, но обработка ещё не завершена". Клиент понимает, что нужно следить за статусом через `GET /api/processes/:id`.
- **Затронуто**: 02-architecture, 03-data-flows, PRESENTATION_TECHNICAL.md

### CHG-010: Переименовано `duration_weeks` → `duration_days` в Product

- **Было**: `Product.duration_weeks` (integer, длительность в неделях)
- **Стало**: `Product.duration_days` (integer, длительность в днях)
- **Почему**: Не все продукты измеряются в неделях — интенсив может длиться 3 дня, а курс 2 месяца. Дни — универсальная единица, удобная для сортировки и фильтрации. Отображение ("6 недель", "3 дня") — задача UI.
- **Затронуто**: 01-domain-model, PRESENTATION_TECHNICAL.md

### CHG-011: B2B-дэшборд обучения сотрудников (Phase F)

- **Было**: Контактное лицо компании видит только счета и список сотрудников
- **Стало**: Добавлена фича (Phase F): контактное лицо может отслеживать прогресс, посещаемость и динамику обучения сотрудников — даже не являясь студентом
- **Почему**: Бизнес-ценность для B2B-клиентов — HR/руководитель хочет видеть ROI обучения. Усиливает отделение роли от связи с компанией (CHG-002).
- **Затронуто**: 01-domain-model, 05-atomic-operations (B.4)

### CHG-012: Добавлено поле `receipt_url` в Payment (фискальный чек, 54-ФЗ)

- **Было**: Payment не хранил ссылку на фискальный чек
- **Стало**: `Payment.receipt_url` (nullable) — ссылка на онлайн-чек (ОФД)
- **Почему**: По 54-ФЗ РФ при онлайн-оплате обязателен фискальный чек. Ссылка приходит в webhook от ЮKassa/Т-Банк. Хранение позволяет: переотправить чек клиенту, использовать в бухгалтерском учёте, пройти аудит.
- **Затронуто**: 01-domain-model

### CHG-009: Обновлены презентации

- **Было**: PRESENTATION.md и PRESENTATION_TECHNICAL.md содержали устаревшие данные (5 ролей, Redis, REST vs tRPC как открытый вопрос, и т.д.)
- **Стало**: Синхронизированы с актуальной архитектурой (4 роли, без Redis, tRPC как выбранное решение, pg-boss, OTP, 202 Accepted)
- **Затронуто**: PRESENTATION.md, PRESENTATION_TECHNICAL.md

---

## 2026-02-10 — Базовые архитектурные решения (v1)

Решения, принятые при первичном проектировании (override PRD заказчика):

| ID       | Было (PRD)                      | Стало                       | Обоснование                                                        |
| -------- | ------------------------------- | --------------------------- | ------------------------------------------------------------------ |
| BASE-001 | Drizzle ORM                     | Prisma ORM                  | Зрелая экосистема, лучшая документация, AI-ассистенты хорошо знают |
| BASE-002 | BullMQ + Redis                  | pg-boss (PostgreSQL)        | Одна точка отказа, ACID-транзакции, достаточная производительность |
| BASE-003 | Redis для кэша/сессий           | Без Redis                   | JWT + OTP в PostgreSQL, 15 активных пользователей, кэш не нужен    |
| BASE-004 | Несколько workers               | 1 worker                    | ~3000 студентов/год, масштабирование — второй экземпляр            |
| BASE-005 | TraceLog в БД                   | Pino (stdout)               | Структурированные логи, не засоряют БД, легко агрегировать         |
| BASE-006 | ProcessStep (отдельная таблица) | JSON-массив steps в Process | Проще, нет лишних JOIN, достаточно для текущего масштаба           |
