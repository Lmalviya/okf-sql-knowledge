---
type: Business Rule
title: Fast Robot
description: Indicates if the robot operates at high speed based on average TCP speed.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 14
---

# Definition

The robot is fast if ATCS > 1000.

# Depends on

* [Average TCP Speed (ATCS)](/knowledge/average-tcp-speed.md)
