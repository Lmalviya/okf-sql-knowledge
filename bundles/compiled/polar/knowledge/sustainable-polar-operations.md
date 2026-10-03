---
type: Business Rule
title: Sustainable Polar Operations (SPO)
description: Defines sustainability standards for polar operations
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 42
---

# Definition

Polar operations are defined as 'sustainable' when the site maintains RSSI > 0.7 and EWRII > 0.65, with wastemanagementstatus = 'Normal' and environmentalimpactindex < 6.0.

# Columns used

* [equipment](/tables/equipment.md): `environmentalimpactindex`
* [lightingandsafety](/tables/lightingandsafety.md): `wastemanagementstatus`

# Depends on

* [Resource Self-Sufficiency Index (RSSI)](/knowledge/resource-self-sufficiency-index.md)
* [Energy-Water Resource Integration Index (EWRII)](/knowledge/energy-water-resource-integration-index.md)
