---
type: Calculation
title: Total Program Cycles (TPC)
description: Sums the program cycle counts across all operations for a specific robot.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 9
---

# Definition

For a given robot R, TPC = \sum_{o \in \text{operation} \mid \text{operbotdetref = R}} progcyclecount

# Columns used

* [operation](/tables/operation.md): `operbotdetref`, `progcyclecount`

# Used by

* [High Cycle Count Robot](/knowledge/high-cycle-count-robot.md)
* [Operation Cycle Efficiency (OCE)](/knowledge/operation-cycle-efficiency.md)
* [Tool Wear Rate (TWR)](/knowledge/tool-wear-rate.md)
* [Cycle Efficiency Category](/knowledge/cycle-efficiency-category.md)
* [Tool Replacement Status](/knowledge/tool-replacement-status.md)
