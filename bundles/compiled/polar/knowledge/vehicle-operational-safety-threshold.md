---
type: Business Rule
title: Vehicle Operational Safety Threshold
description: Defines the safety threshold for vehicle operations based on multiple safety factors.
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 15
---

# Definition

A vehicle is considered 'Safe for Operation' when it maintains a VPC > 0.6, has brake fluid levels above 50%, brake pad wear below 70%, adequate tire pressure (tiremetrics.pressure_kpa > 200), and is operated within recommended load limits (vehicleloadkg within manufacturer specifications).

# Columns used

* [equipment](/tables/equipment.md): `manufacturer`
* [chassisandvehicle](/tables/chassisandvehicle.md): `vehicleloadkg`, `tiremetrics`

# Depends on

* [Vehicle Performance Coefficient (VPC)](/knowledge/vehicle-performance-coefficient.md)
