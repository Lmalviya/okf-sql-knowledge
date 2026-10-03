---
type: Calculation
title: Average Joint 1 Temperature (AJ1T)
description: Calculates the average temperature of Joint 1 across all operations for a specific robot.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 1
---

# Definition

For a given robot R, AJ1T = \frac{\sum_{jc \in \text{joint_condition} \mid \text{jcdetref = R}} j1tempval}{|\{jc \in \text{joint_condition} \mid \text{jcdetref = R}\}|}

# Columns used

* [joint_condition](/tables/joint_condition.md): `jcdetref`, `j1tempval`

# Used by

* [High Temperature Joint 1](/knowledge/high-temperature-joint-1.md)
