---
type: Business Rule
title: Sensitive Data Exposure
description: Highlights data profiles with high sensitivity and weak security.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 14
---

# Definition

A data profile where DSI > 100 and SRS < 2

# Depends on

* [Data Sensitivity Index (DSI)](/knowledge/data-sensitivity-index.md)
* [Security Robustness Score (SRS)](/knowledge/security-robustness-score.md)

# Used by

* [Sensitive Unstable Flow](/knowledge/sensitive-unstable-flow.md)
