---
type: Calculation
title: APE Rank
description: Ranks the Average Position Error within each controller type to assess relative precision.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 53
---

# Definition

For a given robot R, APE Rank = \text{PERCENT_RANK}() \text{ OVER } (\text{PARTITION BY } ctrltypeval \text{ ORDER BY } APE \text{ DESC})

# Columns used

* [robot_details](/tables/robot_details.md): `ctrltypeval`

# Depends on

* [Average Position Error (APE)](/knowledge/average-position-error.md)
