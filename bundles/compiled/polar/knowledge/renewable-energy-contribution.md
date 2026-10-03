---
type: Calculation
title: Renewable Energy Contribution (REC)
description: Calculates the percentage contribution of renewable energy sources to the total power generation.
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 9
---

# Definition

REC = \frac{renewablemetrics.solar.output\_w + renewablemetrics.wind.output\_w}{fuelcelloutputw + renewablemetrics.solar.output\_w + renewablemetrics.wind.output\_w} \times 100, \text{ where higher values indicate greater reliance on renewable energy.}

# Columns used

* [thermalsolarwindandgrid](/tables/thermalsolarwindandgrid.md): `fuelcelloutputw`, `renewablemetrics`

# Used by

* [Sustainable Energy Operation](/knowledge/sustainable-energy-operation.md)
* [Resource Self-Sufficiency Index (RSSI)](/knowledge/resource-self-sufficiency-index.md)
* [Polar Base Energy Security Status (PBESS)](/knowledge/polar-base-energy-security-status.md)
* [Energy Sustainability Classification System (ESCS)](/knowledge/energy-sustainability-classification-system.md)
