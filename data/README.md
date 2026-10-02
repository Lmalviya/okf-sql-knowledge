# The data: LiveSQLBench Base-Lite

This folder holds the raw benchmark files we build on. The files themselves are **not committed**: download them as shown in the [main README](../README.md#5-download-the-benchmark-data). This page explains what's inside them.

## What LiveSQLBench is

[LiveSQLBench](https://livesqlbench.ai) is a public benchmark for text-to-SQL agents, maintained by the [BIRD team at HKU](https://bird-bench.github.io) and Google Cloud. Its questions use business terms that are defined in a separate knowledge file, not in the database. That makes it a good test for our problem: an agent that only reads the schema can't answer them.

It comes in several releases. We use **Base-Lite**: 18 databases and 270 questions. A larger release, [Large-v1](https://huggingface.co/datasets/birdsql/livesqlbench-large-v1), has much bigger databases.

## Folder layout

```text
data/livesqlbench-base-lite/
├── README.md                    the dataset card from the authors
├── livesqlbench_data.jsonl      270 questions, one JSON object per line
├── alien/
│   ├── alien_schema.txt
│   ├── alien_column_meaning_base.json
│   └── alien_kb.jsonl
├── archeology/
│   └── ...
└── ... (18 database folders)
```

Every database folder has the same three files, named after the database.

## The 18 databases

| Database | Tables | Columns | JSON columns | Business rules | Formulas | Definitions | Value explanations |
|---|---:|---:|---:|---:|---:|---:|---:|
| alien | 11 | 136 | 0 | 56 | 21 | 26 | 9 |
| archeology | 14 | 151 | 0 | 54 | 20 | 24 | 10 |
| credit | 6 | 120 | 2 | 52 | 20 | 22 | 10 |
| cross_db | 7 | 131 | 0 | 79 | 31 | 38 | 10 |
| crypto | 10 | 89 | 3 | 53 | 21 | 22 | 10 |
| cybermarket | 9 | 132 | 3 | 50 | 20 | 20 | 10 |
| disaster | 10 | 123 | 3 | 54 | 21 | 23 | 10 |
| fake | 9 | 99 | 3 | 87 | 39 | 37 | 11 |
| gaming | 8 | 160 | 0 | 54 | 21 | 23 | 10 |
| insider | 7 | 105 | 2 | 74 | 31 | 32 | 11 |
| mental | 9 | 107 | 3 | 63 | 26 | 27 | 10 |
| museum | 14 | 185 | 0 | 57 | 20 | 26 | 11 |
| news | 8 | 108 | 3 | 61 | 24 | 23 | 14 |
| polar | 14 | 162 | 8 | 54 | 20 | 25 | 9 |
| robot | 10 | 130 | 3 | 60 | 30 | 20 | 10 |
| solar | 8 | 84 | 3 | 53 | 20 | 23 | 10 |
| vaccine | 7 | 134 | 0 | 66 | 27 | 29 | 10 |
| virtual | 14 | 130 | 5 | 55 | 20 | 23 | 12 |
| **Total** | **175** | **2,286** | **44** | **1,082** | **432** | **463** | **187** |

"Formulas", "Definitions" and "Value explanations" are the three rule types described below.

## File 1: `<db>_schema.txt`

Plain text. For each table:

1. a `CREATE TABLE` statement with column names, types, the primary key and foreign keys,
2. the line `First 3 rows:` followed by up to three sample rows as a text table.

```sql
CREATE TABLE "distributionhubs" (
hubregistry character varying NOT NULL,
disteventref character varying NULL,
hubcaptons numeric NULL,
hubutilpct numeric NULL,
...
    PRIMARY KEY (hubregistry),
    FOREIGN KEY (disteventref) REFERENCES disasterevents(distregistry)
);
```

Things to know:

- Column names are short and cryptic (`hubutilpct`, `storeavailm3`). Their meaning is only in the column descriptions file.
- The type `USER-DEFINED` means the column holds one value from a fixed list (an enum). The allowed values are only in the column descriptions file.
- Some tables have no sample rows. Their sample section says `No data available in this table.`

## File 2: `<db>_column_meaning_base.json`

One JSON object. Each key is `database|table|column`, and each value describes that column.

Most values are a plain sentence, often with the SQL type, an example value, and for enums the list of allowed values:

```json
"disaster|distributionhubs|hubutilpct": "A DECIMAL(7,3) showing the percentage of hub capacity currently utilized (e.g., 85.300).",
"disaster|distributionhubs|warehousestate": "An enum (WarehouseState_enum) describing the warehouse’s condition; values: 'Fair', 'Excellent', 'Good', 'Poor'."
```

Columns of type `jsonb` (44 in total) have a nested value instead: a description of the column plus a description of every field inside the JSON, nested the same way as the JSON itself. Shortened example:

```json
"disaster|disasterevents|impactMetrics": {
  "column_meaning": "JSONB column. Consolidates impact-related metrics of the disaster including population effects, infrastructure damage, and communication status.",
  "fields_meaning": {
    "population": {
      "affected": "An INTEGER counting how many people are affected (e.g., 150000).",
      "displaced": "An INTEGER indicating the number of displaced individuals (e.g., 10000)."
    },
    "damage_level": "An enum (DamageReport_enum) labeling the damage severity; possible values: 'Severe', 'Moderate', 'Minor', 'Catastrophic'."
  }
}
```

Things to know:

- Every column in the schema has a description. We checked all 2,286.
- Key names don't always match the schema's capitalisation (`impactMetrics` here, `impactmetrics` in the schema). Compare them case-insensitively.
- The wording is free text, with no fixed pattern you can parse reliably.

## File 3: `<db>_kb.jsonl`

The business rules, called the knowledge base. One JSON object per line:

```json
{"id": 10, "knowledge": "Resource Utilization Ratio (RUR)", "description": "Measures how effectively hub capacity is being used relative to available resources", "definition": "RUR = \\frac{hubutilpct}{100} \\times \\frac{storecapm3}{storeavailm3 + 1}", "type": "calculation_knowledge", "children_knowledge": -1}
```

| Field | Meaning |
|---|---|
| `id` | Number of the rule within its database. Other rules refer to it by this id. |
| `knowledge` | The rule's name: the business term a question will use. |
| `description` | One sentence about what the rule is for. |
| `definition` | The rule itself. Formulas are written in LaTeX. |
| `type` | `calculation_knowledge` (a formula), `domain_knowledge` (a business definition or threshold), or `value_illustration` (what a column's values mean). |
| `children_knowledge` | List of ids this rule depends on, or `-1` for none. |

Things to know:

- **Rules depend on other rules.** For example, "Resource Utilization Classification" (rule 50) lists `[10]`, because it classifies hubs by their RUR value.
- **Rules name columns, but not tables.** Rule 10 uses `hubutilpct`, `storecapm3` and `storeavailm3`; you find their table in the schema.
- **Some rules name no column at all.** Their definition is plain prose. Matching such a rule to a table takes reading and judgement.
- Value explanations are often named after the column they explain, for example a rule called `hazlevel` explains the levels of the `hazlevel` column.

## The questions: `livesqlbench_data.jsonl`

270 questions, 15 per database, one JSON object per line.

| Field | Meaning |
|---|---|
| `instance_id` | Question id, for example `disaster_1` |
| `selected_database` | Which database the question is about |
| `query` | The question in plain English |
| `category` | `Query` (read data; 180 questions) or `Management` (change data, such as `UPDATE` or creating a view; 90 questions) |
| `difficulty_tier` | `Simple` (91), `Moderate` (124) or `Challenging` (55) |
| `preprocess_sql`, `clean_up_sqls` | SQL to run before and after a question (used by 6 questions) |
| `conditions`, `high_level` | Settings used by the official evaluation |
| `sol_sql`, `test_cases`, `external_knowledge` | **Empty in the public files** (see below) |

## Withheld answers

The correct SQL (`sol_sql`), the test cases and the per-question knowledge are left out of the public files, so automated web crawlers can't collect them. You can request them by email, as described on the [dataset page](https://huggingface.co/datasets/birdsql/livesqlbench-base-lite). They are only needed to score an agent. If you get them, don't commit them to a public repository.

## The database itself

These files describe the databases, but they don't contain the data. To run SQL, you need the PostgreSQL database, which the authors provide separately with a ready-made Docker setup in the [LiveSQLBench repository](https://github.com/bird-bench/livesqlbench). We set it up in Part 3.

## License and credit

LiveSQLBench is created by the BIRD team at HKU and Google Cloud. The license is stated differently in two places: the dataset card on Hugging Face lists **CC BY 4.0**, and the [GitHub repository](https://github.com/bird-bench/livesqlbench) states **CC BY-SA 4.0**. We follow the stricter one, CC BY-SA 4.0. Please credit the authors if you reuse the data.