---
type: PostgreSQL Table
title: environmentalreadingscore
description: '8 columns: monitorcode, readtimestamp, tempc, tempvar24h, relhumidity, humvar24h, airpresshpa. Joins to showcases.'
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_schema.txt
  title: museum schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_column_meaning_base.json
  title: museum column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `monitorcode` | character | CHAR(10) identifier for the monitoring device or sensor (e.g., 'MON000001'). |
| `readtimestamp` | timestamp without time zone | TIMESTAMP NOT NULL indicating the date and time the reading was recorded. |
| `showcaseref` | character | CHAR(12) FOREIGN KEY referencing Showcases(ShowcaseReg), linking the reading to a specific showcase being monitored. |
| `tempc` | smallint | SMALLINT representing the measured temperature in Celsius. |
| `tempvar24h` | real | REAL showing the 24-hour variation in temperature (in °C). |
| `relhumidity` | integer | INT capturing the relative humidity percentage (0–100). |
| `humvar24h` | smallint | SMALLINT indicating the 24-hour variation in humidity (percentage points). |
| `airpresshpa` | real | REAL specifying the measured air pressure in hectopascals (hPa). |

# Joins

* `showcaseref` references `showcasereg` in [showcases](/tables/showcases.md).

# Related knowledge

* [Showcase Environmental Stability Rating (SESR)](/knowledge/showcase-environmental-stability-rating.md)
* [Material Deterioration Rate (MDR)](/knowledge/material-deterioration-rate.md)
* [Environmental Instability Event](/knowledge/environmental-instability-event.md)
* [EnvironmentalReadingsCore.TempC](/knowledge/environmentalreadingscore-tempc.md)
* [EnvironmentalReadingsCore.RelHumidity](/knowledge/environmentalreadingscore-relhumidity.md)
* [Environmental Compliance Index (ECI)](/knowledge/environmental-compliance-index.md)
