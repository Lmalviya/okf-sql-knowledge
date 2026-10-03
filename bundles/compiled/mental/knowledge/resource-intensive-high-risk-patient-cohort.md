---
type: Business Rule
title: Resource-Intensive High-Risk Patient Cohort
description: Identifies patients requiring significant care coordination and intervention due to possessing characteristics of both Complex Care Needs and Frequent Crisis Patterns.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 57
---

# Definition

A patient meeting criteria for both Complex Care Needs AND Frequent Crisis Patient (17).

# Depends on

* [Complex Care Needs](/knowledge/complex-care-needs.md)
* [Frequent Crisis Patient](/knowledge/frequent-crisis-patient.md)
