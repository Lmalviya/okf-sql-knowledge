---
type: PostgreSQL Table
title: sensitivitydata
description: '12 columns: envsensitivity, lightsensitivity, tempsensitivity, humiditysensitivity, vibrasensitivity, pollutantsensitivity, pestsensitivity, handlesensitivity, transportsensitivity, displaysensitivity, storagesensitivity. Joins to artifactscore.'
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
| `artref` | character | CHAR(10) FOREIGN KEY referencing ArtifactsCore(ArtRegistry). |
| `envsensitivity` | character | CHAR(20) for overall environmental sensitivity (possible values: 'Low', 'High', 'Medium'). |
| `lightsensitivity` | character varying | VARCHAR(80) describing light/UV sensitivity (possible values: 'High', 'Low', 'Medium'). |
| `tempsensitivity` | character varying | VARCHAR(50) summarizing temperature tolerance (possible values: 'High', 'Low', 'Medium'). |
| `humiditysensitivity` | text | TEXT detailing humidity requirements or maximum humidity tolerance (possible values: 'Medium', 'High', 'Low'). |
| `vibrasensitivity` | character | CHAR(20) describing vibration tolerance (possible values: 'Medium', 'High', 'Low'). |
| `pollutantsensitivity` | character varying | VARCHAR(100) indicating susceptibility to pollutants (possible values: 'High', 'Medium', 'Low'). |
| `pestsensitivity` | text | TEXT describing vulnerability to pests (possible values: 'High', 'Low', 'Medium'). |
| `handlesensitivity` | character | CHAR(20) for handling sensitivity (possible values: 'Medium', 'Low', 'High'). |
| `transportsensitivity` | character varying | VARCHAR(50) specifying special packaging needs (possible values: 'High', 'Low', 'Medium'). |
| `displaysensitivity` | character varying | VARCHAR(120) noting special display requirements (possible values: 'Low', 'High', 'Medium'). |
| `storagesensitivity` | text | TEXT detailing storage conditions (possible values: 'Medium', 'Low', 'High'). |

# Joins

* `artref` references `artregistry` in [artifactscore](/tables/artifactscore.md).

# Related knowledge

* [Sensitivity Weight Values](/knowledge/sensitivity-weight-values.md)
* [Environmental Risk Factor (ERF)](/knowledge/environmental-risk-factor.md)
* [Organic Material Vulnerability](/knowledge/organic-material-vulnerability.md)
* [SensitivityData.LightSensitivity](/knowledge/sensitivitydata-lightsensitivity.md)
* [SensitivityData.HumiditySensitivity](/knowledge/sensitivitydata-humiditysensitivity.md)
