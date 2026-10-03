---
type: Business Rule
title: Cross-Agency Coordination Crisis
description: Identifies critical failures in multi-agency coordination
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 47
---

# Definition

Situations where CACI < 1.5 AND secincidentcount > 40 AND emerglevel is 'Black', indicating dangerous breakdowns in inter-agency coordination during critical emergency situations

# Columns used

* [operations](/tables/operations.md): `emerglevel`
* [coordinationandevaluation](/tables/coordinationandevaluation.md): `secincidentcount`

# Depends on

* [emerglevel](/knowledge/emerglevel.md)
* [Cross-Agency Coordination Index (CACI)](/knowledge/cross-agency-coordination-index.md)
