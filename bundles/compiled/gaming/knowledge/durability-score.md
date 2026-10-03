---
type: Calculation
title: Durability Score (DS)
description: Quantifies overall device durability based on material quality, environmental resistance, and impact protection.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 7
---

# Definition

DS = \left(\frac{DropHtM}{2} + \frac{BendForce}{100} + \frac{TwistDeg}{90}\right) \times \frac{UsbConnDur}{10000} \times 10, \text{ where higher values indicate more durable devices capable of withstanding physical stress.}

# Columns used

* [physicaldurability](/tables/physicaldurability.md): `drophtm`, `bendforce`, `twistdeg`, `usbconndur`

# Used by

* [Gaming Device Value Index (GDVI)](/knowledge/gaming-device-value-index.md)
* [Competitive-Grade Durability](/knowledge/competitive-grade-durability.md)
* [Physical Endurance Rating (PER)](/knowledge/physical-endurance-rating.md)
* [Ultra-Durable Tournament Device](/knowledge/ultra-durable-tournament-device.md)
