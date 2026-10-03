---
type: Business Rule
title: Excessive Retention Risk
description: Highlights data profiles with prolonged retention and high sensitivity.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 62
---

# Definition

A data profile where DRRS > 50 and DSI > 100

# Depends on

* [Data Sensitivity Index (DSI)](/knowledge/data-sensitivity-index.md)
* [Data Retention Risk Score (DRRS)](/knowledge/data-retention-risk-score.md)
