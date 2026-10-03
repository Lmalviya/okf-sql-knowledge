---
type: Value Illustration
title: DataFlow.SuccessPct
description: Illustrates the success rate of data transfers.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 20
---

# Definition

Ranges from 0 to 100%. A SuccessPct of 95% indicates reliable transfers, while <80% suggests frequent failures, from DataFlow.

# Columns used

* [dataflow](/tables/dataflow.md): `successpct`

# Used by

* [Data Flow Stability Index (DFSI)](/knowledge/data-flow-stability-index.md)
