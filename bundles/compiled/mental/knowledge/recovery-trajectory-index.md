---
type: Calculation
title: Recovery Trajectory Index (RTI)
description: Estimates the effectiveness of treatment adherence in achieving functional improvement at a facility.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 53
---

# Definition

RTI = \frac{\sum_{i \in treatmentoutcomes} (funcimpv\_score_i)}{|treatmentoutcomes|} \times TAR, \text{where } funcimpv\_score = \begin{cases} 3 & \text{if } funcimpv = Significant \\ 2 & \text{if } funcimpv = Moderate \\ 1 & \text{if } funcimpv = Minimal \end{cases}

# Columns used

* [treatmentoutcomes](/tables/treatmentoutcomes.md): `funcimpv`

# Depends on

* [Treatment Adherence Rate (TAR)](/knowledge/treatment-adherence-rate.md)

# Used by

* [Facility with Potential Engagement-Outcome Disconnect](/knowledge/facility-with-potential-engagement-outcome-disconnect.md)
