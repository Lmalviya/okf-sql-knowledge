---
type: Calculation
title: User Demographic Score (UDS)
description: Measures the impact of user demographics by combining age with factors related to gender and occupation.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 30
---

# Definition

UDS = ageval \times genderFactor \times occupationFactor, \text{ where genderFactor and occupationFactor are weights derived from segmentation studies.}

# Columns used

* [users](/tables/users.md): `ageval`

# Depends on

* [genderFactor](/knowledge/genderfactor.md)
* [occupationFactor](/knowledge/occupationfactor.md)

# Used by

* [Subscription Valuation Rule (SVR)](/knowledge/subscription-valuation-rule.md)
* [Composite User Activity Score (CUAS)](/knowledge/composite-user-activity-score.md)
