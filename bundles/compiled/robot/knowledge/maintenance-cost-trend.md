---
type: Calculation
title: Maintenance Cost Trend (MCT)
description: Estimates the trend in maintenance costs over time.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 35
---

# Definition

For a given robot R, MCT = \frac{\sum_{mf \in \text{maintenance_and_fault} \mid \text{upkeeprobot = R}} \text{upkeepcostest} \cdot w(mf)}{\text{|}\{mf \in \text{maintenance_and_fault} \mid \text{upkeeprobot = R}\}|}, \text{where } w(mf) = \frac{1}{1 + \text{upkeepduedays}}

# Columns used

* [maintenance_and_fault](/tables/maintenance_and_fault.md): `upkeeprobot`, `upkeepduedays`, `upkeepcostest`

# Used by

* [Escalating Maintenance Costs](/knowledge/escalating-maintenance-costs.md)
