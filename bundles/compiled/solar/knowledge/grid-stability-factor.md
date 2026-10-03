---
type: Business Rule
title: Grid Stability Factor
description: Measures the contribution of the inverter to grid stability.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 19
---

# Definition

A metric determined by the combination of Power Quality Index, Harmonic Distortion Percentage, and Power Factor, where values closer to 1.0 indicate better contribution to grid stability.

# Used by

* [Grid Integration Quality (GIQ)](/knowledge/grid-integration-quality.md)
