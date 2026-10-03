---
type: Business Rule
title: Registration Quality Threshold
description: Defines the quality threshold for scan registration in archaeological documentation based on error propagation analysis.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 18
---

# Definition

A registration with LogAccuMm < 1.0 and ErrValMm < 2.0, ensuring sufficient accuracy for reliable spatial analysis with maximum tolerable error below the significant feature size threshold.

# Columns used

* [scanregistration](/tables/scanregistration.md): `logaccumm`, `errvalmm`

# Used by

* [Full Archaeological Digital Twin](/knowledge/full-archaeological-digital-twin.md)
