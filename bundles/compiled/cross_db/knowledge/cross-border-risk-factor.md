---
type: Calculation
title: Cross-Border Risk Factor (CBRF)
description: Evaluates risk associated with cross-border data transfers.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 9
---

# Definition

CBRF = \text{RES} \times \begin{cases} 2 & \text{if OrigNation \neq DestNation} \\ 1 & \text{otherwise} \end{cases}

# Columns used

* [dataflow](/tables/dataflow.md): `orignation`, `destnation`

# Depends on

* [Risk Exposure Score (RES)](/knowledge/risk-exposure-score.md)

# Used by

* [Regulatory Risk Exposure](/knowledge/regulatory-risk-exposure.md)
* [Cross-Border Data Volume Risk (CDVR)](/knowledge/cross-border-data-volume-risk.md)
