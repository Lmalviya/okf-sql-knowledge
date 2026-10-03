"""Build one concept file per table."""

from pathlib import Path

from okf_compiler.concept import generated, source, write_concept
from okf_compiler.readers import Table


def describe(table: Table) -> str:
    keys = set(table.primary_key) | {fk.column for fk in table.foreign_keys}
    names = [c.name for c in table.columns if c.name not in keys]
    text = f"{len(table.columns)} columns: {', '.join(names)}."
    joins = sorted({fk.ref_table for fk in table.foreign_keys})
    if joins:
        text += f" Joins to {', '.join(joins)}."
    return text


def cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def json_field_lines(prefix: str, fields: dict) -> list[str]:
    lines = []
    for name, value in fields.items():
        path = f"{prefix}.{name}"
        if isinstance(value, dict):
            lines += json_field_lines(path, value)
        else:
            lines.append(f"* `{path}`: {value}")
    return lines


def table_body(table: Table, related: list[tuple[str, str]]) -> str:
    parts = ["# Schema", "", "| Column | Type | Meaning |", "|---|---|---|"]
    for c in table.columns:
        sql_type = c.sql_type + (", primary key" if c.name in table.primary_key else "")
        parts.append(f"| `{c.name}` | {sql_type} | {cell(c.meaning)} |")

    json_lines = []
    for c in table.columns:
        json_lines += json_field_lines(c.name, c.json_fields)
    if json_lines:
        parts += ["", "# JSON fields", "", *json_lines]

    if table.foreign_keys:
        parts += ["", "# Joins", ""]
        for fk in table.foreign_keys:
            parts.append(
                f"* `{fk.column}` references `{fk.ref_column}` in "
                f"[{fk.ref_table}](/tables/{fk.ref_table}.md)."
            )

    if related:
        parts += ["", "# Related knowledge", ""]
        for title, slug in related:
            parts.append(f"* [{title}](/knowledge/{slug}.md)")
    return "\n".join(parts)


def write_table(table: Table, database: str, bundle: Path, related: list[tuple[str, str]]) -> None:
    frontmatter = {
        "type": "PostgreSQL Table",
        "title": table.name,
        "description": describe(table),
        "tags": [database],
        "generated": generated(),
        "sources": [
            source(database, f"{database}_schema.txt", f"{database} schema (LiveSQLBench)"),
            source(database, f"{database}_column_meaning_base.json",
                   f"{database} column descriptions (LiveSQLBench)"),
        ],
    }
    write_concept(bundle / "tables" / f"{table.name}.md", frontmatter, table_body(table, related))