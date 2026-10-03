"""Read the three raw LiveSQLBench files for one database into Python objects."""

import json
import re
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Column:
    name: str
    sql_type: str
    nullable: bool
    meaning: str = ""
    json_fields: dict = field(default_factory=dict)  # only for JSONB columns


@dataclass
class ForeignKey:
    column: str
    ref_table: str
    ref_column: str


@dataclass
class Table:
    name: str
    columns: list[Column]
    primary_key: list[str]
    foreign_keys: list[ForeignKey]


@dataclass
class Rule:
    id: int
    name: str
    description: str
    definition: str
    kind: str
    depends_on: list[int]


COLUMN_LINE = re.compile(r"^(\w+)\s+(.+?)\s+(NOT NULL|NULL),?$")
PRIMARY_KEY = re.compile(r"PRIMARY KEY \(([^)]+)\)")
FOREIGN_KEY = re.compile(r"FOREIGN KEY \((\w+)\) REFERENCES (\w+)\((\w+)\)")


def read_schema(path: Path) -> list[Table]:
    tables = []
    for block in path.read_text(encoding="utf-8").split("CREATE TABLE ")[1:]:
        name = block.split('"')[1]
        body = block.split(");")[0]
        columns, primary_key, foreign_keys = [], [], []
        for line in body.splitlines()[1:]:
            line = line.strip()
            if m := COLUMN_LINE.match(line):
                columns.append(Column(m[1], m[2], m[3] == "NULL"))
            elif m := PRIMARY_KEY.search(line):
                primary_key = [c.strip() for c in m[1].split(",")]
            elif m := FOREIGN_KEY.search(line):
                foreign_keys.append(ForeignKey(m[1], m[2], m[3]))
        tables.append(Table(name, columns, primary_key, foreign_keys))
    return tables


def add_column_meanings(tables: list[Table], path: Path) -> list[str]:
    """Attach each column's meaning. Returns the columns that have none."""
    meanings = {}
    for key, value in json.loads(path.read_text(encoding="utf-8")).items():
        _, table, column = key.lower().split("|")
        meanings[(table, column)] = value

    missing = []
    for table in tables:
        for column in table.columns:
            value = meanings.get((table.name, column.name))
            if value is None:
                missing.append(f"{table.name}.{column.name}")
            elif isinstance(value, dict):  # JSONB column
                column.meaning = value.get("column_meaning", "")
                column.json_fields = value.get("fields_meaning", {})
            else:
                column.meaning = value
    return missing


def read_rules(path: Path) -> list[Rule]:
    rules = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        raw = json.loads(line)
        children = raw["children_knowledge"]
        rules.append(Rule(
            id=raw["id"],
            name=raw["knowledge"],
            description=raw["description"],
            definition=raw["definition"],
            kind=raw["type"],
            depends_on=children if isinstance(children, list) else [],
        ))
    return rules