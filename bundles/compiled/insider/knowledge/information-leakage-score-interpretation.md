---
type: Value Illustration
title: Information Leakage Score Interpretation
description: Provides context for the information leakage score, indicating potential trading on non-public information.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 27
---

# Definition

`infoleaksc`: A score typically from 0-100. Low scores (<20) suggest little evidence of trading activity ahead of significant news or events. Moderate scores (20-50) warrant attention and may correlate with known events. High scores (>50) strongly suggest potential trading based on material non-public information, requiring investigation.

# Columns used

* [sentimentandfundamentals](/tables/sentimentandfundamentals.md): `infoleaksc`

# Used by

* [Boosted Insider Leakage Score (BILS)](/knowledge/boosted-insider-leakage-score.md)
* [Sentiment-Driven Leakage Risk (SDLR)](/knowledge/sentiment-driven-leakage-risk.md)
