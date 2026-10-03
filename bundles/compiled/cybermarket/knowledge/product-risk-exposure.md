---
type: Calculation
title: Product Risk Exposure (PRE)
description: Quantifies the regulatory exposure risk associated with product listings
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 32
---

# Definition

PRE = prodtheme_weight + (escrowused_numeric \times 10) - \frac{escrowhrs}{24} + \frac{payamtusd}{500}, \text{where prodtheme_weight assigns Digital=10, Data=20, Service=30, Physical=50 based on the product theme classification, and escrowused_numeric is 0 if escrow is used and 1 if not.}

# Columns used

* [transactions](/tables/transactions.md): `payamtusd`, `escrowhrs`

# Depends on

* [cybermarket|products|prodtheme](/knowledge/cybermarket-products-prodtheme.md)

# Used by

* [High-Exposure Product](/knowledge/high-exposure-product.md)
