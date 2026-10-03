---
type: PostgreSQL Table
title: robot_record
description: '3 columns: rects, botcode.'
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_schema.txt
  title: robot schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_column_meaning_base.json
  title: robot column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `recreg` | character varying, primary key | Primary key (VARCHAR(20)) uniquely identifying this record in the robot database. Was 'RecordRegistry' previously. |
| `rects` | timestamp without time zone | TIMESTAMP marking when the record was created or logged. Must be present (NOT NULL). |
| `botcode` | character varying | VARCHAR(25) referencing or naming the robot code or ID. Required field (NOT NULL). |

# Related knowledge

* [Robot Age in Years (RAY)](/knowledge/robot-age-in-years.md)
