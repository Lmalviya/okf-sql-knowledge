---
type: Calculation
title: Scan Coverage Effectiveness (SCE)
description: Measures how effectively a scan covers its target area considering both coverage percentage and overlap redundancy.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 1
---

# Definition

SCE = CoverPct \times \left(1 + \frac{LapPct}{100} \times \left(1 - \frac{CoverPct}{100}\right)\right), \text{ where higher values indicate more effective coverage with appropriate overlap.}

# Columns used

* [scanpointcloud](/tables/scanpointcloud.md): `coverpct`, `lappct`

# Used by

* [Scan Quality Score (SQS)](/knowledge/scan-quality-score.md)
* [Archaeological Documentation Completeness (ADC)](/knowledge/archaeological-documentation-completeness.md)
* [Digital Preservation Quality (DPQ)](/knowledge/digital-preservation-quality.md)
