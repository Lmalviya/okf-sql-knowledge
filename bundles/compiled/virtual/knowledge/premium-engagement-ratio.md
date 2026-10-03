---
type: Calculation
title: Premium Engagement Ratio (PER)
description: Measures the relationship between fan spending and their engagement level
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 30
---

# Definition

PER = \frac{MV}{FEI \times 100}, \text{ where higher values indicate fans who spend more relative to their engagement level.}

# Depends on

* [Fan Engagement Index (FEI)](/knowledge/fan-engagement-index.md)
* [Monetization Value (MV)](/knowledge/monetization-value.md)
