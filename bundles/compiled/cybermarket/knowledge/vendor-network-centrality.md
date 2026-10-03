---
type: Calculation
title: Vendor Network Centrality (VNC)
description: Measures a vendor's connectedness within the market ecosystem
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 31
---

# Definition

VNC = (COUNT(DISTINCT mktref) \times 5) + \frac{vendtxcount}{50} + (VTI \times 0.1) - (1 - sizecluster_numeric) \times 10, \text{where sizecluster_numeric maps Small=1, Medium=2, Large=3, Mega=4 as described in the market size classification, and higher scores indicate more central market positioning.}

# Columns used

* [vendors](/tables/vendors.md): `vendtxcount`, `mktref`
* [buyers](/tables/buyers.md): `mktref`
* [transactions](/tables/transactions.md): `mktref`

# Depends on

* [cybermarket|markets|sizecluster](/knowledge/cybermarket-markets-sizecluster.md)
* [Vendor Trust Index (VTI)](/knowledge/vendor-trust-index.md)

# Used by

* [Market Kingpin](/knowledge/market-kingpin.md)
