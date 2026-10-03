---
type: Calculation
title: Model Average Max Operating Hours
description: The average of the maximum Total Operating Hours recorded for each robot within a specific model series.
tags:
- robot
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:10+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/robot/robot_kb.jsonl
  title: robot business rules (LiveSQLBench), rule 59
---

# Definition

Let M be the model series, \mathcal{R}_M be the set of unique robot identifiers in M. Then Model Avg Max Ops Hours = \frac{\sum_{R \in \mathcal{R}_M} \text{TOH}(R)}{|\mathcal{R}_M|}

# Depends on

* [Total Operating Hours (TOH)](/knowledge/total-operating-hours.md)
