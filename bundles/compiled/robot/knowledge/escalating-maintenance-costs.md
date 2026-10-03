---
type: Business Rule
title: Escalating Maintenance Costs
description: Identifies robots with rising maintenance costs.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 45
---

# Definition

A robot R has Escalating Maintenance Costs if MCT > 500 and RAY > 2.

# Depends on

* [Maintenance Cost Trend (MCT)](/knowledge/maintenance-cost-trend.md)
* [Robot Age in Years (RAY)](/knowledge/robot-age-in-years.md)
