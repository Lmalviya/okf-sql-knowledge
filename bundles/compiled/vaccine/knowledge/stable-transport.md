---
type: Business Rule
title: Stable Transport
description: Identifies stable transport conditions.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 14
---

# Definition

Transport where HQI > 0.9 and TSS > 0.8

# Depends on

* [Temperature Stability Score (TSS)](/knowledge/temperature-stability-score.md)
* [Handling Quality Index (HQI)](/knowledge/handling-quality-index.md)
