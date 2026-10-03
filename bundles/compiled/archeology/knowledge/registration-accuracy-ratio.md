---
type: Calculation
title: Registration Accuracy Ratio (RAR)
description: Evaluates registration accuracy relative to scan resolution using propagation of uncertainty principles.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 33
---

# Definition

RAR = \frac{ScanResolMm}{LogAccuMm \times \sqrt{1 + \frac{ErrValMm}{LogAccuMm}}}, \text{ where values > 1 indicate registration accuracy exceeds scan resolution, a desirable outcome for precise spatial analysis.}

# Columns used

* [scanregistration](/tables/scanregistration.md): `logaccumm`, `errvalmm`
* [scanpointcloud](/tables/scanpointcloud.md): `scanresolmm`

# Used by

* [Digital Preservation Quality (DPQ)](/knowledge/digital-preservation-quality.md)
* [Registration Confidence Level](/knowledge/registration-confidence-level.md)
