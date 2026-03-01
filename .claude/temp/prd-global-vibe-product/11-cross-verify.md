# Кросс-верификация: аудит согласованности продуктового пакета LaunchPilot v2

Дата: 2026-03-01
Аудитор: Agent 6 (скептик и аудитор)

---

## Проверка 1: PRD <-> Аналитика

### 1.1. Core Jobs из PRD покрыты событиями аналитики?

| Core Job из PRD | Покрытие в аналитике | Статус |
|---|---|---|
| CJ1: "Понять, что строить" (AI Interview + Segments) | `flow_step_completed` (step 1, 2), `idea_summary_generated`, `segments_jobs_generated` | Покрыто |
| CJ2: "Провалидировать идею" (Risk Assessment) | `risk_assessment_generated`, verdict property | Покрыто |
| CJ3: "Получить чёткое ТЗ" (Document Generation) | `prd_generated`, `landing_copy_generated`, `analytics_plan_generated`, `document_copied`, `document_downloaded` | Покрыто |
| CJ4: "Научиться ставить задачу AI" (Vibe-Coding) | `vibe_coding_plan_generated`, `checklist_item_completed` | Частично покрыто |
| CJ5: "Освоить product thinking" (Education) | `learning_block_expanded`, `knowledge_base_article_viewed` | Покрыто |

**РАЗРЫВ: CJ4 покрыт неполностью.** PRD описывает FR-4.1 (рекомендация инструмента), FR-4.2 (микро-гайды по установке), FR-4.3 (prompt engineering), FR-4.4 (чеклист "Первый результат"). В аналитике есть `vibe_coding_plan_generated` и `checklist_item_completed`, но нет события для трекинга прохождения конкретных микро-гайдов по установке (FR-4.2). Пользователь может получить план, но мы не знаем, дошёл ли он до установки инструмента и запуска первого промпта.

### 1.2. Aha-момент: PRD vs Аналитика

PRD (раздел 4, таблица Aha-моментов по сегментам):
- **Founders:** "Пользователь видит сырую идею превращённой в структурированный PRD с сегментами, jobs, рисками" -- "конец AI-интервью (шаг 2 из guided flow)"
- **Solopreneurs:** "Чёткий вердикт 'стоит ли тратить время' с обоснованием по рискам" -- "шаг 3 (Risk Assessment)"
- **AI-Curious Professionals:** "Применяет AJTBD к реальной задаче и получает инсайт" -- "шаг 2 (сегментация и jobs)"

Аналитика: Единый `aha_moment_reached` фиксируется при генерации Segments & Jobs документа на шаге 2 для ВСЕХ сегментов.

**РАЗРЫВ:** PRD явно описывает, что для Solopreneurs настоящий Aha-момент наступает на шаге 3 (Risk Assessment), а не на шаге 2. Но аналитика фиксирует единый `aha_moment_reached` на шаге 2 для всех. Это значит, что для Solopreneurs мы будем измерять ложный Aha-момент, и все производные метрики (time to Aha, aha -> paywall conversion) будут искажены для этого сегмента.

### 1.3. Метрики успеха из PRD трекаются в аналитике?

| Метрика из PRD (раздел 8) | Событие в аналитике | Статус |
|---|---|---|
| North Star: Documents Generated per Week | `flow_completed` + document generation events | Покрыто |
| Sign-up to Flow Start Rate >80% | `signup_completed` -> `flow_started` | Покрыто |
| Guided Flow Completion Rate >40% | `flow_started` -> `flow_completed` | Покрыто |
| Time to Aha <25 мин | `aha_moment_reached.time_since_signup_sec` | Покрыто |
| Time to Full Document Set <60 мин | `flow_completed.total_duration_sec` | Покрыто |
| Step-by-step Drop-off Rate <20% | `flow_step_started` -> `flow_step_completed` | Покрыто |
| D7 Return Rate >25% | `session_started` + `days_since_last_session` | Покрыто |
| D30 Return Rate >15% | `session_started` + когортный анализ | Покрыто |
| Projects per User >1.3 | `project_created.project_number` | Покрыто |
| PRD Iteration Rate >20% | `prd_iteration_started` | Покрыто |
| Free-to-Paid >5% | `signup_completed` -> `purchase_completed` | Покрыто |
| MRR >$5K к 3 мес | Вычисляется из revenue events | Частично (нет серверного расчёта MRR) |
| ARPU $29-49 | `purchase_completed.price` по когортам | Покрыто |
| Churn Rate <8%/мес | `subscription_cancelled` | Покрыто |
| Payback Period <2 мес | LTV / CAC | Частично (CAC не в PostHog) |
| **NPS >40** | Нет события | **НЕ ПОКРЫТО** |
| **CSAT per step >4.0/5.0** | Нет события | **НЕ ПОКРЫТО** |
| **PMF survey ("very disappointed") >40%** | Нет события | **НЕ ПОКРЫТО** |
| **Document Quality Score >7/10** | Нет события | **НЕ ПОКРЫТО** |
| Knowledge Base Sessions >2/мес | `knowledge_base_article_viewed` | Покрыто |

**РАЗРЫВ:** 4 ключевых метрики качества (NPS, CSAT, PMF survey, Document Quality Score) не имеют соответствующих событий в аналитическом плане. Это метрики, которые PRD явно называет критически важными для оценки product-market fit. Команда будет "летать вслепую" по самым важным качественным сигналам.

### 1.4. Воронка покрывает полный путь пользователя?

Воронка в аналитике (AARRR): Acquisition -> Activation (Aha) -> Revenue -> Retention -> Referral. Покрывает полный путь от лендинга до referral.

**Замечание:** Воронка не покрывает путь ПОСЛЕ продукта: PRD описывает чеклист "Next Steps" (FR-7.2) с конкретными действиями (экспертные интервью, лендинг-тест, сбор фидбека). В аналитике есть `checklist_item_completed`, но нет трекинга результатов этих действий (например, "пользователь вернулся с фидбеком" vs "пользователь просто отметил пункт"). Это делает retention-метрики поверхностными.

---

## Проверка 2: Сегменты <-> Лендинг

### 2.1. Все сегменты представлены в лендинге?

| Сегмент из 03-chosen-segments | Представлен в блоке "Sound familiar?" | Статус |
|---|---|---|
| Сегмент 1: Non-Technical Founders (0->1) | Да -- "I have a business idea that won't leave me alone." | Совпадает |
| Сегмент 2: Solopreneurs / Side-Hustlers | Да -- "I have 5-10 hours a week. I can't afford to waste them." | Совпадает |
| Сегмент 3: AI-Curious Professionals | Да -- "AI is changing everything. I need to keep up." | Совпадает |

**Статус: Полное покрытие.** Все 3 сегмента из 03-chosen-segments (где Сегмент 3 объединяет Career Builders + AI Future-Proofers + Builders в организации из v1) корректно представлены.

### 2.2. Jobs из сегментов корректно отражены в лендинге?

| Core Job из 03-chosen-segments | Отражение в лендинге | Статус |
|---|---|---|
| Founders: "понять, что именно строить и в каком порядке" | Блок 6: "you don't know what to build first" | Совпадает |
| Founders: "провалидировать идею до разработки, чтобы не выбросить $5-20K" | Блок 6: "You don't know if the idea is good enough to invest $5,000-$20,000" | Совпадает |
| Founders: "иметь чёткое ТЗ (PRD)" | Блок 3 (Micro Job 4): "PRD that AI coding tools actually understand" | Совпадает |
| Solopreneurs: "быстро понять, стоит ли идея моего времени" | Блок 6: "fast way to figure out: Is this idea worth my evenings?" | Совпадает |
| Solopreneurs: "пошаговый план с микро-гайдами" | Блок 6: отсутствует в секции сегмента | **Упущено в блоке "Sound familiar?"** |
| Solopreneurs: "научиться правильно ставить задачу AI" | Блок 6: "started with code, not with thinking" | Косвенно |
| AI-Curious: "научиться создавать продукты с AI" | Блок 6: "practical framework" + "hands-on AI tool skills" | Совпадает |
| AI-Curious: "framework для product thinking" | Блок 6: "understand product thinking (JTBD, risk assessment, MVP scoping)" | Совпадает |
| AI-Curious: "практический опыт, кейс в портфолио" | Блок 6: "a case for your portfolio" | Совпадает |

**Замечание:** Для Solopreneurs core job "пошаговый план с микро-гайдами, чтобы не тратить время на поиск информации" не отражена явно в блоке "Sound familiar?". Вместо этого акцент на проблеме ("started with code, not with thinking"), а не на решении ("дай мне конкретный план на 5-8 часов"). Эта job покрыта в других блоках лендинга (Блок 3, Micro Job 6; Блок 7), но не в точке "узнаёшь себя", где человек принимает решение "это для меня".

### 2.3. Противоречия с анализом конкурентов?

**ЗАМЕЧАНИЕ:** Лендинг (Блок 4, Aha-момент) сравнивает LaunchPilot с "ChatGPT" (generic AI), но не с ChatPRD (ближайший конкурент в категории PRD-генерации, 100,000+ PM-ов). Конкурентный анализ показывает, что ChatPRD тоже предоставляет "AI-коучинг уровня CPO" и "выявление стратегических пробелов". Сравнение только с ChatGPT создаёт ложное чувство уникальности. Пользователь, знакомый с ChatPRD, не увидит на лендинге ответа "чем вы лучше ChatPRD за $15/мес".

**ЗАМЕЧАНИЕ:** Лендинг (Блок 10) утверждает про PRD-генераторы: "They don't teach you WHY the PRD looks this way." Конкурентный анализ фиксирует, что ChatPRD имеет "AI-коучинг: ревью документов уровня CPO -- выявление стратегических пробелов, проверка предположений" и "inline-подсказки и оценка качества документа". Это частично учит "WHY". Лендинг преувеличивает разрыв. Более честная формулировка: "They coach PMs on specific documents. We teach founders to THINK about products from scratch."

### 2.4. Критерии успеха из сегментов vs лендинг

| Критерий из 03-chosen-segments | В лендинге | Статус |
|---|---|---|
| Founders: "Прототип за <1 неделю после документов" | Micro Job 6: "Estimated time to prototype: 2-4 hours" | **Противоречие** |
| Founders: "Готовые документы для Cursor/Claude Code/Lovable" | Блок 3: "Production-ready PRD in Markdown" | Совпадает |
| Solopreneurs: "За 2-3 вечера (5-8 часов) понял стоит ли" | Блок 6: "LaunchPilot gives you the answer in 2-3 evenings" | Совпадает |
| Solopreneurs: "MVP за 2-3 недели вечерней работы" | Нет в лендинге | **Упущено** |
| AI-Curious: "Кейс в портфолио" | Блок 6: "a case for your portfolio" | Совпадает |
| AI-Curious: "Настроенный Cursor/Claude Code" | Блок 7, Step 5 | Совпадает |

**РАЗРЫВ по таймингу прототипа:** Сегмент Founders: "Прототип за <1 неделю после документов". Лендинг: "Estimated time to prototype: 2-4 hours". Лендинг обещает в 10-40 раз быстрее, чем заявлено в критериях сегмента. LaunchPilot НЕ генерирует код -- пользователь делает прототип сам через Cursor/Lovable. 2-4 часа -- крайне агрессивная оценка для нетехнического человека, который впервые работает с AI-кодинг инструментом. Если реальный опыт ближе к "1 неделе", пользователь разочаруется.

---

## Проверка 3: Конкуренты <-> PRD <-> Лендинг

### 3.1. Функциональный паритет с конкурентами

| Критическая фича конкурента | Конкурент | Покрыта в PRD? | Статус |
|---|---|---|---|
| AI-генерация PRD | ChatPRD ($15/мес), PRDGPT ($5/мес) | FR-1.3 | Покрыто |
| AI-коучинг / обратная связь на документы | ChatPRD | FR-5.1 (контекстное обучение) | Покрыто (другой подход) |
| Валидация бизнес-идеи | IdeaProof, DimeADozen | FR-2.1 (Risk Assessment) | Покрыто |
| JTBD-анализ | LeanPivot | FR-1.2 (AJTBD-based) | Покрыто |
| Интеграции с кодинг-инструментами (Linear, Notion, Slack) | ChatPRD | Исключено из MVP | Roadmap (месяц 4) |
| Revenue-моделирование / финансовые прогнозы | IdeaProof | Нет | **Разрыв** |
| Lean Canvas Generator | LeanPivot, LEANSpark | Нет | **Разрыв** |
| Бесплатные калькуляторы (ROI, LTV, CAC) | IdeaProof | Нет (Unit Economics Calculator -- roadmap, месяц 3) | **Разрыв** |
| Обучение вайбкодингу привязанное к задаче | Никто (наше УТП) | FR-4.1 -- FR-4.4 | Покрыто |
| VIBE Coding Tool | LeanPivot (один инструмент) | FR-4.1 -- FR-4.4 (5 инструментов) | Превосходство |
| Gamification | LeanPivot | Нет | Осознанный trade-off |
| Голосовые консультации | ValidatorAI | Исключено из MVP | Осознанный trade-off |

**РАЗРЫВ: Юнит-экономический калькулятор.** Бизнес-контекст (01-business-context) перечисляет "Страховка от ошибок: экономит $5-20K+" как один из 4 слоёв ценности. FR-5.1 обещает обучение юнит-экономике (LTV, CAC, ARPU). Но в PRD нет инструмента для расчёта -- только теория. IdeaProof конкурент даёт бесплатные калькуляторы ROI/LTV/CAC. Это слабое место: пользователь узнаёт про юнит-экономику из обучающих блоков, но не может посчитать для своего продукта.

### 3.2. Заявленные преимущества лендинга обеспечены PRD?

| Заявление на лендинге | Обеспечение в PRD | Статус |
|---|---|---|
| "in under 60 minutes" (One-liner) | FR-6.1: "Общее время: 30-60 минут" | Совпадает |
| "investor-ready documents" (One-liner) | PRD не содержит требований к "investor-ready" формату. Нет pitch deck, executive summary, финмоделей. Раздел 9 PRD явно исключает "Генерация бизнес-плана / финмодели" | **Ложное обещание** |
| "methodology tested on 11,000+ graduates" | Бизнес-контекст: ProductHowTo -- 11000+ выпускников | Покрыто, но методология AJTBD, а не AI-гайд |
| "6 documents" (Summary table, Блок 7) | PRD перечисляет: Idea Summary, Segments & Jobs, Risk Assessment + Validation Plan, PRD, Vibe-Coding Plan + бонусы: Landing Copy, Analytics Plan, Competitor Analysis | Фактически 8 документов, лендинг говорит "6" |
| "$500+ product consultant" за 5 минут | FR-1.2: генерация сегментов | Количественно покрыто, качественно сравнение спорно |
| "$2,000-5,000 agency" за бонусные документы | FR-3.1, FR-3.2 | Сильное преувеличение: AI-генерация != работа агентства |
| "$400/year bootcamp" за Vibe-Coding Plan | FR-4.1 -- FR-4.4 | Корректное сравнение |

**КРИТИЧЕСКИЙ РАЗРЫВ:** One-liner лендинга обещает "investor-ready documents". PRD явно исключает из scope "Генерация бизнес-плана / финмодели" и отличает себя от PitchBob (раздел 9). Документы PRD + Risk Assessment + Landing Copy НЕ являются "investor-ready" -- для этого нужен pitch deck, финмодель, executive summary. Это привлечёт founders, ожидающих fundraising-материалы, и вызовет разочарование.

**ЗАМЕЧАНИЕ по "6 документам":** Лендинг (Блок 7, Summary) обещает "6 documents", но фактически PRD генерирует 8 (Idea Summary, Segments & Jobs, Risk Assessment, Validation Plan, PRD, Vibe-Coding Plan + бонусы Landing Copy, Analytics Plan, Competitor Analysis). Лучше обещать меньше и давать больше -- но несовпадение чисел может запутать.

### 3.3. "Увольнение конкурентов" опирается на реальные слабости?

| Конкурент в лендинге (Блок 10) | Заявленная слабость | Подтверждение из анализа | Статус |
|---|---|---|---|
| ChatGPT/Claude | "No methodology, no structured interview" | Подтверждено: ChatGPT -- generic | Валидно |
| Courses (Buildcamp, Scrimba, Product School) | "20-40 hours, generic examples" | Подтверждено: Buildcamp -- чистое обучение кодингу, 4-6 часов/неделю на 4-6 недель | Валидно |
| ChatPRD/PRDGPT | "Built for PMs in companies, not for founders" | Подтверждено: ChatPRD ориентирован на PM-ов | Валидно |
| DimeADozen/IdeaProof | "One-time snapshot, no teaching" | Подтверждено: одноразовые отчёты | Валидно |
| Lovable/Cursor | "Tool is only as good as the input" | Подтверждено: нет обучения, нет гайденса | Валидно |

**Статус: "Увольнение конкурентов" обосновано корректно.** Каждое утверждение подтверждается данными конкурентного анализа.

---

## Проверка 4: Риски <-> PRD <-> Аналитика

### 4.1. Все риски учтены в PRD?

| Риск из 05-chosen-risks | Учтён в PRD (раздел 7)? | Как именно? |
|---|---|---|
| #1: ChatGPT как конкурент (Score 10.0) | Да | FR-1.2 (AJTBD), FR-6.1 (guided flow), FR-6.2 (anti-stuck), FR-3.3 (workspace) |
| #2: Рынок фрагментирован (9.0) | Да | FR-6.4 (адаптивный flow), FR-5.2 (Knowledge Base как SEO) |
| #3: Micro-guides устаревают (8.0) | Да | FR-4.2 (модульный контент), фокус на принципах |
| #4: WTP за подписку (6.0) | Да | Aha до paywall, fallback на разовые покупки |
| #5: Методология не переносима (6.0) | Да | FR-5.1 (контекстные объяснения), FR-6.1 (guided flow) |
| #6: Completion rate (5.3) | Да | FR-6.1 (короткий flow), FR-6.2 (anti-stuck), FR-6.3 (milestones) |
| #7: Retention (5.3) | Да | FR-7.1-7.4 (множественные проекты, PRD-итерация, email-nudges) |
| #8: Качество AI-guided experience (5.0) | Да | FR-1.2 (методология как "рельсы"), FR-1.1 (adaptive questions) |
| #9: Каналы привлечения (4.5) | Да | FR-5.2 (Knowledge Base как SEO), free tier как acquisition |

**Статус: Все 9 рисков учтены в PRD.** Это одна из сильнейших сторон пакета. Каждый риск имеет конкретные FR и метрику валидации.

### 4.2. Аналитические события для раннего обнаружения рисков

| Риск | Событие-индикатор в аналитике | Покрытие |
|---|---|---|
| #1: ChatGPT как конкурент | `subscription_cancelled.reason`, `flow_abandoned` | Частично (нет exit survey "why not") |
| #2: Рынок фрагментирован | `signup_completed.utm_source` + `flow_completed` по сегментам | Покрыто |
| #3: Micro-guides устаревают | Нет события "шаг гайда не сработал" | **НЕ ПОКРЫТО** |
| #4: WTP за подписку | `paywall_viewed` -> `purchase_completed` conversion | Покрыто |
| #5: Методология не переносима | Нет прямого события для качества обучения | **НЕ ПОКРЫТО** |
| #6: Completion rate | `flow_started` -> `flow_completed`, `flow_abandoned` | Покрыто |
| #7: Retention | `session_started`, D7/D30 return, `prd_iteration_started` | Покрыто |
| #8: Качество AI experience | Нет CSAT/NPS события | **НЕ ПОКРЫТО** |
| #9: Каналы привлечения | UTM-параметры, `signup_completed` по каналам | Покрыто (CAC вне PostHog) |

**РАЗРЫВ:** 3 из 9 рисков не имеют аналитических событий для раннего обнаружения:
- **Риск #3** (micro-guides устаревают): PRD предусматривает "step failed rate <10%", но в аналитике нет события `micro_guide_step_failed` или обратной связи по актуальности.
- **Риск #5** (методология не переносима): Нет NPS/CSAT для оценки качества обучения. PRD ставит цель "NPS >40", но сбор не описан.
- **Риск #8** (качество AI experience): PRD требует "CSAT >4.0/5.0 на каждом шаге", но аналитика не содержит события сбора CSAT.

### 4.3. Маркетинговые гипотезы учитывают риски?

| Риск | Адресован в маркетинге? | Где |
|---|---|---|
| #1: ChatGPT как конкурент | Да | Лендинг Блок 9 (Страх 4), Блок 10 (увольнение ChatGPT) |
| #4: WTP за подписку | Да | Лендинг Блок 9 (Страх 6 -- "$29/month subscription") |
| #6: Completion rate | Частично | Лендинг Блок 7 (показывает простоту 5 шагов) |
| #3: Micro-guides устаревают | Нет | Не адресован |
| #7: Retention | Нет | Лендинг не объясняет, зачем возвращаться |
| #8: Качество AI | Частично | "methodology from 11,000+ graduates" -- но нет реальных testimonials |

**Не адресованные риски в маркетинге:**
- Риск #7 (retention): лендинг не объясняет, зачем возвращаться после первого flow. Нет блока "Here's why you'll come back".
- Маркетинговые гипотезы (Часть 2, 10-landing-copy) полностью сфокусированы на acquisition. Нет ни одной retention-маркетинговой гипотезы (re-engagement campaigns, win-back emails).

---

## Проверка 5: Revenue-события <-> Бизнес-модель

### 5.1. Монетизация из бизнес-контекста отражена в revenue events

Бизнес-контекст (01-business-context): Freemium -> paid. $0 / $29 / $49.

Аналитика: `paywall_viewed`, `plan_selected` (plan: "pro" | "builder"), `purchase_completed` (plan, price, currency, billing_period), `subscription_renewed`, `subscription_cancelled`, `upgrade_completed`, `downgrade_completed`, `refund_requested`.

**Статус: Полное покрытие.** Вся цепочка от показа paywall до отмены подписки трекается.

### 5.2. Ключевые метрики для юнит-экономики

| Метрика юнит-экономики | Трекается? | Как? |
|---|---|---|
| LTV | Да | `subscription_renewed.lifetime_revenue` + `subscription_cancelled.lifetime_revenue` |
| CAC | Частично | UTM-параметры в PostHog, стоимость привлечения -- в рекламных кабинетах |
| ARPU | Да | `purchase_completed.price` по когортам |
| Churn Rate | Да | `subscription_cancelled` / active subscriptions |
| Payback Period | Вычисляется | LTV / CAC |
| MRR | Частично | Нет серверного события `mrr_snapshot` |

**РАЗРЫВ:** PRD ставит цель "MRR >$5K к 3 мес" (раздел 8, Монетизация), но аналитический план не описывает, как считать MRR в PostHog. Нет серверного расчёта или интеграции с billing-системой. Рекомендация: добавить серверное событие `mrr_snapshot` (mrr, new_mrr, churned_mrr, expansion_mrr) или интеграцию со Stripe Dashboard.

### 5.3. Cross-sell / upsell механики

PRD описывает 4 upsell-триггера:
1. Попытка создать 3-й проект (лимит free tier)
2. Попытка экспорта в PDF
3. Попытка итерации PRD (>1 итерации)
4. Исчерпание AI-запросов

Аналитика: `paywall_viewed.trigger` покрывает все 4 триггера ("project_limit" | "export_limit" | "iteration_limit" | "ai_limit"). `ai_limit_reached` отдельно трекает исчерпание лимитов.

**Статус: Покрыто.**

**ЗАМЕЧАНИЕ:** PRD (Приложение A) упоминает fallback "Project Pack: $19-29 за один проект" (one-time purchase) и "Annual plan: $199/год". В аналитике `billing_period` покрывает monthly/annual, но нет события для one-time project pack. Если команда запустит этот fallback, потребуется новое событие.

---

## Проверка 6: Edge-cases <-> PRD

### 6.1. Critical и High edge-кейсы включены в PRD?

| # Edge-кейс | Приоритет | Включён в PRD как требование? | Статус |
|---|---|---|---|
| 1: Prompt injection | Critical | FR-1.5 (AI Content Disclaimer) -- не про injection protection. NF-13 (данные не используются без согласия) -- не про injection | **НЕ ВКЛЮЧЁН** |
| 2: AI-галлюцинации в конкурентном анализе | Critical | FR-1.5 (disclaimer), FR-2.3 (disclaimer на конкурентах) | Частично (disclaimer != prevention) |
| 3: Пользователь копирует промпты в ChatGPT и получает ~80% результата | Critical (бизнес) | Риск #1 в разделе 7. Но нет FR на защиту IP промптов | Частично |
| 4: Бесконечный free tier через новые аккаунты | High | Нет FR и нет NF на anti-abuse | **НЕ ВКЛЮЧЁН** |

**РАЗРЫВ:** Два самых критичных edge-кейса (Prompt Injection и Anti-Abuse) не оформлены как функциональные или нефункциональные требования в PRD. Edge-cases описывают подробные рекомендации (многоуровневая защита, regex-фильтрация, red-team тестирование), но PRD их не содержит. Разработчик, работающий по PRD, их не реализует.

### 6.2. Edge-кейсы, которые убивают ключевые jobs

| Edge-кейс | Какой job убивает | Критичность |
|---|---|---|
| AI-галлюцинации в конкурентном анализе | CJ2: "Провалидировать идею" -- пользователь принимает решение GO/KILL на основе ложных данных | Критическая |
| Пользователь не имеет идеи (пришёл "посмотреть") | CJ1: "Понять, что строить" -- guided flow не запускается без входных данных | Высокая |
| Слишком короткие / абстрактные ответы | CJ1: все документы будут generic и бесполезны | Высокая |

PRD адресует 2 из 3:
- "Нет идеи" -- FR-6.2 (шаблонные идеи для практики: "SaaS for freelancers / Newsletter tool / Habit tracker / AI writing assistant"). Покрыто.
- "Короткие ответы" -- FR-6.2 ("AI мягко просит конкретизировать: Could you tell me more about..."). Покрыто.
- "AI-галлюцинации" -- FR-1.5 (disclaimer) + FR-2.3 (disclaimer на конкурентах). Частично: disclaimer не предотвращает ошибку, а только снимает формальную ответственность. Пользователь всё равно может принять неверное решение.

### 6.3. Аналитические события для детектирования критических edge-кейсов

| Edge-кейс | Событие в аналитике | Покрытие |
|---|---|---|
| Prompt injection | Нет | **НЕ ПОКРЫТО** |
| AI-галлюцинации | Нет (нет `ai_quality_issue_reported`) | **НЕ ПОКРЫТО** |
| Anti-abuse (мультиаккаунты) | Нет явного `abuse_detected` | **НЕ ПОКРЫТО** |
| Пользователь застрял | `stuck_detected`, `stuck_help_offered`, `stuck_help_accepted` | Покрыто |
| Flow abandoned | `flow_abandoned` с `last_step` и `time_on_last_step_sec` | Покрыто |
| Template idea selected | `template_idea_selected` | Покрыто |

**РАЗРЫВ:** Для трёх самых критичных edge-кейсов (prompt injection, AI-галлюцинации, anti-abuse) нет аналитических событий. Команда не узнает о проблеме, пока пользователи не пожалуются через support.

---

## Критические разрывы (ОБЯЗАТЕЛЬНО исправить)

| # | Документ А | Документ Б | Противоречие / разрыв | Рекомендация по исправлению |
|---|---|---|---|---|
| 1 | 10-landing-copy (Блок 1, One-liner) | 07-prd (раздел 9, Исключения) | **"investor-ready documents"** заявлено на лендинге, но PRD явно исключает pitch deck, финмодели, business plan из scope. PRD специально отличает себя от PitchBob. Документы PRD+Risk+Landing НЕ являются investor-ready. Это привлечёт founders, ожидающих fundraising-материалы, и вызовет разочарование | Убрать "investor-ready" из one-liner. Заменить на "build-ready documents and a vibe-coding plan" или "documents that AI coding tools actually understand". Это точнее отражает реальную ценность продукта |
| 2 | 07-prd (раздел 4, таблица Aha-моментов) | 09-analytics-plan (Activation, aha_moment_reached) | **Aha-момент определён по-разному для сегментов в PRD, но трекается единым событием в аналитике.** PRD: Solopreneurs -- Aha на шаге 3 (Risk Assessment, "стоит ли тратить время"). Аналитика: единый `aha_moment_reached` на шаге 2 (Segments & Jobs) для всех. Все метрики "time to Aha" и "aha -> paywall conversion" будут искажены для сегмента Solopreneurs | Привести к единому определению. Рекомендация: (А) унифицировать Aha-момент в PRD = шаг 2 для всех сегментов (т.к. это "первая ощутимая ценность"), а шаг 3 считать "второй активацией" (отдельное событие `risk_assessment_value_realized`). Или (Б) трекать три сегмент-специфичных события |
| 3 | 07-prd (раздел 8, Метрики качества) | 09-analytics-plan | **4 ключевых метрики PMF не имеют событий.** PRD ставит цели: NPS >40, CSAT per step >4.0/5.0, PMF survey "very disappointed" >40%, Document Quality Score >7/10. Ни одна из них не имеет соответствующего события в аналитическом плане. Команда не сможет оценить product-market fit | Добавить в аналитику: `nps_survey_submitted` (score, comment, days_since_signup), `csat_submitted` (step, score), `pmf_survey_submitted` (answer: "very_disappointed" / "somewhat_disappointed" / "not_disappointed"). Описать триггеры показа: NPS -- D7 после первого flow; CSAT -- после каждого шага для первых 200 пользователей; PMF -- D14 |
| 4 | 08-edge-cases (#1 Prompt Injection, Critical) | 07-prd (все FR) | **Prompt injection -- Critical edge-кейс с подробной рекомендацией, но НЕТ FR в PRD.** Edge-cases описывают 4-уровневую защиту, но PRD не содержит ни FR, ни NF на prompt injection protection. Разработчик по PRD этого не реализует | Добавить в PRD: NF-18 "Prompt Injection Protection" с критериями: (1) фильтрация ввода на injection-паттерны, (2) output-фильтр, (3) логирование подозрительных запросов, (4) red-team тестирование перед запуском. Добавить в аналитику: `injection_attempt_detected` |
| 5 | 03-chosen-segments (Founders, "прототип <1 неделя") | 10-landing-copy (Micro Job 6, "2-4 hours") | **10-40x разница в обещании тайминга прототипа.** Сегменты: "<1 неделя после документов". Лендинг: "2-4 hours". LaunchPilot НЕ генерирует код, прототип делается пользователем самостоятельно. 2-4 часа -- нереалистично для non-technical founder, впервые работающего с Cursor | Привести к единому таймингу. Рекомендация: лендинг -- "your first working prototype THIS WEEKEND" (это ближе к реальности и сохраняет мотивацию). Убрать конкретные "2-4 hours" |

---

## Важные улучшения (рекомендуется исправить)

| # | Документ | Что упущено | Рекомендация |
|---|---|---|---|
| 1 | 09-analytics-plan | Нет событий для трекинга прохождения микро-гайдов (FR-4.2). Мы не знаем, установил ли пользователь Cursor после получения Vibe-Coding Plan. Также не покрыт Риск #3 (micro-guides устаревают) | Добавить: `micro_guide_started` (guide_id, tool), `micro_guide_step_completed` (guide_id, step), `micro_guide_completed` (guide_id, total_time_sec), `micro_guide_step_failed` (guide_id, step, feedback) |
| 2 | 07-prd | Нет FR на anti-abuse механику. Бесплатные пользователи могут создавать бесконечные аккаунты через разные email для обхода лимита 2 проектов | Добавить NF-17: "Anti-abuse: rate limiting по IP (макс 3 аккаунта / IP / день), device fingerprinting для free tier". Добавить в аналитику: `abuse_detected` (type, user_id, ip) |
| 3 | 09-analytics-plan | Нет серверного расчёта MRR. PRD цель: "MRR >$5K к 3 мес", но аналитика не описывает как считать | Добавить серверное событие `mrr_snapshot` (mrr, new_mrr, churned_mrr, expansion_mrr, period) -- ежедневный расчёт. Или описать интеграцию Stripe -> PostHog |
| 4 | 10-landing-copy (Блок 2) | Сравнение "$2,000-5,000 agency" за Landing Copy + Analytics Plan + Competitor Analysis -- преувеличение. AI-генерированные бонусные документы не заменяют работу агентства | Смягчить: "What would take a week of research -- generated in minutes alongside your PRD." Убрать конкретные суммы агентств для бонусных документов |
| 5 | 10-landing-copy (Блок 4, Aha-момент) | Сравнение только с ChatGPT (generic), но не с ChatPRD -- ближайшим конкурентом с 100,000+ пользователей, $15/мес. Пользователь, знающий ChatPRD, не увидит отличия | Добавить второе сравнение: "LaunchPilot vs a PRD generator" -- показать, что PRD-генераторы создают документы, но не учат думать, не оценивают риски, не дают vibe-coding план |
| 6 | 07-prd (раздел 5, Roadmap) | Unit Economics Calculator стоит в roadmap на месяц 3, хотя юнит-экономика заявлена как один из ключевых обучающих компонентов (FR-5.1). IdeaProof даёт калькуляторы бесплатно | Перенести простой калькулятор LTV/CAC/ARPU в MVP или месяц 1. Без инструмента обучение юнит-экономике останется теоретическим |
| 7 | 09-analytics-plan | Нет аналитического события для детектирования AI-галлюцинаций. Пользователь может принять решение GO/KILL на основе ложных данных о конкурентах | Добавить: `ai_content_flagged` (document_type, flag_type: "inaccurate" / "outdated", user_feedback). Кнопка "Is this accurate?" на конкурентном анализе и рыночных оценках |
| 8 | 10-landing-copy (Часть 2, маркетинговые гипотезы) | Все 8 маркетинговых гипотез сфокусированы на acquisition. Нет ни одной retention-маркетинговой гипотезы | Добавить гипотезу 9: "Re-engagement email sequence" -- что триггерит возврат (D+3: tip по инструменту, D+7: "talked to users?", D+14: "update your PRD"). И гипотезу 10: "Build in Public community" -- showcase проектов пользователей |

---

## Предложения по усилению (nice to have)

| # | Область | Идея | Ожидаемый эффект |
|---|---|---|---|
| 1 | Лендинг | Добавить интерактивный demo на лендинге -- не статический пример (Блок 4), а возможность ввести свою идею в 1 предложение и увидеть preview сегмента (без регистрации). Сдвинуть Aha-момент до signup | Увеличение конверсии landing -> signup на 20-30%. Реализация принципа "откусить кусочек пользы авансом" из AURA |
| 2 | PRD | Добавить "Export to Cursor" / "Export to Claude Code" -- не просто "copy to clipboard", а форматирование документа специально под промпт конкретного инструмента (например, для Cursor -- в формате .cursorrules) | Усилит CJ3 и CJ4. Создаст реальное преимущество перед ChatPRD, который тоже интегрируется с Cursor/Lovable |
| 3 | Аналитика | Добавить когортный анализ по источнику (SEO vs Reddit vs LinkedIn vs Paid) с привязкой к completion rate и paid conversion. UTM есть, но нет описания конкретных когортных дашбордов по каналам | Рано определит, какой канал приносит качественных пользователей, а не просто sign-ups. Критично для Риска #9 |
| 4 | Аналитика | Добавить proxy-метрику "document_used_externally": `document_copied` -> `session_started` (в течение 7 дней) -- как сигнал, что документ реально использовался в Cursor/Lovable | Proxy для "продукт реально помогает строить", а не просто "документ сгенерирован" |
| 5 | Edge-cases | Добавить "sunset scenario": что происходит с документами, если LaunchPilot закроется. Для серьёзных founders важный фактор доверия | Снижает барьер для paid-подписки. Добавить в FAQ: "Your documents are always yours. Export anytime, no lock-in" |
| 6 | Конкуренты | Добавить раздел "Defensive strategy": что если ChatPRD добавит обучение? Что если Lovable добавит guided flow? Какова защитная стратегия? | Стратегическая готовность к ответу конкурентов. Ключевой актив -- методология AJTBD, отработанная на 11000+ |

---

## Вердикт

**Оценка согласованности пакета: 7.5/10**

### Обоснование

Пакет демонстрирует высокий уровень продуманности и внутренней связности. Все 9 рисков системно учтены в PRD с конкретными FR и метриками валидации. Сегменты корректно переносятся в лендинг. Аналитический план покрывает основную воронку AARRR с 60+ уникальными событиями и готовым TypeScript-кодом для PostHog. Конкурентный анализ глубокий (14 конкурентов, 5 категорий) и корректно используется для обоснования решений в PRD и лендинге.

Снижение оценки на 2.5 балла обусловлено 5 критическими разрывами: (1) ложное обещание "investor-ready documents" при явном исключении fundraising-материалов; (2) рассогласование Aha-момента между PRD и аналитикой; (3) 4 ключевых метрики PMF без механизма сбора; (4) Critical edge-кейсы без FR в PRD; (5) 10-40x расхождение в обещании тайминга прототипа. Разрывы #1 и #5 наиболее опасны -- они создают "expectation gap", который убьёт retention даже при хорошем привлечении.

### Топ-3 сильные стороны

1. **Системный учёт рисков.** Все 9 рисков из 05-chosen-risks детально проработаны в разделе 7 PRD с конкретными мерами минимизации, привязкой к FR и метриками валидации. Каждый риск имеет чёткий "что делаем, если риск реализовался" -- это уровень продуктовой работы выше среднего.

2. **Глубина и реализуемость аналитического плана.** 14 категорий событий, 60+ уникальных событий, полный TypeScript-код для PostHog, типизированные функции для каждого события. Аналитический план можно сразу копировать в код -- это экономит 2-3 дня разработки. Привязка событий к конкретным FR -- отличная трассируемость.

3. **Корректное и честное "увольнение" конкурентов.** Каждое заявление о преимуществе на лендинге подтверждается конкретными данными конкурентного анализа. Нет голословных утверждений. Слабости конкурентов описаны конкретно и верифицируемо. Сводная таблица "конкурент x фича" в анализе -- отличный инструмент для принятия решений.

### Топ-3 слабые стороны

1. **Лендинг систематически завышает ожидания.** "Investor-ready documents" (нет fundraising-материалов), "2-4 hours to prototype" (нереалистично для non-technical), "$2,000-5,000 agency" (преувеличение для бонусных документов). Паттерн: маркетинг обещает больше, чем продукт может дать. Это приведёт к высокому churn в первые 30 дней.

2. **Метрики качества не трекаются.** PRD определяет NPS, CSAT, PMF survey и Document Quality Score как ключевые индикаторы product-market fit, ставит конкретные цели (NPS >40, CSAT >4.0, PMF >40%). Но аналитический план не содержит ни одного события для их сбора. Команда сможет отслеживать количественные метрики (конверсии, retention), но не качественные (удовлетворённость, ценность, готовность рекомендовать).

3. **Critical edge-кейсы не оформлены как требования.** Prompt injection (Critical) и anti-abuse (High) подробно описаны в edge-cases с конкретными рекомендациями, но не перенесены в PRD как FR или NF. При разработке по PRD эти защиты не будут реализованы. Это системная процессная ошибка: edge-кейсы должны порождать требования, а не оставаться отдельным "рекомендательным" документом.
