---
type: Calculation
title: Crisis Intervention Frequency (CIF)
description: Measures the average number of crisis interventions per patient at a facility.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 7
---

# Definition

CIF = \frac{\sum_{i \in treatmentbasics} crisisint_i} {|patients|}

# Used by

* [Frequent Crisis Patient](/knowledge/frequent-crisis-patient.md)
* [Patient Stability Metric (PSM)](/knowledge/patient-stability-metric.md)
* [Support System Pressure Index (SSPI)](/knowledge/support-system-pressure-index.md)
* [Patient with High Crisis & Low Support Profile](/knowledge/patient-with-high-crisis-low-support-profile.md)
* [Crisis Adherence Ratio (CAR)](/knowledge/crisis-adherence-ratio.md)
