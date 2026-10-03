---
type: Calculation
title: Facility Risk Profile Index (FRPI)
description: Generates an index indicating the overall risk level associated with the patient population at a facility.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 32
---

# Definition

FRPI = (\frac{SRP}{100} \times 5) + PFIS, \text{weighting Suicide Risk Prevalence (SRP) and combining with Patient Functional Impairment Score (PFIS)}

# Depends on

* [Suicide Risk Prevalence (SRP)](/knowledge/suicide-risk-prevalence.md)
* [Patient Functional Impairment Score (PFIS)](/knowledge/patient-functional-impairment-score.md)

# Used by

* [High-Need, Under-Resourced Facility](/knowledge/high-need-under-resourced-facility.md)
