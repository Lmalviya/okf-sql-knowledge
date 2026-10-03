---
type: Business Rule
title: Controller Overload Risk
description: Indicates robots with stressed controllers.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 46
---

# Definition

A robot R has Controller Overload Risk if CSI > 100 and NO > 2.

# Depends on

* [Controller Stress Index (CSI)](/knowledge/controller-stress-index.md)
* [Number of Operations (NO)](/knowledge/number-of-operations.md)
