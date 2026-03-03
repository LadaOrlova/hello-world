# Agent Requests

## Topic Lock (v1)

- **Главный вопрос статьи:** Как найти PMF быстрее и пивотиться точнее, если AI резко удешевил прототипирование и ускорил цикл проверки гипотез?
- **In-scope:**
  - PMF как континуум + «алгоритм» движения к нему.
  - Risk Assumption Test / hypothesis pipeline как операционная система.
  - JTBD-оптика: сегмент → job → ценность → proof → экономика → канал.
  - AI/vibe-coding как фактор, меняющий порядок discovery/delivery (но не отменяющий законы).
  - Пивоты: когда, куда, по каким сигналам.
- **Out-of-scope:**
  - Детальный гайд по написанию продакшен-кода/архитектуре.
  - Конкретные туториалы по отдельным AI-инструментам разработки.
  - Growth-механики «после PMF» (масштабирование платных каналов и т.п.) — только как контекст.
- **Тип ценности:** стратегия + алгоритм + контринтуиция + практические шаги и анти-паттерны.

---

## handoff: knowledge-researcher
- status: done
- asks:
  - [ ] Связать тезисы A1–A6 с конкретными механиками из Knowledge Base (RAT, AJTBD, segmentation, validate value, интервью, launch).
  - [ ] Дать точные цитаты (1–3) и полный путь к файлу для каждого «усиливающего» фрагмента.
  - [ ] Отдельно: какие KB-механики помогают **пивотиться** (сигналы, критерии, как не путать локальный/глобальный оптимум).

**Результат (см. `agent-knowledge-researcher.md`):**
- RAT: «мы покупаем знания», «безжалостный селекционер», приоритизация по цене ошибки/стоимости проверки — `1-Context/AURA-Theses/RAT/risk-assumption-test.md`.
- Launch algorithm: «цель — убить продукт», PMF как градиент, Traction Map — `1-Context/AURA-Theses/Algorithms/launch-product.md`.
- Sales validation: «решенческие интервью» итерациями по 6, pivot как смена конкретных assumptions — `1-Context/AURA-Theses/HowTos/validate-value.md`.
- Jobs/segmentation: «работы первичны», «выбрал работу = выбрал судьбу» — `1-Context/AURA-Theses/AJTBD/fundamentals.md`, `1-Context/AURA-Theses/AJTBD/segmentation.md`.
- Pivot vs optimize: local vs global optimum — `1-Context/AURA-Theses/AURA/local-vs-global-optimum.md`.

## handoff: expert-hunter
- status: done
- asks:
  - [ ] Найти 5–7 свежих источников (>= 2025-06-01; ≥80% из 2025-12-02…2026-03-02) от tier-1/2 авторов про: PMF measurement, pivoting, discovery with AI, learning velocity vs build velocity.
  - [ ] Вытащить 3–6 🆕 новых тезисов, которые реально меняют понимание (а не «ещё один совет»).
  - [ ] Для каждого источника: автор/credentials, ключевой тезис, URL, дата (YYYY-MM-DD), tier.

**Результат (см. `agent-expert-hunter.md`):**
- Tier-1/2: a16z (retention/cohorts), Elena Verna (AI growth playbook 2026), Spotify (learning framework).
- Academic evidence: arXiv (vibe-coding qualitative, over-reliance on AI tools, security risks, comment traps, longitudinal logs, productivity perspectives).
- 🆕 тезисы: PMF treadmill (перенаходить), foundational cohort / Cinderella effect, “AI tourists” и M3 retention, vibe-coding как стохастическая co-dev + риск “more code, less validation”.

## handoff: contrarian
- status: done
- asks:
  - [ ] Сильные контраргументы к A1–A6 (>= 2025-06-01, с URL и датой).
  - [ ] Что изменилось после 2025-06-01 в теме PMF/pivot/discovery из-за AI (новые риски, новые иллюзии, новые anti-signals).
  - [ ] Превратить 2–5 контраргументов в самостоятельные 🆕 тезисы (contrarian) — с источниками.

**Результат (см. `agent-contrarian.md`):**
- Контраргументы с источниками: METR (AI productivity illusion), a16z (cohort/retention nuance), arXiv (vibe-coding stochastic + over-reliance/validation debt), The Verge (AI rollback).
- 🆕 contrarian тезисы: `validation bandwidth` как новая валюта, cohort-aware “kill fast”, product theater риск.

---

## challenge-to-knowledge
- KB тянет к “MVP как щуп без продукта”, а автор хочет показывать working product. Нужно явно описать, когда прототип обязателен, а когда лучше продавать/валидировать без продукта (чтобы не тестировать UX-артефакты вместо ценности).

## challenge-to-expert
- Усилить связь AI‑источников с “pivot the right way”: как cohort noise / AI tourists меняют критерии решения “pivot vs iterate” и горизонты сигналов (M3 vs early).
