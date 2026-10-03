---
type: Calculation
title: Missed Appointment Rate (MAR)
description: Calculates the average number of missed appointments per patient at a facility.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 9
---

# Definition

MAR = \frac{\sum_{i \in encounters} missappt_i} {|patients|}

# Used by

* [High Appointment Adherence](/knowledge/high-appointment-adherence.md)
* [Patient Stability Metric (PSM)](/knowledge/patient-stability-metric.md)
* [Engagement Deficit Index (EDI)](/knowledge/engagement-deficit-index.md)
* [Facility Attrition Risk Indicator](/knowledge/facility-attrition-risk-indicator.md)
* [Facility Demonstrating Strong Patient Retention](/knowledge/facility-demonstrating-strong-patient-retention.md)
* [Patient Exhibiting Fragile Stability](/knowledge/patient-exhibiting-fragile-stability.md)
