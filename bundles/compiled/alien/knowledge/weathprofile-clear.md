---
type: Value Illustration
title: 'WeathProfile: Clear'
description: Illustrates optimal weather conditions for signal detection.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 20
---

# Definition

Indicates pristine sky conditions with no clouds, usually associated with $\text{AtmosTransparency} > 0.9$, low $\text{HumidityRate} (< 40\%)$, and minimal $\text{WindSpeedMs} (< 3.0)$. Provides ideal visibility for optical observations and minimal atmospheric interference for radio observations.

# Columns used

* [observatories](/tables/observatories.md): `weathprofile`, `atmostransparency`, `humidityrate`, `windspeedms`
