---
type: Business Rule
title: Subscription Valuation Rule (SVR)
description: Determines the business value of a user by integrating subscription details with demographic and engagement factors.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 49
---

# Definition

A comprehensive user valuation is achieved by weighting subscription duration, engagement performance, and demographic indicators.

# Depends on

* [User Subscription Value (USV)](/knowledge/user-subscription-value.md)
* [User Demographic Score (UDS)](/knowledge/user-demographic-score.md)
