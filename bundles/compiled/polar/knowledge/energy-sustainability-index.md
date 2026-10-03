---
type: Calculation
title: Energy Sustainability Index (ESI)
description: Measures the sustainability of an equipment's energy usage by evaluating energy efficiency and renewable sources.
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 2
---

# Definition

ESI = energyefficiencypercent \times \begin{cases} 1.5 & \text{if powersource IN ('Solar', 'Wind')} \\ 1.2 & \text{if powersource = 'Hybrid'} \\ 1.0 & \text{if powersource = 'Battery'} \\ 0.7 & \text{if powersource = 'Diesel'} \\ 0 & \text{otherwise} \end{cases}, \text{ providing higher ratings for renewable energy and lower ratings for fossil fuels.}

# Columns used

* [powerbattery](/tables/powerbattery.md): `powersource`, `energyefficiencypercent`

# Used by

* [Energy Sustainability Classification](/knowledge/energy-sustainability-classification.md)
* [Polar Transportation Efficiency Coefficient (PTEC)](/knowledge/polar-transportation-efficiency-coefficient.md)
* [Energy-Water Resource Integration Index (EWRII)](/knowledge/energy-water-resource-integration-index.md)
* [Polar Base Energy Security Status (PBESS)](/knowledge/polar-base-energy-security-status.md)
