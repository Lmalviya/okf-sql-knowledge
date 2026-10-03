---
type: Calculation
title: Average GAD-7 Score by Facility (AGSF)
description: Calculates the average GAD-7 anxiety score for patients assessed at a specific facility.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 1
---

# Definition

AGSF = \frac{\sum_{i \in assessmentsymptomsandrisk} (mental\_health\_scores_i['anxiety']['gad7\_score'])} {|assessmentsymptomsandrisk|}, \text{where } mental\_health\_scores_i['anxiety']['gad7\_score'] \text{ is the GAD-7 score for each assessment in the assessmentsymptomsandrisk table, linked to a facility via encounters.facid}

# Columns used

* [encounters](/tables/encounters.md): `facid`

# Used by

* [Symptom Severity Index (SSI)](/knowledge/symptom-severity-index.md)
* [Patient with Severe Comorbid Distress Profile](/knowledge/patient-with-severe-comorbid-distress-profile.md)
