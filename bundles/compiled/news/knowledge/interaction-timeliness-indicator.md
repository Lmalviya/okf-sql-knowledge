---
type: Business Rule
title: Interaction Timeliness Indicator (ITI)
description: Evaluates the promptness of user interactions after content presentation.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 19
---

# Definition

A minimal delay between content exposure and user interaction indicates high interest, thereby enhancing content performance metrics.

# Depends on

* [Content Interaction Efficiency (CIE)](/knowledge/content-interaction-efficiency.md)

# Used by

* [Conversion Impact Factor (CIF)](/knowledge/conversion-impact-factor.md)
