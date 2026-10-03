---
type: Business Rule
title: Cabin Habitability Standard
description: Defines the minimum standards for habitable cabin conditions in polar environments.
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 17
---

# Definition

A cabin meets 'Habitability Standards' when it maintains internal temperature (cabinclimate.temperature_c) between 18-24°C, oxygen levels (cabinclimate.o2_percent) above 19.5%, CO2 levels (cabinclimate.co2_ppm) below 1000 ppm, functioning ventilation systems, and operational heating systems.

# Columns used

* [cabinenvironment](/tables/cabinenvironment.md): `cabinclimate`
