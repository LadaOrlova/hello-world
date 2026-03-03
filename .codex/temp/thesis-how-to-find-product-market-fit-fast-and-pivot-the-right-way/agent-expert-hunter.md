# Agent Report — expert-hunter

**Глава:** How to Find Product-Market Fit Fast — and Pivot the Right Way  
**Дата:** 2026-03-02  
**Требования к источникам:** внешние источники >= 2025-06-01; приоритет last 3 months (2025-12-02…2026-03-02).

Ниже — отобранные источники (с датой) и **🆕 новые тезисы**, которые расширяют авторское поле.

---

## Часть 1 — Карта источников (с URL, датой, tier)

### Tier 2 (VC / аналитика)

1) **a16z — “The Cinderella ‘Glass Slipper’ Effect: Retention Rules in the AI Era”**  
   - **Автор/cred:** Malika Aubakirova (a16z AI Infrastructure)  
   - **Дата:** 2025-12-08 (**Last 3 months**)  
   - **URL:** https://a16z.com/the-cinderella-glass-slipper-effect-retention-rules-in-the-ai-era/  
   - **Ключевой тезис:** в AI «фундаментальная» когорта пользователей может сформироваться сразу на запуске (workload-model fit), а более поздние когорты будут «туристами» и отвалятся; удержание и когорты становятся early‑PMF сигналом.

2) **a16z — “State of Consumer AI 2025: Product Hits, Misses, and What’s Next”**  
   - **Авторы/cred:** Olivia Moore, Justine Moore (a16z)  
   - **Дата:** 2025-12-18 (**Last 3 months**)  
   - **URL:** https://a16z.com/state-of-consumer-ai-2025-product-hits-misses-and-whats-next/  
   - **Ключевой тезис:** потребители концентрируются на одном ассистенте; метрики engagement/retention и подписки сконцентрированы (напр., выводы на базе Yipit/SensorTower в тексте).

3) **a16z — “Retention Is All You Need” (AI retention benchmarks)**  
   - **Авторы/cred:** Santiago Rodriguez, Alex Immerman (a16z Growth)  
   - **Дата:** 2025-09-10 (>=2025-06-01)  
   - **URL:** https://a16z.com/ai-retention-benchmarks/  
   - **Ключевой тезис:** для AI‑продуктов из‑за «AI tourists» лучше смещать оценку удержания к M3 (а не M0/M1) и смотреть на поведение “survivor cohort” как ранний сигнал PMF.

### Tier 1 (эксперт/интервью + первичный контент)

4) **Lenny’s Podcast — “The new AI growth playbook for 2026: How Lovable hit $200M ARR…” (Elena Verna)**  
   - **Автор/cred:** Elena Verna (Head of Growth at Lovable; ex Dropbox/Miro/SurveyMonkey), интервью у Lenny Rachitsky  
   - **Дата:** 2025-12-18 (**Last 3 months**)  
   - **URL:** https://www.lennysnewsletter.com/p/the-new-ai-growth-playbook-for-2026-elena-verna  
   - **Ключевой тезис:** 60–70% старого growth‑плейбука не работает в AI‑категориях; PMF нужно «перенаходить» каждые ~3 месяца; ставка на инновации вместо оптимизаций.

5) **Spotify Engineering — “Beyond Winning: Spotify’s Experiments with Learning Framework”**  
   - **Автор/cred:** Spotify Engineering  
   - **Дата (в URL):** 2025-09 (>=2025-06-01)  
   - **URL:** https://engineering.atspotify.com/2025/9/spotifys-experiments-with-learning-framework  
   - **Ключевой тезис:** ценность экспериментов — не «win rate», а “learning rate”; “нейтральные, но мощные” эксперименты тоже дают знание. Это напрямую усиливает тезис автора про «качество проверки гипотез».

### Academic (доказательная база рисков AI‑кодинга)

6) **arXiv — “Building Software by Rolling the Dice: A Qualitative Study of Vibe Coding”**  
   - **Авторы:** Yi‑Hung Chou et al.  
   - **Дата (submitted):** 2025-12-27 (**Last 3 months**)  
   - **URL:** https://arxiv.org/abs/2512.22418  
   - **Ключевой тезис:** vibe‑coding — спектр практик; общий риск — стохастичность генерации (“rolling the dice”), нагрузка на отладку/оценку и разные ментальные модели.

7) **arXiv — “More code, less validation: Risk factors for over-reliance on AI coding tools…”**  
   - **Авторы:** Gabrielle O’Brien et al.  
   - **Дата (submitted):** 2025-12-22 (**Last 3 months**)  
   - **URL:** https://arxiv.org/abs/2512.19644  
   - **Ключевой тезис:** perceived productivity коррелирует с «сколько строк принимают за раз», а не с практиками валидации; риск “больше кода — меньше проверки”.

8) **arXiv — “AI Code in the Wild: Measuring Security Risks and Ecosystem Shifts of AI-Generated Code…”**  
   - **Авторы:** Bin Wang et al.  
   - **Дата (submitted):** 2025-12-21 (**Last 3 months**)  
   - **URL:** https://arxiv.org/abs/2512.18567  
   - **Ключевой тезис:** AI‑код концентрируется в glue/tests/refactor/docs; есть измеримые security‑последствия и «шаблонные» уязвимости, которые распространяются через модели.

9) **arXiv — “Comment Traps: How Defective Commented-out Code…”**  
   - **Авторы:** Yuan Huang et al.  
   - **Дата (submitted):** 2025-12-23 (**Last 3 months**)  
   - **URL:** https://arxiv.org/abs/2512.20334  
   - **Ключевой тезис:** дефектный commented‑out код в контексте повышает дефекты в генерации (Copilot/Cursor) и плохо “отключается” инструкциями.

10) **arXiv — “Evolving with AI: A Longitudinal Analysis of Developer Logs”**  
   - **Авторы:** Agnia Sergeyuk et al.  
   - **Дата (submitted):** 2026-01-15 (**Last 3 months**)  
   - **URL:** https://arxiv.org/abs/2601.10258  
   - **Ключевой тезис:** при устойчивом использовании AI‑ассистентов люди пишут больше кода и больше удаляют; AI меняет workflow не только «в +скорость».

11) **arXiv — “Beyond the Commit: Developer Perspectives on Productivity with AI Coding Assistants”**  
   - **Авторы:** Valerie Chen et al.  
   - **Дата (submitted):** 2026-02-03 (**Last 3 months**)  
   - **URL:** https://arxiv.org/abs/2602.03593  
   - **Ключевой тезис:** “продуктивность” с AI нужно мерить многомерно; важны долгосрочные факторы (экспертиза, ownership), а не только скорость выполнения задач.

---

## Часть 2 — 🆕 НОВЫЕ ТЕЗИСЫ (которые расширяют авторское поле)

### 🆕 N1 — PMF становится «тредмиллом» в AI‑категориях: ты его не находишь один раз, ты его пере‑находишь каждые ~3 месяца

**Источник:** Elena Verna в Lenny’s Podcast (2025-12-18) — https://www.lennysnewsletter.com/p/the-new-ai-growth-playbook-for-2026-elena-verna  
**Суть:** из‑за быстрого сдвига возможностей моделей и ожиданий пользователей, “fit” может «истекать». Стратегия «нашли → оптимизируем → масштабируем» становится ловушкой: нужно параллельно держать контур инноваций и контур оптимизаций.  
**Почему автор мог не упомянуть:** это более «growth/market dynamics» угол, а не discovery‑процесс как таковой.  
**Спорит/дополняет:** усиливает A4/A5 (конвейер гипотез), но добавляет «почему конвейер должен быть perpetual», а не только до первого PMF.

### 🆕 N2 — Для AI‑продуктов ранний PMF может проявляться как “foundational cohort”, а не как “MVP‑churn‑iterate”

**Источник:** a16z “Cinderella Glass Slipper effect” (2025-12-08) — https://a16z.com/the-cinderella-glass-slipper-effect-retention-rules-in-the-ai-era/  
**Суть:** если продукт/модель решает один высокоценный workload «лучше всех», формируется когорта, которая удерживается аномально хорошо; последующие когорты могут быть более «туристическими». Это меняет диагностику PMF: искать не средний retention, а “кто нашёл стеклянную туфельку и почему”.  
**Почему автор мог не упомянуть:** автор фокусируется на цикле гипотез, а здесь — на когортной механике удержания как сигнала fit.

### 🆕 N3 — “AI tourists” ломают привычные метрики удержания: PMF лучше мерить после первичной волны «туризма» (например, M3‑база)

**Источник:** a16z “Retention Is All You Need” (2025-09-10) — https://a16z.com/ai-retention-benchmarks/  
**Суть:** если в первых неделях много «попробовал и ушёл», M0/M1 retention может выглядеть ужасно и вводить в заблуждение; оценка после M3 лучше отделяет core‑пользователей от туристов.  
**Почему автор мог не упомянуть:** это «метрический» слой, но он критичен, чтобы конвейер гипотез не оптимизировал шум.

### 🆕 N4 — Vibe‑coding не “ускоритель разработки”, а стохастическая со‑разработка: главный скилл — управление доверия/проверки, а не “написать больше кода”

**Источник:** arXiv 2512.22418 (submitted 2025-12-27) — https://arxiv.org/abs/2512.22418  
**Суть:** практики vibe‑coding лежат на спектре от слепой делегации до совместного контроля; отладка и оценка становятся центральным узким местом (“rolling the dice”). Это влияет на PMF‑цикл: дешёвый билд без дисциплины валидации может давать ложные выводы.  
**Спорит/дополняет:** дополняет A1/A4 и создаёт мост к A5: «система проверки» становится важнее «скорости генерации».

### 🆕 N5 — Риск “more code, less validation”: AI подталкивает принимать крупные куски кода и измерять успех “объёмом”, а не проверкой

**Источник:** arXiv 2512.19644 (submitted 2025-12-22) — https://arxiv.org/abs/2512.19644  
**Суть:** perceived productivity растёт вместе с количеством принятого за раз AI‑кода; отсутствие практик тестирования/ревью усиливает иллюзию скорости. Для PMF это означает: можно “быстро показать демо” и получить шум вместо сигнала.  
**Спорит/дополняет:** контринтуитивный ограничитель к A1.

### 🆕 N6 — AI‑код несёт системные security‑и quality‑риски: уязвимости могут «переиспользоваться» как шаблоны между проектами

**Источник:** arXiv 2512.18567 (submitted 2025-12-21) — https://arxiv.org/abs/2512.18567  
**Суть:** AI‑код чаще появляется в glue/tests/refactor/docs, но создаёт экосистемные эффекты: повторяющиеся небезопасные шаблоны и уязвимости могут «расползаться» через одинаковые модели. Это важно для ранней стадии: “быстро собрать” ≠ “безопасно продавать”, особенно если интервью превращаются в ранние production‑инстансы.

