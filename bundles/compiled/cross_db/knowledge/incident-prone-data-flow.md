---
type: Business Rule
title: Incident-Prone Data Flow
description: Flags data flows with poor incident resolution and high risk.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 49
---

# Definition

A data flow where IRE < 0.5 and High-Risk Data Flow

# Depends on

* [High-Risk Data Flow](/knowledge/high-risk-data-flow.md)
* [Data Flow Reliability Score (DFRS)](/knowledge/data-flow-reliability-score.md)
