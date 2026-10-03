---
type: Calculation
title: Effective Performance Index (EPI)
description: Comprehensive metric that accounts for all factors affecting panel performance.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 33
---

# Definition

EPI = PPR × (1 - TSL/PowerRatedW) × (IUR/PaneEffPct), where PPR is the Panel Performance Ratio, TSL is the Total System Loss, and IUR is the Irradiance Utilization Ratio.

# Columns used

* [panel](/tables/panel.md): `paneeffpct`

# Depends on

* [Panel Performance Ratio (PPR)](/knowledge/panel-performance-ratio.md)
* [Irradiance Utilization Ratio (IUR)](/knowledge/irradiance-utilization-ratio.md)
* [Total System Loss (TSL)](/knowledge/total-system-loss.md)

# Used by

* [System Upgrade Candidate](/knowledge/system-upgrade-candidate.md)
* [Total Economic Performance](/knowledge/total-economic-performance.md)
