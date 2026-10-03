---
type: Business Rule
title: Vendor-Driven Risk Flow
description: Identifies data flows with elevated risk due to vendor issues.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 43
---

# Definition

A data flow where VRA > 3 and VCB > 2

# Depends on

* [Vendor Compliance Burden (VCB)](/knowledge/vendor-compliance-burden.md)
* [Vendor Risk Amplification (VRA)](/knowledge/vendor-risk-amplification.md)
