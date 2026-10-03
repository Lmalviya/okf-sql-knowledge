---
type: Business Rule
title: Liquidation Risk Level
description: Categorizes positions based on their proximity to liquidation.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 11
---

# Definition

Positions are categorized as 'Safe', 'Moderate', or 'High Risk' based on how close the current market price is to the liqquote (liquidation price). A position is 'High Risk' when market price is within 5% of liqquote.

# Used by

* [Liquidation Cascade Risk](/knowledge/liquidation-cascade-risk.md)
