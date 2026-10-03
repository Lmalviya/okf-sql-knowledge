---
type: Business Rule
title: Overloaded Robot
description: Flags robots operating near or beyond payload capacity.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 49
---

# Definition

A robot R is Overloaded if PUR > 0.9 and RAY > 1.

# Depends on

* [Payload Utilization Ratio (PUR)](/knowledge/payload-utilization-ratio.md)
* [Robot Age in Years (RAY)](/knowledge/robot-age-in-years.md)
