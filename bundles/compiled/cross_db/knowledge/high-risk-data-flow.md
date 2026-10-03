---
type: Business Rule
title: High-Risk Data Flow
description: Identifies data flows with elevated risk based on risk exposure and sensitivity.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 10
---

# Definition

A data flow where RES > 0.7 and DSI > 100

# Depends on

* [Risk Exposure Score (RES)](/knowledge/risk-exposure-score.md)
* [Data Sensitivity Index (DSI)](/knowledge/data-sensitivity-index.md)

# Used by

* [Incident-Prone Data Flow](/knowledge/incident-prone-data-flow.md)
