"""Write the index files and the log for a bundle."""

from datetime import date
from pathlib import Path

import yaml

from okf_compiler.concept import COMPILER

FOLDERS = {
    "tables": "PostgreSQL tables, with column meanings, JSON fields and joins.",
    "knowledge": "Business rules: calculations, definitions and value illustrations.",
}


def read_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    return yaml.safe_load(text.split("---", 2)[1])


def write_folder_index(folder: Path) -> int:
    groups: dict[str, list[str]] = {}
    for path in sorted(folder.glob("*.md")):
        if path.name == "index.md":
            continue
        meta = read_frontmatter(path)
        line = f"* [{meta['title']}]({path.name}) - {meta['description']}"
        groups.setdefault(meta["type"], []).append(line)

    parts = []
    for concept_type, lines in sorted(groups.items()):
        parts += [f"# {concept_type}", "", *lines, ""]
    (folder / "index.md").write_text("\n".join(parts), encoding="utf-8")
    return sum(len(lines) for lines in groups.values())


def write_indexes(bundle: Path, database: str) -> None:
    counts = {name: write_folder_index(bundle / name) for name in FOLDERS}

    root = ["---", 'okf_version: "0.2"', "---", "", f"# {database} database", ""]
    for name, text in FOLDERS.items():
        root.append(f"* [{name.capitalize()}]({name}/index.md) - {text}")
    (bundle / "index.md").write_text("\n".join(root) + "\n", encoding="utf-8")

    log = [
        "# Update Log",
        "",
        f"## {date.today().isoformat()}",
        f"* **Creation**: Compiled {counts['tables']} tables and {counts['knowledge']} "
        f"business rules from LiveSQLBench `{database}` with `{COMPILER}`.",
    ]
    (bundle / "log.md").write_text("\n".join(log) + "\n", encoding="utf-8")