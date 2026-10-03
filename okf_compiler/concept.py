"""Write one concept file: YAML frontmatter, then a markdown body."""

from datetime import datetime
from pathlib import Path

import yaml

COMPILER = "okf_compiler/0.1"
SOURCE_BASE = "https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main"


def generated() -> dict:
    now = datetime.now().astimezone().isoformat(timespec="seconds")
    return {"by": COMPILER, "at": now}


def source(database: str, filename: str, title: str) -> dict:
    return {
        "id": filename.split(".")[0].removeprefix(f"{database}_"),
        "resource": f"{SOURCE_BASE}/{database}/{filename}",
        "title": title,
    }


def write_concept(path: Path, frontmatter: dict, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    header = yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True, width=1000)
    path.write_text(f"---\n{header}---\n\n{body.strip()}\n", encoding="utf-8")