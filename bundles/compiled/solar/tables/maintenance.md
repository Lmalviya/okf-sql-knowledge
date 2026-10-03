---
type: PostgreSQL Table
title: maintenance
description: '14 columns: inspectmeth, inspectres, inspectdate, maintsched, wtystatus, wtyclaimcnt, maintcostusd, cleancostusd, replacecostusd, revlossusd. Joins to panel, performance, plant.'
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
| `maintregistry` | character varying, primary key | VARCHAR(50) PRIMARY KEY uniquely identifying each maintenance record. |
| `powerref` | uuid | UUID REFERENCES Plant(GrowRegistry), referencing which plant is maintained. |
| `compref` | character varying | VARCHAR(50) REFERENCES Panel(PaneMark), referencing the panel if maintenance is panel-specific. |
| `obsref` | character varying | VARCHAR(50) REFERENCES Performance(PerfRegistry), linking to performance data if relevant. |
| `inspectmeth` | character varying | VARCHAR(100) describing the inspection method (was 'InspectionMethod'). Possible enumerations: 'Visual', 'IR Thermal', 'IV Curve', 'EL Imaging'. |
| `inspectres` | character varying | VARCHAR(150) noting the inspection result (was 'InspectionResult'). Possible enumerations: 'Minor Issues', 'Major Issues', 'Pass'. |
| `inspectdate` | date | DATE specifying when inspection took place (was 'InspectionDate') (e.g., '2023-07-01'). |
| `maintsched` | character varying | VARCHAR(100) summarizing the maintenance schedule (was 'MaintenanceSchedule'). Possible enumerations: 'Delayed', 'Overdue', 'On Schedule'. |
| `wtystatus` | character varying | VARCHAR(50) describing the warranty status (was 'WarrantyStatus'). Possible enumerations: 'Claimed', 'Active', 'Expired'. |
| `wtyclaimcnt` | smallint | SMALLINT counting how many warranty claims have been filed (was 'WarrantyClaimCount'). Possible enumerations: 0, 1, 2, 3, 4, 5. |
| `maintcostusd` | numeric | DECIMAL(9,2) cost of maintenance in USD (was 'MaintenanceCostUSD') (e.g., 250.00). |
| `cleancostusd` | numeric | NUMERIC(8,3) cost of cleaning in USD (was 'CleaningCostUSD') (e.g., 50.125). |
| `replacecostusd` | numeric | DECIMAL(9,3) cost to replace components in USD (was 'ReplacementCostUSD') (e.g., 1200.500). |
| `revlossusd` | numeric | NUMERIC(7,2) revenue loss in USD due to downtime (was 'RevenueLossUSD') (e.g., 100.25). |

# Joins

* `compref` references `panemark` in [panel](/tables/panel.md).
* `obsref` references `perfregistry` in [performance](/tables/performance.md).
* `powerref` references `growregistry` in [plant](/tables/plant.md).
