---
type: Calculation
title: Effective Leverage
description: Calculates the actual leverage considering both explicit leverage setting and position size relative to account balance.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 33
---

# Definition

Effective Leverage = posmagn \times \frac{possum}{walletsum}, \text{where } posmagn \text{ is the position leverage, } possum \text{ is the notional value of position, and } walletsum \text{ is the total wallet balance.}

# Columns used

* [accountbalances](/tables/accountbalances.md): `walletsum`

# Used by

* [Critically Over-Leveraged Position](/knowledge/critically-over-leveraged-position.md)
* [Effective Leverage Risk Classification](/knowledge/effective-leverage-risk-classification.md)
