---
type: Business Rule
title: Optimal Observing Window (OOW)
description: Defines conditions when observational quality is maximized.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 13
---

# Definition

Time periods when $\text{AOI} > 0.85$, $\text{LunarStage}$ is 'New' or 'First Quarter', $\text{LunarDistDeg} > 45$, and $\text{SolarStatus}$ is 'Low' or 'Moderate'.

# Columns used

* [observatories](/tables/observatories.md): `lunarstage`, `lunardistdeg`, `solarstatus`

# Depends on

* [Atmospheric Observability Index (AOI)](/knowledge/atmospheric-observability-index.md)
* [Lunar Interference Factor (LIF)](/knowledge/lunar-interference-factor.md)

# Used by

* [Observation-Verified Signal](/knowledge/observation-verified-signal.md)
