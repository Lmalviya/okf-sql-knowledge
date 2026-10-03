---
type: Calculation
title: Total Environmental Threat Level (TETL)
description: Comprehensive measurement of all environmental threats to an artifact based on multiple risk factors.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 31
---

# Definition

TETL = ERF + LER + (MDR × 2), where ERF is the Environmental Risk Factor, LER is the Light Exposure Risk, and MDR is the Material Deterioration Rat.

# Depends on

* [Environmental Risk Factor (ERF)](/knowledge/environmental-risk-factor.md)
* [Light Exposure Risk (LER)](/knowledge/light-exposure-risk.md)
* [Material Deterioration Rate (MDR)](/knowledge/material-deterioration-rate.md)

# Used by

* [Material Aging Projection (MAP)](/knowledge/material-aging-projection.md)
* [High Deterioration Risk Artifact](/knowledge/high-deterioration-risk-artifact.md)
* [Organic Material Emergency](/knowledge/organic-material-emergency.md)
