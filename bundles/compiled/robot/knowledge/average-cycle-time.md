---
type: Calculation
title: Average Cycle Time
description: Calculates the average time in seconds for completing one program cycle
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 51
---

# Definition

For a given robot R, Average Cycle Time = \frac{\sum_{o \in \text{operation} \mid \text{operbotdetref = R}} \text{cycletimesecval}}{|\{o \in \text{operation} \mid \text{operbotdetref = R}\}|}

# Columns used

* [operation](/tables/operation.md): `operbotdetref`, `cycletimesecval`
