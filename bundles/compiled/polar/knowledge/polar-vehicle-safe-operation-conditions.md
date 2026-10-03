---
type: Business Rule
title: Polar Vehicle Safe Operation Conditions (PVSOC)
description: Determines the conditions for safe operation of polar vehicles
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 44
---

# Definition

Polar vehicles are considered 'suitable for polar missions' when they maintain PTEC > 0.7 and VPC > 0.75, with operationalstatus = 'Active' and safetyindex ≥ 0.8.

# Columns used

* [equipment](/tables/equipment.md): `safetyindex`
* [operationmaintenance](/tables/operationmaintenance.md): `operationalstatus`

# Depends on

* [Vehicle Performance Coefficient (VPC)](/knowledge/vehicle-performance-coefficient.md)
* [Polar Transportation Efficiency Coefficient (PTEC)](/knowledge/polar-transportation-efficiency-coefficient.md)
