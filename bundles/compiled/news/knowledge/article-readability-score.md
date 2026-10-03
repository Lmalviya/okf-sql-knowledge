---
type: Calculation
title: Article Readability Score (ARS)
description: Calculates the readability of an article by correlating estimated reading time with word count and difficulty factor.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 5
---

# Definition

ARS = \frac{readsec \times \log(wordlen)}{w}, \text{ where w is a weight factor assigned according to the article difficulty level (e.g., 1 for Basic, 1.5 for Intermediate, 2 for Advanced, 1.2 for others).}

# Columns used

* [articles](/tables/articles.md): `wordlen`, `readsec`

# Used by

* [Dynamic Content Value (DCV)](/knowledge/dynamic-content-value.md)
* [Adjusted Read Time Estimator (ARTE)](/knowledge/adjusted-read-time-estimator.md)
* [Content Consumption Consistency (CCC)](/knowledge/content-consumption-consistency.md)
* [Readability Segmentation](/knowledge/readability-segmentation.md)
