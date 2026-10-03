---
type: Business Rule
title: Conservation Budget Crisis
description: Identifies when conservation budget allocation is insufficient for high-priority artifacts.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 17
---

# Definition

Occurs when CBE < 0.5 AND at least one artifact has ConserveStatus='Critical' and BudgetAllocStatus='Insufficient'.

# Columns used

* [artifactscore](/tables/artifactscore.md): `conservestatus`
* [conservationandmaintenance](/tables/conservationandmaintenance.md): `budgetallocstatus`

# Depends on

* [Conservation Budget Efficiency (CBE)](/knowledge/conservation-budget-efficiency.md)

# Used by

* [Conservation Resource Crisis](/knowledge/conservation-resource-crisis.md)
