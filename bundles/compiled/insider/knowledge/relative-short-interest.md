---
type: Calculation
title: Relative Short Interest (RSI)
description: Calculates short interest ratio relative to institutional ownership.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 8
---

# Definition

RSI = \frac{\text{shortintrt}}{\text{instownpct}} \text{ (undefined if instownpct = 0)}

# Columns used

* [sentimentandfundamentals](/tables/sentimentandfundamentals.md): `instownpct`, `shortintrt`

# Used by

* [Insider Sentiment Short Ratio (ISSR)](/knowledge/insider-sentiment-short-ratio.md)
