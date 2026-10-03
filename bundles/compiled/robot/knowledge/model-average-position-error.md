---
type: Calculation
title: Model Average Position Error
description: The average of the Average Position Error values for all robots within a specific model series.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 57
---

# Definition

Let M be the model series, \mathcal{R}_M be the set of unique robot identifiers in M. Then Model Avg Pos Error = \frac{\sum_{R \in \mathcal{R}_M} \text{APE}(R)}{|\mathcal{R}_M|}

# Depends on

* [Average Position Error (APE)](/knowledge/average-position-error.md)
