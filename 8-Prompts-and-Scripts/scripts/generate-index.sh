#!/bin/bash
# Обновляет index.md — карту репозитория с осмысленными описаниями файлов.
# Для новых/изменённых файлов генерирует описания через OpenRouter API.
# Для неизменённых файлов сохраняет существующие описания.
#
# Использование:
#   bash 8-Prompts-and-Scripts/scripts/generate-index.sh              — обновить только изменённые файлы
#   bash 8-Prompts-and-Scripts/scripts/generate-index.sh --full       — перегенерировать все описания
#   bash 8-Prompts-and-Scripts/scripts/generate-index.sh --structure  — обновить только структуру (без AI)

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
INDEX_FILE="$REPO_ROOT/index.md"
DESCRIPTIONS_FILE="$REPO_ROOT/.index-descriptions.json"
MODE="${1:-}"

cd "$REPO_ROOT"

# --- Загрузка API ключа ---
OPENROUTER_API_KEY="${OPENROUTER_API_KEY:-}"
if [ -z "$OPENROUTER_API_KEY" ] && [ -f "$REPO_ROOT/.env" ]; then
  OPENROUTER_API_KEY=$(grep '^OPENROUTER_API_KEY=' "$REPO_ROOT/.env" | cut -d'=' -f2-)
fi

# --- Файл описаний (JSON-like, key=value) ---
# Хранит описания в простом формате: path<TAB>description
# Этот файл коммитится в репо и сохраняет описания между запусками.

touch "$DESCRIPTIONS_FILE"

get_description() {
  local path="$1"
  grep -F "	" "$DESCRIPTIONS_FILE" 2>/dev/null | grep "^${path}	" | head -1 | cut -f2-
}

set_description() {
  local path="$1"
  local desc="$2"
  # Удаляем старую запись и добавляем новую
  grep -v "^${path}	" "$DESCRIPTIONS_FILE" > "${DESCRIPTIONS_FILE}.tmp" 2>/dev/null || true
  echo -e "${path}\t${desc}" >> "${DESCRIPTIONS_FILE}.tmp"
  mv "${DESCRIPTIONS_FILE}.tmp" "$DESCRIPTIONS_FILE"
}

# --- Определяем изменённые файлы ---
get_changed_files() {
  if [ "$MODE" = "--full" ]; then
    # Все .md файлы
    find . -name '*.md' -not -path './.git/*' -not -path './node_modules/*' \
      -not -name 'index.md' -not -name 'CLAUDE.md' -not -name '.gitkeep' | sed 's|^./||' | sort
  else
    # Только изменённые в последнем коммите
    git diff --name-only HEAD~1 HEAD 2>/dev/null | grep '\.md$' | grep -v 'index.md' | grep -v 'CLAUDE.md' || true
    # Плюс новые файлы без описаний
    find . -name '*.md' -not -path './.git/*' -not -path './node_modules/*' \
      -not -name 'index.md' -not -name 'CLAUDE.md' | sed 's|^./||' | while read -r f; do
      existing=$(get_description "$f")
      if [ -z "$existing" ]; then
        echo "$f"
      fi
    done
  fi | sort -u
}

# --- Генерация описания через OpenRouter API ---
generate_description() {
  local filepath="$1"
  local content

  if [ ! -f "$filepath" ]; then
    return
  fi

  # Берём первые 150 строк файла (достаточно для понимания сути)
  content=$(head -150 "$filepath" 2>/dev/null | cut -c1-500)

  if [ -z "$content" ]; then
    echo "(пустой файл)"
    return
  fi

  if [ -z "$OPENROUTER_API_KEY" ]; then
    # Без API — извлекаем заголовок
    local title
    title=$(grep -m1 '^#' "$filepath" 2>/dev/null | sed 's/^#\+ *//')
    echo "${title:-Без описания}"
    return
  fi

  # Экранируем контент для JSON
  local escaped_content
  escaped_content=$(echo "$content" | python3 -c "import sys,json; print(json.dumps(sys.stdin.read()))" 2>/dev/null || echo '""')

  local response
  response=$(curl -s --max-time 30 "https://openrouter.ai/api/v1/chat/completions" \
    -H "Authorization: Bearer $OPENROUTER_API_KEY" \
    -H "Content-Type: application/json" \
    -d "{
      \"model\": \"anthropic/claude-haiku\",
      \"max_tokens\": 200,
      \"messages\": [{
        \"role\": \"user\",
        \"content\": \"Напиши 1-2 предложения на русском языке, кратко описывающие содержимое этого файла. Отвечай ТОЛЬКО описанием, без кавычек и префиксов. Файл: ${filepath}\n\n${escaped_content}\"
      }]
    }" 2>/dev/null)

  local desc
  desc=$(echo "$response" | python3 -c "import sys,json; r=json.load(sys.stdin); print(r.get('choices',[{}])[0].get('message',{}).get('content',''))" 2>/dev/null || echo "")

  if [ -n "$desc" ] && [ "$desc" != "null" ]; then
    # Убираем переносы строк, лишние пробелы
    echo "$desc" | tr '\n' ' ' | sed 's/  */ /g' | sed 's/^ //;s/ $//' | cut -c1-250
  else
    # Фоллбэк — заголовок файла
    local title
    title=$(grep -m1 '^#' "$filepath" 2>/dev/null | sed 's/^#\+ *//')
    echo "${title:-Без описания}"
  fi
}

# --- Обновляем описания изменённых файлов ---
if [ "$MODE" != "--structure" ]; then
  changed_files=$(get_changed_files)

  if [ -n "$changed_files" ]; then
    echo "Обновляю описания для изменённых файлов..."
    echo "$changed_files" | while read -r filepath; do
      if [ -f "$filepath" ]; then
        echo "  → $filepath"
        desc=$(generate_description "$filepath")
        if [ -n "$desc" ]; then
          set_description "$filepath" "$desc"
        fi
      fi
    done
  else
    echo "Нет изменённых файлов для обновления описаний."
  fi
fi

# --- Генерируем index.md ---

# Вспомогательная функция: получить описание файла (из кеша или заголовка)
file_desc() {
  local path="$1"
  local desc
  desc=$(get_description "$path")
  if [ -n "$desc" ]; then
    echo "$desc"
  else
    # Фоллбэк — заголовок файла
    grep -m1 '^#' "$path" 2>/dev/null | sed 's/^#\+ *//' || echo ""
  fi
}

# Вспомогательная функция: описание папки из README
dir_desc() {
  local dir="$1"
  if [ -f "${dir}/README.md" ]; then
    grep -v '^#' "${dir}/README.md" 2>/dev/null | grep -v '^$' | head -1 | sed 's/^[[:space:]]*//' | cut -c1-200
  fi
}

# Начинаем генерацию
cat > "$INDEX_FILE" << 'HEADER'
# Index

Карта репозитория с описанием каждого файла. Обновляется автоматически при каждом пуше в main — для изменённых файлов описания генерируются через AI.

## Разделы

HEADER

# Таблица разделов верхнего уровня
echo "| Папка | Что внутри |" >> "$INDEX_FILE"
echo "|-------|-----------|" >> "$INDEX_FILE"

# Собираем описания верхних папок
find . -maxdepth 1 -type d \
  -not -path '.' \
  -not -path './.git' \
  -not -path './.github' \
  -not -path './.claude' \
  -not -path './scripts' \
  -not -path './node_modules' \
  | sort | sed 's|^./||' | while read -r top_dir; do
    desc=$(dir_desc "$top_dir")
    desc=$(get_description "_dir_:${top_dir}")
    if [ -z "$desc" ]; then
      desc=$(dir_desc "$top_dir")
    fi
    echo "| \`${top_dir}/\` | ${desc:-—} |" >> "$INDEX_FILE"
  done

echo "" >> "$INDEX_FILE"
echo "---" >> "$INDEX_FILE"
echo "" >> "$INDEX_FILE"

# --- Детальные секции ---

# Рекурсивная функция для вывода содержимого папки
output_dir_contents() {
  local dir="$1"
  local heading_level="$2"
  local heading_prefix=""

  for ((i=0; i<heading_level; i++)); do heading_prefix="${heading_prefix}#"; done

  # Подпапки
  find "$dir" -maxdepth 1 -type d -not -path "$dir" | sort | while read -r subdir; do
    local subname
    subname=$(basename "$subdir")
    local sub_rel="${subdir#./}"
    local sub_desc
    sub_desc=$(get_description "_dir_:${sub_rel}")
    if [ -z "$sub_desc" ]; then
      sub_desc=$(dir_desc "$subdir")
    fi

    echo "" >> "$INDEX_FILE"
    if [ -n "$sub_desc" ]; then
      echo "${heading_prefix} ${sub_rel}/" >> "$INDEX_FILE"
      echo "" >> "$INDEX_FILE"
      echo "${sub_desc}" >> "$INDEX_FILE"
    else
      echo "${heading_prefix} ${sub_rel}/" >> "$INDEX_FILE"
    fi
    echo "" >> "$INDEX_FILE"

    # Файлы в подпапке
    find "$subdir" -maxdepth 1 -type f \
      -not -name '.DS_Store' -not -name '.gitkeep' -not -name 'README.md' \
      -not -name '*.png' -not -name '*.jpg' -not -name '*.jpeg' -not -name '*.gif' -not -name '*.svg' \
      | sort | while read -r file; do
        local fname
        fname=$(basename "$file")
        local frel="${file#./}"
        local fdesc
        fdesc=$(file_desc "$frel")
        if [ -n "$fdesc" ]; then
          echo "- \`${fname}\` — ${fdesc}" >> "$INDEX_FILE"
        else
          echo "- \`${fname}\`" >> "$INDEX_FILE"
        fi
      done

    # Рекурсия для вложенных подпапок (до 4 уровней)
    if [ "$heading_level" -lt 5 ]; then
      local next_level=$((heading_level + 1))
      find "$subdir" -maxdepth 1 -type d -not -path "$subdir" | sort | while read -r nested; do
        output_dir_contents "$nested" "$next_level"
      done 2>/dev/null || true
    fi
  done

  # Файлы в текущей папке (не в подпапках)
  local has_files=false
  find "$dir" -maxdepth 1 -type f \
    -not -name '.DS_Store' -not -name '.gitkeep' -not -name 'README.md' \
    -not -name '*.png' -not -name '*.jpg' -not -name '*.jpeg' -not -name '*.gif' -not -name '*.svg' \
    | sort | while read -r file; do
      local fname
      fname=$(basename "$file")
      local frel="${file#./}"
      local fdesc
      fdesc=$(file_desc "$frel")
      if [ -n "$fdesc" ]; then
        echo "- \`${fname}\` — ${fdesc}" >> "$INDEX_FILE"
      else
        echo "- \`${fname}\`" >> "$INDEX_FILE"
      fi
    done
}

# Основные секции
find . -maxdepth 1 -type d \
  -not -path '.' \
  -not -path './.git' \
  -not -path './.github' \
  -not -path './.claude' \
  -not -path './scripts' \
  -not -path './node_modules' \
  | sort | sed 's|^./||' | while read -r top_dir; do

    echo "## ${top_dir}/" >> "$INDEX_FILE"
    echo "" >> "$INDEX_FILE"

    # Описание папки
    desc=$(get_description "_dir_:${top_dir}")
    if [ -z "$desc" ]; then
      desc=$(dir_desc "$top_dir")
    fi
    if [ -n "$desc" ]; then
      echo "${desc}" >> "$INDEX_FILE"
      echo "" >> "$INDEX_FILE"
    fi

    # Файлы в корне раздела
    find "./$top_dir" -maxdepth 1 -type f \
      -not -name '.DS_Store' -not -name '.gitkeep' -not -name 'README.md' \
      -not -name '*.png' -not -name '*.jpg' -not -name '*.jpeg' -not -name '*.gif' -not -name '*.svg' \
      | sort | while read -r file; do
        local fname
        fname=$(basename "$file")
        local frel="${file#./}"
        local fdesc
        fdesc=$(file_desc "$frel")
        if [ -n "$fdesc" ]; then
          echo "- \`${fname}\` — ${fdesc}" >> "$INDEX_FILE"
        else
          echo "- \`${fname}\`" >> "$INDEX_FILE"
        fi
      done

    # Подпапки
    find "./$top_dir" -maxdepth 1 -type d -not -path "./$top_dir" | sort | while read -r subdir; do
      local subname
      subname=$(basename "$subdir")
      local sub_rel="${subdir#./}"
      local sub_desc
      sub_desc=$(get_description "_dir_:${sub_rel}")
      if [ -z "$sub_desc" ]; then
        sub_desc=$(dir_desc "$subdir")
      fi

      echo "" >> "$INDEX_FILE"
      echo "### ${sub_rel}/" >> "$INDEX_FILE"
      echo "" >> "$INDEX_FILE"
      if [ -n "$sub_desc" ]; then
        echo "${sub_desc}" >> "$INDEX_FILE"
        echo "" >> "$INDEX_FILE"
      fi

      # Файлы в подпапке
      find "$subdir" -maxdepth 1 -type f \
        -not -name '.DS_Store' -not -name '.gitkeep' -not -name 'README.md' \
        -not -name '*.png' -not -name '*.jpg' -not -name '*.jpeg' -not -name '*.gif' -not -name '*.svg' \
        | sort | while read -r file; do
          local fname
          fname=$(basename "$file")
          local frel="${file#./}"
          local fdesc
          fdesc=$(file_desc "$frel")
          if [ -n "$fdesc" ]; then
            echo "- \`${fname}\` — ${fdesc}" >> "$INDEX_FILE"
          else
            echo "- \`${fname}\`" >> "$INDEX_FILE"
          fi
        done

      # Вложенные подпапки (уровень 3)
      find "$subdir" -maxdepth 1 -type d -not -path "$subdir" | sort | while read -r nested; do
        local nname
        nname=$(basename "$nested")
        local n_rel="${nested#./}"
        local n_desc
        n_desc=$(get_description "_dir_:${n_rel}")

        echo "" >> "$INDEX_FILE"
        echo "**${nname}/**" >> "$INDEX_FILE"
        if [ -n "$n_desc" ]; then
          echo "${n_desc}" >> "$INDEX_FILE"
        fi
        echo "" >> "$INDEX_FILE"

        find "$nested" -maxdepth 1 -type f \
          -not -name '.DS_Store' -not -name '.gitkeep' -not -name 'README.md' \
          -not -name '*.png' -not -name '*.jpg' -not -name '*.jpeg' -not -name '*.gif' -not -name '*.svg' \
          | sort | while read -r file; do
            local fname
            fname=$(basename "$file")
            local frel="${file#./}"
            local fdesc
            fdesc=$(file_desc "$frel")
            if [ -n "$fdesc" ]; then
              echo "- \`${fname}\` — ${fdesc}" >> "$INDEX_FILE"
            else
              echo "- \`${fname}\`" >> "$INDEX_FILE"
            fi
          done
      done
    done

    echo "" >> "$INDEX_FILE"
    echo "---" >> "$INDEX_FILE"
    echo "" >> "$INDEX_FILE"
  done

# Корневые файлы
root_files=$(find . -maxdepth 1 -type f \
  -not -name '.DS_Store' -not -name '.gitignore' -not -name '.env' \
  -not -name 'index.md' -not -name 'CLAUDE.md' -not -name '.index-descriptions.json' \
  | sort | sed 's|^./||')

if [ -n "$root_files" ]; then
  echo "## Корневые файлы" >> "$INDEX_FILE"
  echo "" >> "$INDEX_FILE"
  echo "$root_files" | while read -r file; do
    local fdesc
    fdesc=$(file_desc "$file")
    if [ -n "$fdesc" ]; then
      echo "- \`${file}\` — ${fdesc}" >> "$INDEX_FILE"
    else
      echo "- \`${file}\`" >> "$INDEX_FILE"
    fi
  done
fi

echo ""
echo "index.md обновлён."
