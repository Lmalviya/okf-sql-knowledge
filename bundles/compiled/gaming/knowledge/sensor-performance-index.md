---
type: Calculation
title: Sensor Performance Index (SPI)
description: A composite metric that evaluates overall sensor quality based on resolution, accuracy, and response time.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 0
---

# Definition

SPI = \frac{DpiRes}{1000} \times \left(1 - \frac{McRespTime}{10}\right) \times 10, \text{ where higher values indicate better overall sensor performance with balanced resolution and responsiveness.}

# Columns used

* [deviceidentity](/tables/deviceidentity.md): `mcresptime`, `dpires`

# Used by

* [Gaming Device Value Index (GDVI)](/knowledge/gaming-device-value-index.md)
* [Premium Gaming Mouse](/knowledge/premium-gaming-mouse.md)
* [Competitive Gaming Performance Index (CGPI)](/knowledge/competitive-gaming-performance-index.md)
* [Professional Adoption Rating (PAR)](/knowledge/professional-adoption-rating.md)
