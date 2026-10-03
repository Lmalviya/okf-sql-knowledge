---
type: Calculation
title: Point Cloud Density Ratio (PCDR)
description: Evaluates the relationship between total points and cloud density, used to assess scan efficiency and data distribution.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 2
---

# Definition

PCDR = \frac{TotalPts}{CloudDense \times AreaM2}, \text{ where higher values suggest more efficient and spatially consistent scanning techniques.}

# Columns used

* [scanspatial](/tables/scanspatial.md): `aream2`
* [scanpointcloud](/tables/scanpointcloud.md): `totalpts`, `clouddense`

# Used by

* [Feature Extraction Efficiency (FEE)](/knowledge/feature-extraction-efficiency.md)
