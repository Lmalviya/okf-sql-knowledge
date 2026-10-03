---
type: PostgreSQL Table
title: waterandwaste
description: '7 columns: waterlevelpercent, waterpressurekpa, watertemperaturec, waterflowlpm, waterqualityindex, wastetanklevelpercent. Joins to equipment.'
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:09+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_schema.txt
  title: polar schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_column_meaning_base.json
  title: polar column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `watereqref` | character varying | A VARCHAR(70) foreign key referencing Equipment(EquipmentCode), associating water/waste data with equipment. |
| `waterlevelpercent` | real | A REAL value showing the current water tank level percentage. |
| `waterpressurekpa` | numeric | A DECIMAL(7,2) indicating water pressure in kilopascals. |
| `watertemperaturec` | double precision | A FLOAT representing the water temperature in Celsius. |
| `waterflowlpm` | numeric | A NUMERIC(8,3) specifying water flow rate in liters per minute. |
| `waterqualityindex` | integer | An INT rating or index representing overall water quality (e.g., 0–100 scale). |
| `wastetanklevelpercent` | numeric | A DECIMAL(5,2) measuring how full the waste tank is as a percentage of capacity. |

# Joins

* `watereqref` references `equipmentcode` in [equipment](/tables/equipment.md).

# Related knowledge

* [Water Resource Management Index (WRMI)](/knowledge/water-resource-management-index.md)
* [Water Quality Classification System (WQCS)](/knowledge/water-quality-classification-system.md)
