---
type: Business Rule
title: Patient with High Crisis & Low Support Profile
description: Identifies patients characterized by frequent crisis interventions and weak social support systems.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 47
---

# Definition

A patient where their individual crisisint count (from treatmentbasics table) > 2 AND their individual SSE score (calculated from assessmentsocialanddiagnosis) < 3. \text{This profile relates to high contribution to CIF and low individual SSE}.

# Columns used

* [treatmentbasics](/tables/treatmentbasics.md): `crisisint`

# Depends on

* [Crisis Intervention Frequency (CIF)](/knowledge/crisis-intervention-frequency.md)
* [Social Support Effectiveness (SSE)](/knowledge/social-support-effectiveness.md)
