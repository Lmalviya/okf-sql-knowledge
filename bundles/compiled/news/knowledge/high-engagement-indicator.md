---
type: Business Rule
title: High Engagement Indicator (HEI)
description: Determines if a session or article demonstrates outstanding user engagement.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 40
---

# Definition

An item is marked as high engagement when the User Engagement Rate is above the threshold and the Content Interaction Efficiency is high.

# Depends on

* [User Engagement Rate (UER)](/knowledge/user-engagement-rate.md)
* [Content Interaction Efficiency (CIE)](/knowledge/content-interaction-efficiency.md)
