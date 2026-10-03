---
type: Business Rule
title: Vendor Compliance Risk Cluster
description: Identifies vendors contributing to concentrated compliance risks.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 63
---

# Definition

A vendor where VRC > 2 and VCB > 2

# Depends on

* [Vendor Compliance Burden (VCB)](/knowledge/vendor-compliance-burden.md)
* [Vendor Risk Concentration (VRC)](/knowledge/vendor-risk-concentration.md)
