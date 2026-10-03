---
type: Calculation
title: Average PHQ-9 Score by Facility (APSF)
description: Calculates the average PHQ-9 depression score for patients assessed at a specific facility.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 0
---

# Definition

APSF = \frac{\sum_{i \in assessmentsymptomsandrisk} (mental\_health\_scores_i['depression']['phq9\_score'])} {|assessmentsymptomsandrisk|}

# Used by

* [Symptom Severity Index (SSI)](/knowledge/symptom-severity-index.md)
* [Comprehensive Facility Risk Score (CFRS)](/knowledge/comprehensive-facility-risk-score.md)
* [Patient with Severe Comorbid Distress Profile](/knowledge/patient-with-severe-comorbid-distress-profile.md)
