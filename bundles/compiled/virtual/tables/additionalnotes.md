---
type: PostgreSQL Table
title: additionalnotes
description: '3 columns: noteinfo. Joins to retentionandinfluence.'
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: schema
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_schema.txt
  title: virtual schema (LiveSQLBench)
- id: column_meaning_base
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_column_meaning_base.json
  title: virtual column descriptions (LiveSQLBench)
---

# Schema

| Column | Type | Meaning |
|---|---|---|
| `notesreg` | character varying, primary key | A VARCHAR(20) primary key for additional notes records (e.g., 'NOTE001'). |
| `notesretainpivot` | character varying | A VARCHAR(20) FK referencing RetentionAndInfluence(RetReg). |
| `noteinfo` | text | A TEXT field storing any free-form notes or remarks about the fan. |

# Joins

* `notesretainpivot` references `retreg` in [retentionandinfluence](/tables/retentionandinfluence.md).
