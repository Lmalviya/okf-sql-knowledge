---
type: Calculation
title: Vehicle Performance Coefficient (VPC)
description: A metric that evaluates vehicle performance based on mechanical condition and operational efficiency.
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 5
---

# Definition

VPC = (1 - \frac{brakepadwearpercent + trackwearpercent}{200}) \times \frac{vehiclespeedkmh}{50} \times \frac{engineloadpercent}{100}, \text{ where lower wear percentages and optimal engine load contribute to better performance.}

# Columns used

* [engineandfluids](/tables/engineandfluids.md): `engineloadpercent`
* [chassisandvehicle](/tables/chassisandvehicle.md): `brakepadwearpercent`, `trackwearpercent`, `vehiclespeedkmh`

# Used by

* [Vehicle Operational Safety Threshold](/knowledge/vehicle-operational-safety-threshold.md)
* [Polar Transportation Efficiency Coefficient (PTEC)](/knowledge/polar-transportation-efficiency-coefficient.md)
* [Polar Vehicle Safe Operation Conditions (PVSOC)](/knowledge/polar-vehicle-safe-operation-conditions.md)
