---
type: Business Rule
title: Critical Data Flow Risk
description: Identifies data flows with both high risk exposure and poor reliability.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 39
---

# Definition

A data flow where RES > 0.7 and DFRS < 0.5

# Depends on

* [Risk Exposure Score (RES)](/knowledge/risk-exposure-score.md)
* [Data Flow Reliability Score (DFRS)](/knowledge/data-flow-reliability-score.md)

# Used by

* [Unstable High-Risk Flow](/knowledge/unstable-high-risk-flow.md)
