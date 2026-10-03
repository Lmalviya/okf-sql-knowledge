---
type: Business Rule
title: Environmental Instability Event
description: Identifies periods when showcase environmental conditions fluctuate beyond acceptable parameters.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 13
---

# Definition

Occurs when TempVar24h > 1°C OR HumVar24h > 3 within a 24-hour period.

# Columns used

* [environmentalreadingscore](/tables/environmentalreadingscore.md): `tempvar24h`, `humvar24h`

# Used by

* [Environmental Control Failure](/knowledge/environmental-control-failure.md)
