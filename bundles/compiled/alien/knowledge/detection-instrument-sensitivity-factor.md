---
type: Calculation
title: Detection Instrument Sensitivity Factor (DISF)
description: Calculates the effective sensitivity of the detection setup based on telescope and environmental factors.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 5
---

# Definition

$\text{DISF} = (10 - \frac{|\text{AirTempC} - 15|}{10}) \times \text{AtmosTransparency} \times (1 - \frac{\text{HumidityRate}}{200}) \times \frac{100 - \text{LunarDistDeg}}{100}$, where values closer to 10 indicate optimal detection sensitivity.

# Columns used

* [observatories](/tables/observatories.md): `atmostransparency`, `lunardistdeg`, `airtempc`, `humidityrate`
