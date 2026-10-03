---
type: Calculation
title: Extreme Climate Adaptation Coefficient (ECAC)
description: Evaluates equipment adaptation capability under extreme climate conditions
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 36
---

# Definition

ECAC = SSF × (1 + TIE × 0.5) × \begin{cases} 0.7 & \text{if externaltemperaturec < -30} \\ 0.85 & \text{if externaltemperaturec < -15} \\ 1.0 & \text{otherwise} \end{cases}

# Columns used

* [weatherandstructure](/tables/weatherandstructure.md): `externaltemperaturec`

# Depends on

* [Structural Safety Factor (SSF)](/knowledge/structural-safety-factor.md)
* [Thermal Insulation Efficiency (TIE)](/knowledge/thermal-insulation-efficiency.md)

# Used by

* [Extreme Operating Conditions (EOC)](/knowledge/extreme-operating-conditions.md)
* [Comprehensive Environmental Adaptability Rating (CEAR)](/knowledge/comprehensive-environmental-adaptability-rating.md)
