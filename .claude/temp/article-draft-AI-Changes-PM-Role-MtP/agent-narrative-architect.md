# Narrative Architect Report — AI Changes PM Role (MtP Article)

> **Agent:** narrative-architect
> **Дата:** 2026-03-02
> **Статья:** Practical Guide for PMs in the Vibe Coding Era
> **Издание:** Mind the Product
> **Лимит:** ~1200 слов (1000-1800)
> **Язык:** English
> **Тезисы:** A1, A2, A3, A4, N5

---

## ЗАДАЧА 1: Нарративная арка

### Конфликт
PM-ы видят, как vibe coding и AI-агенты стирают границы между ролями. Коллеги-инженеры строят продукты сами, фаундеры говорят, что 3 человека = 30. Паника: "Если AI делает execution бесплатным, зачем нужен PM?" Правда ли, что PM-ы исчезнут?

### Трансформация
Нет. Но "старый PM" -- тот, кто двигает таски и пишет PRD -- действительно умирает. Трансформация: от координатора (middleman) к оператору, который принимает решения, строит прототипы, управляет конвейером гипотез и владеет story продукта от идеи до рынка.

### Эмоциональная арка (по секциям)

| Этап | Эмоция читателя | Что происходит в тексте |
|------|-----------------|------------------------|
| Hook | Узнавание + тревога | PM впервые пробует vibe coding и понимает: старые навыки не работают |
| Секция 1 (Reframe) | Переосмысление | "Execution стал бесплатным. Judgment -- нет. Вот ваш новый актив." |
| Секция 2 (New identity) | Clarity | "Вы не PM, вы builder. Что это значит конкретно." |
| Секция 3 (Operating model) | Практический энтузиазм | "Конвейер гипотез + prompt sets вместо PRD. Вот как это работает." |
| Секция 4 (Full stack to market) | Уверенность + честность | "Distribution > production. PM + PMM fusion. И чего ждать через 12-24 мес." |
| Финал | Actionable clarity | Конкретные шаги на следующую неделю. Не мотивационная речь -- checklist. |

---

## ЗАДАЧА 2: Hook (3 варианта)

### ЗАПРЕЩЕНО повторять:
Старый hook: "Two facts that shouldn't coexist: 54K layoffs + 35% salary premium" -- статистический парадокс, K-shape framing.

---

### Вариант A: Personal story (РЕКОМЕНДУЕМЫЙ)

> Last November, I opened Cursor for the first time and built a working prototype in four hours -- something that would have taken my engineering team two sprints. I sat there staring at the screen, feeling two things at once: exhilaration that I could move this fast, and a quiet dread that I had just made my own job description obsolete. If I can build this without engineers, what exactly is the PM supposed to do now? I spent the next three months finding out. This is what I learned.

**Почему работает:** Личный опыт автора, конкретная деталь (Cursor, 4 часа), emotional hook (exhilaration + dread), promise of resolution. MtP любит first-person experience. НЕ совпадает со старым hook (никаких цифр рынка или K-shaped framing).

---

### Вариант B: Provocative question

> Here's a question most PMs are afraid to ask out loud: if a founder with Cursor and Claude Code can build, test, and ship a product without a single PM on the team -- and some of the best startups in YC's latest batch are doing exactly that -- then what is the PM role actually *for*? The answer turns out to be both simpler and more demanding than you'd expect. It's not about building. It's about knowing what's worth building, and for whom. That's a fundamentally different job -- and it requires a fundamentally different playbook.

**Почему работает:** Ставит острый вопрос от лица читателя, ссылается на YC (credibility), сразу дает reframe. Провокация, но не кликбейт.

---

### Вариант C: Counter-intuitive insight

> The most valuable PM skill of 2026 has nothing to do with AI tools, prompt engineering, or vibe coding. It's the ability to look at ten things you *could* build this week -- because AI makes all of them cheap -- and say no to nine. When execution costs approach zero, the bottleneck moves upstream: to judgment, to knowing which hypothesis deserves your next four hours, and to being honest about killing the ones that don't. This article is a practical guide to operating as a PM when the hardest part of the job is no longer getting things built.

**Почему работает:** Counter-intuitive ("not about AI tools"), reframe in the first paragraph, directly sets up the practical guide promise. Ясно отличается от старого hook.

---

### Рекомендация: **Вариант A** как основной, с элементами C во втором абзаце.

Обоснование:
1. MtP ценит personal experience и "honest practitioner voice"
2. Вариант A создает empathy и узнавание (каждый PM пробовал или планирует)
3. Вариант C дает intellectual reframe, который усиливает A
4. Вариант B хорош как fallback, но менее personal

---

## ЗАДАЧА 3: Порядок тезисов-секций (2 варианта)

### Анализ тезисов по весу

| Тезис | Самостоятельность | Можно объединить с | Слова (solo) |
|-------|-------------------|-------------------|-------------|
| А1: Business Judgment | Высокая | -- | 250 |
| А2: Full-stack builders | Высокая | А4 (оба про "делать руками") | 250 |
| А3: Конвейер гипотез | Высокая | -- | 250 |
| А4: Полный цикл 12-24 мес | Средняя (тонкий) | А2 или N5 | 150 |
| N5: PM+PMM fusion | Средняя | А4 | 150 |

**Проблема:** 5 тезисов x 240 слов = 1200 -- а hook и close тоже нужны (~250 слов). Итого нужно ~1450, что в рамках, но плотно.

**Решение:** Объединить А4 + N5 в одну секцию "From prototype to market" (300-350 слов). Итого 4 секции.

---

### Вариант 1: Problem -> Reframe -> New skills -> Action steps

**Порядок:** Hook -> А1 (Judgment reframe) -> А2 (Full-stack builder) -> А3 (Hypothesis pipeline) -> А4+N5 (From prototype to market) -> Close

| # | Секция | Роль в нарративе | Слова |
|---|--------|-----------------|-------|
| 0 | Hook (Вариант A+C) | Ситуация: PM попробовал vibe coding, мир перевернулся | 120 |
| 1 | **Judgment is the new premium** (А1) | Reframe: execution бесплатно, judgment -- нет. RAT формула. Feature mill trap. | 250 |
| 2 | **You're a builder now** (А2) | Новая идентичность: full-stack builder. Cherny, Andreessen, LinkedIn APB. | 250 |
| 3 | **Run a hypothesis factory** (А3) | Операционная модель: prompt sets вместо PRD, 10x throughput, delegation по риску. | 250 |
| 4 | **From prototype to market** (А4+N5) | Полный цикл: distribution > production. PM+PMM fusion. Chesky. Kill criteria. 12-24 мес timeline. | 250 |
| 5 | Close (action checklist) | Конкретные шаги на понедельник | 80 |
| | **ИТОГО** | | **~1200** |

**Обоснование:** Классическая структура "what changed -> what it means -> what to do". Линейная, предсказуемая, легко сканируется. Подходит для MtP (их формат = practical articles with structure).

**Сильные стороны:** Логичный поток, каждая секция строится на предыдущей.
**Слабые стороны:** Может казаться слишком линейной; А1 (judgment) в начале = абстрактнее, чем А2 (builder).

---

### Вариант 2: Personal hook -> What changed -> 3 concrete shifts -> What to do Monday (РЕКОМЕНДУЕМЫЙ)

**Порядок:** Hook -> А2 (Builder, конкретика) -> А1 (Judgment reframe) -> А3+А4+N5 (Operating model + market) -> Close

| # | Секция | Роль в нарративе | Слова |
|---|--------|-----------------|-------|
| 0 | Hook (Вариант A) | Личная история: 4 часа, прототип, дрожь | 120 |
| 1 | **The builder era is here** (А2) | Конкретика: Cherny 100% AI code, Andreessen Mexican standoff, LinkedIn APB. "Full-stack builder = не "научился кодить"". | 280 |
| 2 | **Speed without judgment is the feature mill on steroids** (А1) | Reframe: RAT формула. Judgment = ваш новый актив. Feature mill trap + vibe coding = 10x waste. | 250 |
| 3 | **Your new operating system** (А3 + А4 + N5) | Три сдвига в одной секции: (a) prompt sets вместо PRD, (b) delegation по уровню риска, (c) distribution > production, PM+PMM fusion. Kill criteria. | 350 |
| 4 | Close (Monday morning checklist) | 5 конкретных шагов. Не мотивация -- actions. | 100 |
| | **ИТОГО** | | **~1100** |

**Обоснование:** Начинает с конкретного и тактильного (А2 = "builder", код, инструменты), потом поднимает на уровень абстракции (А1 = judgment), потом дает операционную модель (А3+А4+N5). Этот порядок следует natural discovery path PM-а: "Я попробовал -> Я понял что скорость без направления опасна -> Вот как работать по-новому."

**Сильные стороны:**
- Начало с конкретики = высокий engagement
- А1 после А2 = judgment как ответ на проблему ("я умею строить, но ЧТО строить?")
- Объединение А3+А4+N5 = единая секция "как работать", а не 3 тонких
- Экономнее по словам, оставляет пространство для примеров

**Слабые стороны:** Объединение 3 тезисов в одну секцию требует дисциплины от writer-a.

---

### Рекомендация: **Вариант 2**

Причины:
1. Более natural для PM-reader (от конкретного к абстрактному)
2. Лучше дифференцируется от старой статьи (та начинала с цифр рынка; новая -- с личного опыта и builder-identity)
3. Экономнее по словам при 3 тезисах в одной секции
4. Сильнее emotional arc: "Wow, I can build!" -> "Wait, speed without direction is dangerous" -> "Here's the operating system" -> "Do this Monday"

---

## ЗАДАЧА 4: Переходы между секциями

### Hook -> Секция 1 (A2: Builder era)

> **Transition:** "I'm not alone in this. The shift from PM to builder isn't a metaphor anymore -- it's happening across the industry, and it's happening fast."

Затем сразу факты: Cherny, Andreessen, LinkedIn APB.

### Секция 1 (A2: Builder) -> Секция 2 (A1: Judgment)

> **Transition:** "But here's what nobody tells you about the builder era: building faster is the easy part. The hard part is knowing what's worth building. And that distinction is about to become the single biggest differentiator in the PM profession."

Почему работает: Прямое столкновение "exciting" (builder) с "dangerous" (без judgment). Создает tension перед A1.

### Секция 2 (A1: Judgment) -> Секция 3 (A3+A4+N5: Operating system)

> **Transition:** "So if judgment is the asset and building is the tool -- what does the day-to-day actually look like? Here's the operating model that's replacing the PRD-sprint-ship cycle."

Почему работает: Отвечает на прямой вопрос читателя ("Ок, я понял ЧТО важно, но КАК это работает?"). Переводит от mindset к операционке.

### Секция 3 -> Close

> **Transition:** "None of this requires a restructuring or a leadership mandate. You can start this week."

Почему работает: Снимает барьер "мне нужно разрешение". Empowerment перед checklist.

---

## ЗАДАЧА 5: Финал (2 варианта)

### ЗАПРЕЩЕНО повторять:
Старый финал: "You don't need a three-year plan. You need a three-week experiment." -- временной фрейм + эксперимент.

---

### Вариант 1: Monday Morning Checklist (РЕКОМЕНДУЕМЫЙ)

> **Here's your Monday morning:**
>
> 1. Pick one hypothesis from your backlog. Build a working prototype this week -- not to ship, but to learn what your judgment tells you when testing costs nothing.
> 2. Replace one PRD with a prompt set. Write the intent, the examples, and the constraints -- and hand it to an AI agent.
> 3. Ask yourself the RAT question for every item in your backlog: "If this assumption is wrong, what do we lose?" Rank by consequence, not by effort.
> 4. Talk to one customer this week. No AI can replicate what you learn from watching someone struggle with your product in real time.
> 5. Kill one feature. Seriously. Find the zombie that's burning compute and margin and delete it.
>
> The PM role isn't disappearing. But the PM who only coordinates is. The builder who judges -- who knows what to build, for whom, and when to stop -- that PM has never been more essential.

**Почему работает:** 5 конкретных actions (MtP любит actionable). Каждый step привязан к тезису статьи. Финальное предложение -- reframe, не мотивация. Не повторяет "three-week experiment" формат.

**Слов:** ~140

---

### Вариант 2: Honest reflection + one shift

> The irony of the AI era is that the most human skill -- the ability to sit with ambiguity, choose a direction, and take responsibility for the outcome -- is now the most valuable one. Tools will keep getting better. Models will keep getting faster. The PM who treats that speed as a weapon without a target will produce more waste, faster.
>
> But the PM who pairs that speed with judgment -- who runs ten experiments instead of shipping ten features, who writes prompt sets instead of PRDs, who owns the story all the way to the customer -- that PM isn't being replaced. That PM is being unleashed.
>
> Start with one hypothesis. Build it yourself. See what your judgment tells you when cost is no longer the constraint.

**Почему работает:** Philosophical but grounded. "Unleashed" как positive reframe. Заканчивается одним конкретным шагом. Отличается от старого финала тоном (не "три недели", а mindset + одно действие).

**Слов:** ~120

---

### Рекомендация: **Вариант 1** (Monday Morning Checklist)

Причины:
1. MtP explicit requirement: "actionable insights, reader should know what to do in the next sprint"
2. Checklist = scannable, shareable, bookmarkable
3. Каждый пункт привязан к тезису, усиливает recall
4. Финальная строка дает reframe без пафоса

---

## ЗАДАЧА 6: Word Budget

### Рекомендуемое распределение (Вариант 2 порядка)

| Элемент | Слов | % | Содержание |
|---------|------|---|-----------|
| **Hook** | 120 | 10% | Personal story: 4 часа, Cursor, прототип, двойственное чувство |
| **Секция 1: The builder era** (A2) | 280 | 23% | Cherny 100% AI code, +200% productivity. Andreessen "Mexican standoff". LinkedIn APB. Torres: прототип за часы. BUT: full-stack = не "научился кодить". Контраргумент: METR 19% slower. |
| **Секция 2: Judgment > speed** (A1) | 250 | 21% | RAT формула. Feature mill trap x AI = 10x waste. "What to build" > "how to build". Vibe coding без judgment = проклятый цикл на стероидах. Psychological safety reframe (кратко). |
| **Секция 3: Your new operating system** (A3+A4+N5) | 300 | 25% | Три подсекции: (a) Prompt sets as new PRDs, delegation по уровню риска, 3-4 = 30-50 teams. (b) 12-24 мес timeline, kill criteria, reversibility, circuit breakers. (c) PM+PMM fusion: distribution > production, Chesky "меньше PM, больше PMM". |
| **Close: Monday morning** | 140 | 12% | 5 concrete steps + reframe sentence |
| **Подзаголовки, переходы** | 110 | 9% | Transitions между секциями |
| **ИТОГО** | **~1200** | **100%** | |

### Распределение must-include элементов по секциям

| Секция | DATA | QUOTE | CONCEPT | KB | COUNTER | TOTAL |
|--------|------|-------|---------|----|---------| ------|
| Hook | 0 | 0 | 0 | 0 | 0 | 0 |
| Builder era (A2) | 3-4 | 2 | 3 | 1 | 1 | 10-11 |
| Judgment (A1) | 2-3 | 1-2 | 3 | 2 | 0-1 | 8-11 |
| Operating system (A3+A4+N5) | 3-4 | 2-3 | 4-5 | 1-2 | 1 | 11-15 |
| Close | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **8-11** | **5-7** | **10-11** | **4-5** | **2-3** | **~35** |

---

## ИТОГОВЫЙ BLUEPRINT ДЛЯ WRITER-а

### Структура статьи (рекомендуемая)

```
TITLE: [TBD by writer, but direction: "The PM's Practical Guide to the Vibe Coding Era"
        or "What to Do When AI Makes Building Free"
        or "Judgment, Not Features: A PM's Guide to the Builder Era"]

HOOK (120 words)
- Personal story: first vibe coding experience
- Двойственное чувство: power + existential dread
- Promise: "Here's what I learned about what PMs actually do now."

H2: THE BUILDER ERA IS HERE (280 words)
- Cherny: 100% AI code, +200% productivity
- Andreessen: "Mexican standoff" PM/eng/design
- LinkedIn APB, Meta "AI builders"
- Key reframe: full-stack builder ≠ learned to code. Full-stack builder = learned to maintain production quality.
- Honest caveat: METR study (19% slower), security flaws
- Transition: "Building faster is the easy part..."

H2: SPEED WITHOUT JUDGMENT IS THE FEATURE MILL ON STEROIDS (250 words)
- RAT formula: AI crushes denominator, numerator (judgment) dominates
- Feature mill trap: 90% resources in dead features. With AI: 10x faster waste.
- "What to build" > "how to build" (a16z)
- Business judgment defined: diagnosing WHERE in the causal chain the problem sits
- Psychological safety brief: hesitation ≠ ego, it's rational response to ambiguity
- Transition: "So what does the day-to-day look like?"

H2: YOUR NEW OPERATING SYSTEM (300 words)
Three shifts:
(a) From PRDs to prompt sets
    - Chennapragada: "prompt sets = new PRDs"
    - Delegation by risk level: AI gets low-risk, PM keeps high-risk
    - Teams shrink: Doshi "3-4 = 30-50"
(b) From one-off launches to hypothesis pipeline
    - "We're not launching products -- we're buying knowledge"
    - 12-24 month timeline to full cycle
    - Kill criteria, reversibility, circuit breakers (MtP's own Chigrinets)
(c) From inbound to full-funnel
    - Chesky: fewer PMs, more product marketing
    - Distribution > production when building is cheap
    - PM+PMM fusion: own the story from hypothesis to customer

H2: YOUR MOVE (or: MONDAY MORNING) (140 words)
- 5 concrete steps (checklist format)
- Reframe closing sentence
```

### Ключевые принципы для writer-а

1. **Голос:** First-person practitioner, не thought leader. "I tried" > "Research shows."
2. **Структура:** Short paragraphs (3-5 sentences max). Subheadings. Bullet lists where appropriate.
3. **Контраргументы:** Включать 1-2 honest caveats per section (METR study, security flaws, agent 2.5% success rate). MtP ценит honesty.
4. **Ссылки:** Inline hyperlinks, не footnotes. Каждый факт -- со ссылкой.
5. **Длина:** Жестко 1000-1200 слов. Не раздувать. Лучше под-1200, чем пере-1200.
6. **Дифференциация от старой статьи:**
   - НЕ использовать: "bifurcation", "K-shaped", "splitting in two", "two facts that shouldn't coexist"
   - НЕ начинать с цифр рынка
   - НЕ заканчивать "three-week experiment"
   - ДА: personal story hook, builder identity, operating model, Monday checklist
7. **Тон:** Urgent but not panicked. Honest but not doomer. Practical above all.
8. **KB integration:** RAT formula и "we buy knowledge, not launch products" -- two core KB concepts to weave in naturally, не как цитаты из учебника.

---

## КРАТКАЯ СВОДКА РЕШЕНИЙ

| Решение | Выбор | Альтернатива |
|---------|-------|-------------|
| Hook | Вариант A (personal story) | B (provocative question) |
| Порядок тезисов | Вариант 2: A2 -> A1 -> A3+A4+N5 | Вариант 1: A1 -> A2 -> A3 -> A4+N5 |
| Объединение тезисов | A3 + A4 + N5 в одну секцию | A4 + N5 (оставив A3 отдельно) |
| Финал | Вариант 1 (Monday checklist) | Вариант 2 (honest reflection) |
| Word budget | ~1200 слов (4 секции) | ~1400 (5 секций) |
| Количество H2 секций | 4 (builder + judgment + operating system + your move) | 5 (builder + judgment + pipeline + market + your move) |
