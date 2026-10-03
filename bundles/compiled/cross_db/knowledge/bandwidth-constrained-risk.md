---
type: Business Rule
title: Bandwidth-Constrained Risk
description: Identifies data flows where bandwidth saturation amplifies risk.
tags:
- cross_db
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:56+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cross_db/cross_db_kb.jsonl
  title: cross_db business rules (LiveSQLBench), rule 47
---

# Definition

A data flow where BRF > 100 and RES > 0.7

# Depends on

* [Risk Exposure Score (RES)](/knowledge/risk-exposure-score.md)
* [Bandwidth Risk Factor (BRF)](/knowledge/bandwidth-risk-factor.md)
