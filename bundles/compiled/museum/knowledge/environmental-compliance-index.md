---
type: Calculation
title: Environmental Compliance Index (ECI)
description: Measures how well current environmental conditions meet the requirements for an artifact.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 39
---

# Definition

ECI = 10 - (|(TempC - IdealTemp)| + |(RelHumidity - IdealHumidity)| ÷ 5 + ERF ÷ 2), where ERF is the Environmental Risk Factor. Higher values indicate better compliance with requirements.

# Columns used

* [environmentalreadingscore](/tables/environmentalreadingscore.md): `tempc`, `relhumidity`

# Depends on

* [Environmental Risk Factor (ERF)](/knowledge/environmental-risk-factor.md)

# Used by

* [Environmental Control Failure](/knowledge/environmental-control-failure.md)
