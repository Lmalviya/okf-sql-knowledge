---
type: Business Rule
title: High Fault Risk
description: Indicates if the robot has a high risk of fault based on average fault prediction score.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 15
---

# Definition

The robot has high fault risk if RFPS > 0.5.

# Depends on

* [Recent Fault Prediction Score (RFPS)](/knowledge/recent-fault-prediction-score.md)
