---
type: Calculation
title: Scan Time Efficiency (STE)
description: Measures how efficiently scanning time was used relative to data quality and completeness metrics.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 30
---

# Definition

STE = \frac{SQS \times \sqrt{CoverPct}}{SpanMin \times \sqrt{ScanCount}}, \text{ where SQS is the Scan Quality Score and higher STE values indicate more efficient use of scanning time relative to coverage achieved.}

# Columns used

* [scans](/tables/scans.md): `scancount`, `spanmin`
* [scanpointcloud](/tables/scanpointcloud.md): `coverpct`

# Depends on

* [Scan Quality Score (SQS)](/knowledge/scan-quality-score.md)
