---
type: Calculation
title: Patient Stability Metric (PSM)
description: Calculates an index reflecting patient stability, inversely related to crisis frequency and missed appointments.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 33
---

# Definition

PSM = \frac{1}{1 + CIF + MAR}, \text{where higher values indicate greater stability based on Crisis Intervention Frequency (CIF) and Missed Appointment Rate (MAR)}

# Depends on

* [Crisis Intervention Frequency (CIF)](/knowledge/crisis-intervention-frequency.md)
* [Missed Appointment Rate (MAR)](/knowledge/missed-appointment-rate.md)

# Used by

* [Facility Efficiency Index (FEI)](/knowledge/facility-efficiency-index.md)
* [Facility Performance Quadrant (FPQ)](/knowledge/facility-performance-quadrant.md)
