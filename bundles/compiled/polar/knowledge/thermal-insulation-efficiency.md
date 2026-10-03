---
type: Calculation
title: Thermal Insulation Efficiency (TIE)
description: Measures how effectively a structure retains heat based on insulation status and heat loss rate.
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 6
---

# Definition

TIE = \begin{cases} 0.9 - \frac{heatlossratekwh}{10} & \text{if insulationstatus = 'Good'} \\ 0.6 - \frac{heatlossratekwh}{10} & \text{if insulationstatus = 'Fair'} \\ 0.3 - \frac{heatlossratekwh}{10} & \text{if insulationstatus = 'Poor'} \end{cases}, \text{ where lower heat loss and better insulation result in higher efficiency.}

# Columns used

* [thermalsolarwindandgrid](/tables/thermalsolarwindandgrid.md): `insulationstatus`, `heatlossratekwh`

# Used by

* [Life Support System Reliability (LSSR)](/knowledge/life-support-system-reliability.md)
* [Extreme Climate Adaptation Coefficient (ECAC)](/knowledge/extreme-climate-adaptation-coefficient.md)
