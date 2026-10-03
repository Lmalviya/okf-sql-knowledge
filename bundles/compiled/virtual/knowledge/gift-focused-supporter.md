---
type: Business Rule
title: Gift-Focused Supporter
description: Identifies fans whose primary support comes through gifting rather than direct spending
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 49
---

# Definition

A fan with GIQ > 50 but spendusd < 100, showing a preference for gift-based support mechanisms over traditional subscription or purchase options.

# Columns used

* [membershipandspending](/tables/membershipandspending.md): `spendusd`

# Depends on

* [interactions.gifttot_interactions.giftvalusd](/knowledge/interactions-gifttot-interactions-giftvalusd.md)
* [Gift Impact Quotient (GIQ)](/knowledge/gift-impact-quotient.md)
