---
type: Calculation
title: Scan Quality Score (SQS)
description: Comprehensive quality metric combining resolution, coverage, and noise factors with weighted importance.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 3
---

# Definition

SQS = \left(\frac{10}{SRI}\right)^{1.5} \times \left(\frac{SCE}{100}\right) \times \left(1 - \frac{NoiseDb}{30}\right)^2, \text{ where higher values indicate exponentially better overall scan quality with emphasis on resolution.}

# Columns used

* [scanpointcloud](/tables/scanpointcloud.md): `noisedb`

# Depends on

* [Scan Resolution Index (SRI)](/knowledge/scan-resolution-index.md)
* [Scan Coverage Effectiveness (SCE)](/knowledge/scan-coverage-effectiveness.md)

# Used by

* [Archaeological Documentation Completeness (ADC)](/knowledge/archaeological-documentation-completeness.md)
* [Premium Quality Scan](/knowledge/premium-quality-scan.md)
* [Scan Time Efficiency (STE)](/knowledge/scan-time-efficiency.md)
* [Environmental Impact Factor (EIF)](/knowledge/environmental-impact-factor.md)
* [Equipment Effectiveness Ratio (EER)](/knowledge/equipment-effectiveness-ratio.md)
