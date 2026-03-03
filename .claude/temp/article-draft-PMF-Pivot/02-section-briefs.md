# Section Briefs — How to Find PMF Fast and Pivot the Right Way

## Нарративная структура (выбрано)

**Hook:** Variant A (Shock Opening) — PMF expires in 90 days (Lovable case)
**Порядок секций:** Problem-First Cascade: A3 → A6 → A1 → A5 → A4 → N2 → N1
**Финал:** Algorithm Card + closing reframe from Variant 2
**Total words:** ~1800 (upper range of 1000-2000 HackerNoon brief)

**Narrative logic in one sentence:**
"Your idea is already dead (A3) → because you started with the wrong job (A6) → AI makes building fast but not learning (A1) → here is how to prioritize what to test (A5) → here is the full operating system (A4) → but read the signal right, not the average (N2) → because this machine runs forever (N1)."

---

## STYLE GUIDE (key rules from agent-style-researcher.md)

- **Voice:** First person ("I") for personal experience. "You" for advice. HackerNoon REQUIRES first person.
- **Tone:** Conversational-professional (4/10 formality). Contractions OK. Light humor 1-2 times.
- **Paragraphs:** 2-4 sentences. Max 5-6 for complex ideas. Single-sentence paragraphs for emphasis.
- **Subheadings:** Every 250-350 words. Mix questions, steps, declarative claims.
- **Data:** 4-5 data points woven into narrative. Always name source.
- **Expert quotes:** 2-3, under 20 words each. Inline: "As [Name] puts it: '[quote]'."
- **Cases:** 3-4 brief (2-4 sentences). Mix known and fresh.
- **Named frameworks:** Give key concepts memorable names.
- **Conclusion:** SHORT (2-4 sentences). Do NOT summarize. Push to action or reframe.
- **PROHIBITED:** Starting with definitions, academic tone, corporate "we", paragraphs >6 sentences, generic advice, no personal experience.

---

## Section Brief: HOOK
**Word budget:** ~110 words
**Позиция:** Opening

### ТЕКСТ ХУКА (на основе narrative-architect Variant A + Lovable case):

Writer должен написать hook по следующей канве:
- Lovable hit $200M ARR in under a year — fastest AI startup ever to $100M ARR (8 months)
- Elena Verna (Head of Growth, ex-Dropbox/Miro/SurveyMonkey) says PMF there is a "perishable good" — must re-earn fit every 90 days
- The "find PMF → scale" playbook is a trap
- This article is the operating manual for the treadmill that never stops

**MUST-INCLUDE:**
- [ ] Lovable $200M ARR, 90-day PMF cycle — https://www.elenaverna.com/p/the-product-market-fit-treadmill
- [ ] Elena Verna name + credentials
- [ ] "Perishable good" / treadmill concept

**Transition to A3:** "So if PMF is a treadmill, the first step is admitting where you actually stand. And the honest answer is brutal."

### TOTAL MUST-INCLUDE items: 3

---

## Section Brief: Section 1 — "Your Idea Is Already Dead"
**Покрывает тезис:** A3
**Word budget:** ~220 words
**Позиция:** 1-я секция из 7

### СУТЬ ТЕЗИСА — КАРКАС СЕКЦИИ:
Новая идея почти всегда держится на ложных предположениях. Поэтому правильная цель ранней стадии — не "выпустить продукт", а купить знание о том, что именно его убьёт (рынок/сегмент/job/ценность/канал/экономика), и сделать pivot как смену конкретных assumptions. Но "kill fast" надо делать на правильном сигнале: в AI-категориях ранние когорты могут быть "туристическими", и средние метрики искажают картину.

### ЭЛЕМЕНТЫ ДЛЯ ОБОГАЩЕНИЯ:

**DATA:**
1. 90-95% новых идей/продуктов проваливаются

**QUOTE:**
1. a16z (2025-12-08): foundational cohort может "внезапно" удержаться; средние метрики не равны истине — https://a16z.com/the-cinderella-glass-slipper-effect-retention-rules-in-the-ai-era/

**CONCEPT:**
1. "Ваша идея уже мертва — вы просто ещё не знаете, что её убьёт"
2. Цель ранней стадии = купить знание, а не выпустить продукт
3. Pivot = смена конкретных assumptions (не "перепридумывание")

**KB:**
1. > «Мы не запускаем продукт --- мы покупаем знания.» — Источник: `1-Context/AURA-Theses/RAT/risk-assumption-test.md`

### КЕЙС: Notion — nearly died in 2015, reborn by finding real cause of death
Notion V1 (programming app for non-coders) failed. Ivan Zhao fired all 4 employees, moved to Kyoto, rebuilt. Insight: "people don't want to build software; they want to get stuff done." Pivoted to modular workspace. V2 launched 2018, 1M users fast, now $10B. The cause of death was a wrong assumption about the Job.
URL: https://www.figma.com/blog/design-on-a-deadline-how-notion-pulled-itself-back-from-the-brink-of-failure/

### ПЕРЕХОДЫ:
- **ОТ хука:** "So if PMF is a treadmill, the first step is admitting where you actually stand. And the honest answer is brutal."
- **К A6:** "If the goal of early stage is to buy knowledge about what kills your idea, the next question is obvious: where do you start digging?"

### TOTAL MUST-INCLUDE items: 8

---

## Section Brief: Section 2 — "Start With the Job, Not the Solution"
**Покрывает тезис:** A6 (расширен автором)
**Word budget:** ~230 words
**Позиция:** 2-я секция из 7

### СУТЬ ТЕЗИСА — КАРКАС СЕКЦИИ:
Продукт существует, чтобы выполнять Job клиента, а прибыль появляется только если вы создаёте добавочную ценность в выбранном сегменте. Самая частая ошибка — пропустить выбор сегмента и "лучшего Job", и сразу уйти в решение. AI может ускорить генерацию сегментов/assumptions, но повышает риск "много слов, мало знания": нужно явно описать процесс превращения LLM-гипотез в доказательства (интервью, пресейл, когорты).

**РАСШИРЕНИЕ АВТОРА:** Работа является первопричиной ВСЕГО в продукте. Найти правильный сегмент и правильную работу — это абсолютно ключевое. При запуске нового продукта именно сюда должна уходить большая часть времени и усилий. Когда продаём продукт — ищем в первую очередь сегмент и job, и только потом валидируем гипотезу ценности и модель коммуникации.

### ЭЛЕМЕНТЫ ДЛЯ ОБОГАЩЕНИЯ:

**DATA:**
1. Самая частая ошибка = пропустить выбор сегмента и job

**CONCEPT:**
1. Jobs первичны — работа = первопричина ВСЕГО в продукте
2. Выбор сегмента + Job = ключевое стратегическое решение при запуске
3. Порядок: сегмент → job → валидация ценности → коммуникация
4. LLM-гипотезы → доказательства (интервью, пресейл, когорты)

**KB:**
1. > «Работы являются первопричиной всех действий человека.» — Источник: `1-Context/AURA-Theses/AJTBD/fundamentals.md`

**COUNTER:**
1. arXiv (2025-12-22): over-reliance и падение validation при использовании AI — https://arxiv.org/abs/2512.19644

### КЕЙС: Wispr Flow — killed 16-year hardware dream, found PMF in voice dictation
Wispr spent years building hardware voice device. After board meeting in mid-2024, confronted truth: voice dictation wasn't good enough for hardware adoption. Job was "type faster and more naturally", not "own a cool device". Killed hardware, launched macOS app. #1 Product Hunt, ~20% free-to-paid conversion (vs 3-4% industry), 90% MoM growth, $81M raised.
URL: https://www.producthunt.com/p/wisprflow/how-wispr-flow-found-pmf-through-a-pivot

### ПЕРЕХОДЫ:
- **ОТ A3:** "If the goal of early stage is to buy knowledge about what kills your idea, the next question is obvious: where do you start digging? The answer is more fundamental than most teams realize."
- **К A1:** "Finding the right segment and job has always been the hard part. What changed in 2025 is that everything around it got radically cheaper — and that is both an accelerator and a trap."

### TOTAL MUST-INCLUDE items: 9

---

## Section Brief: Section 3 — "AI Made Building Free. It Did Not Make Learning Free."
**Покрывает тезис:** A1
**Word budget:** ~250 words
**Позиция:** 3-я секция из 7

### СУТЬ ТЕЗИСА — КАРКАС СЕКЦИИ:
Раньше код был дорогим, поэтому типовой порядок был: ресерч → MVP → спрос → разработка. AI снижает барьер прототипирования, поэтому можно чаще показывать людям более "реальные" решения и быстрее получать возражения/страхи/попадание в ценность. Но скорость генерации кода не равна скорости получения знания: vibe-coding может быть стохастичным, а AI-инструменты подталкивают к "more code, less validation". Поэтому правильный алгоритм: использовать AI как ускоритель артефактов, но измерять прогресс количеством **валидных** проверок и качеством сигнала.

### ЭЛЕМЕНТЫ ДЛЯ ОБОГАЩЕНИЯ:

**DATA:**
1. METR (2025-07-10): AI может замедлять опытных разработчиков при субъективном ощущении ускорения
2. arXiv (2025-12-22): "more code, less validation" риск

**QUOTE:**
1. arXiv (2025-12-27): vibe-coding = "rolling the dice" — https://arxiv.org/abs/2512.22418

**CONCEPT:**
1. Vibe-coding как стохастичный процесс
2. "more code, less validation" — анти-паттерн
3. AI как ускоритель артефактов, НЕ ускоритель знания
4. Прогресс = количество валидных проверок + качество сигнала

**KB:**
1. > «Лучший способ провалидировать гипотезу ценности — это продажи.» — Источник: `1-Context/AURA-Theses/HowTos/validate-value.md`

**COUNTER:**
1. METR: AI может замедлять при субъективном ощущении ускорения — https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/

### КЕЙС: EnrichLead — 100% AI-coded, collapsed in 72 hours
EnrichLead (sales SaaS) built entirely with Cursor AI — "zero hand-written code." Within 72 hours, users found ALL security logic on client side. Anyone could bypass paywall by changing one value in browser console. Founder couldn't audit 15,000 lines of AI code. Shut down. Building was free; validation was skipped.
URL: https://ruinunes.com/vibe-coding-trap-ai-built-mvp/

### ПЕРЕХОДЫ:
- **ОТ A6:** "Finding the right segment and job has always been the hard part. What changed in 2025 is that everything around it got radically cheaper — and that is both an accelerator and a trap."
- **К A5:** "If AI gives you speed but not direction, you need a compass. Here is the formula that tells you which assumption to test first."

### TOTAL MUST-INCLUDE items: 11

---

## Section Brief: Section 4 — "The Killer Assumption Formula"
**Покрывает тезис:** A5 (изменённая формула)
**Word budget:** ~220 words
**Позиция:** 4-я секция из 7

### СУТЬ ТЕЗИСА — КАРКАС СЕКЦИИ:
PMF — континуум. В каждый момент времени у вас есть самый опасный риск, который может убить бизнес, и его нужно тестировать первым. RAT формализует приоритет: цена ошибки и стоимость проверки. Но в AI-категориях особый риск — неверная интерпретация ранних метрик (AI tourists), поэтому нужно заранее определять горизонт сигнала (например, M3 retention) и критерии pivot/iterate.

**ИЗМЕНЕНИЕ АВТОРА:** Формула = вероятность ошибки × последствия ошибки / стоимость теста.

### ЭЛЕМЕНТЫ ДЛЯ ОБОГАЩЕНИЯ:

**DATA:**
1. PMF = континуум, не бинарное состояние

**QUOTE:**
1. Elena Verna (2025-12-18): PMF treadmill и необходимость постоянного контура — https://www.lennysnewsletter.com/p/the-new-ai-growth-playbook-for-2026-elena-verna

**CONCEPT:**
1. PMF = континуум (не бинарный)
2. Killer assumption = самый опасный риск в каждый момент
3. ФОРМУЛА: вероятность ошибки × последствия ошибки / стоимость теста
4. Горизонт сигнала (M3 retention) как защита от AI tourists

**KB:**
1. > «…ранжируем по риску (цена ошибки) и стоимости проверки, проверяем сначала самые рискованные.» — Источник: `1-Context/AURA-Theses/RAT/risk-assumption-test.md`

### КЕЙС: Popsa — x4 installs from testing a single-word assumption
Popsa (photo book app) was #1 in App Store but installs were underwhelming. Tagline: "Fast, Easy Photo Books." User test: one person thought "fast" meant 2 hours. Actual time: 5 minutes. Changed to "Photo Books in Five Minutes." Conversion x4 overnight. The killer assumption was hiding in a single word. Cost to test: one round of user interviews.
URL: https://review.firstround.com/founder-led-growth-playbook/

### ПЕРЕХОДЫ:
- **ОТ A1:** "If AI gives you speed but not direction, you need a compass. Here is the formula that tells you which assumption to test first."
- **К A4:** "One formula is not enough. When you are running dozens of assumptions through the pipeline, you need an operating system."

### TOTAL MUST-INCLUDE items: 9

---

## Section Brief: Section 5 — "The Hypothesis Factory Operating System"
**Покрывает тезис:** A4
**Word budget:** ~230 words
**Позиция:** 5-я секция из 7

### СУТЬ ТЕЗИСА — КАРКАС СЕКЦИИ:
AI повышает количество проверяемых гипотез "в единицу времени". Это делает фаундера оператором конвейера: выбирать гипотезы, ставить тесты, интерпретировать результаты и делать decisions. Но AI также меняет workflow: люди пишут больше и удаляют больше кода, а продуктивность становится многомерной (ownership/качество/долгосрочная поддерживаемость). Поэтому фабрика гипотез должна иметь операционную систему: assumption ledger, decision log, правила staged validation и критерии остановки.

### ЭЛЕМЕНТЫ ДЛЯ ОБОГАЩЕНИЯ:

**DATA:**
1. arXiv (2026-01-15): "more code + more deletion" в реальных логах — https://arxiv.org/abs/2601.10258

**QUOTE:**
1. arXiv (2026-01-15): "more code + more deletion" pattern — https://arxiv.org/abs/2601.10258

**CONCEPT:**
1. Фаундер как оператор фабрики проверки гипотез
2. ОС фабрики: assumption ledger + decision log + staged validation + критерии остановки
3. Продуктивность многомерна

**KB:**
1. > «Вам нужно увидеть все гипотезы… увидеть полный набор.» — Источник: `1-Context/AURA-Theses/RAT/risk-assumption-test.md`

**COUNTER:**
1. arXiv (2512.19644): throughput без validation = over-reliance — https://arxiv.org/abs/2512.19644

### КЕЙС: Spotify — 520 experiments, 12% win rate, 64% learning rate
Spotify's EwL framework (2025): 520 experiments across 58 teams. Win rate only ~12%, but learning rate ~64%. Key insight: most value from discovering what NOT to ship. Shifted metric from "experiment velocity" to "learning velocity."
URL: https://engineering.atspotify.com/2025/9/spotifys-experiments-with-learning-framework

### ПЕРЕХОДЫ:
- **ОТ A5:** "One formula is not enough. When you are running dozens of assumptions through the pipeline, you need an operating system — not just a prioritization rule."
- **К N2:** "But even the best-run factory can kill a good idea if it reads the signal wrong."

### TOTAL MUST-INCLUDE items: 9

---

## Section Brief: Section 6 — "The Glass Slipper: PMF Is Cohort-Specific"
**Покрывает тезис:** N2
**Word budget:** ~150 words
**Позиция:** 6-я секция из 7

### СУТЬ ТЕЗИСА — КАРКАС СЕКЦИИ:
Ранние метрики часто обманывают: может быть много туристов и много шума. В AI-категориях важнее найти одну когорту, которая удерживается и возвращается, потому что продукт попал в один высокоценный workload. Поэтому диагностика PMF должна включать вопрос: "кто удержался, что именно они делают, и почему это повторяемо?"

### ЭЛЕМЕНТЫ ДЛЯ ОБОГАЩЕНИЯ:

**QUOTE:**
1. a16z / Malika Aubakirova (2025-12-08): "Glass slipper" cohort-эффект — https://a16z.com/the-cinderella-glass-slipper-effect-retention-rules-in-the-ai-era/

**CONCEPT:**
1. "Glass slipper" cohort — найти одну когорту с высоким удержанием
2. PMF может быть когортным, а не средним
3. Диагностика: "кто удержался, что делают, почему повторяемо?"
4. Туристы vs foundational cohort

### КЕЙС: Superhuman — PMF score 22% to 58% by focusing on "very disappointed" cohort
Superhuman found only 22% "very disappointed" users (40% = PMF). Instead of pleasing everyone, Vohra identified the specific cohort that loved speed. 50% resources on what they loved, 50% on on-the-fence users who looked like them. Score doubled to 58% in 3 quarters. Now $36M ARR, acquired by Grammarly.
URL: https://review.firstround.com/how-superhuman-built-an-engine-to-find-product-market-fit/

### ПЕРЕХОДЫ:
- **ОТ A4:** "But even the best-run factory can kill a good idea if it reads the signal wrong. There is a specific trap here."
- **К N1:** "Finding the foundational cohort is powerful. But here is the part most teams miss: you will have to do it again. And again."

### TOTAL MUST-INCLUDE items: 7

---

## Section Brief: Section 7 — "The PMF Treadmill" (MAIN THESIS — CLIMAX)
**Покрывает тезис:** N1 (ГЛАВНЫЙ, расширен автором)
**Word budget:** ~250 words
**Позиция:** 7-я секция из 7 (КУЛЬМИНАЦИЯ)

### СУТЬ ТЕЗИСА — КАРКАС СЕКЦИИ:
В ряде AI-рынков PMF становится менее устойчивым: меняются модели, ожидания пользователей, и конкурентные преимущества быстрее "испаряются". Поэтому стратегия "нашли PMF → оптимизируем → масштабируем" превращается в ловушку. Нужны два контура: оптимизация текущего fit и постоянный инновационный контур (новые ставки). Это превращает фабрику гипотез в perpetual engine.

**РАСШИРЕНИЕ АВТОРА:** Это НЕ только про AI/EA категории — это про ВСЕ категории. PMF теперь нужно постоянно перенаходить в любом рынке.

### ЭЛЕМЕНТЫ ДЛЯ ОБОГАЩЕНИЯ:

**DATA:**
1. Elena Verna: PMF re-earned every ~90 days at Lovable

**QUOTE:**
1. Elena Verna (⭐⭐⭐): AI-growth меняет правила; PMF становится treadmill — https://www.lennysnewsletter.com/p/the-new-ai-growth-playbook-for-2026-elena-verna

**CONCEPT:**
1. PMF treadmill — fit нужно постоянно перенаходить (ВСЕ категории)
2. Два контура: оптимизация текущего fit + инновационный контур
3. "нашли PMF → масштабируем" = ловушка
4. Фабрика гипотез как perpetual engine

### КЕЙС: Jasper AI — $120M to $35M ARR when ChatGPT ate their lunch
Jasper was THE AI writing tool. $120M ARR, $1.5B valuation. ChatGPT launched → traffic -30% in 2 months → revenue crashed to $35M (53% decline). Both co-founders out. 3 pivots in 12 months. Perfect PMF vaporized because the market moved.
URL: https://research.contrary.com/company/jasper

### ПЕРЕХОДЫ:
- **ОТ N2:** "Finding the foundational cohort is powerful. But here is the part most teams miss: you will have to do it again. And again."
- **К финалу:** "The treadmill never stops. But now you have the operating manual."

### TOTAL MUST-INCLUDE items: 8

---

## Section Brief: FINALE
**Word budget:** ~120 words

### СТРУКТУРА (Algorithm Card + Reframe):
1. 7-step operating checklist:
   - Start with jobs and segments
   - List riskiest assumptions. Prioritize by: (probability × consequences) / cost of test
   - Use AI to build fast — measure progress in validated checks, not shipped features
   - Run the factory with an OS: assumption ledger, decision log, staged validation, stop criteria
   - Look for the foundational cohort before killing an idea
   - When pivoting, name exactly which assumption changed and why
   - Accept the treadmill. Schedule re-validation before you need it

2. Closing reframe: "PMF is not something you find. It is something you keep finding."

### TOTAL MUST-INCLUDE items: 2

---

## DROPPED Elements (с объяснениями)

| Element | Тезис | Причина |
|---------|-------|---------|
| arXiv (2026-02-03): продуктивность с AI зависит от долгосрочных факторов | A4 | Word budget — A4 уже содержит "more code + more deletion" data point |
| "Kill fast" на правильном сигнале (не на шуме) | A3 | Частично покрыто через N2 (glass slipper = правильный сигнал) |
| AI ускоряет генерацию сегментов/assumptions | A6 | Сжато — упомянуто в СУТЬ но без отдельного data point |

---

## Статистика покрытия

| Тезис | Элементов в must-include | В section briefs | % |
|-------|--------------------------|------------------|---|
| N1 (главный) | 8 | 7 | 88% |
| A1 | 12 | 9 | 75% |
| A3 | 10 | 8 | 80% |
| A4 | 11 | 9 | 82% |
| A5 | 11 | 9 | 82% |
| A6 | 9 | 8 | 89% |
| N2 | 8 | 7 | 88% |
| **ИТОГО** | **69** | **57** | **83%** |

Глубокие тезисы: A1=75%, A3=80%, A4=82%, A5=82%, N1=88% — все ≥75%. CHECK.
Средние: N2=88% — ≥60%. CHECK.
