---
type: Calculation
title: Route Completion Percentage (RCP)
description: Calculates the percentage of route completed.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 4
---

# Definition

RCP = \frac{DistDoneKm}{DistDoneKm + DistLeftKm} \times 100

# Columns used

* [transportinfo](/tables/transportinfo.md): `distdonekm`, `distleftkm`

# Used by

* [High-Risk Route](/knowledge/high-risk-route.md)
* [Transport Safety Rating (TSR)](/knowledge/transport-safety-rating.md)
* [Route Risk Factor (RRF)](/knowledge/route-risk-factor.md)
* [Logistics Performance Metric (LPM)](/knowledge/logistics-performance-metric.md)
