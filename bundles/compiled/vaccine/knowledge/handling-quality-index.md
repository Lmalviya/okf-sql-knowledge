---
type: Calculation
title: Handling Quality Index (HQI)
description: Measures quality of shipment handling.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 8
---

# Definition

HQI = (1 - \frac{HandleEvents}{100}) \times (1 - \frac{CritEvents}{10})

# Columns used

* [sensordata](/tables/sensordata.md): `handleevents`, `critevents`

# Used by

* [Stable Transport](/knowledge/stable-transport.md)
* [Total Risk Score (TRS)](/knowledge/total-risk-score.md)
* [Shipment Quality Index (SQI)](/knowledge/shipment-quality-index.md)
* [Transport Safety Rating (TSR)](/knowledge/transport-safety-rating.md)
* [Multi-Parameter Risk Assessment (MPRA)](/knowledge/multi-parameter-risk-assessment.md)
* [Logistics Performance Metric (LPM)](/knowledge/logistics-performance-metric.md)
* [Multi-System Failure Risk](/knowledge/multi-system-failure-risk.md)
