---
type: Calculation
title: Expected Energy Yield (EEY)
description: Calculates the expected energy production considering current conditions.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 36
---

# Definition

EEY = PowerRatedW × EPE × SIF × POAIrradianceWM2 / 1000, where EPE is the Energy Production Efficiency and SIF is the Soiling Impact Factor.

# Depends on

* [Energy Production Efficiency (EPE)](/knowledge/energy-production-efficiency.md)
* [Soiling Impact Factor (SIF)](/knowledge/soiling-impact-factor.md)
* [POAIrradianceWM2 (Plane-of-Array Irradiance)](/knowledge/poairradiancewm2.md)

# Used by

* [Optimal Cleaning Schedule](/knowledge/optimal-cleaning-schedule.md)
