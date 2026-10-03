---
type: Calculation
title: Value Proposition Index (VPI)
description: A comprehensive metric evaluating a gaming device's overall value by balancing performance, durability, ergonomics, and professional adoption.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 39
---

# Definition

VPI = \left(GDVI \times 0.4\right) + \left(ESF \times 0.3\right) + \left(PER \times 0.2\right) + \left(PAR \times 0.1\right)

# Depends on

* [Gaming Device Value Index (GDVI)](/knowledge/gaming-device-value-index.md)
* [Ergonomic Sustainability Factor (ESF)](/knowledge/ergonomic-sustainability-factor.md)
* [Physical Endurance Rating (PER)](/knowledge/physical-endurance-rating.md)
* [Professional Adoption Rating (PAR)](/knowledge/professional-adoption-rating.md)

# Used by

* [Elite Gaming Ecosystem](/knowledge/elite-gaming-ecosystem.md)
