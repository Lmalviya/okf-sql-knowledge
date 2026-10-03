---
type: Calculation
title: Engagement-Adherence Score (EAS)
description: Computes a composite score reflecting patient participation and adherence to treatment plans at a facility.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 31
---

# Definition

EAS = \frac{TES + (TAR \times 3)}{2}, \text{normalizing Treatment Adherence Rate (TAR) to the Therapy Engagement Score (TES) scale (0-3)}

# Depends on

* [Therapy Engagement Score (TES)](/knowledge/therapy-engagement-score.md)
* [Treatment Adherence Rate (TAR)](/knowledge/treatment-adherence-rate.md)

# Used by

* [Facility with Engaged but High-Impairment Population](/knowledge/facility-with-engaged-but-high-impairment-population.md)
* [Facility Attrition Risk Indicator](/knowledge/facility-attrition-risk-indicator.md)
* [Clinical Improvement Potential Index (CIPI)](/knowledge/clinical-improvement-potential-index.md)
* [Facility with High Clinical Leverage Potential](/knowledge/facility-with-high-clinical-leverage-potential.md)
