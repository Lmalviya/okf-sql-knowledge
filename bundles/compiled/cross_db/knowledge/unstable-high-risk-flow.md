---
type: Business Rule
title: Unstable High-Risk Flow
description: Identifies high-risk data flows with poor stability.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 60
---

# Definition

A data flow where DFSI < 0.5 and Critical Data Flow Risk exists

# Depends on

* [Critical Data Flow Risk](/knowledge/critical-data-flow-risk.md)
* [Data Flow Stability Index (DFSI)](/knowledge/data-flow-stability-index.md)
