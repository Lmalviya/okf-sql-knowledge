---
type: Business Rule
title: Old Robot
description: Indicates if a robot is old based on its age.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 10
---

# Definition

A robot is considered old if RAY >= 2.

# Depends on

* [Robot Age in Years (RAY)](/knowledge/robot-age-in-years.md)
