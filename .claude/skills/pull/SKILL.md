---
name: pull
description: Стянуть изменения из git remote. Обрабатывает все конфликтные ситуации автоматически (unstaged changes, diverged branches, merge conflicts).
user-invocable: true
---

# Skill: Git Pull

Стянуть все изменения из remote-репозитория в локальную ветку. Скилл автоматически обрабатывает все проблемные ситуации.

---

## АЛГОРИТМ

Выполни шаги строго по порядку. Каждый шаг — одна команда Bash.

### Шаг 1: Проверь текущее состояние

```bash
git status --short -u
```

Запомни результат — он определит, какой путь дальше.

### Шаг 2: Стяни изменения

**Если есть незакоммиченные изменения (modified/untracked файлы):**

```bash
git stash --include-untracked && git pull --rebase && git stash pop
```

**Если рабочая директория чистая:**

```bash
git pull --rebase
```

### Шаг 3: Обработка ошибок

**Если `git stash pop` дал конфликт:**
1. Выполни `git diff` чтобы увидеть конфликты
2. Для каждого конфликтного файла: прочитай файл, разреши конфликт вручную (сохрани обе версии изменений, объединив логически)
3. `git add <conflicted-files>`
4. `git stash drop`

**Если `git pull --rebase` дал конфликт:**
1. Выполни `git diff` чтобы увидеть конфликты
2. Для каждого конфликтного файла: прочитай файл, разреши конфликт (сохрани обе версии, объединив логически)
3. `git add <conflicted-files>`
4. `git rebase --continue`

**Если `git pull --rebase` говорит "divergent branches":**

```bash
git pull --rebase --autostash
```

**Если remote ветка не настроена:**

```bash
git branch --set-upstream-to=origin/main main && git pull --rebase
```

### Шаг 4: Подтверди результат

```bash
git log --oneline -3
```

Выведи пользователю: какие коммиты пришли с remote, и текущий статус.

---

## ПРАВИЛА

- НИКОГДА не делай `git pull` без `--rebase` — это создаёт merge-коммиты
- НИКОГДА не теряй локальные изменения — всегда stash перед pull
- Если stash pop конфликтует — РАЗРЕШИ конфликт, не дропай stash с потерей данных
- Используй `--include-untracked` в stash чтобы не потерять новые файлы
- Если что-то идёт совсем не так — останови и спроси пользователя, НЕ делай `git reset --hard`
