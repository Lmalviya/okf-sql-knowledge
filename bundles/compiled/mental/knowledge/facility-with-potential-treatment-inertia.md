---
type: Business Rule
title: Facility with Potential Treatment Inertia
description: Identifies facilities where patients seem engaged in therapy (high TES) but struggle with overall treatment adherence (low TAR), suggesting potential systemic barriers or resistance.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 46
---

# Definition

A facility where TES > 2.2 and TAR < 0.6, \text{based on Therapy Engagement Score (TES) and Treatment Adherence Rate (TAR)}

# Depends on

* [Therapy Engagement Score (TES)](/knowledge/therapy-engagement-score.md)
* [Treatment Adherence Rate (TAR)](/knowledge/treatment-adherence-rate.md)
