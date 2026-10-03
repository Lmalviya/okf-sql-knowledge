---
type: Business Rule
title: Maintenance Priority Level
description: Classifies robots into maintenance priority categories based on fault prediction scores and remaining useful life
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 40
---

# Definition

For a robot R, the Maintenance Priority Level is:
- 'CRITICAL' if WFPS > 0.6 AND MRUL < 500
- 'WARNING' if WFPS > 0.4 OR MRUL < 500
- 'NORMAL' otherwise

# Depends on

* [Weighted Fault Prediction Score (WFPS)](/knowledge/weighted-fault-prediction-score.md)
* [Minimum Remaining Useful Life (MRUL)](/knowledge/minimum-remaining-useful-life.md)
