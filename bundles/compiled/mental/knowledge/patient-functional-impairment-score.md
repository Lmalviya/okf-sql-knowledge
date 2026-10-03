---
type: Calculation
title: Patient Functional Impairment Score (PFIS)
description: Calculates an average functional impairment score across patients.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 6
---

# Definition

PFIS = \frac{\sum_{i \in assessmentsocialanddiagnosis} funcimp\_score_i} {|assessmentsocialanddiagnosis|}, \text{where } funcimp\_score = \begin{cases} 3 & \text{if } funcimp = Severe \\ 2 & \text{if } funcimp = Moderate \\ 1 & \text{if } funcimp = Mild \end{cases}

# Columns used

* [assessmentsocialanddiagnosis](/tables/assessmentsocialanddiagnosis.md): `funcimp`

# Used by

* [Complex Care Needs](/knowledge/complex-care-needs.md)
* [Facility Risk Profile Index (FRPI)](/knowledge/facility-risk-profile-index.md)
* [Resource-Demand Differential (RDD)](/knowledge/resource-demand-differential.md)
* [Adherence Effectiveness Ratio (AER)](/knowledge/adherence-effectiveness-ratio.md)
* [Comprehensive Facility Risk Score (CFRS)](/knowledge/comprehensive-facility-risk-score.md)
* [Facility with Engaged but High-Impairment Population](/knowledge/facility-with-engaged-but-high-impairment-population.md)
* [Patient with Strong Recovery Capital](/knowledge/patient-with-strong-recovery-capital.md)
* [Patient with Severe Comorbid Distress Profile](/knowledge/patient-with-severe-comorbid-distress-profile.md)
