---
type: Business Rule
title: Precision Category
description: Categorizes the precision of the robot based on average position error.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 13
---

# Definition

If APE < 0.1, 'High Precision'; else if APE < 0.5, 'Medium Precision'; else 'Low Precision'.

# Depends on

* [Average Position Error (APE)](/knowledge/average-position-error.md)
