---
type: Calculation
title: Vendor Relationship Strength (VRS)
description: Measures the strength of relationships between a vendor and their customers
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 37
---

# Definition

VRS = (vendrate \times 10) + \frac{vendsucccount}{vendtxcount} \times 50 + (vendchecklvl_numeric \times 15) - \frac{venddisputecount}{vendtxcount} \times 100, \text{where vendchecklvl_numeric maps Basic=1, Advanced=2, Premium=3, else=0 according to the vendor verification system, and higher scores represent stronger vendor-customer relationships.}

# Columns used

* [vendors](/tables/vendors.md): `vendrate`, `vendtxcount`, `vendsucccount`, `venddisputecount`

# Depends on

* [cybermarket|vendors|vendchecklvl](/knowledge/cybermarket-vendors-vendchecklvl.md)

# Used by

* [Customer Loyalty Network](/knowledge/customer-loyalty-network.md)
