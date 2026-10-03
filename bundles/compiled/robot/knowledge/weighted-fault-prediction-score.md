---
type: Calculation
title: Weighted Fault Prediction Score (WFPS)
description: Calculates a weighted average fault prediction score, prioritizing recent records.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 30
---

# Definition

For a given robot R, WFPS = \frac{\sum_{mf \in \text{maintenance_and_fault} \mid \text{upkeeprobot = R}} (faultpredscore \cdot w(mf))}{\sum_{mf \in \text{maintenance_and_fault} \mid \text{upkeeprobot = R}} w(mf)}, \text{where } w(mf) = 1 / (1 + \text{upkeepduedays})

# Columns used

* [maintenance_and_fault](/tables/maintenance_and_fault.md): `upkeeprobot`, `faultpredscore`, `upkeepduedays`

# Used by

* [Maintenance Priority Level](/knowledge/maintenance-priority-level.md)
