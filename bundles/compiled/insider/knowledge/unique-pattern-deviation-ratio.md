---
type: Calculation
title: Unique Pattern Deviation Ratio (UPDR)
description: Measures the ratio of unique pattern deviation (anomaly) to the similarity with known illicit patterns, indicating how unusual the potentially illicit behavior is.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 52
---

# Definition

UPDR = \frac{\text{PAS}}{\text{Max}(0.01, \text{patsim})}

# Columns used

* [advancedbehavior](/tables/advancedbehavior.md): `patsim`

# Depends on

* [Pattern Anomaly Score (PAS)](/knowledge/pattern-anomaly-score.md)
* [Pattern Similarity Score Context](/knowledge/pattern-similarity-score-context.md)
