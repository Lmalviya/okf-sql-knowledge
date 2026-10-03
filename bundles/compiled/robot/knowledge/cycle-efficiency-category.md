---
type: Business Rule
title: Cycle Efficiency Category
description: Categorizes robots based on their program cycle efficiency performance
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 43
---

# Definition

For a robot R, the Cycle Efficiency Category is:
- 'Low Efficiency' if OCE < 100 AND TPC > 500000
- 'Medium Efficiency' if OCE < 150 OR TPC > 300000
- 'High Efficiency' otherwise

# Depends on

* [Operation Cycle Efficiency (OCE)](/knowledge/operation-cycle-efficiency.md)
* [Total Program Cycles (TPC)](/knowledge/total-program-cycles.md)
