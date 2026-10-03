---
type: Calculation
title: Scan Resolution Index (SRI)
description: A sophisticated compound index measuring the overall resolution quality of a scan based on resolution and point density.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 0
---

# Definition

SRI = \frac{\log_{10}(ScanResolMm \times 10^3)}{\log_{10}(PointDense)} \times 5, \text{ where lower values indicate higher quality resolution and more balanced scanning parameters.}

# Columns used

* [scanpointcloud](/tables/scanpointcloud.md): `scanresolmm`, `pointdense`

# Used by

* [Scan Quality Score (SQS)](/knowledge/scan-quality-score.md)
