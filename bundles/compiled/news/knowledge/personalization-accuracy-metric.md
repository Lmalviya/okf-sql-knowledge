---
type: Calculation
title: Personalization Accuracy Metric (PAM)
description: Computes the accuracy of personalization by balancing recommendation performance and priority assignment.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 35
---

# Definition

PAM = \frac{RRS + PP}{2}, where RRS offers recommendation effectiveness and PP defines the Personalization Priority.

# Depends on

* [Recommendation Relevance Score (RRS)](/knowledge/recommendation-relevance-score.md)
* [Personalization Priority (PP)](/knowledge/personalization-priority.md)

# Used by

* [Targeted Personalization Benchmark (TPB)](/knowledge/targeted-personalization-benchmark.md)
