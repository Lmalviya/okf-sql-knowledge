---
type: Calculation
title: Average Position Error (APE)
description: Calculates the average position error across all actuations for a specific robot.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 3
---

# Definition

For a given robot R, APE = \frac{\sum_{ad \in \text{actuation_data} \mid \text{actdetref = R}} poserrmmval}{|\{ad \in \text{actuation_data} \mid \text{actdetref = R}\}|}

# Columns used

* [actuation_data](/tables/actuation_data.md): `actdetref`, `poserrmmval`

# Used by

* [Precision Category](/knowledge/precision-category.md)
* [APE Rank](/knowledge/ape-rank.md)
* [Model Average Position Error](/knowledge/model-average-position-error.md)
