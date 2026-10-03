---
type: Calculation
title: Market Stability Index (MSI)
description: Measures the operational stability of a market
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 15
---

# Definition

MSI = \frac{mktspan}{365} \times \frac{esccomprate}{100} \times \left(1 - \frac{\sum venddisputecount}{\sum vendtxcount} \right) \times 100, \text{where higher scores indicate more stable markets less likely to disappear suddenly.}

# Columns used

* [markets](/tables/markets.md): `mktspan`, `esccomprate`
* [vendors](/tables/vendors.md): `vendtxcount`, `venddisputecount`

# Used by

* [Market Vulnerability Index (MVI)](/knowledge/market-vulnerability-index.md)
* [Unstable Market](/knowledge/unstable-market.md)
