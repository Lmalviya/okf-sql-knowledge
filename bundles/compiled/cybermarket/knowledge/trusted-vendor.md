---
type: Business Rule
title: Trusted Vendor
description: Identifies vendors with established positive reputation
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 21
---

# Definition

A vendor with VTI > 80, vendchecklvl of 'Advanced' or 'Premium', a dispute rate below 5% of total transactions, and an active history exceeding 90 days. These vendors represent stabilizing forces within markets and typically pose lower immediate enforcement priorities.

# Columns used

* [vendors](/tables/vendors.md): `vendchecklvl`

# Depends on

* [cybermarket|vendors|vendchecklvl](/knowledge/cybermarket-vendors-vendchecklvl.md)
* [Vendor Trust Index (VTI)](/knowledge/vendor-trust-index.md)

# Used by

* [Market Kingpin](/knowledge/market-kingpin.md)
