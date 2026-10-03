---
type: Calculation
title: Order Fill Rate
description: Calculates the percentage of an order that has been filled.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 8
---

# Definition

Order Fill Rate = \frac{dealcount - remaincount}{dealcount} \times 100, \text{where } dealcount \text{ is the order quantity and } remaincount \text{ is how many units remain unfilled.}

# Columns used

* [orders](/tables/orders.md): `dealcount`
* [orderexecutions](/tables/orderexecutions.md): `remaincount`

# Used by

* [Market Depth Ratio](/knowledge/market-depth-ratio.md)
