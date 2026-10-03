---
type: Calculation
title: Material Deterioration Rate (MDR)
description: Estimates the rate of material deterioration based on environmental factors.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 7
---

# Definition

MDR = \frac{ArtAgeYears \times ERF \times (RelHumidity - 50)^2 \times TempC}{100000}, \text{where higher values indicate faster deterioration}

# Columns used

* [artifactscore](/tables/artifactscore.md): `artageyears`
* [environmentalreadingscore](/tables/environmentalreadingscore.md): `tempc`, `relhumidity`

# Depends on

* [Environmental Risk Factor (ERF)](/knowledge/environmental-risk-factor.md)

# Used by

* [Accelerated Deterioration Scenario](/knowledge/accelerated-deterioration-scenario.md)
* [Total Environmental Threat Level (TETL)](/knowledge/total-environmental-threat-level.md)
* [Material Aging Projection (MAP)](/knowledge/material-aging-projection.md)
