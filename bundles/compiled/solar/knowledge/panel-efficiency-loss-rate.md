---
type: Calculation
title: Panel Efficiency Loss Rate (PELR)
description: Calculates the percentage of efficiency loss per year for a solar panel.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 1
---

# Definition

PELR = \frac{CurrentEfficiencyPercent - InitialEfficiencyPercent}{Years\_Since\_Installation} \times 100\%, \text{where CurrentEfficiencyPercent is obtained from efficiency_profile.current_efficiency.curreffpct.}

# Columns used

* [performance](/tables/performance.md): `efficiency_profile`

# Used by

* [Normalized Degradation Index (NDI)](/knowledge/normalized-degradation-index.md)
* [Financial Impact of Degradation (FID)](/knowledge/financial-impact-of-degradation.md)
* [Environmental Stress Classification](/knowledge/environmental-stress-classification.md)
