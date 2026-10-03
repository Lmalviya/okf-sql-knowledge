---
type: Business Rule
title: Frequent Crisis Patient
description: Identifies patients with frequent crisis interventions.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 17
---

# Definition

A patient with CIF > 2

# Depends on

* [Crisis Intervention Frequency (CIF)](/knowledge/crisis-intervention-frequency.md)

# Used by

* [Resource-Intensive High-Risk Patient Cohort](/knowledge/resource-intensive-high-risk-patient-cohort.md)
