---
type: Calculation
title: Spread Percentage
description: Calculates the spread as a percentage of the midpoint price.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 0
---

# Definition

Spread Percentage = \frac{askquote - bidquote}{midquote} \times 100, \text{where } askquote \text{ is the best ask price, } bidquote \text{ is the best bid price, and } midquote \text{ is the midpoint price.}

# Used by

* [Volatility-Adjusted Spread](/knowledge/volatility-adjusted-spread.md)
