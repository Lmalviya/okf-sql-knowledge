---
type: Calculation
title: Maintenance Cost Efficiency (MCE)
description: Evaluates the cost-effectiveness of maintenance relative to the plant's capacity.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 7
---

# Definition

MCE = \frac{MaintenanceCostUSD + CleaningCostUSD + ReplacementCostUSD}{GenCapMW}, \text{where lower values indicate more cost-effective maintenance.}

# Columns used

* [plant](/tables/plant.md): `gencapmw`

# Used by

* [Maintenance Return on Investment (MROI)](/knowledge/maintenance-return-on-investment.md)
