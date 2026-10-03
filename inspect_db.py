import sys
from pathlib import Path

from okf_compiler.readers import add_column_meanings, read_rules, read_schema

name = sys.argv[1]
folder = Path("data/livesqlbench-base-lite") / name

tables = read_schema(folder / f"{name}_schema.txt")
missing = add_column_meanings(tables, folder / f"{name}_column_meaning_base.json")
rules = read_rules(folder / f"{name}_kb.jsonl")

print(f"tables:  {len(tables)}")
print(f"columns: {sum(len(t.columns) for t in tables)}")
print(f"columns without a meaning: {', '.join(missing) or 'none'}")
print(f"rules:   {len(rules)}")
print()
for table in tables:
    joins = ", ".join(fk.ref_table for fk in table.foreign_keys) or "-"
    print(f"{table.name:<28} {len(table.columns):>3} columns   joins: {joins}")