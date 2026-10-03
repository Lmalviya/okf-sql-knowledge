---
type: Calculation
title: Adherence Effectiveness Ratio (AER)
description: Calculates a ratio comparing treatment adherence rate to the average functional impairment, suggesting potential treatment impact relative to need.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 36
---

# Definition

AER = \frac{TAR}{PFIS}, \text{using Treatment Adherence Rate (TAR) and Patient Functional Impairment Score (PFIS) (handle PFIS=0)}

# Depends on

* [Treatment Adherence Rate (TAR)](/knowledge/treatment-adherence-rate.md)
* [Patient Functional Impairment Score (PFIS)](/knowledge/patient-functional-impairment-score.md)
