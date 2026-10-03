---
type: Calculation
title: Coolant Efficiency Index (CEI)
description: Measures how efficiently coolant is maintaining temperature stability.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 31
---

# Definition

CEI = \text{TSS} \times \frac{\text{CoolRemainPct}}{100} \times (1 - \frac{\text{CDR}}{20})

# Columns used

* [container](/tables/container.md): `coolremainpct`

# Depends on

* [Temperature Stability Score (TSS)](/knowledge/temperature-stability-score.md)
* [Coolant Depletion Rate (CDR)](/knowledge/coolant-depletion-rate.md)

# Used by

* [Container Efficiency Score (CES)](/knowledge/container-efficiency-score.md)
* [Route Risk Factor (RRF)](/knowledge/route-risk-factor.md)
* [Vaccine Safety Index (VSI)](/knowledge/vaccine-safety-index.md)
* [Severe Container Risk](/knowledge/severe-container-risk.md)
* [Environmental Stress Factor (ESF)](/knowledge/environmental-stress-factor.md)
