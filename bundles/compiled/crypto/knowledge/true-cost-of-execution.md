---
type: Calculation
title: True Cost of Execution
description: Calculates the total cost of order execution including fees and slippage.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 31
---

# Definition

True Cost of Execution = feetotal + (dealcount \times dealquote \times Slippage Impact \times 0.01), \text{where } feetotal \text{ is the total fee charged and } Slippage Impact \text{ is the expected price slippage impact for the order size.}

# Columns used

* [orders](/tables/orders.md): `dealquote`, `dealcount`
* [fees](/tables/fees.md): `feetotal`

# Depends on

* [Slippage Impact](/knowledge/slippage-impact.md)

# Used by

* [Arbitrage ROI](/knowledge/arbitrage-roi.md)
