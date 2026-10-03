---
type: Calculation
title: Physical Endurance Rating (PER)
description: 'Measures the physical endurance of a device under intense gaming conditions, combining durability with effective heat management. '
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 37
---

# Definition

PER = DS \times \left(1 + \frac{DustRes score + WaterRes score}{6}\right) \times \left(1 - \frac{100 - BendForce}{200}\right), where DustRes and WaterRes are scored based on IP ratings (IPX0=0, IPX1=1, IPX2=2, IPX3=3).

# Columns used

* [physicaldurability](/tables/physicaldurability.md): `dustres`, `waterres`, `bendforce`

# Depends on

* [Durability Score (DS)](/knowledge/durability-score.md)

# Used by

* [Value Proposition Index (VPI)](/knowledge/value-proposition-index.md)
* [Ultra-Durable Tournament Device](/knowledge/ultra-durable-tournament-device.md)
