---
type: Business Rule
title: Low Engagement Risk
description: Identifies patients at risk of disengagement from therapy.
tags:
- mental
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:05+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/mental/mental_kb.jsonl
  title: mental business rules (LiveSQLBench), rule 14
---

# Definition

A patient with TES < 1.5 and txeng \in \{Low, Non-compliant\}

# Columns used

* [treatmentoutcomes](/tables/treatmentoutcomes.md): `txeng`

# Depends on

* [Therapy Engagement Score (TES)](/knowledge/therapy-engagement-score.md)
