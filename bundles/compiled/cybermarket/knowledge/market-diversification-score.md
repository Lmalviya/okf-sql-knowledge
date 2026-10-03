---
type: Calculation
title: Market Diversification Score (MDS)
description: Evaluates the diversity of products and vendors within a market
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 35
---

# Definition

MDS = \frac{COUNT(DISTINCT prodsubcat)}{5} + \frac{vendcount}{50} + \frac{COUNT(txregistry)}{vendcount} \times 0.5 - \frac{mktclass\_weight}{10}, \text{where mktclass\_weight assigns Forum=1, Service=2, Marketplace=4, Exchange=3 as per the market classification system defined in cybermarket|markets|mktclass, and higher scores represent greater market diversification.}

# Columns used

* [markets](/tables/markets.md): `mktclass`, `vendcount`
* [products](/tables/products.md): `prodsubcat`
* [transactions](/tables/transactions.md): `txregistry`

# Depends on

* [cybermarket|markets|mktclass](/knowledge/cybermarket-markets-mktclass.md)

# Used by

* [Diversified Marketplace](/knowledge/diversified-marketplace.md)
