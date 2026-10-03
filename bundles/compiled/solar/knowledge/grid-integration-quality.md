---
type: Calculation
title: Grid Integration Quality (GIQ)
description: Measures the overall quality of power delivered to the grid.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 37
---

# Definition

GIQ = PWRQualIDX × (1 - power_metrics.harmdistpct/100) × power_metrics.invertpowfac, using PWRQualIDX from the inverter table.

# Columns used

* [inverter](/tables/inverter.md): `pwrqualidx`, `power_metrics`

# Depends on

* [Grid Stability Factor](/knowledge/grid-stability-factor.md)

# Used by

* [Grid Export Quality Classification](/knowledge/grid-export-quality-classification.md)
