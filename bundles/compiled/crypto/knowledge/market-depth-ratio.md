---
type: Calculation
title: Market Depth Ratio
description: Measures the ratio of order book depth to position size to assess market liquidity for position exit.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 36
---

# Definition

Market Depth Ratio = \frac{biddepth \text{ or } askdepth}{dealcount} \times Liquidity Ratio, \text{where } biddepth/askdepth \text{ is used depending on position direction (posedge), } dealcount \text{ is the order quantity, and } Liquidity Ratio \text{ measures available liquidity to total market volume.}

# Columns used

* [orders](/tables/orders.md): `dealcount`

# Depends on

* [Liquidity Ratio](/knowledge/liquidity-ratio.md)
* [Order Fill Rate](/knowledge/order-fill-rate.md)

# Used by

* [Liquidity Constrained Position](/knowledge/liquidity-constrained-position.md)
