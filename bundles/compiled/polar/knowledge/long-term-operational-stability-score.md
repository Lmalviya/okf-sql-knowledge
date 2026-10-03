---
type: Calculation
title: Long-term Operational Stability Score (LOSS)
description: Evaluates the stability of equipment during long-term operation
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 37
---

# Definition

LOSS = 0.5 × EER + 0.5 × ORS × (1 - \frac{operationhours}{20000})

# Columns used

* [operationmaintenance](/tables/operationmaintenance.md): `operationhours`

# Depends on

* [Equipment Efficiency Rating (EER)](/knowledge/equipment-efficiency-rating.md)
* [Operational Readiness Score (ORS)](/knowledge/operational-readiness-score.md)

# Used by

* [Critical Infrastructure Protection Level (CIPL)](/knowledge/critical-infrastructure-protection-level.md)
