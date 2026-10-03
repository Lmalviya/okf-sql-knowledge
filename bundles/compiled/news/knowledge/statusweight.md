---
type: Value Illustration
title: statusWeight
description: A weight assigned to different subscription tiers to reflect their business value.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 6
---

# Definition

'Premium' = 2.0, 'Enterprise' = 3.0, 'Basic' = 1.0, and others = 0.5. It reflects the assumed revenue or importance of the subscription tier.

# Used by

* [User Subscription Value (USV)](/knowledge/user-subscription-value.md)
* [Composite System Stability (CSS)](/knowledge/composite-system-stability.md)
