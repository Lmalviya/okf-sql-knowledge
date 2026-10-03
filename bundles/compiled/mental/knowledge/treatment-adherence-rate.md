---
type: Calculation
title: Treatment Adherence Rate (TAR)
description: Measures the proportion of patients with high or medium treatment adherence at a facility.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 2
---

# Definition

TAR = \frac{|treatmentoutcomes \text{ with } txadh \in \{High, Medium\}|} {|treatmentoutcomes|}

# Columns used

* [treatmentoutcomes](/tables/treatmentoutcomes.md): `txadh`

# Used by

* [Engagement-Adherence Score (EAS)](/knowledge/engagement-adherence-score.md)
* [Adherence Effectiveness Ratio (AER)](/knowledge/adherence-effectiveness-ratio.md)
* [Facility with Potential Treatment Inertia](/knowledge/facility-with-potential-treatment-inertia.md)
* [Facility Demonstrating Strong Patient Retention](/knowledge/facility-demonstrating-strong-patient-retention.md)
* [Recovery Trajectory Index (RTI)](/knowledge/recovery-trajectory-index.md)
* [Crisis Adherence Ratio (CAR)](/knowledge/crisis-adherence-ratio.md)
* [Correlation Between Resource Adequacy and Adherence (CRAA)](/knowledge/correlation-between-resource-adequacy-and-adherence.md)
* [Facility Performance Quadrant (FPQ)](/knowledge/facility-performance-quadrant.md)
