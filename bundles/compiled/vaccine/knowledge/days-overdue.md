---
type: Calculation
title: Days Overdue
description: Calculates the number of days past the scheduled maintenance or calibration date.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 61
---

# Definition

DaysOverdue = \max\left( (\text{Current_Date} - \text{MaintDateNext}), (\text{Current_Date} - \text{CalibDateNext}), 0 \right)

# Columns used

* [regulatoryandmaintenance](/tables/regulatoryandmaintenance.md): `maintdatenext`, `calibdatenext`

# Used by

* [Urgency Rank](/knowledge/urgency-rank.md)
