---
type: Business Rule
title: Customer Loyalty Network
description: Identifies vendor-customer networks with unusual loyalty patterns
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 47
---

# Definition

A network centered on a vendor with VRS > 90, having repeated transactions with the same buyers (> 5 transactions per buyer), receiving exceptionally high ratings (vendrate > 4.8), and 'Advanced' or 'Premium' verification level as defined in the vendor verification system. These networks often indicate established trust circles warranting deeper investigation.

# Columns used

* [vendors](/tables/vendors.md): `vendrate`

# Depends on

* [cybermarket|vendors|vendchecklvl](/knowledge/cybermarket-vendors-vendchecklvl.md)
* [Vendor Relationship Strength (VRS)](/knowledge/vendor-relationship-strength.md)
