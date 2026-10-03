---
type: Calculation
title: Engagement Deficit Index (EDI)
description: Quantifies the degree of patient disengagement, considering both therapy engagement scores and appointment attendance.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 37
---

# Definition

EDI = (3 - TES) \times (1 + MAR), \text{calculating the gap from maximum Therapy Engagement Score (TES) weighted by Missed Appointment Rate (MAR)}

# Depends on

* [Therapy Engagement Score (TES)](/knowledge/therapy-engagement-score.md)
* [Missed Appointment Rate (MAR)](/knowledge/missed-appointment-rate.md)
