---
type: Calculation
title: Data Flow Reliability Score (DFRS)
description: Quantifies the reliability of a data flow based on success rate and retry attempts.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 30
---

# Definition

DFRS = \text{DTE} \times (1 - \text{RtryTally} / (\text{ErrTally} + 1))

# Columns used

* [dataflow](/tables/dataflow.md): `errtally`, `rtrytally`

# Depends on

* [Data Transfer Efficiency (DTE)](/knowledge/data-transfer-efficiency.md)
* [DataFlow.ErrTally](/knowledge/dataflow-errtally.md)

# Used by

* [Critical Data Flow Risk](/knowledge/critical-data-flow-risk.md)
* [Incident-Prone Data Flow](/knowledge/incident-prone-data-flow.md)
* [Data Flow Stability Index (DFSI)](/knowledge/data-flow-stability-index.md)
