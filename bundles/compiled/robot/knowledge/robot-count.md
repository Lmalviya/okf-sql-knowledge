---
type: Calculation
title: Robot Count
description: The number of distinct robots within a specific group (e.g., model series).
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 56
---

# Definition

Let M be the model series, \mathcal{R}_M be the set of unique robot identifiers in M. Then Robot Count = |\mathcal{R}_M|
