---
type: Calculation
title: Conservation Budget Efficiency (CBE)
description: Measures the efficiency of conservation budget allocation relative to artifact importance.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 9
---

# Definition

CBE = \frac{\sum_{i \in artifacts} (CPI_i \times BudgetRatio_i)}{|artifacts|}, \text{where BudgetRatio is the proportion of total conservation budget allocated to each artifact}

# Depends on

* [Conservation Priority Index (CPI)](/knowledge/conservation-priority-index.md)

# Used by

* [Conservation Budget Crisis](/knowledge/conservation-budget-crisis.md)
* [Conservation Resource Allocation Efficiency (CRAE)](/knowledge/conservation-resource-allocation-efficiency.md)
