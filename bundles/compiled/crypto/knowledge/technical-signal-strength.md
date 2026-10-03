---
type: Calculation
title: Technical Signal Strength
description: Quantifies the strength of technical signals based on multiple indicators.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 39
---

# Definition

Technical Signal Strength = \frac{|rsi14spot - 50| + |macdtrail| + (bbandspan \times 0.01)}{3} \times (techmeter == 'Buy' ? 1 : techmeter == 'Sell' ? -1 : 0), \text{where } rsi14spot \text{ is the RSI indicator, } macdtrail \text{ is the MACD line, } bbandspan \text{ is the Bollinger Band width, and } techmeter \text{ determines direction (Buy, Sell, Hold).}

# Depends on

* [Momentum Divergence](/knowledge/momentum-divergence.md)
* [techmeter](/knowledge/techmeter.md)

# Used by

* [Technical Reversal Signal](/knowledge/technical-reversal-signal.md)
* [Perfect Technical Setup](/knowledge/perfect-technical-setup.md)
