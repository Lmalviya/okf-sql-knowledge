---
type: Business Rule
title: Regulatory Risk Exposure
description: Identifies data flows with high regulatory risk due to compliance gaps and cross-border transfers.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 19
---

# Definition

A data flow with CBRF > 1.5 and Cross-Border Compliance Gap exists

# Depends on

* [Cross-Border Risk Factor (CBRF)](/knowledge/cross-border-risk-factor.md)
* [Cross-Border Compliance Gap](/knowledge/cross-border-compliance-gap.md)

# Used by

* [Regulatory Overload Flow](/knowledge/regulatory-overload-flow.md)
* [High-Impact Audit Risk Flow](/knowledge/high-impact-audit-risk-flow.md)
