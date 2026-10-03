---
type: PostgreSQL Table
title: airqualityreadings
description: '11 columns: co2ppm, tvocppb, ozoneppb, so2ppb, no2ppb, pm25conc, pm10conc, hchoconc, airexrate, airvelms. Joins to environmentalreadingscore.'
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
| `envreadref` | bigint | BIGINT FOREIGN KEY referencing EnvironmentalReadingsCore(EnvReadRegistry). Links this record to its main environmental reading. |
| `co2ppm` | smallint | SMALLINT measuring CO2 concentration in parts per million (ppm). Typical range: 300–2000. |
| `tvocppb` | integer | INT capturing total volatile organic compounds in parts per billion (ppb). |
| `ozoneppb` | integer | INT indicating ozone concentration in ppb. |
| `so2ppb` | smallint | SMALLINT for sulfur dioxide concentration in ppb. |
| `no2ppb` | bigint | BIGINT for nitrogen dioxide concentration in ppb. |
| `pm25conc` | real | REAL measuring particulate matter (PM2.5) in µg/m³ or a similar metric. |
| `pm10conc` | numeric | NUMERIC(5,2) measuring PM10 concentration, possibly µg/m³ as well. |
| `hchoconc` | numeric | NUMERIC(7,4) for formaldehyde (HCHO) concentration (e.g., mg/m³ or another scale). |
| `airexrate` | numeric | NUMERIC(4,1) indicating air exchange rate (e.g., air changes per hour). |
| `airvelms` | numeric | NUMERIC(5,2) capturing air velocity in meters per second (m/s). |

# Joins

* `envreadref` references `envreadregistry` in [environmentalreadingscore](/tables/environmentalreadingscore.md).

# Related knowledge

* [AirQualityReadings.PM25Conc](/knowledge/airqualityreadings-pm25conc.md)
