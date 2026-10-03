---
type: Calculation
title: Symptom Severity Index (SSI)
description: Calculates a combined average symptom severity score for a facility, based on depression and anxiety.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 30
---

# Definition

SSI = \frac{APSF + AGSF}{2}, \text{using Average PHQ-9 Score (APSF) and Average GAD-7 Score (AGSF)}

# Depends on

* [Average PHQ-9 Score by Facility (APSF)](/knowledge/average-phq-9-score-by-facility.md)
* [Average GAD-7 Score by Facility (AGSF)](/knowledge/average-gad-7-score-by-facility.md)

# Used by

* [Clinical Improvement Potential Index (CIPI)](/knowledge/clinical-improvement-potential-index.md)
* [Facility with High Clinical Leverage Potential](/knowledge/facility-with-high-clinical-leverage-potential.md)
