---
type: Calculation
title: Energy Efficiency Ratio (EER)
description: Measures energy efficiency by comparing energy usage to operating hours.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 31
---

# Definition

For a given robot R, EER = \frac{\sum_{ps \in \text{performance_and_safety} \mid \text{effectivenessrobot = R}} energyusekwhval}{\text{TOH}}, \text{where TOH is used to normalize energy consumption.}

# Columns used

* [performance_and_safety](/tables/performance_and_safety.md): `effectivenessrobot`, `energyusekwhval`

# Depends on

* [Total Operating Hours (TOH)](/knowledge/total-operating-hours.md)

# Used by

* [Energy Inefficient Robot](/knowledge/energy-inefficient-robot.md)
* [EER Rank](/knowledge/eer-rank.md)
