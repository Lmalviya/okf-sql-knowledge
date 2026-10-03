---
type: Calculation
title: Sentiment-Weighted Option Volume (SWOV)
description: Adjusts the option volume ratio based on the divergence between news and social sentiment.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 34
---

# Definition

SWOV = \text{optvolrt} \times (1 + \text{SDF}) \\ \text{where SDF is the Sentiment Divergence Factor .}

# Columns used

* [sentimentandfundamentals](/tables/sentimentandfundamentals.md): `optvolrt`

# Depends on

* [Sentiment Divergence Factor (SDF)](/knowledge/sentiment-divergence-factor.md)

# Used by

* [Potential Insider Trading Flag](/knowledge/potential-insider-trading-flag.md)
* [Sentiment-Driven Leakage Risk (SDLR)](/knowledge/sentiment-driven-leakage-risk.md)
