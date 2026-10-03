---
type: Business Rule
title: High Audit Compliance Pressure
description: Identifies data flows with elevated audit compliance pressure based on audit findings and data subject request load.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 74
---

# Definition

A data flow where ACP > 5

# Depends on

* [Audit Compliance Pressure (ACP)](/knowledge/audit-compliance-pressure.md)
