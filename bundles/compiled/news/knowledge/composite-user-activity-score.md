---
type: Calculation
title: Composite User Activity Score (CUAS)
description: Integrates multiple user activity metrics into one composite score.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 50
---

# Definition

CUAS = \frac{UER + UDS + USV}{3}, where UER is the User Engagement Rate, UDS is the User Demographic Score, and USV is the User Subscription Value.

# Depends on

* [User Engagement Rate (UER)](/knowledge/user-engagement-rate.md)
* [User Subscription Value (USV)](/knowledge/user-subscription-value.md)
* [User Demographic Score (UDS)](/knowledge/user-demographic-score.md)
