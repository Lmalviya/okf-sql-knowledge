---
type: Business Rule
title: Overloaded Data Flow
description: Flags data flows with high bandwidth saturation and low efficiency.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 18
---

# Definition

A data flow where BSI > 50 and DTE < 1.0

# Depends on

* [Data Transfer Efficiency (DTE)](/knowledge/data-transfer-efficiency.md)
* [Bandwidth Saturation Index (BSI)](/knowledge/bandwidth-saturation-index.md)
