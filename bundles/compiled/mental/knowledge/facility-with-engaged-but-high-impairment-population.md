---
type: Business Rule
title: Facility with Engaged but High-Impairment Population
description: Identifies facilities where the patient population is generally engaged and adherent but continues to struggle with high functional impairment.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 41
---

# Definition

A facility where EAS > 2.0 and PFIS > 2.0, \text{showing high Engagement-Adherence Score (EAS) alongside high Patient Functional Impairment Score (PFIS)}

# Depends on

* [Engagement-Adherence Score (EAS)](/knowledge/engagement-adherence-score.md)
* [Patient Functional Impairment Score (PFIS)](/knowledge/patient-functional-impairment-score.md)
