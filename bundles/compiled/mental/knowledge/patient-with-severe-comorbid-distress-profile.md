---
type: Business Rule
title: Patient with Severe Comorbid Distress Profile
description: Identifies patients experiencing significant simultaneous distress across depression, anxiety, and functional domains.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 45
---

# Definition

A patient where mental_health_scores['depression']['phq9_score'] \geq 15 AND mental_health_scores['anxiety']['gad7_score'] \geq 15 AND funcimp = 'Severe'. \text{This profile relates to high individual contributions to APSF, AGSF, and PFIS}.

# Columns used

* [assessmentsymptomsandrisk](/tables/assessmentsymptomsandrisk.md): `mental_health_scores`
* [assessmentsocialanddiagnosis](/tables/assessmentsocialanddiagnosis.md): `funcimp`

# Depends on

* [Average PHQ-9 Score by Facility (APSF)](/knowledge/average-phq-9-score-by-facility.md)
* [Average GAD-7 Score by Facility (AGSF)](/knowledge/average-gad-7-score-by-facility.md)
* [Patient Functional Impairment Score (PFIS)](/knowledge/patient-functional-impairment-score.md)
