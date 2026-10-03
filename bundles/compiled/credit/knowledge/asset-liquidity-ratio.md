---
type: Calculation
title: Asset Liquidity Ratio (ALR)
description: Measures the proportion of customer assets that can be quickly converted to cash.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 35
---

# Definition

ALR = \frac{liqassets}{totassets} = \frac{liqassets}{Net Worth + totliabs}, \text{where Net Worth is the difference between assets and liabilities}

# Columns used

* [expenses_and_assets](/tables/expenses_and_assets.md): `liqassets`, `totassets`, `totliabs`

# Depends on

* [Net Worth](/knowledge/net-worth.md)

# Used by

* [Investment Services Target](/knowledge/investment-services-target.md)
