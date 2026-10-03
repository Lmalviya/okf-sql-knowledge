---
type: Calculation
title: Total Operating Hours (TOH)
description: The maximum total operating hours recorded for the robot across all operations.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 7
---

# Definition

For a given robot R, TOH = \max_{o \in \text{operation} \mid \text{operbotdetref = R}} totopshrval

# Columns used

* [operation](/tables/operation.md): `operbotdetref`, `totopshrval`

# Used by

* [Heavily Used Robot](/knowledge/heavily-used-robot.md)
* [Energy Efficiency Ratio (EER)](/knowledge/energy-efficiency-ratio.md)
* [Energy Inefficient Robot](/knowledge/energy-inefficient-robot.md)
* [JDI-TOH Regression Slope](/knowledge/jdi-toh-regression-slope.md)
* [Model Average Max Operating Hours](/knowledge/model-average-max-operating-hours.md)
