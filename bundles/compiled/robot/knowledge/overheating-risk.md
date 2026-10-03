---
type: Business Rule
title: Overheating Risk
description: Indicates if there is a risk of overheating based on maximum joint temperature.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 12
---

# Definition

There is an overheating risk if MJT > 70.

# Depends on

* [Maximum Joint Temperature (MJT)](/knowledge/maximum-joint-temperature.md)
