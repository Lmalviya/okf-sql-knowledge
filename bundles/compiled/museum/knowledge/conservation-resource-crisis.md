---
type: Business Rule
title: Conservation Resource Crisis
description: Identifies serious conservation resource allocation problems.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 45
---

# Definition

Occurs when CRAE < 0.3 AND there is a Conservation Budget Crisis.

# Depends on

* [Conservation Resource Allocation Efficiency (CRAE)](/knowledge/conservation-resource-allocation-efficiency.md)
* [Conservation Budget Crisis](/knowledge/conservation-budget-crisis.md)
