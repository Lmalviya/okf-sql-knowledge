---
type: Business Rule
title: Peer Mimicry Suspicion
description: Flags traders whose behavior closely matches peers but deviates little from known patterns, potentially mimicking a risky group.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 49
---

# Definition

A trader with a low Pattern Anomaly Score (PAS)  (e.g., < 0.1) BUT a high peercorr (e.g., > 0.7), suggesting potential mimicry rather than independent strategy, possibly following a group engaged in problematic behavior.

# Columns used

* [advancedbehavior](/tables/advancedbehavior.md): `peercorr`

# Depends on

* [Pattern Anomaly Score (PAS)](/knowledge/pattern-anomaly-score.md)

# Used by

* [Networked Mimicry Risk](/knowledge/networked-mimicry-risk.md)
