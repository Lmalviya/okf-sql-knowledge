---
type: Business Rule
title: Advanced Performance Degradation Alert
description: Identifies panels showing accelerated degradation requiring intervention.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 40
---

# Definition

A panel requires urgent attention when its Normalized Degradation Index exceeds 1.5 and its TAPR is below the Critical Performance Threshold.

# Depends on

* [Critical Performance Threshold](/knowledge/critical-performance-threshold.md)
* [Temperature Adjusted Performance Ratio (TAPR)](/knowledge/temperature-adjusted-performance-ratio.md)
* [Normalized Degradation Index (NDI)](/knowledge/normalized-degradation-index.md)
