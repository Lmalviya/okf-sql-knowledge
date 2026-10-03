---
type: Business Rule
title: Optimal Trading Window
description: Identifies periods with ideal conditions for order execution.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 44
---

# Definition

Market conditions where the Volatility-Adjusted Spread is less than 1.0 and the Market Maker Activity indicates 'High', suggesting tight spreads relative to volatility and strong liquidity provision.

# Depends on

* [Market Maker Activity](/knowledge/market-maker-activity.md)
* [Volatility-Adjusted Spread](/knowledge/volatility-adjusted-spread.md)
