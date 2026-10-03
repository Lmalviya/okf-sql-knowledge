---
type: Calculation
title: Session Count (SC)
description: Measures the total number of session records associated with an account.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:01+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 75
---

# Definition

SC_a = \left| \{ \text{sessref} \in \text{sessionbehavior} \mid \text{sessprofref} = \text{profkey}, \text{profaccref} = a \} \right|

# Columns used

* [profile](/tables/profile.md): `profkey`, `profaccref`
* [sessionbehavior](/tables/sessionbehavior.md): `sessref`, `sessprofref`

# Used by

* [High-Activity Account](/knowledge/high-activity-account-77.md)
