---
type: PostgreSQL Table
title: plant
description: '4 columns: growalias, gencapmw, initdate.'
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_schema.txt
  title: solar schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_column_meaning_base.json
  title: solar column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `growregistry` | uuid, primary key | UUID PRIMARY KEY uniquely identifying each plant record (was 'RecordID') (e.g., '3fa85f64-5717-4562-b3fc-2c963f66afa6'). |
| `growalias` | character varying | VARCHAR(100) naming or aliasing the plant (was 'PlantName') (e.g., 'DesertSolarOne', 'ValleyGridAlpha'). |
| `gencapmw` | numeric | NUMERIC(7,3) indicating the generation capacity in megawatts (was 'PlantCapacityMW') (e.g., 12.500). |
| `initdate` | date | DATE representing the plant’s installation or commissioning date (was 'InstallationDate') (e.g., '2022-05-10'). |

# Related knowledge

* [Maintenance Cost Efficiency (MCE)](/knowledge/maintenance-cost-efficiency.md)
* [Revenue Loss Rate (RLR)](/knowledge/revenue-loss-rate.md)
* [Financial Impact of Degradation (FID)](/knowledge/financial-impact-of-degradation.md)
