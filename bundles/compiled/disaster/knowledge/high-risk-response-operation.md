---
type: Business Rule
title: High-Risk Response Operation
description: Identifies disaster operations with elevated risk factors
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 21
---

# Definition

Operations where emerglevel is 'Red' or 'Black' AND safetyranking is 'High Risk' AND secincidentcount > 50, indicating dangerous conditions requiring special safety protocols

# Columns used

* [operations](/tables/operations.md): `emerglevel`
* [coordinationandevaluation](/tables/coordinationandevaluation.md): `secincidentcount`, `safetyranking`

# Depends on

* [emerglevel](/knowledge/emerglevel.md)
