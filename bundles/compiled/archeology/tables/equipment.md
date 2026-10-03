---
type: PostgreSQL Table
title: equipment
description: '6 columns: equipform, equipdesign, equiptune, equipstatus, powerlevel.'
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
| `equipregistry` | character, primary key | Full name: 'Equipment ID'. Explanation: Primary key for equipment. Data type: CHAR(10). Example: 'SN20065'. |
| `equipform` | character varying | Full name: 'Equipment Type'. Explanation: Type or category of scanning equipment. Data type: VARCHAR(28). Possible categories: LiDAR, Structured Light, Photogrammetry, Laser. |
| `equipdesign` | character varying | Full name: 'Equipment Model'. Explanation: Model name or identifier. Data type: VARCHAR(14). Example: 'Model-669'. |
| `equiptune` | date | Full name: 'Calibration Date'. Explanation: Date the equipment was last calibrated. Data type: DATE. Example: '2024-11-01'. |
| `equipstatus` | character varying | Full name: 'Equipment Condition'. Explanation: Overall condition of the equipment. Data type: VARCHAR(16). Possible categories: Excellent, Good, Fair, Poor. |
| `powerlevel` | smallint | Full name: 'Battery Level (%)'. Explanation: Battery level as an integer percentage. Data type: SMALLINT. Example: 62. |

# Related knowledge

* [Equipment Effectiveness Ratio (EER)](/knowledge/equipment-effectiveness-ratio.md)
