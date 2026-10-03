---
type: Calculation
title: Revenue Loss Rate (RLR)
description: Calculates the revenue loss per MW of capacity due to maintenance issues.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 8
---

# Definition

RLR = \frac{RevenueLossUSD}{GenCapMW}, \text{where higher values indicate greater financial impact from downtime.}

# Columns used

* [plant](/tables/plant.md): `gencapmw`

# Used by

* [Maintenance Return on Investment (MROI)](/knowledge/maintenance-return-on-investment.md)
