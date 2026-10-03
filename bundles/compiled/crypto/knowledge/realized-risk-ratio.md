---
type: Calculation
title: Realized Risk Ratio (RRR)
description: Calculates the ratio of realized PnL to position value at risk.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 6
---

# Definition

RRR = \frac{realline}{PVaR}, \text{where } realline \text{ is the realized PnL and } PVaR \text{ is the Position Value at Risk.}

# Columns used

* [accountbalances](/tables/accountbalances.md): `realline`

# Depends on

* [Position Value at Risk (PVaR)](/knowledge/position-value-at-risk.md)

# Used by

* [Risk-Adjusted Return](/knowledge/risk-adjusted-return.md)
* [Profit Factor](/knowledge/profit-factor.md)
