---
type: Calculation
title: Compliance Overhead Ratio (COR)
description: Measures the operational burden of compliance relative to data subject request load.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 51
---

# Definition

COR = \text{DSRP} / (\text{CostUSD} + 1)

# Columns used

* [riskmanagement](/tables/riskmanagement.md): `costusd`

# Depends on

* [Data Subject Request Pressure (DSRP)](/knowledge/data-subject-request-pressure.md)

# Used by

* [Audit-Stressed Data Flow](/knowledge/audit-stressed-data-flow.md)
