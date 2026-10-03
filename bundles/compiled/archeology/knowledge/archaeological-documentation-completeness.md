---
type: Calculation
title: Archaeological Documentation Completeness (ADC)
description: Comprehensive score for how completely a site has been documented through scanning with weighted importance factors.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 9
---

# Definition

ADC = \left(SQS \times 0.4\right) + \left(MFS \times 0.4\right) + \left(SCE \times 0.2\right) - 5 \times \sqrt{\frac{NoiseDb}{10}}, \text{ where higher values indicate more complete documentation with multiple quality factors.}

# Columns used

* [scanpointcloud](/tables/scanpointcloud.md): `noisedb`

# Depends on

* [Scan Quality Score (SQS)](/knowledge/scan-quality-score.md)
* [Model Fidelity Score (MFS)](/knowledge/model-fidelity-score.md)
* [Scan Coverage Effectiveness (SCE)](/knowledge/scan-coverage-effectiveness.md)

# Used by

* [Full Archaeological Digital Twin](/knowledge/full-archaeological-digital-twin.md)
* [Digital Preservation Quality (DPQ)](/knowledge/digital-preservation-quality.md)
* [Multi-Phase Documentation Project](/knowledge/multi-phase-documentation-project.md)
