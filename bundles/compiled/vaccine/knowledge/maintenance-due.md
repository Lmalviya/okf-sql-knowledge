---
type: Business Rule
title: Maintenance Due
description: Identifies equipment requiring maintenance.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 13
---

# Definition

Equipment where MCS < 0.7 and (Current_Date > MaintDateNext or Current_Date > CalibDateNext)

# Columns used

* [regulatoryandmaintenance](/tables/regulatoryandmaintenance.md): `maintdatenext`, `calibdatenext`

# Depends on

* [Maintenance Compliance Score (MCS)](/knowledge/maintenance-compliance-score.md)
