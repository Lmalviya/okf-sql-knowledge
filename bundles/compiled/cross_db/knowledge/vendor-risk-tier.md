---
type: Business Rule
title: Vendor Risk Tier
description: Categorizes vendors into risk tiers based on security and compliance.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 16
---

# Definition

A vendor is: High Risk if VRI < 2, Medium Risk if 2 ≤ VRI < 3, Low Risk if VRI ≥ 3

# Depends on

* [Vendor Reliability Index (VRI)](/knowledge/vendor-reliability-index.md)
