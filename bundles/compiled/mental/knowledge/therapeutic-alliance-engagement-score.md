---
type: Calculation
title: Therapeutic Alliance & Engagement Score (TAES)
description: Computes a combined score reflecting both the average clinician-reported therapeutic alliance and the calculated therapy engagement score for a facility.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 52
---

# Definition

TAES = \frac{Average(theralliance\_score) + TES}{2}, \text{where } theralliance\_score = \begin{cases} 3 & \text{if } theralliance = Strong \\ 2 & \text{if } theralliance = Moderate \\ 1 & \text{if } theralliance = Weak \\ 0 & \text{if } theralliance = Poor \end{cases}, \text{averaged across treatmentoutcomes, combined with Therapy Engagement Score (TES)}.

# Columns used

* [treatmentoutcomes](/tables/treatmentoutcomes.md): `theralliance`

# Depends on

* [Therapy Engagement Score (TES)](/knowledge/therapy-engagement-score.md)
