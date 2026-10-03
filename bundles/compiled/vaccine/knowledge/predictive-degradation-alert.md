---
type: Business Rule
title: Predictive Degradation Alert
description: Forecasts potential quality degradation based on current trends.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 59
---

# Definition

Alert when TWQD increases over 3 consecutive readings AND ESF > 0.5 AND TempDevCount > 3

# Columns used

* [sensordata](/tables/sensordata.md): `tempdevcount`

# Depends on

* [Time-Weighted Quality Decay (TWQD)](/knowledge/time-weighted-quality-decay.md)
* [Environmental Stress Factor (ESF)](/knowledge/environmental-stress-factor.md)
