---
type: Calculation
title: Efficiency Metrics
description: Aggregates efficiency-related metrics, including the most efficient program and average program Operation Cycle Efficiency.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 55
---

# Definition

For a model series, Efficiency Metrics = \text{jsonb_build_object}('most_efficient_program', \text{currprogval with Program Efficiency Rank = 1}, 'avg_program_efficiency', \text{AVG(avg_program_oce)}), \text{where avg_program_oce is the average Operation Cycle Efficiency per program.}

# Columns used

* [operation](/tables/operation.md): `currprogval`

# Depends on

* [Operation Cycle Efficiency (OCE)](/knowledge/operation-cycle-efficiency.md)
