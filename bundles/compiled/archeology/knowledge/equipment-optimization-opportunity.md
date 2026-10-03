---
type: Business Rule
title: Equipment Optimization Opportunity
description: Identifies scenarios where equipment settings could be optimized for better results based on performance analysis.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 49
---

# Definition

Scanning scenarios where EER < 30 but ESI > 80, where EER is Equipment Effectiveness Ratio and ESI is Environmental Suitability Index, indicating potential for improved equipment utilization in favorable conditions through calibration adjustment and scanning parameter optimization.

# Depends on

* [Equipment Effectiveness Ratio (EER)](/knowledge/equipment-effectiveness-ratio.md)
* [Environmental Suitability Index (ESI)](/knowledge/environmental-suitability-index.md)
