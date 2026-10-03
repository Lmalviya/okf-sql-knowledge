---
type: Calculation
title: Conservation Backlog Risk (CBR)
description: Quantifies the risk associated with delayed conservation treatments.
tags:
- museum
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:06+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/museum/museum_kb.jsonl
  title: museum business rules (LiveSQLBench), rule 33
---

# Definition

CBR = (CPI × (Days since LastCleaningDate - CleanIntervalDays)) ÷ 100, where CPI is the Conservation Priority Index. Higher values indicate higher risk from delayed conservation.

# Columns used

* [conservationandmaintenance](/tables/conservationandmaintenance.md): `lastcleaningdate`, `cleanintervaldays`

# Depends on

* [Conservation Priority Index (CPI)](/knowledge/conservation-priority-index.md)

# Used by

* [Conservation Resource Allocation Efficiency (CRAE)](/knowledge/conservation-resource-allocation-efficiency.md)
