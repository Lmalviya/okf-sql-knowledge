---
type: Value Illustration
title: DataFlow.ErrTally
description: Illustrates the count of errors in data transfers.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 27
---

# Definition

Integer ≥ 0. An ErrTally of 0 indicates flawless transfers, while >10 suggests reliability issues, from DataFlow.

# Columns used

* [dataflow](/tables/dataflow.md): `errtally`

# Used by

* [Data Flow Reliability Score (DFRS)](/knowledge/data-flow-reliability-score.md)
* [Data Flow Stability Index (DFSI)](/knowledge/data-flow-stability-index.md)
