---
type: Calculation
title: Material Aging Projection (MAP)
description: Projects the rate of artifact aging based on material type and environmental conditions.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 37
---

# Definition

MAP = MDR × (1 + (TETL ÷ 20)), where MDR is the Material Deterioration Rate and TETL is the Total Environmental Threat Level. Higher values indicate faster projected aging.

# Depends on

* [Material Deterioration Rate (MDR)](/knowledge/material-deterioration-rate.md)
* [Total Environmental Threat Level (TETL)](/knowledge/total-environmental-threat-level.md)

# Used by

* [Dynasty Artifact at Risk](/knowledge/dynasty-artifact-at-risk.md)
