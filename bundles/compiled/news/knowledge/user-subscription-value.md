---
type: Calculation
title: User Subscription Value (USV)
description: Evaluates the relative value of a user's subscription based on subscription duration and status.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 17
---

# Definition

USV = subdays \times statusWeight, \text{ where statusWeight is a multiplier defined by the subscription status (for example, Premium, Enterprise, or Basic).}

# Columns used

* [users](/tables/users.md): `subdays`

# Depends on

* [statusWeight](/knowledge/statusweight.md)

# Used by

* [Subscription Valuation Rule (SVR)](/knowledge/subscription-valuation-rule.md)
* [Composite User Activity Score (CUAS)](/knowledge/composite-user-activity-score.md)
