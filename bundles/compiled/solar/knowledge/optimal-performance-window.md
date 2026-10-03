---
type: Business Rule
title: Optimal Performance Window
description: Defines the environmental conditions for optimal panel performance.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 15
---

# Definition

The optimal performance window occurs when cell temperature is between 25-45°C, POA irradiance exceeds 800 W/m², and soiling loss is less than 2%.

# Used by

* [High-Risk Weather Condition](/knowledge/high-risk-weather-condition.md)
* [Environmental Stress Classification](/knowledge/environmental-stress-classification.md)
