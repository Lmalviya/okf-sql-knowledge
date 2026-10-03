---
type: Business Rule
title: Whale
description: Identifies fans who provide extraordinary financial support
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 27
---

# Definition

A fan with giftvalusd > 500 or spendusd > 1000 within a 90-day period, regardless of other engagement metrics. These fans form the financial backbone of idol economic ecosystems.

# Columns used

* [interactions](/tables/interactions.md): `giftvalusd`
* [membershipandspending](/tables/membershipandspending.md): `spendusd`

# Depends on

* [interactions.gifttot_interactions.giftvalusd](/knowledge/interactions-gifttot-interactions-giftvalusd.md)

# Used by

* [Engagement-Deficient Whale](/knowledge/engagement-deficient-whale.md)
