---
type: Business Rule
title: Diversified Marketplace
description: Identifies markets with exceptional product and vendor diversity
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 45
---

# Definition

A market with MDS > 65, at least 15 distinct product categories (COUNT(DISTINCT prodsubcat) >= 15), high vendor count (vendcount > 200), and 'Marketplace' classification (mktclass = 'Marketplace') as defined in the market classification system. These markets typically present challenging enforcement targets due to their diversified nature.

# Columns used

* [markets](/tables/markets.md): `mktclass`, `vendcount`
* [products](/tables/products.md): `prodsubcat`

# Depends on

* [cybermarket|markets|mktclass](/knowledge/cybermarket-markets-mktclass.md)
* [Market Diversification Score (MDS)](/knowledge/market-diversification-score.md)
