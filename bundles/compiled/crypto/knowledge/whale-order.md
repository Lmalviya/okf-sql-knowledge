---
type: Business Rule
title: Whale Order
description: Identifies large orders that could significantly impact market prices.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 10
---

# Definition

An order where the dealcount exceeds 10% of the available liquidity (bidunits or askunits) at the current best bid or ask price.

# Columns used

* [orders](/tables/orders.md): `dealcount`

# Used by

* [Whale-Driven Market](/knowledge/whale-driven-market.md)
