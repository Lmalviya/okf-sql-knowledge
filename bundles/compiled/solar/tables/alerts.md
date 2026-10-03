---
type: PostgreSQL Table
title: alerts
description: '10 columns: alertmoment, alertstat, alertcnt, maintprior, replaceprior, optpotential. Joins to panel, performance, plant.'
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
| `alertreg` | character varying, primary key | VARCHAR(50) PRIMARY KEY uniquely identifying each alert record. |
| `compreg` | uuid | UUID REFERENCES Plant(GrowRegistry), referencing which plant component triggered the alert. |
| `deviceref` | character varying | VARCHAR(50) REFERENCES Panel(PaneMark), linking alert to a specific panel if needed. |
| `incidentref` | character varying | VARCHAR(50) REFERENCES Performance(PerfRegistry), linking alert to performance data if relevant. |
| `alertmoment` | timestamp without time zone | TIMESTAMP logging when the alert was generated (e.g., '2023-07-20 14:05:00'). |
| `alertstat` | character varying | VARCHAR(50) summarizing the alert’s status or severity (was 'AlertStatus'). Possible enumerations: 'Warning', 'Critical'. |
| `alertcnt` | smallint | SMALLINT counting how many times this alert occurred (was 'AlertCount') (e.g., 3). |
| `maintprior` | character varying | VARCHAR(50) describing the maintenance priority (was 'MaintenancePriority'). Possible enumerations: 'High', 'Medium', 'Low'. |
| `replaceprior` | character varying | VARCHAR(50) indicating the replacement priority (was 'ReplacementPriority'). Possible enumerations: 'High', 'Medium', 'Low'. |
| `optpotential` | character varying | VARCHAR(100) reflecting any optimization potential (was 'OptimizationPotential'). Possible enumerations: 'Medium', 'High', 'Low'. |

# Joins

* `compreg` references `growregistry` in [plant](/tables/plant.md).
* `deviceref` references `panemark` in [panel](/tables/panel.md).
* `incidentref` references `perfregistry` in [performance](/tables/performance.md).
