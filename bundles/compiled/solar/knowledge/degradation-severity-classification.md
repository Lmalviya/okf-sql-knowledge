---
type: Business Rule
title: Degradation Severity Classification
description: Defines thresholds for high, moderate, and normal degradation based on NDI value.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 52
---

# Definition

Panels are classified as 'High Degradation' if NDI exceeds 1.5, 'Moderate Degradation' if NDI is between 1.0 and 1.5, and 'Normal Degradation' if below 1.0.

# Depends on

* [Normalized Degradation Index (NDI)](/knowledge/normalized-degradation-index.md)
