# Changelog: что изменилось в новых драфтах v2/v3

> Этот документ описывает все изменения по кейсам и ссылкам, которые Claude внёс в новые версии статей по сравнению с Ваниными оригиналами.
> Оригиналы НЕ тронуты — новые версии лежат отдельными файлами.

---

## СТАТЬЯ 1: MtP (Mind the Product)

**Ванин оригинал:** `Draft-AI-Changes-PM-Role-MtP.md`
**Новая версия:** `Draft-AI-Changes-PM-Role-MtP-v3.md`

### Кейсы: что изменено

| Секция | У Вани | В v3 | Что сделано и почему |
|--------|--------|------|----------------------|
| T1 Builder era | Нет отдельного кейса (данные Boris Cherny + YC) | **+Spotify/Honk** (инженеры не пишут код с дек 2025, шипают с телефона) | Добавлен как наглядный кейс "builder era" — ярче чем просто статистика |
| T1 Builder era | Нет | **+Figma Shifting Roles** (70% PM-ов wireframe-ят) | Добавлен как доп. данные про размытие ролей |
| T2 Judgment | Нет кейса, только Cagan + Mehta цитаты | **+Klarna** (уволили 40% → AI обслуживание → CEO "we went too far" → наняли обратно) | Добавлен cautionary case — MtP любит cautionary tales |
| T3 Hypothesis | Ссылка на Shreyas Doshi (3-4 чел = 30-50 команд) | **+Shopify** (Tobi Lutke: докажите что AI не может → потом нанимайте) | Заменён Doshi (URL оказался 404, реальный не нашёлся) |
| T3 Hypothesis | Shreyas Doshi | **Убран Shreyas Doshi** | URL оказался фейковый (404). Утверждение "3-4 person startups" оставлено без ссылки |
| T3 Hypothesis | Boris Cherny цитата "Claude coming up with ideas" | **Убрана** | Не влезло в word budget |
| T4 Full cycle | Нет кейса | **+Replit** (AI agent удалил 1200 записей, соврал про recovery) | Добавлен как proof что production не готов |
| T5 K-split | Нет кейса | **+HBR** (AI убивает apprenticeship tasks → junior PMs не набирают judgment) | Добавлен как structural mechanism для K-split |

### Ссылки: добавленные (6 новых)

| URL | Кейс | Проверена? |
|-----|------|------------|
| techcrunch.com/2026/02/12/spotify-says-its-best-developers... | Spotify/Honk | Проверена case-hunter агентом |
| figma.com/blog/2025-shifting-roles-report/ | Figma | Проверена case-hunter агентом |
| tech.co/news/klarna-reverses-ai-overhaul | Klarna | Проверена case-hunter агентом |
| techcrunch.com/2025/04/07/shopify-ceo-tells-teams... | Shopify | Проверена case-hunter агентом |
| fortune.com/2025/07/23/ai-coding-tool-replit... | Replit | Проверена case-hunter агентом |
| hbr.org/2026/02/how-do-workers-develop-good-judgment... | HBR | Проверена case-hunter агентом |

### Ссылки: сохранённые из Ваниного драфта (8)

| URL | Кейс |
|-----|------|
| lennysnewsletter.com/p/head-of-claude-code-what-happens | Boris Cherny |
| techcrunch.com/2025/03/06/...yc-codebases... | YC W25 |
| theguardian.com/...vibe-coding... | Collins WotY |
| lennysnewsletter.com/p/marc-andreessen-the-real-ai-boom | Andreessen |
| lennysnewsletter.com/p/why-linkedin-is-replacing-pms | LinkedIn |
| svpg.com/product-coaching-and-ai/ | Cagan |
| atlassian.com/blog/.../shift-from-craft-to-judgement-ai | Mehta |
| weforum.org/stories/2025/10/... | WEF |

### Ссылки: убранные

Только Shreyas Doshi (ссылки у Вани не было, а фейковый URL был пойман и удалён).

### Хук: заменён

**У Вани:** "Over the past three months, I built 20 products with vibe coding..." (личный опыт)
**В v3:** "Vibe coding makes it trivially easy to ship..." (tension/paradox) + why-now данные (LinkedIn, Collins, YC)

**Почему:** MtP стилистически предпочитает tension hook, и ТЗ говорило что статья должна отличаться от версии SGG. Ванин хук сохранён как альтернатива Hook B в конце файла.

---

## СТАТЬЯ 2: HackerNoon (PMF)

**Ванин оригинал:** `Draft-How-to-Find-PMF-Fast-and-Pivot-the-Right-Way.md`
**Новая версия:** `Draft-How-to-Find-PMF-Fast-v2.md`

### Кейсы: что изменено

| Секция | У Вани | В v2 | Что сделано и почему |
|--------|--------|------|----------------------|
| Hook | **Lovable** ($200M ARR, Elena Verna "perishable good") | **Убран** → заменён paradox hook | Lovable сохранён как альтернативный Hook B в конце файла |
| T1 | **Notion** (V1, Kyoto, $10B) | **Оставлен** без изменений | Ванин кейс, не тронут |
| T2 | **Wispr Flow** (hardware → dictation, 20%, $81M) | **Оставлен**, убран только "$81M" и ссылка на TechCrunch fundraising | Упрощён, ссылка на PH осталась |
| T3 | **EnrichLead** (100% AI-coded, collapsed 72h) | **Заменён на Moltbook** (1.5M API keys exposed, янв 2026, vibe-coded) | Свежее (янв 2026 vs 2025), крупнее масштаб, верифицирован Wiz Research |
| T3 | **METR study** + **2 статьи arXiv** | **Восстановлен METR**, убраны оба arXiv | Ваня сам убрал METR в своём обновлении, восстановлен т.к. сильный data point. arXiv убраны — word budget |
| T4 | **Popsa** + **Elena Verna** + **Spotify** (520 experiments) | **Восстановлен Popsa** + **добавлен Booking.com** (25K experiments/yr) | Ваня сам убрал Popsa/Spotify/Elena в своём обновлении. Popsa восстановлен (яркий proof формулы), Spotify заменён на Booking.com (масштабнее) |
| T5 | **Jasper AI** ($120M→$35M) + Elena Verna | **Оставлен Jasper** + **добавлен Chegg** ($15B→99% drop) | Chegg усиливает тезис "в каждом рынке" — другая индустрия, тот же паттерн |

### Ссылки: добавленные (5 новых)

| URL | Кейс | Проверена? |
|-----|------|------------|
| wiz.io/blog/exposed-moltbook-database... | Moltbook | WebFetch — ОК, но Moltbook НЕ умер (исправлено в тексте) |
| metr.org/blog/2025-07-10-... | METR study | Была у Вани в v1, он убрал, восстановлена. URL из его же Sources |
| hbr.org/2020/03/building-a-culture-of-experimentation | Booking.com | Проверена case-hunter агентом |
| review.firstround.com/founder-led-growth-playbook/ | Popsa | Была у Вани в v1, он убрал, восстановлена. URL из его же Sources |
| cnbc.com/2025/10/27/chegg-slashes-45percent... | Chegg | Проверена через WebSearch (45% layoffs, 99% drop подтверждено) |

### Ссылки: сохранённые из Ваниного драфта (5)

| URL | Кейс |
|-----|------|
| figma.com/blog/...notion... | Notion |
| whatastartup.substack.com/p/...notion... | Notion |
| producthunt.com/p/wisprflow/... | Wispr Flow |
| research.contrary.com/company/jasper | Jasper AI |
| elenaverna.com/p/the-product-market-fit-treadmill | Elena Verna |

### Ссылки: убранные (11)

| URL | Почему |
|-----|--------|
| elenaverna.com/p/6-months-at-lovable... | Hook заменён, Lovable в alt hook B |
| lennysnewsletter.com/p/the-new-ai-growth-playbook... | Word budget |
| techcrunch.com/2025/06/24/wispr-flow-raises-30m... | Убраны детали про $81M |
| ruinunes.com/vibe-coding-trap-ai-built-mvp/ | EnrichLead → заменён на Moltbook |
| techstartups.com/2025/12/11/... | Вторая ссылка EnrichLead |
| arxiv.org/abs/2512.19644 | arXiv (word budget) |
| arxiv.org/abs/2512.22418 | arXiv (word budget) |
| arxiv.org/abs/2601.10258 | arXiv (word budget) |
| engineering.atspotify.com/2025/9/... | Spotify → заменён на Booking.com |
| infoq.com/news/2025/12/... | Вторая ссылка Spotify |
| sqmagazine.co.uk/jasper-ai-statistics/ | Вторая ссылка Jasper |

### Хук: заменён

**У Вани:** Lovable $200M ARR + Elena Verna "perishable good" (story-driven)
**В v2:** "Building has never been cheaper. Killing a startup has never been easier." (tension/paradox)

**Почему:** Narrative-architect рекомендовал для HackerNoon contrarian hook. Ванин хук сохранён как альтернатива Hook B с обновлённой цифрой ($300M ARR).

### Фактчек-правки

1. **Moltbook:** Было "The company died" → исправлено на "Users paid the price" (Moltbook починил баг и выжил)
2. **Chegg:** Было "$12B" → исправлено на "peaked near $15B" (реальный пик ~$14.7B); было "87.5% drop" → исправлено на "99%" (верифицировано через CNBC)

---

## Как пользоваться этим документом

Ваня может пройтись по таблицам и отметить:
- ✅ — кейс/ссылка ОК, оставляем
- ❌ — кейс не подходит по логике, откатываем к оригиналу
- 🔄 — нужна другая замена

После фидбэка — точечно внесём правки в v2/v3 файлы.
