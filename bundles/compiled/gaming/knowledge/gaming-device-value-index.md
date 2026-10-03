---
type: Calculation
title: Gaming Device Value Index (GDVI)
description: A comprehensive metric evaluating overall gaming device value considering performance, durability, and comfort.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 9
---

# Definition

GDVI = \left(SPI \times 0.3\right) + \left(IRS \times 0.3\right) + \left(DS \times 0.2\right) + \left(CI \times 0.2\right), \text{ where higher values indicate better overall device quality across multiple dimensions.}

# Depends on

* [Sensor Performance Index (SPI)](/knowledge/sensor-performance-index.md)
* [Input Responsiveness Score (IRS)](/knowledge/input-responsiveness-score.md)
* [Durability Score (DS)](/knowledge/durability-score.md)
* [Comfort Index (CI)](/knowledge/comfort-index.md)

# Used by

* [Full-Featured Gaming Setup](/knowledge/full-featured-gaming-setup.md)
* [Value Proposition Index (VPI)](/knowledge/value-proposition-index.md)
* [Elite Gaming Ecosystem](/knowledge/elite-gaming-ecosystem.md)
