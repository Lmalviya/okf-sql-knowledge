---
type: Calculation
title: Market-Adjusted Pattern Anomaly (MAPA)
description: Calculates pattern anomaly score adjusted for market correlation, highlighting non-market related deviations.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 39
---

# Definition

MAPA = \text{PAS} \times (1 - \text{mktcorr}) \\ \text{where PAS is Pattern Anomaly Score .}

# Columns used

* [advancedbehavior](/tables/advancedbehavior.md): `mktcorr`

# Depends on

* [Pattern Anomaly Score (PAS)](/knowledge/pattern-anomaly-score.md)

# Used by

* [Significant Enforcement Action](/knowledge/significant-enforcement-action.md)
* [Market-Agnostic Suspicion Index (MASI)](/knowledge/market-agnostic-suspicion-index.md)
