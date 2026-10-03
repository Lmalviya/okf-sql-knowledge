---
type: Business Rule
title: Overburdened Compliance Flow
description: Flags data flows with high compliance costs and audit remediation needs.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 40
---

# Definition

A data flow where CCR > 0.8 and ARL > 10

# Depends on

* [Compliance Cost Ratio (CCR)](/knowledge/compliance-cost-ratio.md)
* [Audit Remediation Load (ARL)](/knowledge/audit-remediation-load.md)
