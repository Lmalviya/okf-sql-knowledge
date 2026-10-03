---
type: Business Rule
title: Content Virality Threshold (CVT)
description: Defines the performance level at which content is likely to go viral.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 44
---

# Definition

Content is considered viral when its Dynamic Content Value and Interactive Content Amplifier both exceed the established virality thresholds.

# Depends on

* [Dynamic Content Value (DCV)](/knowledge/dynamic-content-value.md)
* [Interactive Content Amplifier (ICA)](/knowledge/interactive-content-amplifier.md)
