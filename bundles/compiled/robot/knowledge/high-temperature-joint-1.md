---
type: Business Rule
title: High Temperature Joint 1
description: Indicates if Joint 1 has a high average temperature.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 11
---

# Definition

Joint 1 has high temperature if AJ1T > 50.

# Depends on

* [Average Joint 1 Temperature (AJ1T)](/knowledge/average-joint-1-temperature.md)
