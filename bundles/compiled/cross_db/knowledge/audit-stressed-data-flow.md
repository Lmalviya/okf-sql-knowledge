---
type: Business Rule
title: Audit-Stressed Data Flow
description: Identifies data flows under pressure from audit findings and compliance burdens.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 65
---

# Definition

A data flow where ACP > 5 and COR > 0.5.

# Depends on

* [Compliance Overhead Ratio (COR)](/knowledge/compliance-overhead-ratio.md)
* [Audit Compliance Pressure (ACP)](/knowledge/audit-compliance-pressure.md)
