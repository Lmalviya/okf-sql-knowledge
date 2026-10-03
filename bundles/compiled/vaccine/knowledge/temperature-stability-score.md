---
type: Calculation
title: Temperature Stability Score (TSS)
description: Calculates the overall temperature stability of a container based on deviations and critical events.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 0
---

# Definition

TSS = (1 - \frac{TempDevCount}{100}) \times (1 - \frac{CritEvents}{10}) \times TempStabIdx

# Columns used

* [sensordata](/tables/sensordata.md): `tempdevcount`, `tempstabidx`, `critevents`

# Used by

* [Container Risk Index (CRI)](/knowledge/container-risk-index.md)
* [Vaccine Viability Period (VVP)](/knowledge/vaccine-viability-period.md)
* [Container Health Status](/knowledge/container-health-status.md)
* [Stable Transport](/knowledge/stable-transport.md)
* [Efficient Container](/knowledge/efficient-container.md)
* [Coolant Efficiency Index (CEI)](/knowledge/coolant-efficiency-index.md)
* [Logger Reliability Score (LRS)](/knowledge/logger-reliability-score.md)
* [Thermal Stability Coefficient (TSC)](/knowledge/thermal-stability-coefficient.md)
* [Time-Weighted Quality Decay (TWQD)](/knowledge/time-weighted-quality-decay.md)
* [Environmental Stress Factor (ESF)](/knowledge/environmental-stress-factor.md)
