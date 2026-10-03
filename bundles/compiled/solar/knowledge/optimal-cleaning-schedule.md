---
type: Business Rule
title: Optimal Cleaning Schedule
description: Determines the ideal cleaning frequency based on environmental conditions and soiling rates.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 42
---

# Definition

Cleaning should be scheduled when SIF × DustDensityGM2 exceeds the Soiling Cleaning Threshold or when Expected Energy Yield is reduced by more than 3% due to soiling.

# Depends on

* [Soiling Impact Factor (SIF)](/knowledge/soiling-impact-factor.md)
* [Soiling Cleaning Threshold](/knowledge/soiling-cleaning-threshold.md)
* [Expected Energy Yield (EEY)](/knowledge/expected-energy-yield.md)
