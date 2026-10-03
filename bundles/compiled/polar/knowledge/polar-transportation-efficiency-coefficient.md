---
type: Calculation
title: Polar Transportation Efficiency Coefficient (PTEC)
description: Measures vehicle transportation efficiency in polar conditions, considering vehicle performance and energy sustainability
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 31
---

# Definition

PTEC = VPC × (0.6 + 0.4 × ESI ÷ 100)

# Depends on

* [Energy Sustainability Index (ESI)](/knowledge/energy-sustainability-index.md)
* [Vehicle Performance Coefficient (VPC)](/knowledge/vehicle-performance-coefficient.md)

# Used by

* [Polar Vehicle Safe Operation Conditions (PVSOC)](/knowledge/polar-vehicle-safe-operation-conditions.md)
