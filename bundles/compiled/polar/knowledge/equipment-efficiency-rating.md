---
type: Calculation
title: Equipment Efficiency Rating (EER)
description: A composite metric that evaluates the overall efficiency of equipment based on performance, reliability, and environmental impact.
tags:
- polar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:08+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/polar/polar_kb.jsonl
  title: polar business rules (LiveSQLBench), rule 0
---

# Definition

EER = \frac{performanceindex + reliabilityindex}{2} \times (1 - \frac{environmentalimpactindex}{10}), \text{ where higher values indicate more efficient equipment with better performance and lower environmental impact.}

# Columns used

* [equipment](/tables/equipment.md): `reliabilityindex`, `performanceindex`, `environmentalimpactindex`

# Used by

* [Overall Safety Performance Index (OSPI)](/knowledge/overall-safety-performance-index.md)
* [Long-term Operational Stability Score (LOSS)](/knowledge/long-term-operational-stability-score.md)
* [Comprehensive Operational Reliability Indicator (CORI)](/knowledge/comprehensive-operational-reliability-indicator.md)
