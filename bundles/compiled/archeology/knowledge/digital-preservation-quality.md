---
type: Calculation
title: Digital Preservation Quality (DPQ)
description: Comprehensive metric for evaluating digital preservation quality for archaeological sites with weighted quality factors.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 38
---

# Definition

DPQ = (0.3 \times ADC) + (0.3 \times MFS) + (0.2 \times RAR) + (0.2 \times SCE) - 2 \times \sqrt{\frac{ErrValMm}{ScanResolMm}}, \text{ where ADC is Archaeological Documentation Completeness, MFS is Model Fidelity Score, RAR is Registration Accuracy Ratio, and SCE is Scan Coverage Effectiveness.}

# Columns used

* [scanregistration](/tables/scanregistration.md): `errvalmm`
* [scanpointcloud](/tables/scanpointcloud.md): `scanresolmm`

# Depends on

* [Archaeological Documentation Completeness (ADC)](/knowledge/archaeological-documentation-completeness.md)
* [Model Fidelity Score (MFS)](/knowledge/model-fidelity-score.md)
* [Registration Accuracy Ratio (RAR)](/knowledge/registration-accuracy-ratio.md)
* [Scan Coverage Effectiveness (SCE)](/knowledge/scan-coverage-effectiveness.md)

# Used by

* [Multi-Phase Documentation Project](/knowledge/multi-phase-documentation-project.md)
