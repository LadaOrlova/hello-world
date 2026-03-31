# UTM-система Zamesin Academy

Единый справочник UTM-меток для всех каналов коммуникации.

---

## Формат ссылки

```
{base_url}?utm_source={source}&utm_medium={medium}&utm_campaign={campaign}&utm_content={content}
```

### Главные правила

1. **ВСЕ ссылки — с UTM.** Единственное исключение — точечные ссылки на конкретный шаг бота (deep link). К ним UTM не добавляется — сломает ссылку.

2. **При создании любого контента (пост, сторис, карточки, рассылка) — всегда спрашивать у автора:**
   - "Куда ведёшь? Пришли мне ссылку"
   - Получив ссылку — собрать к ней UTM-метку по правилам ниже
   - Никогда не вставлять ссылку без UTM

3. **Не задваивать параметры.** В ссылке должен быть только один `?`. Всё после первого параметра — через `&`. Неправильно: `?utm_source=x?utm_medium=y`. Правильно: `?utm_source=x&utm_medium=y`.

4. **Только строчные латинские буквы.** Никакого CamelCase, кириллицы, пробелов. Разделитель — нижнее подчёркивание `_`. Яндекс.Метрика и GA4 различают регистр: `Email` и `email` — два разных канала.

5. **Не ставить UTM на внутренние ссылки сайта.** UTM-метки перезаписывают источник визита. Если человек пришёл из Telegram и кликнул внутреннюю ссылку с UTM — Метрика запишет новый визит и потеряет исходный источник.

---

## utm_source — откуда пришёл

Конкретная площадка или канал, откуда пришёл пользователь.

| Значение | Канал |
|----------|-------|
| `tg_zamesin` | Telegram-канал @zamesin |
| `tg_potok` | Telegram «Поток» (канал для студентов) |
| `tg_bot` | Telegram-бот (рассылки, онбординг) |
| `email` | Email-рассылка |
| `ig` | Instagram |
| `yt` | YouTube |
| `kinescope` | Кинескоп (запись вебинара) |
| `webinar_{партнёр}` | Ссылки во время эфира. Пример: `webinar_sokolova` |
| `site` | Наш сайт (баннеры, кросс-ссылки между разделами) |
| `oldblog` | Старый блог |

---

## utm_medium — тип маркетингового канала

**Важно:** utm_medium определяет, в какой канал Яндекс.Метрика и GA4 отнесут трафик в стандартных отчётах. Используй только значения из таблицы ниже — иначе трафик попадёт в «Не определено».

| Значение | Тип канала | Когда использовать |
|----------|------------|-------------------|
| `social` | Органические соцсети | Посты, сторис, рассылки в боте, чаты — всё из Telegram, Instagram |
| `email` | Email | Любые email-рассылки |
| `video` | Видео | YouTube, Кинескоп, видео-контент |
| `display` | Баннеры и реклама | Баннеры на сайте, рекламные размещения |
| `referral` | Партнёрский трафик | Ссылки с партнёрских сайтов, QR-коды на мероприятиях |
| `cpc` | Платный поиск | Контекстная реклама (Яндекс.Директ, Google Ads) |
| `paid_social` | Платные соцсети | Таргетированная реклама в соцсетях |

---

## utm_content — формат и размещение (опционально, но рекомендуется)

Уточняет, **как именно** была показана ссылка внутри канала. Позволяет различать форматы в рамках одного source+medium.

| Значение | Что это |
|----------|---------|
| `message` | Рассылка в боте |
| `card` | Карточка / карусель |
| `text` | Текстовый пост |
| `story` | Сторис |
| `qr` | QR-код (на слайде, в карточке, в печати) |
| `chat` | Ссылка в чате вебинара |
| `start` | Первый запуск бота (онбординг) |
| `banner` | Баннер на сайте |
| `bio` | Ссылка в описании профиля |
| `description` | Ссылка в описании видео |

---

## utm_campaign — про что

Формат: `тип_название[_дата]`

| Тип | Пример | Когда |
|-----|--------|-------|
| `case_{название}` | `case_pleada` | Кейс выпускника |
| `webinar_{партнёр}_{ММДД}` | `webinar_sokolova_0320` | Вебинар |
| `announce_{событие}_{ММДД}` | `announce_webinar_sokolova_0320` | Анонс мероприятия |
| `lastcall_{событие}_{ММДД}` | `lastcall_webinar_sokolova_0320` | Последний шанс зарегистрироваться |
| `followup_{событие}_{ММДД}` | `followup_webinar_sokolova_0320` | Фоллоуап после мероприятия |
| `recording_{событие}_{ММДД}` | `recording_webinar_sokolova_0320` | Запись мероприятия |
| `launch_{продукт}{поток}` | `launch_kdp59` | Запуск потока / продукта |

---

## Воронка вебинара — полный набор меток

При проведении вебинара с партнёром нужно **заранее** подготовить UTM-метки на все этапы воронки. Ниже — шаблон. Подставь имя партнёра и дату.

**Пример: вебинар с Олей Соколовой 20 марта 2026**

### 1. Анонс (до вебинара)

| Где | source | medium | campaign | content |
|-----|--------|--------|----------|---------|
| Рассылка в боте | `tg_bot` | `social` | `announce_webinar_sokolova_0320` | `message` |
| Пост в @zamesin | `tg_zamesin` | `social` | `announce_webinar_sokolova_0320` | `text` |
| Карточка в боте | `tg_bot` | `social` | `announce_webinar_sokolova_0320` | `card` |
| Instagram сторис | `ig` | `social` | `announce_webinar_sokolova_0320` | `story` |

### 2. Последний шанс (за 1-2 дня)

| Где | source | medium | campaign | content |
|-----|--------|--------|----------|---------|
| Рассылка в боте | `tg_bot` | `social` | `lastcall_webinar_sokolova_0320` | `message` |
| Пост в @zamesin | `tg_zamesin` | `social` | `lastcall_webinar_sokolova_0320` | `text` |

### 3. Во время эфира

| Где | source | medium | campaign | content |
|-----|--------|--------|----------|---------|
| QR на слайдах | `webinar_sokolova` | `referral` | `webinar_sokolova_0320` | `qr` |
| Ссылка в чате | `webinar_sokolova` | `referral` | `webinar_sokolova_0320` | `chat` |

### 4. После вебинара (фоллоуап)

| Где | source | medium | campaign | content |
|-----|--------|--------|----------|---------|
| Рассылка в боте | `tg_bot` | `social` | `followup_webinar_sokolova_0320` | `message` |
| Email | `email` | `email` | `followup_webinar_sokolova_0320` | — |

### 5. Запись

| Где | source | medium | campaign | content |
|-----|--------|--------|----------|---------|
| YouTube (описание) | `yt` | `video` | `recording_webinar_sokolova_0320` | `description` |
| Кинескоп | `kinescope` | `video` | `recording_webinar_sokolova_0320` | — |

> **Как потом найти всё по вебинару:** фильтр в Метрике по `*sokolova*` в campaign — покажет все этапы воронки.

---

## QR-коды

### Правила генерации
1. **При создании любого контента** (карточки, пост, рассылка) — всегда спрашивать: "Нужен QR-код?"
2. Если да — генерировать QR-код со следующими параметрами:
   - **Стиль:** округлые линии (rounded), не квадратные пиксели
   - **Содержимое:** полная ссылка с UTM-меткой
   - **UTM в QR:** utm_content=qr (остальные параметры — по контексту)
3. **Где размещается:** на CTA-карточке (последней в наборе), на слайде презентации, или в сторис
4. QR-код — это самостоятельный элемент, не замена текстовой ссылки. В посте может быть и ссылка, и QR

### Пример UTM для QR
```
zamesin.ru/producthowto?utm_source=ig&utm_medium=social&utm_campaign=case_pleada&utm_content=qr
```

---

## Примеры готовых ссылок

**Кейс PLEADA → бот (карточки):**
```
zamesin.ru/producthowto?utm_source=tg_bot&utm_medium=social&utm_campaign=case_pleada&utm_content=card
```

**Фоллоуап вебинара → email-рассылка:**
```
zamesin.ru/producthowto?utm_source=email&utm_medium=email&utm_campaign=followup_webinar_sokolova_0320
```

**Анонс вебинара → Instagram сторис с QR:**
```
zamesin.ru/webinar?utm_source=ig&utm_medium=social&utm_campaign=announce_webinar_sokolova_0320&utm_content=qr
```

**Баннер на сайте → страница кейсов:**
```
zamesin.ru/producthowto?utm_source=site&utm_medium=display&utm_campaign=case_pleada&utm_content=banner
```

**Кейс → @zamesin (текстовый пост):**
```
zamesin.ru/producthowto?utm_source=tg_zamesin&utm_medium=social&utm_campaign=case_pleada&utm_content=text
```

---

## Что изменилось (март 2026)

Раньше формат контента (card, message, qr) ставился в utm_medium. Это неправильно по стандартам — Яндекс.Метрика и GA4 используют utm_medium для определения канала трафика. Нестандартные значения попадают в «Не определено».

**Было (неправильно):** `utm_medium=message`, `utm_medium=card`, `utm_medium=qr`
**Стало (правильно):** `utm_medium=social` + `utm_content=message` / `card` / `qr`

Стандартные значения utm_medium (`social`, `email`, `video`, `display`, `referral`, `cpc`) обеспечивают корректную группировку в аналитике. Детализация формата — через utm_content.
