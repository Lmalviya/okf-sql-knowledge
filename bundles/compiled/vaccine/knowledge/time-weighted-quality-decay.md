---
type: Calculation
title: Time-Weighted Quality Decay (TWQD)
description: Calculates quality deterioration rate considering time and environmental factors.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 52
---

# Definition

TWQD = -\frac{d}{dt}(\text{VVP}) \times (1 + \beta\text{TBS}) \times (1 + \gamma(\text{1-TSS}))

# Depends on

* [Vaccine Viability Period (VVP)](/knowledge/vaccine-viability-period.md)
* [Temperature Breach Severity (TBS)](/knowledge/temperature-breach-severity.md)
* [Temperature Stability Score (TSS)](/knowledge/temperature-stability-score.md)

# Used by

* [Critical Cascade Condition](/knowledge/critical-cascade-condition.md)
* [Predictive Degradation Alert](/knowledge/predictive-degradation-alert.md)
