---
type: Value Illustration
title: interactions.gifttot_interactions.giftvalusd
description: Explains the statistical significance of gift quantity and value
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 7
---

# Definition

gifttot represents the total number of gifts sent by fans, typically classified as: fewer than 10 is considered minimal gifting, 10-50 represents moderate support, and above 50 indicates substantial support; giftvalusd represents the USD value of gifts, generally $1-5 for small support, $5-20 for moderate support, $20-100 for large support, and above $100 for super support. Both metrics combined assess a fan's economic support level.

# Columns used

* [interactions](/tables/interactions.md): `gifttot`, `giftvalusd`

# Used by

* [Whale](/knowledge/whale.md)
* [Gift Impact Quotient (GIQ)](/knowledge/gift-impact-quotient.md)
* [Gift-Focused Supporter](/knowledge/gift-focused-supporter.md)
