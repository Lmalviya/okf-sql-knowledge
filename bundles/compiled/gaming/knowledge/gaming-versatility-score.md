---
type: Calculation
title: Gaming Versatility Score (GVS)
description: Assesses a device's versatility across different gaming genres and use cases based on adaptability and feature set.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 36
---

# Definition

GVS = \frac{ProfCount + 1}{3} \times \left(CGPI \times 0.6\right) + \left(IEC \times 0.4\right)

# Columns used

* [deviceidentity](/tables/deviceidentity.md): `profcount`

# Depends on

* [Competitive Gaming Performance Index (CGPI)](/knowledge/competitive-gaming-performance-index.md)
* [Immersion Enhancement Coefficient (IEC)](/knowledge/immersion-enhancement-coefficient.md)

# Used by

* [Professional Multi-Genre Setup](/knowledge/professional-multi-genre-setup.md)
