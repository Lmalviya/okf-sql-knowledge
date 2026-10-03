---
type: Business Rule
title: High-Exposure Product
description: Identifies products with elevated regulatory risk factors
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 42
---

# Definition

A product with PRE > 60, in the 'Physical' theme category as defined in the product theme classification, without escrow protection (escrowused = 'No'), and transacted with privacy-focused cryptocurrency (paymethod = 'Crypto_B'). These products require immediate monitoring due to their heightened risk profile.

# Columns used

* [transactions](/tables/transactions.md): `paymethod`, `escrowused`

# Depends on

* [cybermarket|transactions|paymethod](/knowledge/cybermarket-transactions-paymethod.md)
* [cybermarket|products|prodtheme](/knowledge/cybermarket-products-prodtheme.md)
* [Product Risk Exposure (PRE)](/knowledge/product-risk-exposure.md)
