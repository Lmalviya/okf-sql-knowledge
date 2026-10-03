---
type: Calculation
title: Irradiance Utilization Ratio (IUR)
description: Measures how effectively the panel converts available solar irradiance to power.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 9
---

# Definition

IUR = \frac{MeasuredPowerW / PanelAreaM2}{POAIrradianceWM2}, \text{where POAIrradianceWM2 is from irradiance_conditions.irradiance_types[3] and PanelAreaM2 is the area of the panel.}

# Columns used

* [environment](/tables/environment.md): `irradiance_conditions`

# Used by

* [Effective Performance Index (EPI)](/knowledge/effective-performance-index.md)
