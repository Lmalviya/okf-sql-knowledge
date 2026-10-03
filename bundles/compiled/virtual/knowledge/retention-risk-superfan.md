---
type: Business Rule
title: Retention Risk Superfan
description: Identifies high-value fans showing early warning signs of potential churn
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 44
---

# Definition

A fan with tierstep ≥ 8, FEI > 0.7, and MV > 200, but also showing RRF > 2.0, representing significant value at risk of being lost.

# Columns used

* [fans](/tables/fans.md): `tierstep`

# Depends on

* [Retention Risk Factor (RRF)](/knowledge/retention-risk-factor.md)
* [Superfan](/knowledge/superfan.md)
