---
type: Business Rule
title: Polar Base Energy Security Status (PBESS)
description: Determines the security status of energy supply for polar bases
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 48
---

# Definition

A polar base is assessed as being in an 'energy secure' state when it maintains REC > 65%, ESI > 0.7, and RSSI > 0.75, with batterystatus.level_percent > 75 and hydrogenlevelpercent > 70.

# Columns used

* [thermalsolarwindandgrid](/tables/thermalsolarwindandgrid.md): `hydrogenlevelpercent`
* [powerbattery](/tables/powerbattery.md): `batterystatus`

# Depends on

* [Energy Sustainability Index (ESI)](/knowledge/energy-sustainability-index.md)
* [Renewable Energy Contribution (REC)](/knowledge/renewable-energy-contribution.md)
* [Resource Self-Sufficiency Index (RSSI)](/knowledge/resource-self-sufficiency-index.md)
