---
type: Calculation
title: Temperature Adjusted Performance Ratio (TAPR)
description: Enhances the Panel Performance Ratio by accounting for temperature effects.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 30
---

# Definition

TAPR = PPR + (TPCI / PowerRatedW), where PPR is the Panel Performance Ratio and TPCI is the Temperature Performance Coefficient Impact.

# Depends on

* [Panel Performance Ratio (PPR)](/knowledge/panel-performance-ratio.md)
* [Temperature Performance Coefficient Impact (TPCI)](/knowledge/temperature-performance-coefficient-impact.md)

# Used by

* [Advanced Performance Degradation Alert](/knowledge/advanced-performance-degradation-alert.md)
