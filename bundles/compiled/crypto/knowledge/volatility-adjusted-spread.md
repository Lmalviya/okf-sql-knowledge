---
type: Calculation
title: Volatility-Adjusted Spread
description: Normalizes the spread by the market volatility to determine if spread is wide relative to expected price movement.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 37
---

# Definition

Volatility-Adjusted Spread = \frac{Spread Percentage}{volmeter \times 0.1}, \text{where } Spread Percentage \text{ is the spread as percentage of midpoint price and } volmeter \text{ is the volatility or fluctuation rating.}

# Columns used

* [marketstats](/tables/marketstats.md): `volmeter`

# Depends on

* [Spread Percentage](/knowledge/spread-percentage.md)

# Used by

* [Optimal Trading Window](/knowledge/optimal-trading-window.md)
