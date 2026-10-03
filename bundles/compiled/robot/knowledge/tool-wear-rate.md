---
type: Calculation
title: Tool Wear Rate (TWR)
description: Estimates the rate of tool wear relative to program cycles.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 37
---

# Definition

For a given robot R, TWR = \frac{\sum_{ps \in \text{performance_and_safety} \mid \text{effectivenessrobot = R}} toolwearpct}{\text{TPC}}, \text{where TPC normalizes tool wear percentage.}

# Columns used

* [performance_and_safety](/tables/performance_and_safety.md): `effectivenessrobot`, `toolwearpct`

# Depends on

* [Total Program Cycles (TPC)](/knowledge/total-program-cycles.md)

# Used by

* [Tool Replacement Status](/knowledge/tool-replacement-status.md)
