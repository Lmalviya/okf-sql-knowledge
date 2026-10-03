---
type: Calculation
title: Total System Loss (TSL)
description: Calculates the combined power losses from all major sources.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 31
---

# Definition

TSL = (PowerRatedW × CumDegPct/100) + (MeasuredPowerW × SoilingLossPct/100) + IEL, where IEL is the Inverter Efficiency Loss and CumDegPct is from efficiency_profile.degradation.cumdegpct.

# Columns used

* [performance](/tables/performance.md): `efficiency_profile`

# Depends on

* [Inverter Efficiency Loss (IEL)](/knowledge/inverter-efficiency-loss.md)
* [CumDegPct (Cumulative Degradation Percentage)](/knowledge/cumdegpct.md)

# Used by

* [Effective Performance Index (EPI)](/knowledge/effective-performance-index.md)
