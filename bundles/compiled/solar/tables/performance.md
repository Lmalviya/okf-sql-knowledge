---
type: PostgreSQL Table
title: performance
description: '6 columns: perfmoment, measpoww, powlossw, efficiency_profile. Joins to panel.'
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
| `perfregistry` | character varying, primary key | VARCHAR(50) PRIMARY KEY uniquely identifying each performance record. |
| `solmodref` | character varying | VARCHAR(50) REFERENCES Panel(PaneMark), linking performance data to a panel. |
| `perfmoment` | timestamp without time zone | TIMESTAMP noting when these performance metrics were recorded (e.g., '2023-07-15 10:30:00'). |
| `measpoww` | numeric | NUMERIC(9,3) logging the measured power in watts (was 'MeasuredPowerW') (e.g., 595.000). |
| `powlossw` | numeric | DECIMAL(8,3) detailing power loss in watts (was 'PowerLossW') (e.g., 10.500). |
| `efficiency_profile` | jsonb | JSONB column. Captures efficiency and degradation metrics for a solar panel, including current efficiency, losses, and degradation rates. |

# JSON fields

* `efficiency_profile.current_efficiency.curreffpct`: NUMERIC(7,3) representing the current measured efficiency percentage (was 'CurrentEfficiencyPercent') (e.g., 18.750).
* `efficiency_profile.current_efficiency.efflosspct`: DECIMAL(7,3) indicating the efficiency loss percentage (was 'EfficiencyLossPercent') (e.g., 1.250).
* `efficiency_profile.degradation.anndegrate`: NUMERIC(7,3) capturing annual degradation rate percentage (was 'AnnualDegradationRate') (e.g., 0.500).
* `efficiency_profile.degradation.cumdegpct`: DECIMAL(7,3) storing cumulative degradation percentage (was 'CumulativeDegradationPercent') (e.g., 2.750).

# Joins

* `solmodref` references `panemark` in [panel](/tables/panel.md).

# Related knowledge

* [Panel Efficiency Loss Rate (PELR)](/knowledge/panel-efficiency-loss-rate.md)
* [Total System Loss (TSL)](/knowledge/total-system-loss.md)
* [Normalized Degradation Index (NDI)](/knowledge/normalized-degradation-index.md)
* [Weather Corrected Efficiency (WCE)](/knowledge/weather-corrected-efficiency.md)
