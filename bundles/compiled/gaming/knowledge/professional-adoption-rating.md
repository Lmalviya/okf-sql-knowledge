---
type: Calculation
title: Professional Adoption Rating (PAR)
description: Quantifies the level of professional gamer adoption and tournament presence of a device based on performance metrics and pro-level features.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 38
---

# Definition

PAR = \frac{CGPI}{10} \times \left(1 + \frac{ProfCount}{5}\right) \times \left(\frac{SPI + IRS}{15}\right)

# Columns used

* [deviceidentity](/tables/deviceidentity.md): `profcount`

# Depends on

* [Competitive Gaming Performance Index (CGPI)](/knowledge/competitive-gaming-performance-index.md)
* [Sensor Performance Index (SPI)](/knowledge/sensor-performance-index.md)
* [Input Responsiveness Score (IRS)](/knowledge/input-responsiveness-score.md)

# Used by

* [Value Proposition Index (VPI)](/knowledge/value-proposition-index.md)
* [Pro-Player Performance Certified](/knowledge/pro-player-performance-certified.md)
