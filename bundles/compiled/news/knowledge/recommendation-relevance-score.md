---
type: Calculation
title: Recommendation Relevance Score (RRS)
description: Computes the overall relevance of a recommendation by averaging recommendation score, algorithm confidence, and utility.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 2
---

# Definition

RRS = \frac{(recscore + confval + recutil)}{3}, \text{ where the contributing factors capture recommendation performance.}

# Columns used

* [recommendations](/tables/recommendations.md): `recscore`, `confval`
* [sessions](/tables/sessions.md): `recutil`

# Used by

* [Content Recommendation Strategy (CRS)](/knowledge/content-recommendation-strategy.md)
* [Dynamic Content Value (DCV)](/knowledge/dynamic-content-value.md)
* [Optimized Recommendation Score (ORS)](/knowledge/optimized-recommendation-score.md)
* [Personalization Accuracy Metric (PAM)](/knowledge/personalization-accuracy-metric.md)
* [Interactive Content Amplifier (ICA)](/knowledge/interactive-content-amplifier.md)
