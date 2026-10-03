---
type: Business Rule
title: Targeted Personalization Benchmark (TPB)
description: Establishes a benchmark for assessing the effectiveness of personalized content.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 42
---

# Definition

Content meets the targeted personalization benchmark when it aligns with the criteria set by Personalization Priority and is corroborated by a high Personalization Accuracy Metric.

# Depends on

* [Personalization Priority (PP)](/knowledge/personalization-priority.md)
* [Personalization Accuracy Metric (PAM)](/knowledge/personalization-accuracy-metric.md)
