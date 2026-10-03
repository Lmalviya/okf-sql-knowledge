---
type: Calculation
title: Social Support Effectiveness (SSE)
description: Evaluates the effectiveness of social support based on social support level and relationship quality.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 8
---

# Definition

SSE = \frac{\sum_{i \in assessmentsocialanddiagnosis} (socsup\_score_i + relqual\_score_i)} {|assessmentsocialanddiagnosis|}, \text{where } socsup\_score = \begin{cases} 3 & \text{if } socsup = Strong \\ 2 & \text{if } socsup = Moderate \\ 1 & \text{if } socsup = Limited \end{cases}, \text{and } relqual\_score = \begin{cases} 3 & \text{if } relqual = Good \\ 2 & \text{if } relqual = Fair \\ 1 & \text{if } relqual = Poor \\ 0 & \text{if } relqual = Conflicted \end{cases}

# Columns used

* [assessmentsocialanddiagnosis](/tables/assessmentsocialanddiagnosis.md): `socsup`, `relqual`

# Used by

* [High Social Support Patient](/knowledge/high-social-support-patient.md)
* [Socio-Environmental Support Index (SESI)](/knowledge/socio-environmental-support-index.md)
* [Support System Pressure Index (SSPI)](/knowledge/support-system-pressure-index.md)
* [Patient with Strong Recovery Capital](/knowledge/patient-with-strong-recovery-capital.md)
* [Well-Resourced High-Support Environment](/knowledge/well-resourced-high-support-environment.md)
* [Patient with High Crisis & Low Support Profile](/knowledge/patient-with-high-crisis-low-support-profile.md)
* [Patient Exhibiting Fragile Stability](/knowledge/patient-exhibiting-fragile-stability.md)
