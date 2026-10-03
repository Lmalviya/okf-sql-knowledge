---
type: Calculation
title: Thermal Stability Coefficient (TSC)
description: Advanced temperature stability metric incorporating thermal mass and ambient conditions.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 50
---

# Definition

TSC = \text{TSS} \cdot e^{-\frac{|\text{TempNowC} - \text{StoreTempC}|}{5}} \cdot \left(1 - \alpha \cdot \frac{\text{TempNowC} - \text{TempPrevC}}{\text{ReadingInterval}}\right)

# Columns used

* [sensordata](/tables/sensordata.md): `storetempc`, `tempnowc`

# Depends on

* [Temperature Stability Score (TSS)](/knowledge/temperature-stability-score.md)
* [ReadingInterval](/knowledge/readinginterval.md)

# Used by

* [Critical Cascade Condition](/knowledge/critical-cascade-condition.md)
* [Dynamic Stability Threshold](/knowledge/dynamic-stability-threshold.md)
* [Multi-System Failure Risk](/knowledge/multi-system-failure-risk.md)
