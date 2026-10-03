---
type: Calculation
title: Comprehensive Facility Risk Score (CFRS)
description: A normalized index assessing overall facility risk based on combined depression severity, suicide risk prevalence, and functional impairment.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 38
---

# Definition

CFRS = \frac{APSF}{27} + \frac{SRP}{100} + \frac{PFIS}{3}, \text{normalizing Average PHQ-9 Score (APSF), Suicide Risk Prevalence (SRP), and Patient Functional Impairment Score (PFIS) to a 0-1 scale and summing}

# Depends on

* [Average PHQ-9 Score by Facility (APSF)](/knowledge/average-phq-9-score-by-facility.md)
* [Suicide Risk Prevalence (SRP)](/knowledge/suicide-risk-prevalence.md)
* [Patient Functional Impairment Score (PFIS)](/knowledge/patient-functional-impairment-score.md)
