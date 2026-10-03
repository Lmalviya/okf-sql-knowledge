---
type: Calculation
title: Program Efficiency Rank
description: Ranks programs based on their average Operation Cycle Efficiency across robots.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 54
---

# Definition

For a program P, Program Efficiency Rank = \text{DENSE_RANK}() \text{ OVER } (\text{ORDER BY } \text{AVG(program_oce)} \text{ DESC}), \text{where program_oce is the Operation Cycle Efficiency for program P on each robot.}

# Depends on

* [Operation Cycle Efficiency (OCE)](/knowledge/operation-cycle-efficiency.md)
