---
type: Calculation
title: Inverter Efficiency Loss (IEL)
description: Calculates the energy lost due to inverter inefficiency.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 4
---

# Definition

IEL = MeasuredPowerW \times (1 - InverterEfficiencyPercent/100), \text{where InverterEfficiencyPercent is from power_metrics.inverteffpct.}

# Columns used

* [inverter](/tables/inverter.md): `power_metrics`

# Used by

* [Total System Loss (TSL)](/knowledge/total-system-loss.md)
