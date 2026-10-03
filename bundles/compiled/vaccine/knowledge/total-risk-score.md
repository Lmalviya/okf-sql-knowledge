---
type: Calculation
title: Total Risk Score (TRS)
description: Combines container risk and handling quality for overall risk assessment.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 30
---

# Definition

TRS = \text{CRI} \times (1 - \text{HQI}) \times (1 + \text{TBS})

# Depends on

* [Container Risk Index (CRI)](/knowledge/container-risk-index.md)
* [Handling Quality Index (HQI)](/knowledge/handling-quality-index.md)
* [Temperature Breach Severity (TBS)](/knowledge/temperature-breach-severity.md)

# Used by

* [Transport Safety Rating (TSR)](/knowledge/transport-safety-rating.md)
* [Route Risk Factor (RRF)](/knowledge/route-risk-factor.md)
* [Vaccine Safety Index (VSI)](/knowledge/vaccine-safety-index.md)
* [Critical Transport Condition](/knowledge/critical-transport-condition.md)
* [Container Alert Status](/knowledge/container-alert-status.md)
* [Logistics Performance Metric (LPM)](/knowledge/logistics-performance-metric.md)
