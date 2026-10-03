---
type: Calculation
title: Compliance Cost Ratio (CCR)
description: Evaluates the cost of compliance relative to potential penalties.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 3
---

# Definition

CCR = \frac{\text{CostUSD}}{\text{PenUSD} + 1}

# Columns used

* [riskmanagement](/tables/riskmanagement.md): `costusd`, `penusd`

# Used by

* [Overburdened Compliance Flow](/knowledge/overburdened-compliance-flow.md)
