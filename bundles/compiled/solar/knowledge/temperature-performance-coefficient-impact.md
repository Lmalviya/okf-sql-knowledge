---
type: Calculation
title: Temperature Performance Coefficient Impact (TPCI)
description: Quantifies the impact of temperature on panel performance based on its temperature coefficient.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 2
---

# Definition

TPCI = PowerRatedW \times TempCoef \times (CellTempC - 25), \text{where TempCoef is the temperature coefficient and 25°C is the standard test condition temperature.}

# Columns used

* [panel](/tables/panel.md): `tempcoef`
* [environment](/tables/environment.md): `celltempc`

# Used by

* [Temperature Adjusted Performance Ratio (TAPR)](/knowledge/temperature-adjusted-performance-ratio.md)
