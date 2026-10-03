---
type: Calculation
title: Sentiment-Driven Leakage Risk (SDLR)
description: Calculates potential information leakage risk weighted by sentiment-driven unusual option volume.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 51
---

# Definition

SDLR = \text{SWOV} \times \text{infoleaksc}.

# Columns used

* [sentimentandfundamentals](/tables/sentimentandfundamentals.md): `infoleaksc`

# Depends on

* [Information Leakage Score Interpretation](/knowledge/information-leakage-score-interpretation.md)
* [Sentiment-Weighted Option Volume (SWOV)](/knowledge/sentiment-weighted-option-volume.md)

# Used by

* [High SDLR Transaction](/knowledge/high-sdlr-transaction.md)
