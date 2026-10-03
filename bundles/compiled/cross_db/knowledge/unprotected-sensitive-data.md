---
type: Business Rule
title: Unprotected Sensitive Data
description: Identifies sensitive data lacking adequate encryption coverage.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 41
---

# Definition

A data profile where DSI > 100 and ECR < 2

# Depends on

* [Data Sensitivity Index (DSI)](/knowledge/data-sensitivity-index.md)
* [Encryption Coverage Ratio (ECR)](/knowledge/encryption-coverage-ratio.md)
