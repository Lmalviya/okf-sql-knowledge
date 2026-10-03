---
type: Calculation
title: Recommendation Click-Through Rate (RCTR)
description: Defines RCTR as the ratio of clicks to total recommendations.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 58
---

# Definition

RCTR = (clicks / recommendations) when recommendations are greater than zero.
