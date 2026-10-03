---
type: PostgreSQL Table
title: panel
description: '9 columns: panemfr, paneline, panetype, powratew, paneeffpct, nomtempc, tempcoef. Joins to plant.'
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
| `panemark` | character varying, primary key | VARCHAR(50) PRIMARY KEY uniquely identifying each panel record. |
| `hubregistry` | uuid | UUID REFERENCES Plant(GrowRegistry), linking this panel to a specific plant. |
| `panemfr` | character varying | VARCHAR(100) describing the manufacturer’s name (was 'PanelManufacturer'). Possible enumerations: 'Longi', 'Canadian Solar', 'JA Solar', 'JinkoSolar', 'Trina'. |
| `paneline` | character varying | VARCHAR(100) capturing the panel’s model line or series (was 'PanelModel') (e.g., 'ModelX', 'CS6K-P'). |
| `panetype` | character varying | VARCHAR(50) labeling the panel type (was 'PanelType'). Possible enumerations: 'Mono-PERC', 'HJT', 'Poly-PERC', 'Bifacial', 'TOPCon'. |
| `powratew` | smallint | SMALLINT specifying the rated power output of the panel in watts (was 'PanelRatedPowerW'). Possible enumerations: 650, 450, 600, 550, 500. |
| `paneeffpct` | numeric | DECIMAL(7,3) storing the panel’s nominal efficiency percentage (was 'PanelEfficiencyPercent') (e.g., 21.345). |
| `nomtempc` | numeric | NUMERIC(7,3) indicating the panel’s nominal operating temperature in °C (was 'NominalOperatingTempC') (e.g., 45.000). |
| `tempcoef` | numeric | DECIMAL(4,3) capturing the temperature coefficient for panel performance (was 'TemperatureCoefficient') (e.g., -0.350). |

# Joins

* `hubregistry` references `growregistry` in [plant](/tables/plant.md).

# Related knowledge

* [Temperature Performance Coefficient Impact (TPCI)](/knowledge/temperature-performance-coefficient-impact.md)
* [PaneEffPct (Panel Efficiency Percentage)](/knowledge/paneeffpct.md)
* [TempCoef (Temperature Coefficient)](/knowledge/tempcoef.md)
* [Effective Performance Index (EPI)](/knowledge/effective-performance-index.md)
* [Weather Corrected Efficiency (WCE)](/knowledge/weather-corrected-efficiency.md)
