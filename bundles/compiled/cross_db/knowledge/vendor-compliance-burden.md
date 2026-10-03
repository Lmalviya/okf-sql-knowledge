---
type: Calculation
title: Vendor Compliance Burden (VCB)
description: Measures the compliance burden of a vendor based on audit findings and security rating.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 32
---

# Definition

VCB = \text{AFS} \times (5 - \text{VendSecRate value})

# Columns used

* [vendormanagement](/tables/vendormanagement.md): `vendsecrate`

# Depends on

* [Audit Finding Severity (AFS)](/knowledge/audit-finding-severity.md)
* [VendorManagement.VendSecRate](/knowledge/vendormanagement-vendsecrate.md)

# Used by

* [Vendor-Driven Risk Flow](/knowledge/vendor-driven-risk-flow.md)
* [Vendor Security Cost Index (VSCI)](/knowledge/vendor-security-cost-index.md)
* [Vendor Compliance Risk Cluster](/knowledge/vendor-compliance-risk-cluster.md)
