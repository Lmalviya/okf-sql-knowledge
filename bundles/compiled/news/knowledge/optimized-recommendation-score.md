---
type: Calculation
title: Optimized Recommendation Score (ORS)
description: Adjusts recommendation quality by incorporating system performance metrics.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 33
---

# Definition

ORS = \frac{RRS \times SPI}{k}, where RRS reflects recommendation quality and SPI represents the System Performance Index, with k as a normalization constant.

# Depends on

* [Recommendation Relevance Score (RRS)](/knowledge/recommendation-relevance-score.md)
* [System Performance Index (SPI)](/knowledge/system-performance-index.md)
