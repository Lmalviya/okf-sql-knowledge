---
type: Calculation
title: Data Transfer Efficiency (DTE)
description: Measures the efficiency of data transfers based on success rate and error count.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 0
---

# Definition

DTE = \frac{\text{SuccessPct}}{\text{ErrTally} + 1}

# Columns used

* [dataflow](/tables/dataflow.md): `successpct`, `errtally`

# Used by

* [Overloaded Data Flow](/knowledge/overloaded-data-flow.md)
* [Data Flow Reliability Score (DFRS)](/knowledge/data-flow-reliability-score.md)
