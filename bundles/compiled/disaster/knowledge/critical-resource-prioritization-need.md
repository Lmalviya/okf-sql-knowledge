---
type: Business Rule
title: Critical Resource Prioritization Need
description: Identifies operations requiring immediate resource redistribution
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 40
---

# Definition

Operations experiencing Critical Resource Shortage where PER < 0.5 AND emerglevel is either 'Red' or 'Black', indicating a severe mismatch between available resources and critical operational needs

# Columns used

* [operations](/tables/operations.md): `emerglevel`

# Depends on

* [emerglevel](/knowledge/emerglevel.md)
* [Personnel Effectiveness Ratio (PER)](/knowledge/personnel-effectiveness-ratio.md)
* [Critical Resource Shortage](/knowledge/critical-resource-shortage.md)
