---
type: Business Rule
title: Costly Vendor Risk Flow
description: Identifies data flows with high vendor-related costs and risks.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 67
---

# Definition

A data flow where VSCI > 1 and VRA > 3

# Depends on

* [Vendor Risk Amplification (VRA)](/knowledge/vendor-risk-amplification.md)
* [Vendor Security Cost Index (VSCI)](/knowledge/vendor-security-cost-index.md)
