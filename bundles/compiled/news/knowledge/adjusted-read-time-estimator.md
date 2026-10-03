---
type: Calculation
title: Adjusted Read Time Estimator (ARTE)
description: Provides an estimation of effective reading time by adjusting raw reading seconds.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 34
---

# Definition

ARTE = readsec \times \frac{ARS}{UER}, where ARS is the Article Readability Score and UER is the User Engagement Rate.

# Columns used

* [articles](/tables/articles.md): `readsec`

# Depends on

* [Article Readability Score (ARS)](/knowledge/article-readability-score.md)
* [User Engagement Rate (UER)](/knowledge/user-engagement-rate.md)
