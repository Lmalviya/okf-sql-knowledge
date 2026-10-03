---
type: Calculation
title: Battery Efficiency Ratio (BER)
description: Measures how efficiently a device uses its battery capacity relative to its power draw under active conditions.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 1
---

# Definition

BER = \frac{BattLifeH \times BattCapMah}{PwrActMw \times 10}, \text{ where higher values indicate more efficient power management and battery utilization.}

# Columns used

* [testsessions](/tables/testsessions.md): `battcapmah`, `battlifeh`
* [deviceidentity](/tables/deviceidentity.md): `pwractmw`

# Used by

* [Extended Battery Life Device](/knowledge/extended-battery-life-device.md)
* [Wireless Performance Efficiency (WPE)](/knowledge/wireless-performance-efficiency.md)
* [Extended Tournament Ready Wireless](/knowledge/extended-tournament-ready-wireless.md)
* [Battery Efficiency Classification](/knowledge/battery-efficiency-classification.md)
* [Global Efficiency Percentile (GEP)](/knowledge/global-efficiency-percentile.md)
