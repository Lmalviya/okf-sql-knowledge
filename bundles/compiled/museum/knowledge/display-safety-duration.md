---
type: Calculation
title: Display Safety Duration (DSD)
description: Calculates the recommended maximum display duration for an artifact based on its sensitivities.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 4
---

# Definition

DSD = \frac{BaseDuration \times (10 - LightSensWeight) \times (10 - TempSensWeight) \times (10 - HumidSensWeight)}{1000}, \text{where BaseDuration=36 months, and SensWeight uses Sensitivity Weight Values.}

# Depends on

* [Sensitivity Weight Values](/knowledge/sensitivity-weight-values.md)

# Used by

* [Exhibition Rotation Candidate](/knowledge/exhibition-rotation-candidate.md)
* [Exhibition Rotation Priority Score (ERPS)](/knowledge/exhibition-rotation-priority-score.md)
