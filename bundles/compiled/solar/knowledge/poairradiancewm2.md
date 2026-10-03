---
type: Value Illustration
title: POAIrradianceWM2 (Plane-of-Array Irradiance)
description: Illustrates the solar energy available to panels in their installed orientation.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 28
---

# Definition

Measured in watts per square meter (W/m²), representing the solar energy reaching the panel surface. Typical daytime values range from 200 W/m² on heavily overcast days to 1000+ W/m² under clear sky conditions at solar noon.

# Used by

* [Weather Corrected Efficiency (WCE)](/knowledge/weather-corrected-efficiency.md)
* [Expected Energy Yield (EEY)](/knowledge/expected-energy-yield.md)
