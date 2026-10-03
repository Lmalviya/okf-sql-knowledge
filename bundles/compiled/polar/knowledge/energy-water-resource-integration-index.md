---
type: Calculation
title: Energy-Water Resource Integration Index (EWRII)
description: Evaluates the integration efficiency of energy and water resource management
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 38
---

# Definition

EWRII = 0.5 × ESI + 0.5 × WRMI × (1 - \frac{heatertemperaturec}{100})

# Columns used

* [cabinenvironment](/tables/cabinenvironment.md): `heatertemperaturec`

# Depends on

* [Energy Sustainability Index (ESI)](/knowledge/energy-sustainability-index.md)
* [Water Resource Management Index (WRMI)](/knowledge/water-resource-management-index.md)

# Used by

* [Sustainable Polar Operations (SPO)](/knowledge/sustainable-polar-operations.md)
