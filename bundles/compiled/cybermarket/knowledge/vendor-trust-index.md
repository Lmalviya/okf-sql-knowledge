---
type: Calculation
title: Vendor Trust Index (VTI)
description: Measures vendor reliability based on transaction history
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 11
---

# Definition

VTI = \frac{vendsucccount}{vendtxcount} \times 100 - \frac{venddisputecount}{vendtxcount} \times 50 + (vendrate \times 5), \text{where higher scores indicate more trustworthy vendors.}

# Columns used

* [vendors](/tables/vendors.md): `vendrate`, `vendtxcount`, `vendsucccount`, `venddisputecount`

# Used by

* [Trusted Vendor](/knowledge/trusted-vendor.md)
* [Vendor Network Centrality (VNC)](/knowledge/vendor-network-centrality.md)
