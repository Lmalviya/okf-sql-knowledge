---
type: Calculation
title: Average TCP Speed (ATCS)
description: Calculates the average speed of the Tool Center Point across all actuations for a specific robot.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 4
---

# Definition

For a given robot R, ATCS = \frac{\sum_{ad \in \text{actuation_data} \mid \text{actdetref = R}} tcpspeedval}{|\{ad \in \text{actuation_data} \mid \text{actdetref = R}\}|}

# Columns used

* [actuation_data](/tables/actuation_data.md): `actdetref`, `tcpspeedval`

# Used by

* [Fast Robot](/knowledge/fast-robot.md)
* [Model Average TCP Speed](/knowledge/model-average-tcp-speed.md)
