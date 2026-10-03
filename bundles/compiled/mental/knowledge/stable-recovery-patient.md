---
type: Business Rule
title: Stable Recovery Patient
description: Identifies patients showing stable recovery with good functional outcomes.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 13
---

# Definition

A patient with recstatus = Stable and funcimpv \in \{Moderate, Significant\}

# Columns used

* [treatmentoutcomes](/tables/treatmentoutcomes.md): `funcimpv`
* [assessmentsocialanddiagnosis](/tables/assessmentsocialanddiagnosis.md): `recstatus`

# Used by

* [Patient Exhibiting Fragile Stability](/knowledge/patient-exhibiting-fragile-stability.md)
