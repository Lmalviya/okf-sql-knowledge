---
type: Value Illustration
title: TempCoef (Temperature Coefficient)
description: Illustrates how panel performance changes with temperature.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 22
---

# Definition

Expressed as a percentage per degree Celsius (usually negative), indicating how much a panel's power output decreases for each degree above 25°C. Typical values range from -0.25% to -0.50% per °C, with lower absolute values indicating better high-temperature performance.

# Columns used

* [panel](/tables/panel.md): `tempcoef`

# Used by

* [Weather Corrected Efficiency (WCE)](/knowledge/weather-corrected-efficiency.md)
