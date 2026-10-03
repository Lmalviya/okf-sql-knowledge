---
type: Calculation
title: Atmospheric Observability Index (AOI)
description: Quantifies how conducive atmospheric conditions are for signal detection.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 1
---

# Definition

$\text{AOI} = \text{AtmosTransparency} \times (1 - \frac{\text{HumidityRate}}{100}) \times (1 - 0.02 \times \text{WindSpeedMs})$, where values closer to 1 indicate ideal observation conditions.

# Columns used

* [observatories](/tables/observatories.md): `atmostransparency`, `humidityrate`, `windspeedms`

# Used by

* [Optimal Observing Window (OOW)](/knowledge/optimal-observing-window.md)
* [Signal Degradation Scenario (SDS)](/knowledge/signal-degradation-scenario.md)
* [Observational Confidence Level (OCL)](/knowledge/observational-confidence-level.md)
* [Observation Quality Factor (OQF)](/knowledge/observation-quality-factor.md)
