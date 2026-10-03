---
type: Calculation
title: Sentiment Divergence Factor (SDF)
description: Measures the difference between news and social media sentiment scores.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 7
---

# Definition

SDF = |\text{newsscore} - \text{socscore}|

# Columns used

* [sentimentandfundamentals](/tables/sentimentandfundamentals.md): `newsscore`, `socscore`

# Used by

* [Sentiment-Weighted Option Volume (SWOV)](/knowledge/sentiment-weighted-option-volume.md)
* [Volatile Event Speculator](/knowledge/volatile-event-speculator.md)
