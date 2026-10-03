---
type: Calculation
title: Recent Fault Prediction Score (RFPS)
description: The fault prediction score from the most recent maintenance record for a robot.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 5
---

# Definition

For a given robot R, \text{faultpredscore}(mf) \text{ where } mf \in \text{maintenance_and_fault}, \text{upkeeprobot} = R, \text{and } \text{upkeepduedays}(mf) = \min_{mf' \in \text{maintenance_and_fault} \mid \text{upkeeprobot} = R} \text{upkeepduedays}(mf').

# Columns used

* [maintenance_and_fault](/tables/maintenance_and_fault.md): `upkeeprobot`, `faultpredscore`, `upkeepduedays`

# Used by

* [High Fault Risk](/knowledge/high-fault-risk.md)
