---
type: Business Rule
title: Sensitive Unstable Flow
description: Flags sensitive data flows with stability issues.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 68
---

# Definition

A data flow where DFSI < 0.5 and Sensitive Data Exposure exists

# Depends on

* [Sensitive Data Exposure](/knowledge/sensitive-data-exposure.md)
* [Data Flow Stability Index (DFSI)](/knowledge/data-flow-stability-index.md)
