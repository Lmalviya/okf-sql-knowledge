---
type: Business Rule
title: High-Pressure Data Flow
description: Highlights data flows under strain from data subject requests and bandwidth saturation.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 42
---

# Definition

A data flow where DSRP > 50 and BSI > 50

# Depends on

* [Bandwidth Saturation Index (BSI)](/knowledge/bandwidth-saturation-index.md)
* [Data Subject Request Pressure (DSRP)](/knowledge/data-subject-request-pressure.md)
