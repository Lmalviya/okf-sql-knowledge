---
type: Calculation
title: Account Activity Frequency (AAF)
description: Measures how frequently an account engages in platform activities relative to its age.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 0
---

# Definition

AAF = \frac{\text{sesscount}}{\text{acctagespan}}

# Columns used

* [account](/tables/account.md): `acctagespan`
* [sessionbehavior](/tables/sessionbehavior.md): `sesscount`

# Used by

* [Behavioral Anomaly Score (BAS)](/knowledge/behavioral-anomaly-score.md)
* [Temporal Pattern Deviation Score (TPDS)](/knowledge/temporal-pattern-deviation-score.md)
