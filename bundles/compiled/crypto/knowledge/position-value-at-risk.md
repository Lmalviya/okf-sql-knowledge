---
type: Calculation
title: Position Value at Risk (PVaR)
description: Calculates the value at risk for a position based on current market conditions.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 2
---

# Definition

PVaR = possum \times volmeter \times 0.01, \text{where } possum \text{ is the notional value of position and } volmeter \text{ is the volatility or fluctuation rating.}

# Columns used

* [marketstats](/tables/marketstats.md): `volmeter`

# Used by

* [Realized Risk Ratio (RRR)](/knowledge/realized-risk-ratio.md)
* [Risk-Adjusted Return](/knowledge/risk-adjusted-return.md)
