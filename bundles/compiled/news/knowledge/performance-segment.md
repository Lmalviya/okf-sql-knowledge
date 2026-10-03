---
type: Business Rule
title: Performance Segment
description: Categorizes sessions based on their relative bounce rate and CTR performance using percentile rankings.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 54
---

# Definition

A classification of sessions into performance categories based on specific percentile criteria: 'High Bounce, Low CTR' (bounce_percentile < 0.25, ctr_percentile < 0.25), 'High Bounce, High CTR' (bounce_percentile < 0.25, ctr_percentile >= 0.75), 'Low Bounce, Low CTR' (bounce_percentile >= 0.75, ctr_percentile < 0.25), 'Low Bounce, High CTR' (bounce_percentile >= 0.75, ctr_percentile >= 0.75), or 'Average Performance' for all other combinations.

# Depends on

* [Bounce Percentile](/knowledge/bounce-percentile.md)
* [CTR Percentile](/knowledge/ctr-percentile.md)
