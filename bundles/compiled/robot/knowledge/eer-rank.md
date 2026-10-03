---
type: Calculation
title: EER Rank
description: Ranks the Energy Efficiency Ratio within each application type to assess relative efficiency.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 52
---

# Definition

EER Rank = \text{PERCENT_RANK}() \text{ OVER } (\text{PARTITION BY } apptypeval \text{ ORDER BY } EER \text{ DESC})}

# Columns used

* [operation](/tables/operation.md): `apptypeval`

# Depends on

* [Energy Efficiency Ratio (EER)](/knowledge/energy-efficiency-ratio.md)
