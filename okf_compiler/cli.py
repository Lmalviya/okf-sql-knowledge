"""Compile one LiveSQLBench database into an OKF bundle."""

import shutil
import sys
from pathlib import Path

from okf_compiler.indexes import write_indexes
from okf_compiler.readers import add_column_meanings, read_rules, read_schema
from okf_compiler.rules import find_tables, write_rules
from okf_compiler.tables import write_table

DATA = Path("data/livesqlbench-base-lite")
OUT = Path("bundles/compiled")


def compile_database(name: str) -> None:
    folder = DATA / name
    tables = read_schema(folder / f"{name}_schema.txt")
    missing = add_column_meanings(tables, folder / f"{name}_column_meaning_base.json")
    rules = read_rules(folder / f"{name}_kb.jsonl")

    bundle = OUT / name
    shutil.rmtree(bundle, ignore_errors=True)
    related = write_rules(rules, tables, name, bundle)
    for table in tables:
        write_table(table, name, bundle, related[table.name])
    write_indexes(bundle, name)

    unlinked = [r for r in rules if not find_tables(r, tables)]
    print(f"{name}: {len(tables)} tables, {len(rules)} rules written to {bundle}")
    if missing:
        print(f"  columns without a description: {', '.join(missing)}")
    if unlinked:
        print(f"  rules not linked to any table ({len(unlinked)}):")
        for rule in unlinked:
            print(f"    {rule.id}: {rule.name}")


if __name__ == "__main__":
    if sys.argv[1] == "all":
        for folder in sorted(DATA.iterdir()):
            if (folder / f"{folder.name}_schema.txt").exists():
                compile_database(folder.name)
    else:
        compile_database(sys.argv[1])