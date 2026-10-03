---
type: Calculation
title: Maximum Joint Temperature (MJT)
description: Finds the maximum temperature recorded for any joint across all operations for a specific robot.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 2
---

# Definition

For a given robot R, MJT = \max_{jc \in \text{joint_condition} \mid \text{jcdetref = R}} \max(jc.j1tempval, jc.j2tempval, jc.j3tempval, jc.j4tempval, jc.j5tempval, jc.j6tempval)

# Columns used

* [joint_condition](/tables/joint_condition.md): `jcdetref`, `j1tempval`, `j2tempval`, `j3tempval`, `j4tempval`, `j5tempval`, `j6tempval`

# Used by

* [Overheating Risk](/knowledge/overheating-risk.md)
* [Joint Degradation Index (JDI)](/knowledge/joint-degradation-index.md)
* [Joint Health Risk](/knowledge/joint-health-risk.md)
* [Operational Instability](/knowledge/operational-instability.md)
