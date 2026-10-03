---
type: Business Rule
title: Signal Degradation Scenario (SDS)
description: Characterizes situations where signal quality is compromised by environmental factors.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 14
---

# Definition

Observation conditions where one or more of: $\text{AtmosTransparency} < 0.7$, $\text{HumidityRate} > 70$, $\text{WindSpeedMs} > 8$, or $\text{GeomagStatus}$ contains 'Storm', resulting in compromised data quality.

# Columns used

* [observatories](/tables/observatories.md): `atmostransparency`, `geomagstatus`, `humidityrate`, `windspeedms`

# Depends on

* [Atmospheric Observability Index (AOI)](/knowledge/atmospheric-observability-index.md)
