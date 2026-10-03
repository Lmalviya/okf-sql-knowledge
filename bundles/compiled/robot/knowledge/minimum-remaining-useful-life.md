---
type: Calculation
title: Minimum Remaining Useful Life (MRUL)
description: Finds the minimum Remaining Useful Life across all maintenance records for a specific robot.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 6
---

# Definition

For a given robot R, MRUL = \min_{mf \in \text{maintenance_and_fault} \mid \text{upkeeprobot = R}} rulhours

# Columns used

* [maintenance_and_fault](/tables/maintenance_and_fault.md): `upkeeprobot`, `rulhours`

# Used by

* [Urgent Maintenance Needed](/knowledge/urgent-maintenance-needed.md)
* [Maintenance Priority Level](/knowledge/maintenance-priority-level.md)
