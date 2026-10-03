---
type: Calculation
title: Storage Efficiency Ratio (SER)
description: Measures how efficiently container volume is utilized.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 5
---

# Definition

SER = \frac{VialTally \times 10}{VolLiters}

# Columns used

* [container](/tables/container.md): `volliters`
* [vaccinedetails](/tables/vaccinedetails.md): `vialtally`

# Used by

* [Efficient Container](/knowledge/efficient-container.md)
* [Container Efficiency Score (CES)](/knowledge/container-efficiency-score.md)
* [Efficiency Rank](/knowledge/efficiency-rank.md)
