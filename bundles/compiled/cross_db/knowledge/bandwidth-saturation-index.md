---
type: Calculation
title: Bandwidth Saturation Index (BSI)
description: Quantifies how close a data flow is to saturating available bandwidth.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 1
---

# Definition

BSI = \text{BwidthPct} \times \frac{\text{DataSizeMB}}{\text{DurMin}}

# Columns used

* [dataflow](/tables/dataflow.md): `datasizemb`, `durmin`, `bwidthpct`

# Used by

* [Overloaded Data Flow](/knowledge/overloaded-data-flow.md)
* [Bandwidth Risk Factor (BRF)](/knowledge/bandwidth-risk-factor.md)
* [High-Pressure Data Flow](/knowledge/high-pressure-data-flow.md)
