---
type: Business Rule
title: High Cycle Count Robot
description: Indicates if the robot has a high total program cycle count.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 19
---

# Definition

The robot has a high cycle count if TPC > 1000000.

# Depends on

* [Total Program Cycles (TPC)](/knowledge/total-program-cycles.md)
