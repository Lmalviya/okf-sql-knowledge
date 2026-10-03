---
type: Calculation
title: Risk-Adjusted Return
description: Calculates return on position adjusted for risk exposure.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 30
---

# Definition

Risk-Adjusted Return = \frac{realline}{PVaR \times posriskrate}, \text{where } realline \text{ is the realized PnL, } PVaR \text{ is the Position Value at Risk, and } posriskrate \text{ is the position risk ratio.}

# Columns used

* [accountbalances](/tables/accountbalances.md): `realline`

# Depends on

* [Position Value at Risk (PVaR)](/knowledge/position-value-at-risk.md)
* [Realized Risk Ratio (RRR)](/knowledge/realized-risk-ratio.md)

# Used by

* [Risk-Efficient Position](/knowledge/risk-efficient-position.md)
