---
type: Calculation
title: Operation Cycle Efficiency (OCE)
description: Calculates the efficiency of program cycles relative to cycle time.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 33
---

# Definition

For a given robot R, OCE = \frac{\text{TPC}}{\sum_{o \in \text{operation} \mid \text{operbotdetref = R}} cycletimesecval}

# Columns used

* [operation](/tables/operation.md): `operbotdetref`, `cycletimesecval`

# Depends on

* [Total Program Cycles (TPC)](/knowledge/total-program-cycles.md)

# Used by

* [Cycle Efficiency Category](/knowledge/cycle-efficiency-category.md)
* [Program Efficiency Rank](/knowledge/program-efficiency-rank.md)
* [Efficiency Metrics](/knowledge/efficiency-metrics.md)
