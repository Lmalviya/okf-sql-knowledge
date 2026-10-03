---
type: Calculation
title: Urgency Rank
description: Ranks vehicles based on maintenance risk and overdue days.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 65
---

# Definition

\text{Rank assigned to vehicles based on descending order of } \text{CMR} + \text{DaysOverdue} / 30

# Depends on

* [Combined Maintenance Risk (CMR)](/knowledge/combined-maintenance-risk.md)
* [Days Overdue](/knowledge/days-overdue.md)
