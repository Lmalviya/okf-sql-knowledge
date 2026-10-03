---
type: Calculation
title: Light Exposure Risk (LER)
description: Quantifies the risk from light exposure based on artifact sensitivity and current light levels.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 8
---

# Definition

LER = \frac{LightLux \times LightSensWeight \times VisibleExpLxh}{1000}, \text{where LightSensWeight uses Sensitivity Weight Values}

# Columns used

* [lightandradiationreadings](/tables/lightandradiationreadings.md): `lightlux`, `visibleexplxh`

# Depends on

* [Sensitivity Weight Values](/knowledge/sensitivity-weight-values.md)

# Used by

* [Exhibition Rotation Candidate](/knowledge/exhibition-rotation-candidate.md)
* [Total Environmental Threat Level (TETL)](/knowledge/total-environmental-threat-level.md)
* [Exhibition Rotation Priority Score (ERPS)](/knowledge/exhibition-rotation-priority-score.md)
* [Light Exposure Thresholds](/knowledge/light-exposure-thresholds.md)
