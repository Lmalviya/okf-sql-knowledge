---
type: Calculation
title: Environmental Stress Factor (ESF)
description: Quantifies combined environmental stressors on vaccine stability.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 53
---

# Definition

ESF = \text{TSS} \cdot (1 + \frac{\text{TBS}}{5}) \cdot \text{CEI} \cdot (1 + \frac{|\text{TempNowC} - \text{StoreTempC}|}{\text{TempTolC}})

# Columns used

* [sensordata](/tables/sensordata.md): `storetempc`, `temptolc`, `tempnowc`

# Depends on

* [Temperature Stability Score (TSS)](/knowledge/temperature-stability-score.md)
* [Temperature Breach Severity (TBS)](/knowledge/temperature-breach-severity.md)
* [Coolant Efficiency Index (CEI)](/knowledge/coolant-efficiency-index.md)

# Used by

* [Critical Cascade Condition](/knowledge/critical-cascade-condition.md)
* [Compound Quality Risk](/knowledge/compound-quality-risk.md)
* [Multi-System Failure Risk](/knowledge/multi-system-failure-risk.md)
* [Predictive Degradation Alert](/knowledge/predictive-degradation-alert.md)
