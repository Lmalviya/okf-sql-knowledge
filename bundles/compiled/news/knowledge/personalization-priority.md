---
type: Business Rule
title: Personalization Priority (PP)
description: Establishes criteria for prioritizing content that aligns closely with individual user preferences based on prior interactions.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 11
---

# Definition

Content that strongly matches user preferences and exhibits high interaction rates is prioritized in personalized recommendations.

# Used by

* [Personalization Accuracy Metric (PAM)](/knowledge/personalization-accuracy-metric.md)
* [Targeted Personalization Benchmark (TPB)](/knowledge/targeted-personalization-benchmark.md)
* [Content Consumption Consistency (CCC)](/knowledge/content-consumption-consistency.md)
