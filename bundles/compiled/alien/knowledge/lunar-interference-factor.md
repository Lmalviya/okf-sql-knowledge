---
type: Calculation
title: Lunar Interference Factor (LIF)
description: Calculates the potential interference from lunar illumination on observations.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 9
---

# Definition

$\text{LIF} = (1 - \frac{\text{LunarDistDeg}}{180}) \times (1 - \text{AtmosTransparency})$, where higher values indicate more lunar interference. Values above 0.5 suggest significant lunar contamination in data.

# Columns used

* [observatories](/tables/observatories.md): `atmostransparency`, `lunardistdeg`

# Used by

* [Optimal Observing Window (OOW)](/knowledge/optimal-observing-window.md)
* [Observation Quality Factor (OQF)](/knowledge/observation-quality-factor.md)
* [High Lunar Interference Events](/knowledge/high-lunar-interference-events.md)
