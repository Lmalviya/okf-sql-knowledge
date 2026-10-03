---
type: Calculation
title: Weather Corrected Efficiency (WCE)
description: Adjusts panel efficiency measurements to account for weather conditions.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 35
---

# Definition

WCE = CurrentEfficiencyPercent × (1 + TempCoef × (25 - CellTempC) / 100) × (1000 / POAIrradianceWM2), where CurrentEfficiencyPercent is from efficiency_profile.current_efficiency.curreffpct.

# Columns used

* [panel](/tables/panel.md): `tempcoef`
* [performance](/tables/performance.md): `efficiency_profile`
* [environment](/tables/environment.md): `celltempc`

# Depends on

* [TempCoef (Temperature Coefficient)](/knowledge/tempcoef.md)
* [CellTempC (Cell Temperature)](/knowledge/celltempc.md)
* [POAIrradianceWM2 (Plane-of-Array Irradiance)](/knowledge/poairradiancewm2.md)

# Used by

* [Inverter-Panel Compatibility Index](/knowledge/inverter-panel-compatibility-index.md)
