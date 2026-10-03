---
type: Calculation
title: Article Quality Index (AQI)
description: Determines the quality index of an article by integrating quality score, freshness, sentiment, and controversy factors.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 1
---

# Definition

AQI = \frac{(qualscore + freshscore + sentscore - contrscore)}{3}, \text{ where each score is normalized on a uniform scale.}

# Columns used

* [articles](/tables/articles.md): `freshscore`, `qualscore`, `sentscore`, `contrscore`

# Used by

* [Dynamic Content Value (DCV)](/knowledge/dynamic-content-value.md)
* [Premium Article Distinction (PAD)](/knowledge/premium-article-distinction.md)
