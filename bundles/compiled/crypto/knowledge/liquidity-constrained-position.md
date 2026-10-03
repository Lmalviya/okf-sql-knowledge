---
type: Business Rule
title: Liquidity Constrained Position
description: Identifies positions that may be difficult to exit due to insufficient market liquidity.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 43
---

# Definition

A position where the Market Depth Ratio is less than 2.0, indicating that the position size is large relative to available market depth, potentially leading to significant slippage upon exit.

# Depends on

* [Market Depth Ratio](/knowledge/market-depth-ratio.md)
