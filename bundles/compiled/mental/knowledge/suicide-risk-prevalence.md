---
type: Calculation
title: Suicide Risk Prevalence (SRP)
description: Calculates the percentage of assessments indicating high or severe suicide risk at a facility.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 3
---

# Definition

SRP = \frac{|assessmentsymptomsandrisk \text{ with } suicrisk \in \{High, Severe\}|} {|assessmentsymptomsandrisk|} \times 100

# Columns used

* [assessmentsymptomsandrisk](/tables/assessmentsymptomsandrisk.md): `suicrisk`

# Used by

* [Complex Care Needs](/knowledge/complex-care-needs.md)
* [Facility Risk Profile Index (FRPI)](/knowledge/facility-risk-profile-index.md)
* [Comprehensive Facility Risk Score (CFRS)](/knowledge/comprehensive-facility-risk-score.md)
