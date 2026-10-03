---
type: Business Rule
title: Cross-Border Audit Risk
description: Flags cross-border data flows with significant audit issues.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 44
---

# Definition

A data flow where CDVR > 1000 and AFS > 0.5

# Depends on

* [Audit Finding Severity (AFS)](/knowledge/audit-finding-severity.md)
* [Cross-Border Data Volume Risk (CDVR)](/knowledge/cross-border-data-volume-risk.md)
