---
type: Calculation
title: Order Book Imbalance Ratio
description: Quantifies the imbalance between bid and ask sides of the order book.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 32
---

# Definition

Order Book Imbalance Ratio = \frac{biddepth - askdepth}{biddepth + askdepth}, \text{where } biddepth \text{ is the deeper bid liquidity and } askdepth \text{ is the deeper ask liquidity. A positive Imbalance Ratio indicates stronger buying pressure, while negative indicates stronger selling pressure.

# Depends on

* [Liquidity Ratio](/knowledge/liquidity-ratio.md)

# Used by

* [Liquidation Cascade Risk](/knowledge/liquidation-cascade-risk.md)
