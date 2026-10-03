---
type: Business Rule
title: Complex Care Needs
description: Identifies patients requiring intensive care coordination due to multiple risk factors.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 12
---

# Definition

A patient with SRP > 20\% and PFIS > 2.5 and subuse \in \{Opioids, Multiple\}

# Columns used

* [assessmentsymptomsandrisk](/tables/assessmentsymptomsandrisk.md): `subuse`

# Depends on

* [Suicide Risk Prevalence (SRP)](/knowledge/suicide-risk-prevalence.md)
* [Patient Functional Impairment Score (PFIS)](/knowledge/patient-functional-impairment-score.md)

# Used by

* [Resource-Intensive High-Risk Patient Cohort](/knowledge/resource-intensive-high-risk-patient-cohort.md)
