---
type: Calculation
title: Gift Impact Quotient (GIQ)
description: Evaluates the relative impact of a fan's gifting behavior considering both volume and value
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 34
---

# Definition

GIQ = \frac{giftvalusd \times gifttot}{100}, \text{ producing an amplified measure of gifting significance by combining both quantity and monetary value.}

# Columns used

* [interactions](/tables/interactions.md): `gifttot`, `giftvalusd`

# Depends on

* [interactions.gifttot_interactions.giftvalusd](/knowledge/interactions-gifttot-interactions-giftvalusd.md)

# Used by

* [Gift-Focused Supporter](/knowledge/gift-focused-supporter.md)
