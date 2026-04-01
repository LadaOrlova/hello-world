---
name: push
description: Закоммитить ВСЕ незакоммиченные файлы и запушить в remote. Обрабатывает все ситуации автоматически (unstaged, untracked, remote ahead, diverged branches).
user-invocable: true
---

# Skill: Git Push

Закоммитить ВСЕ незакоммиченные изменения (modified, deleted, untracked) и запушить в remote. Скилл автоматически обрабатывает все проблемные ситуации.

---

## АЛГОРИТМ

Выполни шаги строго по порядку.

### Шаг 1: Проверь состояние

```bash
git status --short -u
```

Если нет изменений — скажи пользователю «Нечего коммитить, всё чисто» и завершись.

### Шаг 2: Посмотри стиль коммитов

```bash
git log --oneline -5
```

Коммит-месседжи пишутся на РУССКОМ языке. Формат: глагол в инфинитиве + суть изменений. Примеры:
- «Добавить расшифровки созвонов 31.03-01.04»
- «Обновить TODO и идеи для NewKDP»
- «Удалить устаревшие файлы DEMO-Workshop»

### Шаг 3: Проанализируй изменения

```bash
git diff --stat
```

Посмотри на все изменённые, удалённые и новые файлы. Сгруппируй по смыслу для коммит-месседжа.

### Шаг 4: Добавь ВСЕ файлы и закоммить

```bash
git add -A && git commit -m "$(cat <<'EOF'
<коммит-месседж на русском>

<если файлов много — краткий список что добавлено/изменено/удалено>

Co-Authored-By: Claude Opus 4.6 (1M context) <noreply@anthropic.com>
EOF
)"
```

**ВАЖНО:**
- Используй `git add -A` чтобы добавить ВСЕ: modified, deleted, untracked
- Коммит-месседж ВСЕГДА через HEREDOC (для корректного форматирования)
- ВСЕГДА добавляй Co-Authored-By в конце

### Шаг 5: Запушь с обработкой ошибок

```bash
git push
```

**Если push rejected (remote ahead):**

```bash
git pull --rebase && git push
```

**Если pull --rebase при push дал конфликт:**
1. `git diff` — посмотри конфликты
2. Прочитай каждый конфликтный файл, разреши конфликт (объедини обе версии логически)
3. `git add <файлы>`
4. `git rebase --continue`
5. `git push`

**Если pull --rebase говорит "unstaged changes":**

```bash
git stash --include-untracked && git pull --rebase && git stash pop && git push
```

**Если stash pop дал конфликт:**
1. Разреши конфликты вручную (прочитай файлы, объедини изменения)
2. `git add <файлы>`
3. `git stash drop`
4. `git push`

**Если remote ветка не настроена:**

```bash
git push -u origin main
```

**Если "divergent branches":**

```bash
git pull --rebase --autostash && git push
```

### Шаг 6: Подтверди результат

```bash
git status --short && git log --oneline -1
```

Выведи пользователю: хэш коммита, что было закоммичено, что push прошёл успешно.

---

## ПРАВИЛА

- ВСЕГДА коммить ВСЕ файлы (`git add -A`). Не спрашивай, какие файлы коммитить — коммить всё
- НИКОГДА не пропускай файлы с кириллическими именами — `git add -A` их подхватывает
- Коммит-месседж на РУССКОМ языке
- ВСЕГДА добавляй Co-Authored-By
- Если push отклонён — СНАЧАЛА pull --rebase, ПОТОМ push. Не делай force push
- Если что-то идёт совсем не так — останови и спроси пользователя, НЕ делай `git push --force`
- НИКОГДА не делай `--no-verify`, `--force`, `git reset --hard`
