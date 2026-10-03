---
type: Calculation
title: Interactive Content Amplifier (ICA)
description: Enhances content value by factoring in user interactions and recommendation quality.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 39
---

# Definition

ICA = CIE + (\alpha \times RRS), where CIE captures Content Interaction Efficiency and RRS contributes the Recommendation Relevance Score.

# Depends on

* [Content Interaction Efficiency (CIE)](/knowledge/content-interaction-efficiency.md)
* [Recommendation Relevance Score (RRS)](/knowledge/recommendation-relevance-score.md)

# Used by

* [Content Virality Threshold (CVT)](/knowledge/content-virality-threshold.md)
* [Conversion Potential Indicator (CPI)](/knowledge/conversion-potential-indicator.md)
