---
type: Calculation
title: Slippage Impact
description: Calculates the expected price slippage impact for a given order size.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 1
---

# Definition

Slippage Impact = \frac{dealcount}{bidunits \text{ or } askunits} \times spreadband, \text{where } dealcount \text{ is the order quantity, } bidunits/askunits \text{ is the quantity available at best bid/ask, and } spreadband \text{ is the raw spread.}

# Columns used

* [orders](/tables/orders.md): `dealcount`

# Used by

* [Market Efficiency Ratio (MER)](/knowledge/market-efficiency-ratio.md)
* [True Cost of Execution](/knowledge/true-cost-of-execution.md)
