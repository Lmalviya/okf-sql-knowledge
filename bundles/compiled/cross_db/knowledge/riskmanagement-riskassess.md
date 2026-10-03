---
type: Value Illustration
title: RiskManagement.RiskAssess
description: Illustrates the risk assessment score.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 21
---

# Definition

Ranges from 0 to 100. A RiskAssess > 80 indicates high risk, while <20 suggests minimal risk, from RiskManagement.

# Columns used

* [riskmanagement](/tables/riskmanagement.md): `riskassess`
