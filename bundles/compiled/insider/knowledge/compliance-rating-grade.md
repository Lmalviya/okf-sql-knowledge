---
type: Value Illustration
title: Compliance Rating Grade
description: Explains the overall compliance assessment grade assigned in compliance cases.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 71
---

# Definition

`comprate`: The compliance rating grade. 'A' represents excellent compliance. 'B' indicates good compliance with minor issues. 'C' suggests significant compliance deficiencies needing attention. 'D' signifies serious or repeated compliance failures requiring immediate action.

# Columns used

* [compliancecase](/tables/compliancecase.md): `comprate`

# Used by

* [Compliance Health Score (CHS)](/knowledge/compliance-health-score.md)
