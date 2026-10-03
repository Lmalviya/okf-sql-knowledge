---
type: Business Rule
title: Energy Inefficient Robot
description: Flags robots with poor energy efficiency.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 41
---

# Definition

A robot R is Energy Inefficient if EER > 0.01 and TOH > 1000.

# Depends on

* [Energy Efficiency Ratio (EER)](/knowledge/energy-efficiency-ratio.md)
* [Total Operating Hours (TOH)](/knowledge/total-operating-hours.md)
