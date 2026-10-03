---
type: Business Rule
title: Smart Money Flow
description: Identifies directional bias of sophisticated traders.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 15
---

# Definition

Market conditions where smartforce exceeds both retailflow and instflow by at least 20%, indicating strong directional bias from sophisticated traders.

# Used by

* [Whale-Driven Market](/knowledge/whale-driven-market.md)
* [Smart Money Accuracy](/knowledge/smart-money-accuracy.md)
