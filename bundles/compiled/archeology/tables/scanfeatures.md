---
type: PostgreSQL Table
title: scanfeatures
description: '10 columns: traitextract, traitcount, articount, structkind, matkind, huestudy, texturestudy, patternnote. Joins to equipment, sites.'
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_schema.txt
  title: archeology schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_column_meaning_base.json
  title: archeology column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `zoneref` | character varying | Full name: 'Site Reference'. Explanation: Site code tied to these features. Data type: VARCHAR(12). Example: 'SC9016'. |
| `equipref` | character | Full name: 'Equipment Reference'. Explanation: Equipment ID used to detect these features. Data type: CHAR(10). Example: 'SN20065'. |
| `traitextract` | character varying | Full name: 'Feature Extraction Method'. Explanation: Method used to extract features (manual or automated). Data type: VARCHAR(25). Possible categories: Manual, Semi-automatic, Automatic. |
| `traitcount` | integer | Full name: 'Number of Detected Features'. Explanation: How many features were identified. Data type: INTEGER. Example: 516. |
| `articount` | integer | Full name: 'Artifact Count'. Explanation: Number of artifacts recognized. Data type: INTEGER. Example: 71. |
| `structkind` | character varying | Full name: 'Structure Type'. Explanation: Type of structural element. Data type: VARCHAR(15). Possible categories: Artifact, Complex, Wall, Foundation. |
| `matkind` | character varying | Full name: 'Material Type'. Explanation: Primary composition or material. Data type: VARCHAR(15). Possible categories: Organic, Metal, Mixed, Ceramic, Stone. |
| `huestudy` | character varying | Full name: 'Color Analysis'. Explanation: Status of color analysis (done or pending). Data type: VARCHAR(15). Possible categories: Partial, Completed, Not Required. |
| `texturestudy` | character varying | Full name: 'Texture Analysis'. Explanation: Status of texture analysis. Data type: VARCHAR(15). Possible categories: Partial, Completed, Not Required. |
| `patternnote` | text | Full name: 'Pattern Recognition'. Explanation: Notes regarding detected patterns. Data type: TEXT. Possible categories: Not Required, None, Partial. |

# Joins

* `equipref` references `equipregistry` in [equipment](/tables/equipment.md).
* `zoneref` references `zoneregistry` in [sites](/tables/sites.md).

# Related knowledge

* [Feature Extraction Efficiency (FEE)](/knowledge/feature-extraction-efficiency.md)
* [Texture-Critical Artifact](/knowledge/texture-critical-artifact.md)
