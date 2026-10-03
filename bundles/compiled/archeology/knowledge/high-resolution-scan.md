---
type: Business Rule
title: High Resolution Scan
description: Defines what constitutes a high-resolution archaeological scan based on quantitative parameters.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 10
---

# Definition

A scan with ScanResolMm \leq 1.0 and PointDense \geq 1000, allowing for sub-millimeter precision in archaeological documentation and feature detection.

# Columns used

* [scanpointcloud](/tables/scanpointcloud.md): `scanresolmm`, `pointdense`

# Used by

* [Premium Quality Scan](/knowledge/premium-quality-scan.md)
