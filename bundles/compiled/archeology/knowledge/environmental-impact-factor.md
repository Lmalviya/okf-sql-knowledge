---
type: Calculation
title: Environmental Impact Factor (EIF)
description: Quantifies how environmental conditions affected scan quality using statistical correlation analysis.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 31
---

# Definition

EIF = \frac{SQS}{\text{ESI} + 10} \times 100, \text{ where SQS is the Scan Quality Score and ESI is the Environmental Suitability Index. Values closer to 100 indicate minimal environmental interference with data acquisition.}

# Depends on

* [Scan Quality Score (SQS)](/knowledge/scan-quality-score.md)
* [Environmental Suitability Index (ESI)](/knowledge/environmental-suitability-index.md)

# Used by

* [Environmental Challenge Scan](/knowledge/environmental-challenge-scan.md)
