---
type: Calculation
title: Data Flow Stability Index (DFSI)
description: Quantifies the stability of data flows by balancing reliability and error recovery.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 50
---

# Definition

DFSI = \text{DFRS} \times \frac{\text{SuccessPct}}{\text{ErrTally} + 1}

# Columns used

* [dataflow](/tables/dataflow.md): `successpct`, `errtally`

# Depends on

* [DataFlow.SuccessPct](/knowledge/dataflow-successpct.md)
* [DataFlow.ErrTally](/knowledge/dataflow-errtally.md)
* [Data Flow Reliability Score (DFRS)](/knowledge/data-flow-reliability-score.md)

# Used by

* [Unstable High-Risk Flow](/knowledge/unstable-high-risk-flow.md)
* [Sensitive Unstable Flow](/knowledge/sensitive-unstable-flow.md)
