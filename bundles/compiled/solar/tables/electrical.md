---
type: PostgreSQL Table
title: electrical
description: '15 columns: iscinita, isccurra, vocinitv, voccurrv, impinita, impcurra, vmpinitv, vmpcurrv, ffactorinit, ffactorcurr, seriesresohm, shuntresohm. Joins to panel, performance.'
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
| `elecregistry` | character varying, primary key | VARCHAR(50) PRIMARY KEY uniquely identifying each electrical record. |
| `engyunitref` | character varying | VARCHAR(50) REFERENCES Panel(PaneMark), tying this electrical record to a panel. |
| `efflogref` | character varying | VARCHAR(50) REFERENCES Performance(PerfRegistry), linking to a performance record if relevant. |
| `iscinita` | numeric | DECIMAL(7,3) short-circuit current (Isc) at initial measurement (was 'IscInitialA') (e.g., 9.200). |
| `isccurra` | numeric | NUMERIC(7,3) current Isc measurement (was 'IscCurrentA') (e.g., 8.950). |
| `vocinitv` | numeric | NUMERIC(7,3) open-circuit voltage (Voc) initially (was 'VocInitialV') (e.g., 49.000). |
| `voccurrv` | numeric | DECIMAL(7,3) current Voc measurement (was 'VocCurrentV') (e.g., 48.500). |
| `impinita` | numeric | DECIMAL(7,3) current at maximum power initially (was 'ImpInitialA') (e.g., 8.700). |
| `impcurra` | numeric | NUMERIC(7,3) current Imp measurement (was 'ImpCurrentA') (e.g., 8.450). |
| `vmpinitv` | numeric | DECIMAL(7,3) voltage at maximum power initially (was 'VmpInitialV') (e.g., 46.500). |
| `vmpcurrv` | numeric | NUMERIC(6,2) current Vmp measurement (was 'VmpCurrentV') (e.g., 46.12). |
| `ffactorinit` | numeric | DECIMAL(7,3) fill factor initially (was 'FillFactorInitial') (e.g., 0.780). |
| `ffactorcurr` | numeric | NUMERIC(7,3) current fill factor (was 'FillFactorCurrent') (e.g., 0.765). |
| `seriesresohm` | numeric | DECIMAL(7,3) series resistance in ohms (was 'SeriesResistanceOhm') (e.g., 0.300). |
| `shuntresohm` | numeric | DECIMAL(4,1) shunt resistance in ohms (was 'ShuntResistanceOhm') (e.g., 400.0). |

# Joins

* `efflogref` references `perfregistry` in [performance](/tables/performance.md).
* `engyunitref` references `panemark` in [panel](/tables/panel.md).

# Related knowledge

* [Electrical Degradation Index (EDI)](/knowledge/electrical-degradation-index.md)
