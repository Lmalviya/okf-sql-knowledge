---
type: PostgreSQL Table
title: lightandradiationreadings
description: '5 columns: lightlux, uvuwcm2, irwm2, visibleexplxh. Joins to environmentalreadingscore.'
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
| `envreadref` | bigint | BIGINT FOREIGN KEY referencing EnvironmentalReadingsCore(EnvReadRegistry). Associates light data with an existing environment reading. |
| `lightlux` | integer | INT measuring visible light intensity in lux. |
| `uvuwcm2` | numeric | NUMERIC(6,2) capturing UV radiation in microwatts per cm² (µW/cm²). |
| `irwm2` | numeric | NUMERIC(6,2) measuring infrared radiation in W/m². |
| `visibleexplxh` | integer | INT indicating total visible light exposure over time in lux-hours (Lx·h). |

# Joins

* `envreadref` references `envreadregistry` in [environmentalreadingscore](/tables/environmentalreadingscore.md).

# Related knowledge

* [Light Exposure Risk (LER)](/knowledge/light-exposure-risk.md)
* [LightAndRadiationReadings.LightLux](/knowledge/lightandradiationreadings-lightlux.md)
