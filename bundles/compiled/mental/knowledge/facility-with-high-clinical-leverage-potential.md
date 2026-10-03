---
type: Business Rule
title: Facility with High Clinical Leverage Potential
description: Identifies facilities with a highly engaged and adherent patient population that still experiences significant symptom severity, suggesting readiness for potentially more intensive or alternative interventions.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 55
---

# Definition

A facility where EAS > 2.5 AND SSI > 15, \text{indicating high Engagement-Adherence Score (EAS) alongside a high Symptom Severity Index (SSI).}

# Depends on

* [Engagement-Adherence Score (EAS)](/knowledge/engagement-adherence-score.md)
* [Symptom Severity Index (SSI)](/knowledge/symptom-severity-index.md)
