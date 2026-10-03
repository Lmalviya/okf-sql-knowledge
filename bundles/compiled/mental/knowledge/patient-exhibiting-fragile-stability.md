---
type: Business Rule
title: Patient Exhibiting Fragile Stability
description: Identifies patients currently classified as 'Stable Recovery' but who exhibit risk factors like frequent missed appointments or low social support, suggesting potential for destabilization.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 56
---

# Definition

A patient meeting Stable Recovery Patient criteria BUT having an average missappt > 2 across their encounters OR an individual SSE score < 3. \text{Combines Stable Recovery Patient status with risk factors related to MAR and SSE}.

# Columns used

* [encounters](/tables/encounters.md): `missappt`

# Depends on

* [Stable Recovery Patient](/knowledge/stable-recovery-patient.md)
* [Missed Appointment Rate (MAR)](/knowledge/missed-appointment-rate.md)
* [Social Support Effectiveness (SSE)](/knowledge/social-support-effectiveness.md)
