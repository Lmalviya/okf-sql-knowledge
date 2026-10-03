---
type: Calculation
title: Data Sensitivity Index (DSI)
description: Quantifies the sensitivity of data based on volume and sensitivity level.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 4
---

# Definition

DSI = \text{VolGB} \times \begin{cases} 3 & \text{if DataSense = 'High'} \\ 2 & \text{if DataSense = 'Medium'} \\ 1 & \text{if DataSense = 'Low'} \end{cases}

# Columns used

* [dataprofile](/tables/dataprofile.md): `datasense`, `volgb`

# Used by

* [High-Risk Data Flow](/knowledge/high-risk-data-flow.md)
* [Sensitive Data Exposure](/knowledge/sensitive-data-exposure.md)
* [Encryption Coverage Ratio (ECR)](/knowledge/encryption-coverage-ratio.md)
* [Bandwidth Risk Factor (BRF)](/knowledge/bandwidth-risk-factor.md)
* [Unprotected Sensitive Data](/knowledge/unprotected-sensitive-data.md)
* [Data Retention Risk Score (DRRS)](/knowledge/data-retention-risk-score.md)
* [Excessive Retention Risk](/knowledge/excessive-retention-risk.md)
