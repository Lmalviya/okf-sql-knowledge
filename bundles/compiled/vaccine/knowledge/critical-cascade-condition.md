---
type: Business Rule
title: Critical Cascade Condition
description: Identifies systemic failure patterns in the cold chain.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 55
---

# Definition

A condition where (MPRA > 0.8 AND TSC < 0.4) OR (TWQD > 0.6 AND ESF > 0.7)

# Depends on

* [Multi-Parameter Risk Assessment (MPRA)](/knowledge/multi-parameter-risk-assessment.md)
* [Thermal Stability Coefficient (TSC)](/knowledge/thermal-stability-coefficient.md)
* [Time-Weighted Quality Decay (TWQD)](/knowledge/time-weighted-quality-decay.md)
* [Environmental Stress Factor (ESF)](/knowledge/environmental-stress-factor.md)
