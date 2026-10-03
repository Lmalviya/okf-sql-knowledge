---
type: Business Rule
title: Processing Bottleneck
description: Identifies processing workflows that are experiencing resource constraints using performance metrics.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 17
---

# Definition

A processing record with PER < 0.5, where PER is the Processing Efficiency Ratio, indicating potential hardware limitations affecting processing speed and output quality, requiring workflow optimization.

# Depends on

* [Processing Efficiency Ratio (PER)](/knowledge/processing-efficiency-ratio.md)
