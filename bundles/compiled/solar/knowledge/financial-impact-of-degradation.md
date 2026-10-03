---
type: Calculation
title: Financial Impact of Degradation (FID)
description: Calculates the financial cost of degradation over time.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 39
---

# Definition

FID = GenCapMW × 1000 × NDI × PELR × ElectricityPricePerKWh × 24 × 365, where NDI is the Normalized Degradation Index and PELR is the Panel Efficiency Loss Rate.

# Columns used

* [plant](/tables/plant.md): `gencapmw`

# Depends on

* [Panel Efficiency Loss Rate (PELR)](/knowledge/panel-efficiency-loss-rate.md)
* [Normalized Degradation Index (NDI)](/knowledge/normalized-degradation-index.md)

# Used by

* [System Upgrade Candidate](/knowledge/system-upgrade-candidate.md)
* [Total Economic Performance](/knowledge/total-economic-performance.md)
