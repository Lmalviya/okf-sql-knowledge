---
type: Value Illustration
title: CellTempC (Cell Temperature)
description: Illustrates the operating temperature of solar cells.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 23
---

# Definition

Measured in degrees Celsius, representing the actual temperature of the solar cells during operation. Typically ranges from 40°C to 70°C depending on ambient conditions and panel design, with temperatures above 80°C potentially causing accelerated degradation.

# Columns used

* [environment](/tables/environment.md): `celltempc`

# Used by

* [Weather Corrected Efficiency (WCE)](/knowledge/weather-corrected-efficiency.md)
* [High-Risk Weather Condition](/knowledge/high-risk-weather-condition.md)
