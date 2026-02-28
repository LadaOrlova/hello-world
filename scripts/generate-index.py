#!/usr/bin/env python3
"""
Обновляет index.md — карту репозитория с осмысленными описаниями файлов.
Для новых/изменённых файлов генерирует описания через OpenRouter API.
Для неизменённых файлов сохраняет существующие описания.

Использование:
  python3 scripts/generate-index.py              — обновить только изменённые файлы
  python3 scripts/generate-index.py --full       — перегенерировать все описания
  python3 scripts/generate-index.py --structure  — обновить только структуру (без AI)
"""

import os
import sys
import json
import subprocess
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DESCRIPTIONS_FILE = REPO_ROOT / ".index-descriptions.json"
INDEX_FILE = REPO_ROOT / "index.md"

# Папки и файлы, которые не включаем в индекс
SKIP_DIRS = {".git", ".github", ".claude", "scripts", "node_modules", "__pycache__"}
SKIP_FILES = {".DS_Store", ".gitkeep", ".env", ".gitignore", "index.md", "CLAUDE.md", ".index-descriptions.json"}
SKIP_EXTENSIONS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico"}

# --- Работа с описаниями ---

def load_descriptions() -> dict:
    """Загружает описания из TSV-файла."""
    descriptions = {}
    if DESCRIPTIONS_FILE.exists():
        for line in DESCRIPTIONS_FILE.read_text(encoding="utf-8").splitlines():
            if "\t" in line:
                path, desc = line.split("\t", 1)
                descriptions[path] = desc
    return descriptions


def save_descriptions(descriptions: dict):
    """Сохраняет описания в TSV-файл."""
    lines = []
    for path in sorted(descriptions.keys()):
        lines.append(f"{path}\t{descriptions[path]}")
    DESCRIPTIONS_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")


# --- Обнаружение изменений ---

def get_changed_files() -> set:
    """Возвращает файлы, изменённые в последнем коммите."""
    try:
        result = subprocess.run(
            ["git", "diff", "--name-only", "HEAD~1", "HEAD"],
            capture_output=True, text=True, cwd=REPO_ROOT
        )
        return {f for f in result.stdout.strip().split("\n") if f.endswith(".md")}
    except Exception:
        return set()


def get_all_indexable_files() -> set:
    """Возвращает все индексируемые файлы в репозитории (.md, .txt, .json и др.)."""
    files = set()
    for root, dirs, filenames in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in filenames:
            if f in SKIP_FILES:
                continue
            if any(f.endswith(ext) for ext in SKIP_EXTENSIONS):
                continue
            rel = os.path.relpath(os.path.join(root, f), REPO_ROOT)
            files.add(rel)
    return files


# --- Генерация описаний через AI ---

def get_api_key() -> str:
    key = os.environ.get("OPENROUTER_API_KEY", "")
    if not key:
        env_file = REPO_ROOT / ".env"
        if env_file.exists():
            for line in env_file.read_text().splitlines():
                if line.startswith("OPENROUTER_API_KEY="):
                    key = line.split("=", 1)[1]
    return key


def generate_description_ai(filepath: str, api_key: str) -> str:
    """Генерирует описание файла через OpenRouter API."""
    import urllib.request

    full_path = REPO_ROOT / filepath
    if not full_path.exists():
        return ""

    # Читаем первые 3000 символов файла
    content = full_path.read_text(encoding="utf-8", errors="ignore")[:3000]
    if not content.strip():
        return "(пустой файл)"

    prompt = (
        f"Напиши 1-2 предложения на русском языке, кратко описывающие содержимое этого файла. "
        f"Отвечай ТОЛЬКО описанием, без кавычек, префиксов и вступлений.\n\n"
        f"Путь файла: {filepath}\n\n"
        f"Содержимое:\n{content}"
    )

    payload = json.dumps({
        "model": "anthropic/claude-haiku",
        "max_tokens": 200,
        "messages": [{"role": "user", "content": prompt}]
    }).encode()

    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read())
            desc = data["choices"][0]["message"]["content"].strip()
            # Убираем переносы, ограничиваем длину
            desc = " ".join(desc.split())[:250]
            return desc
    except Exception as e:
        print(f"    ⚠ API ошибка для {filepath}: {e}")
        return extract_title(filepath)


def extract_title(filepath: str) -> str:
    """Извлекает заголовок # из файла как фоллбэк."""
    full_path = REPO_ROOT / filepath
    if not full_path.exists():
        return ""
    try:
        for line in full_path.read_text(encoding="utf-8", errors="ignore").splitlines()[:20]:
            if line.startswith("#"):
                return line.lstrip("#").strip()
    except Exception:
        pass
    return ""


# --- Обновление описаний ---

def update_descriptions(mode: str):
    """Обновляет описания для новых/изменённых файлов."""
    descriptions = load_descriptions()
    all_files = get_all_indexable_files()
    api_key = get_api_key()

    # Определяем, для каких файлов нужны описания
    if mode == "--full":
        files_to_update = all_files
    elif mode == "--structure":
        files_to_update = set()  # Не обновляем описания
    else:
        changed = get_changed_files()
        # Изменённые + новые (без описания)
        files_to_update = changed | {f for f in all_files if f not in descriptions}

    # Удаляем описания для несуществующих файлов
    for path in list(descriptions.keys()):
        if not path.startswith("_dir_:") and path not in all_files:
            del descriptions[path]
            print(f"  ✕ Удалено: {path}")

    if files_to_update:
        print(f"Обновляю описания для {len(files_to_update)} файлов...")
        for filepath in sorted(files_to_update):
            if filepath not in all_files:
                continue
            print(f"  → {filepath}")
            if api_key:
                desc = generate_description_ai(filepath, api_key)
            else:
                desc = extract_title(filepath)
            if desc:
                descriptions[filepath] = desc

    save_descriptions(descriptions)
    return descriptions


# --- Генерация index.md ---

def get_repo_tree():
    """Строит дерево репозитория."""
    tree = {}
    for root, dirs, files in os.walk(REPO_ROOT):
        dirs[:] = sorted([d for d in dirs if d not in SKIP_DIRS])
        rel_root = os.path.relpath(root, REPO_ROOT)
        if rel_root == ".":
            rel_root = ""

        filtered_files = sorted([
            f for f in files
            if f not in SKIP_FILES and not any(f.endswith(ext) for ext in SKIP_EXTENSIONS)
        ])

        if rel_root:
            tree[rel_root] = {"dirs": dirs, "files": filtered_files}
        else:
            tree[""] = {"dirs": dirs, "files": filtered_files}

    return tree


def generate_index(descriptions: dict):
    """Генерирует index.md."""
    tree = get_repo_tree()
    lines = []

    # Шапка
    lines.append("# Index")
    lines.append("")
    lines.append("Карта репозитория с описанием каждого файла. Обновляется автоматически при каждом пуше в main — для изменённых файлов описания генерируются через AI.")
    lines.append("")

    # Таблица разделов верхнего уровня
    lines.append("## Разделы")
    lines.append("")
    lines.append("| Папка | Что внутри |")
    lines.append("|-------|-----------|")

    top_dirs = tree.get("", {}).get("dirs", [])
    for d in top_dirs:
        desc = descriptions.get(f"_dir_:{d}", "")
        lines.append(f"| `{d}/` | {desc or '—'} |")

    lines.append("")
    lines.append("---")
    lines.append("")

    # Детальные секции
    for top_dir in top_dirs:
        lines.append(f"## {top_dir}/")
        lines.append("")

        dir_desc = descriptions.get(f"_dir_:{top_dir}", "")
        if dir_desc:
            lines.append(dir_desc)
            lines.append("")

        # Файлы в корне раздела
        top_info = tree.get(top_dir, {"dirs": [], "files": []})
        for f in top_info["files"]:
            if f == "README.md":
                continue
            fpath = f"{top_dir}/{f}"
            desc = descriptions.get(fpath, "")
            if desc:
                lines.append(f"- `{f}` — {desc}")
            else:
                lines.append(f"- `{f}`")

        # Подпапки первого уровня
        for sub in top_info["dirs"]:
            sub_path = f"{top_dir}/{sub}"
            sub_info = tree.get(sub_path, {"dirs": [], "files": []})
            sub_desc = descriptions.get(f"_dir_:{sub_path}", "")

            lines.append("")
            lines.append(f"### {sub_path}/")
            lines.append("")
            if sub_desc:
                lines.append(sub_desc)
                lines.append("")

            # Файлы в подпапке
            for f in sub_info["files"]:
                if f == "README.md":
                    continue
                fpath = f"{sub_path}/{f}"
                desc = descriptions.get(fpath, "")
                if desc:
                    lines.append(f"- `{f}` — {desc}")
                else:
                    lines.append(f"- `{f}`")

            # Вложенные подпапки (уровень 3)
            for nested in sub_info["dirs"]:
                nested_path = f"{sub_path}/{nested}"
                nested_info = tree.get(nested_path, {"dirs": [], "files": []})
                nested_desc = descriptions.get(f"_dir_:{nested_path}", "")

                lines.append("")
                lines.append(f"**{nested}/**")
                if nested_desc:
                    lines.append(nested_desc)
                lines.append("")

                for f in nested_info["files"]:
                    if f == "README.md":
                        continue
                    fpath = f"{nested_path}/{f}"
                    desc = descriptions.get(fpath, "")
                    if desc:
                        lines.append(f"- `{f}` — {desc}")
                    else:
                        lines.append(f"- `{f}`")

                # Уровень 4 (если есть)
                for deep in nested_info.get("dirs", []):
                    deep_path = f"{nested_path}/{deep}"
                    deep_info = tree.get(deep_path, {"dirs": [], "files": []})
                    if deep_info["files"]:
                        lines.append("")
                        lines.append(f"*{deep}/*")
                        lines.append("")
                        for f in deep_info["files"]:
                            if f == "README.md":
                                continue
                            fpath = f"{deep_path}/{f}"
                            desc = descriptions.get(fpath, "")
                            if desc:
                                lines.append(f"- `{f}` — {desc}")
                            else:
                                lines.append(f"- `{f}`")

        lines.append("")
        lines.append("---")
        lines.append("")

    # Корневые файлы
    root_files = tree.get("", {}).get("files", [])
    if root_files:
        lines.append("## Корневые файлы")
        lines.append("")
        for f in root_files:
            desc = descriptions.get(f, "")
            if desc:
                lines.append(f"- `{f}` — {desc}")
            else:
                lines.append(f"- `{f}`")
        lines.append("")

    INDEX_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"index.md обновлён ({len(lines)} строк).")


# --- Main ---

if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    descriptions = update_descriptions(mode)
    generate_index(descriptions)
