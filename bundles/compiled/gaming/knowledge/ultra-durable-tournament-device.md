---
type: Business Rule
title: Ultra-Durable Tournament Device
description: Defines devices with exceptional physical durability designed to withstand the rigors of frequent tournament travel and intensive competition use.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 47
---

# Definition

A device with PER > 9.0, DS > 8.5, UsbConnDur > 20000, and at least one premium durability feature (DropHtM > 2.0 or WaterRes containing 'IPX7' or higher), engineered to maintain performance integrity despite frequent transportation, setup/teardown cycles, and competition intensity.

# Columns used

* [physicaldurability](/tables/physicaldurability.md): `waterres`, `drophtm`, `usbconndur`

# Depends on

* [Physical Endurance Rating (PER)](/knowledge/physical-endurance-rating.md)
* [Durability Score (DS)](/knowledge/durability-score.md)
