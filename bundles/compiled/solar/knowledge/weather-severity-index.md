---
type: Business Rule
title: Weather Severity Index
description: Classifies environmental conditions based on their potential impact on solar plant operations.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 18
---

# Definition

A composite index calculated from extreme values of temperature, humidity, wind speed, and precipitation, where higher values indicate more severe operating conditions and increased risk of performance issues.

# Used by

* [High-Risk Weather Condition](/knowledge/high-risk-weather-condition.md)
* [Environmental Stress Classification](/knowledge/environmental-stress-classification.md)
