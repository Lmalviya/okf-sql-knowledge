---
type: Calculation
title: Conservation Resource Allocation Efficiency (CRAE)
description: Measures how efficiently conservation resources are allocated based on priorities and budget.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 36
---

# Definition

CRAE = CBE × (1 - (CBR ÷ 10)), where CBE is the Conservation Budget Efficiency and CBR is the Conservation Backlog Risk. Higher values indicate more efficient resource allocation.

# Depends on

* [Conservation Budget Efficiency (CBE)](/knowledge/conservation-budget-efficiency.md)
* [Conservation Backlog Risk (CBR)](/knowledge/conservation-backlog-risk.md)

# Used by

* [Conservation Resource Crisis](/knowledge/conservation-resource-crisis.md)
