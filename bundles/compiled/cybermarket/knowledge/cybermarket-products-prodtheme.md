---
type: Value Illustration
title: cybermarket|products|prodtheme
description: Clarifies product theme classifications and their enforcement implications
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 4
---

# Definition

'Digital' products include software, account credentials, and virtual goods requiring no physical shipping; 'Data' encompasses information packages like databases, personal information, and intellectual property; 'Service' refers to activities rather than tangible products, including hacking, documentation, or technical assistance; 'Physical' indicates tangible goods requiring actual shipment through delivery networks, representing the highest exposure risk category.

# Columns used

* [products](/tables/products.md): `prodtheme`

# Used by

* [Product Risk Exposure (PRE)](/knowledge/product-risk-exposure.md)
* [High-Exposure Product](/knowledge/high-exposure-product.md)
