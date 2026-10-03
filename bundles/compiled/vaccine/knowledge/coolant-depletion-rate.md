---
type: Calculation
title: Coolant Depletion Rate (CDR)
description: Measures how quickly the coolant is being depleted.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 1
---

# Definition

CDR = \frac{100 - CoolRemainPct}{(Current_Date - RefillLatest)}

# Columns used

* [container](/tables/container.md): `coolremainpct`, `refilllatest`

# Used by

* [Coolant Critical](/knowledge/coolant-critical.md)
* [Coolant Efficiency Index (CEI)](/knowledge/coolant-efficiency-index.md)
* [Multi-Parameter Risk Assessment (MPRA)](/knowledge/multi-parameter-risk-assessment.md)
* [Depletion Rank](/knowledge/depletion-rank.md)
