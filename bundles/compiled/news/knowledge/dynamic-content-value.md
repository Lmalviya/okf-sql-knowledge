---
type: Calculation
title: Dynamic Content Value (DCV)
description: Measures an article's overall value by combining quality, recommendation relevance, and readability factors.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 32
---

# Definition

DCV = \frac{AQI + RRS + (100 - ARS)}{3}, where AQI is the Article Quality Index, RRS the Recommendation Relevance Score, and ARS the Article Readability Score.

# Depends on

* [Article Quality Index (AQI)](/knowledge/article-quality-index.md)
* [Recommendation Relevance Score (RRS)](/knowledge/recommendation-relevance-score.md)
* [Article Readability Score (ARS)](/knowledge/article-readability-score.md)

# Used by

* [Content Virality Threshold (CVT)](/knowledge/content-virality-threshold.md)
