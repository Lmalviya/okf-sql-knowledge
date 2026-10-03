---
type: Business Rule
title: High-Risk Weather Condition
description: Identifies weather patterns that pose significant risk to panel performance or longevity.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 43
---

# Definition

Weather conditions are considered high-risk when the Weather Severity Index exceeds 7.0 and Cell Temperature exceeds the upper limit of the Optimal Performance Window.

# Depends on

* [Optimal Performance Window](/knowledge/optimal-performance-window.md)
* [Weather Severity Index](/knowledge/weather-severity-index.md)
* [CellTempC (Cell Temperature)](/knowledge/celltempc.md)
