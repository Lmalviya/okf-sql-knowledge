---
type: Calculation
title: Fill Factor Degradation Rate (FFDR)
description: Calculates the rate at which the fill factor of a panel is degrading over time.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 5
---

# Definition

FFDR = \frac{FillFactorInitial - FillFactorCurrent}{Years\_Since\_Installation} \times 100\%, \text{where FillFactorInitial and FillFactorCurrent are from the electrical table.}
