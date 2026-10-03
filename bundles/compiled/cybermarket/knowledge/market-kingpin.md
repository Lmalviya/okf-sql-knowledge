---
type: Business Rule
title: Market Kingpin
description: Identifies vendors with exceptional influence and reach across multiple markets
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 41
---

# Definition

A vendor with VNC > 85, operating on at least 3 different markets (COUNT(DISTINCT mktref) >= 3), with 'Premium' verification level (vendchecklvl = 'Premium'), and displaying the characteristics of a Trusted Vendor. These operators represent significant intelligence targets due to their wide-reaching influence.

# Columns used

* [vendors](/tables/vendors.md): `vendchecklvl`, `mktref`
* [buyers](/tables/buyers.md): `mktref`
* [transactions](/tables/transactions.md): `mktref`

# Depends on

* [cybermarket|vendors|vendchecklvl](/knowledge/cybermarket-vendors-vendchecklvl.md)
* [Trusted Vendor](/knowledge/trusted-vendor.md)
* [Vendor Network Centrality (VNC)](/knowledge/vendor-network-centrality.md)
