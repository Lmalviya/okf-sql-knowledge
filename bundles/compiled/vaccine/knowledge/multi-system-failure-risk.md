---
type: Business Rule
title: Multi-System Failure Risk
description: Identifies concurrent failures across multiple subsystems.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 58
---

# Definition

A state where (CRI + TBS + (1-HQI))/3 > 0.7 AND all of (TSC, LPM, ESF) < 0.3

# Depends on

* [Container Risk Index (CRI)](/knowledge/container-risk-index.md)
* [Handling Quality Index (HQI)](/knowledge/handling-quality-index.md)
* [Temperature Breach Severity (TBS)](/knowledge/temperature-breach-severity.md)
* [Thermal Stability Coefficient (TSC)](/knowledge/thermal-stability-coefficient.md)
* [Logistics Performance Metric (LPM)](/knowledge/logistics-performance-metric.md)
* [Environmental Stress Factor (ESF)](/knowledge/environmental-stress-factor.md)
