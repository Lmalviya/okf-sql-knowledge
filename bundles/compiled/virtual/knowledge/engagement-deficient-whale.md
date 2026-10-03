---
type: Business Rule
title: Engagement-Deficient Whale
description: Identifies high-spending fans with surprisingly low engagement
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 41
---

# Definition

A fan with giftvalusd > 500 or spendusd > 1000, but with FEI < 0.3, indicating significant financial contribution despite limited platform participation.

# Columns used

* [interactions](/tables/interactions.md): `giftvalusd`
* [membershipandspending](/tables/membershipandspending.md): `spendusd`

# Depends on

* [Fan Engagement Index (FEI)](/knowledge/fan-engagement-index.md)
* [Whale](/knowledge/whale.md)
