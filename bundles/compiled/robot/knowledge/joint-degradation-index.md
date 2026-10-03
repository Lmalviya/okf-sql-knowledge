---
type: Calculation
title: Joint Degradation Index (JDI)
description: Computes a composite index of joint health based on temperature and vibration.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 32
---

# Definition

For a given robot R, JDI = \frac{\sum_{jc \in \text{joint_condition} \mid \text{jcdetref = R}} \sum_{i=1}^6 (jitempval_i / \text{MJT} + jivibval_i)}{\text{|}\{jc \in \text{joint_condition} \mid \text{jcdetref = R}\}| \cdot 6}, \text{where MJT normalizes temperatures, and jitempval_i, jivibval_i are joint i's temperature and vibration.}

# Columns used

* [joint_condition](/tables/joint_condition.md): `jcdetref`

# Depends on

* [Maximum Joint Temperature (MJT)](/knowledge/maximum-joint-temperature.md)

# Used by

* [Joint Health Risk](/knowledge/joint-health-risk.md)
* [JDI-TOH Regression Slope](/knowledge/jdi-toh-regression-slope.md)
