---
type: Calculation
title: Data Retention Risk Score (DRRS)
description: Evaluates risk from prolonged data retention relative to sensitivity.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 56
---

# Definition

DRRS = \text{DSI} \times \frac{\text{RetDays}}{365}

# Columns used

* [dataprofile](/tables/dataprofile.md): `retdays`

# Depends on

* [Data Sensitivity Index (DSI)](/knowledge/data-sensitivity-index.md)

# Used by

* [Excessive Retention Risk](/knowledge/excessive-retention-risk.md)
