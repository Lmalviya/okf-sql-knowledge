---
type: PostgreSQL Table
title: showcases
description: '17 columns: airtightness, showcasematerial, sealcondition, maintstatus, filterstatus, silicagelstatus, silicagelchangedate, humiditybuffercap, pollutantabsorbcap, leakrate, pressurepa, inertgassysstatus, firesuppresssys, empowerstatus, backupsysstatus. Joins to exhibitionhalls.'
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
| `showcasereg` | character, primary key | CHAR(12) PRIMARY KEY for identifying each showcase (e.g., 'SHOW00000012'). |
| `hallref` | character | CHAR(8) FOREIGN KEY referencing ExhibitionHalls(HallRegistry). Connects the showcase to a particular hall. |
| `airtightness` | real | REAL measuring the physical seal quality, often tested as a numeric rating or leakage rate. |
| `showcasematerial` | character varying | VARCHAR(80) describing the material (possible values: 'Tempered Glass', 'Glass', 'Acrylic'). |
| `sealcondition` | character varying | VARCHAR(30) indicating the seal’s condition (possible values: 'Poor', 'Excellent', 'Good', 'Fair'). |
| `maintstatus` | character | CHAR(15) for the showcase’s maintenance status (possible values: 'Overdue', 'Due', 'Good'). |
| `filterstatus` | text | TEXT detailing installed filters (possible values: 'Replace Now', 'Replace Soon', 'Clean'). |
| `silicagelstatus` | character | CHAR(20) noting the condition of silica gel (possible values: 'Active', 'Replace Soon', 'Replace Now'). |
| `silicagelchangedate` | date | DATE of the last silica gel replacement or recharge. |
| `humiditybuffercap` | smallint | SMALLINT rating or index of the showcase’s capacity to buffer humidity. |
| `pollutantabsorbcap` | numeric | NUMERIC(5,2) for the pollutant absorption capacity (quantity or threshold). |
| `leakrate` | real | REAL specifying the rate of air leakage, often tested to ensure stable internal conditions. |
| `pressurepa` | bigint | BIGINT capturing the internal pressure (in pascals) if pressurization is used. |
| `inertgassysstatus` | character varying | VARCHAR(50) describing any inert gas system status (possible values: 'Active', 'Standby', 'Maintenance'). |
| `firesuppresssys` | character varying | VARCHAR(50) summarizing fire suppression condition (possible values: 'Maintenance', 'Active', 'Standby'). |
| `empowerstatus` | character | CHAR(10) indicating emergency power readiness (possible values: 'Testing', 'Active', 'Standby'). |
| `backupsysstatus` | text | TEXT describing any backup systems (possible values: 'Ready', 'Maintenance', 'Testing') and their condition. |

# Joins

* `hallref` references `hallrecord` in [exhibitionhalls](/tables/exhibitionhalls.md).

# Related knowledge

* [Showcase Environmental Stability Rating (SESR)](/knowledge/showcase-environmental-stability-rating.md)
* [Showcase Failure Risk](/knowledge/showcase-failure-risk.md)
* [Showcases.Airtightness](/knowledge/showcases-airtightness.md)
