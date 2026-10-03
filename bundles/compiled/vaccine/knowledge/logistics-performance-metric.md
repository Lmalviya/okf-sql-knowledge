---
type: Calculation
title: Logistics Performance Metric (LPM)
description: Evaluates overall logistics efficiency with temporal considerations.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 54
---

# Definition

LPM = \text{RCP} \cdot \frac{\text{HQI}}{\sqrt{1 + \text{TRS}}}

# Depends on

* [Route Completion Percentage (RCP)](/knowledge/route-completion-percentage.md)
* [Handling Quality Index (HQI)](/knowledge/handling-quality-index.md)
* [Total Risk Score (TRS)](/knowledge/total-risk-score.md)

# Used by

* [Compound Quality Risk](/knowledge/compound-quality-risk.md)
* [Multi-System Failure Risk](/knowledge/multi-system-failure-risk.md)
