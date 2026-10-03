---
type: Business Rule
title: Patient with Strong Recovery Capital
description: Identifies patients demonstrating high social support effectiveness coupled with low functional impairment.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 42
---

# Definition

A patient where SSE \geq 5 and their funcimp value corresponds to a score of 1 (Mild), potentially indicating strong basis for sustained recovery. Relates to concepts measured by SSE and PFIS.

# Columns used

* [assessmentsocialanddiagnosis](/tables/assessmentsocialanddiagnosis.md): `funcimp`

# Depends on

* [Social Support Effectiveness (SSE)](/knowledge/social-support-effectiveness.md)
* [Patient Functional Impairment Score (PFIS)](/knowledge/patient-functional-impairment-score.md)
