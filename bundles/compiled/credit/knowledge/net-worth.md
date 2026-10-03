---
type: Calculation
title: Net Worth
description: Calculates the financial value of a customer by subtracting liabilities from assets.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:54+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 4
---

# Definition

Net Worth = \text{Total Assets} - \text{Total Liabilities} = totassets - totliabs = networth

# Columns used

* [expenses_and_assets](/tables/expenses_and_assets.md): `totassets`, `totliabs`, `networth`

# Used by

* [Asset Liquidity Ratio (ALR)](/knowledge/asset-liquidity-ratio.md)
* [Financial Stress Indicator](/knowledge/financial-stress-indicator.md)
