---
type: PostgreSQL Table
title: exhibitionhalls
description: '9 columns: cctvcoverage, motiondetectstatus, alarmsysstatus, accessctrlstatus, visitorcountdaily, visitorflowrate, visitordwellmin, visitorbehaviornotes. Joins to artifactscore.'
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
| `hallrecord` | character, primary key |  |
| `cctvcoverage` | character varying | VARCHAR(100) describing the CCTV coverage (possible values: 'Partial', 'Full', 'Limited'). |
| `motiondetectstatus` | character varying | VARCHAR(50) summarizing motion detection status (possible values: 'Active', 'Maintenance', 'Partial'). |
| `alarmsysstatus` | character | CHAR(15) for alarm system status (possible values: 'Armed', 'Maintenance', 'Partial'). |
| `accessctrlstatus` | character varying | VARCHAR(80) describing the level of access control (possible values: 'Maintenance', 'Active', 'Partial'). |
| `visitorcountdaily` | integer | INT representing the typical or observed daily visitor count (unbounded integer). |
| `visitorflowrate` | USER-DEFINED | SMALLINT indicating how many visitors pass through (possible values: 'Low', 'Medium', 'High'). |
| `visitordwellmin` | smallint | SMALLINT specifying the average dwell time (in minutes) per visitor. |
| `visitorbehaviornotes` | text | TEXT field for any additional notes on visitor behaviors, traffic patterns, or compliance issues. |

# Joins

* `hallrecord` references `artregistry` in [artifactscore](/tables/artifactscore.md).

# Related knowledge

* [Visitor Impact Risk (VIR)](/knowledge/visitor-impact-risk.md)
* [ExhibitionHalls.CCTVCoverage](/knowledge/exhibitionhalls-cctvcoverage.md)
