"""Build one concept file per business rule, and link rules to tables."""

import re
from pathlib import Path

from okf_compiler.concept import generated, source, write_concept
from okf_compiler.readers import Rule, Table

TYPE_NAMES = {
    "calculation_knowledge": "Calculation",
    "domain_knowledge": "Business Rule",
    "value_illustration": "Value Illustration",
}
WORD = re.compile(r"[A-Za-z_][A-Za-z0-9_]*")


def make_slugs(rules: list[Rule]) -> dict[int, str]:
    """A file name for every rule, e.g. 'resource-utilization-ratio'."""
    slugs, used = {}, set()
    for rule in rules:
        name = re.sub(r"\([^)]*\)", "", rule.name)
        slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
        if slug in used:
            slug = f"{slug}-{rule.id}"
        used.add(slug)
        slugs[rule.id] = slug
    return slugs


def find_tables(rule: Rule, tables: list[Table]) -> dict[str, list[str]]:
    """Tables whose column names appear in the rule's name or definition."""
    words = {w.lower() for w in WORD.findall(f"{rule.name} {rule.definition}")}
    found = {}
    for table in tables:
        columns = [c.name for c in table.columns if c.name.lower() in words]
        if columns:
            found[table.name] = columns
    return found


def rule_body(rule: Rule, rules_by_id: dict[int, Rule], used_by: list[int],
              slugs: dict[int, str], tables: dict[str, list[str]]) -> str:
    parts = ["# Definition", "", rule.definition]

    if tables:
        parts += ["", "# Columns used", ""]
        for table, columns in tables.items():
            names = ", ".join(f"`{c}`" for c in columns)
            parts.append(f"* [{table}](/tables/{table}.md): {names}")

    for heading, ids in (("Depends on", rule.depends_on), ("Used by", used_by)):
        links = [f"* [{rules_by_id[i].name}](/knowledge/{slugs[i]}.md)"
                 for i in ids if i in rules_by_id]
        if links:
            parts += ["", f"# {heading}", "", *links]
    return "\n".join(parts)


def write_rules(rules: list[Rule], tables: list[Table], database: str,
                bundle: Path) -> dict[str, list[tuple[str, str]]]:
    """Write every rule concept. Returns, per table, the rules that use it."""
    slugs = make_slugs(rules)
    rules_by_id = {r.id: r for r in rules}
    used_by = {r.id: [] for r in rules}
    for rule in rules:
        for parent in rule.depends_on:
            if parent in used_by:
                used_by[parent].append(rule.id)

    related = {t.name: [] for t in tables}
    for rule in rules:
        found = find_tables(rule, tables)
        for table in found:
            related[table].append((rule.name, slugs[rule.id]))

        frontmatter = {
            "type": TYPE_NAMES.get(rule.kind, rule.kind),
            "title": rule.name,
            "description": rule.description,
            "tags": [database],
            "generated": generated(),
            "sources": [source(database, f"{database}_kb.jsonl",
                               f"{database} business rules (LiveSQLBench), rule {rule.id}")],
        }
        body = rule_body(rule, rules_by_id, used_by[rule.id], slugs, found)
        write_concept(bundle / "knowledge" / f"{slugs[rule.id]}.md", frontmatter, body)
    return related