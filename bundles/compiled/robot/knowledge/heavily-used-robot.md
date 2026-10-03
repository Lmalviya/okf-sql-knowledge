---
type: Business Rule
title: Heavily Used Robot
description: Indicates if the robot has been heavily used based on total operating hours.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 17
---

# Definition

The robot is heavily used if TOH > 10000.

# Depends on

* [Total Operating Hours (TOH)](/knowledge/total-operating-hours.md)
