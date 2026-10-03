---
type: Business Rule
title: Superfan
description: Identifies fans with exceptional platform value and engagement
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 20
---

# Definition

A fan with tierstep ≥ 8, FEI > 0.7, and MV > 200, representing the highest value segment providing substantial financial support while maintaining high engagement.

# Columns used

* [fans](/tables/fans.md): `tierstep`

# Depends on

* [fans.tierstep](/knowledge/fans-tierstep.md)
* [Fan Engagement Index (FEI)](/knowledge/fan-engagement-index.md)
* [Monetization Value (MV)](/knowledge/monetization-value.md)

# Used by

* [Retention Risk Superfan](/knowledge/retention-risk-superfan.md)
