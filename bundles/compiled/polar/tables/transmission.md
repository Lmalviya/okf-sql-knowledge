---
type: PostgreSQL Table
title: transmission
description: '8 columns: transmissiontemperaturec, transmissionpressurekpa, transmissiongear, differentialtemperaturec, axletemperaturec, transopmaintref. Joins to engineandfluids, equipment.'
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
| `transeqref` | character varying | A VARCHAR(70) foreign key referencing Equipment(EquipmentCode), linking the transmission data to a specific piece of equipment. |
| `transengfluidsref` | integer | An INTEGER foreign key referencing EngineAndFluids(EngineRegistry), associating this transmission with a particular engine/fluids record. |
| `transmissiontemperaturec` | real | A REAL value measuring the current transmission temperature in Celsius. |
| `transmissionpressurekpa` | numeric | A DECIMAL(8,2) indicating transmission fluid pressure in kilopascals. |
| `transmissiongear` | smallint | A SMALLINT representing the currently engaged gear (e.g., 3, -1, 1, 6, 0, 2, 5, 4). |
| `differentialtemperaturec` | double precision | A DOUBLE PRECISION value for the differential’s temperature in Celsius. |
| `axletemperaturec` | double precision | A FLOAT specifying the axle’s temperature in Celsius. |
| `transopmaintref` | integer | An INTEGER optionally referencing an OperationMaintenance(OpMaintRegistry) record for linking maintenance or operational data. |

# Joins

* `transengfluidsref` references `engineregistry` in [engineandfluids](/tables/engineandfluids.md).
* `transeqref` references `equipmentcode` in [equipment](/tables/equipment.md).
