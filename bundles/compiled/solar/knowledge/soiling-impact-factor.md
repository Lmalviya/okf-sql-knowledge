---
type: Calculation
title: Soiling Impact Factor (SIF)
description: Quantifies the impact of soiling on power production based on dust density.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 6
---

# Definition

SIF = SoilingLossPercent / DustDensityGM2, \text{where higher values indicate greater sensitivity to dust accumulation.}

# Used by

* [Expected Energy Yield (EEY)](/knowledge/expected-energy-yield.md)
* [Optimal Cleaning Schedule](/knowledge/optimal-cleaning-schedule.md)
