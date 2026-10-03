---
type: Business Rule
title: Soiling Cleaning Threshold
description: Defines when panel cleaning should be performed based on soiling conditions.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 13
---

# Definition

Cleaning should be performed when Soiling Loss Percentage exceeds 5% or when Dust Density exceeds 0.15 g/m², whichever occurs first.

# Used by

* [Optimal Cleaning Schedule](/knowledge/optimal-cleaning-schedule.md)
* [Cleaning Triggers](/knowledge/cleaning-triggers.md)
