---
type: Calculation
title: Clinical Improvement Potential Index (CIPI)
description: Calculates a ratio comparing patient engagement/adherence to overall symptom severity at a facility, suggesting potential responsiveness to intervention.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 50
---

# Definition

CIPI = \frac{EAS}{SSI + 1}, \text{using Engagement-Adherence Score (EAS) and Symptom Severity Index (SSI). Higher values suggest higher engagement relative to current symptom burden.}

# Depends on

* [Engagement-Adherence Score (EAS)](/knowledge/engagement-adherence-score.md)
* [Symptom Severity Index (SSI)](/knowledge/symptom-severity-index.md)
