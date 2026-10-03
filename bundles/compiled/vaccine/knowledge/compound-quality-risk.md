---
type: Business Rule
title: Compound Quality Risk
description: Identifies complex quality degradation scenarios.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 56
---

# Definition

A status where VSI decreases over three consecutive readings AND LPM < 0.5 AND ESF > 0.6

# Depends on

* [Vaccine Safety Index (VSI)](/knowledge/vaccine-safety-index.md)
* [Logistics Performance Metric (LPM)](/knowledge/logistics-performance-metric.md)
* [Environmental Stress Factor (ESF)](/knowledge/environmental-stress-factor.md)
