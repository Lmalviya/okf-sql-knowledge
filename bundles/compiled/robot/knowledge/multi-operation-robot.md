---
type: Business Rule
title: Multi-Operation Robot
description: Indicates if the robot has performed multiple operations.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 18
---

# Definition

The robot has performed multiple operations if NO > 1.

# Depends on

* [Number of Operations (NO)](/knowledge/number-of-operations.md)
