---
type: Calculation
title: Profit Factor
description: Measures the ratio of profitable trades to losing trades adjusted for their values.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 34
---

# Definition

Profit Factor = \frac{\sum positive\ realline}{|\sum negative\ realline|}, \text{where } realline \text{ is the realized PnL, calculated separately for positive and negative values.}

# Columns used

* [accountbalances](/tables/accountbalances.md): `realline`

# Depends on

* [Realized Risk Ratio (RRR)](/knowledge/realized-risk-ratio.md)
