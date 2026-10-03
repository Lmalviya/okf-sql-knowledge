---
type: Business Rule
title: Non-Compliant Vendor
description: Identifies vendors failing compliance standards.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 12
---

# Definition

A vendor where PolComp = 'Non-compliant' or ProcComp = 'Non-compliant'

# Columns used

* [vendormanagement](/tables/vendormanagement.md): `polcomp`, `proccomp`
