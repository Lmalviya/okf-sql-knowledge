---
type: Calculation
title: Liquidity Ratio
description: Measures the ratio of available liquidity to total market volume.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 5
---

# Definition

Liquidity Ratio = \frac{(bidunits + askunits) \times midquote}{volday}, \text{where } bidunits \text{ and } askunits \text{ are quantities at best bid and ask, } midquote \text{ is the midpoint price, and } volday \text{ is the 24h volume.}

# Columns used

* [marketstats](/tables/marketstats.md): `volday`

# Used by

* [Liquidity Crisis](/knowledge/liquidity-crisis.md)
* [Order Book Imbalance Ratio](/knowledge/order-book-imbalance-ratio.md)
* [Market Depth Ratio](/knowledge/market-depth-ratio.md)
