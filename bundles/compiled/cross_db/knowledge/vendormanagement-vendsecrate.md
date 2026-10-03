---
type: Value Illustration
title: VendorManagement.VendSecRate
description: Illustrates the vendor security rating.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 24
---

# Definition

Enum: 'A' = 4, 'B' = 3, 'C' = 2, 'D' or others = 1. This numeric scale quantifies vendor security, where 'A' reflects top-tier security (score 4), and lower ratings (down to 'D') indicate progressively weaker security controls.

# Columns used

* [vendormanagement](/tables/vendormanagement.md): `vendsecrate`

# Used by

* [Vendor Compliance Burden (VCB)](/knowledge/vendor-compliance-burden.md)
