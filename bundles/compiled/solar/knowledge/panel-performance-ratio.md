---
type: Calculation
title: Panel Performance Ratio (PPR)
description: Measures how well a solar panel is performing relative to its rated power.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 0
---

# Definition

PPR = \frac{MeasuredPowerW}{PowerRatedW} \times 100\%, \text{where MeasuredPowerW is the measured power output and PowerRatedW is the rated power of the panel.}

# Used by

* [Energy Production Efficiency (EPE)](/knowledge/energy-production-efficiency.md)
* [Critical Performance Threshold](/knowledge/critical-performance-threshold.md)
* [Temperature Adjusted Performance Ratio (TAPR)](/knowledge/temperature-adjusted-performance-ratio.md)
* [Effective Performance Index (EPI)](/knowledge/effective-performance-index.md)
