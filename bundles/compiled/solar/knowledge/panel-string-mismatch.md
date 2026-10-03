---
type: Business Rule
title: Panel String Mismatch
description: Identifies when panels in a string have mismatched electrical characteristics.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 16
---

# Definition

A string has significant mismatch when the standard deviation of current measurements (Imp or Isc) across panels exceeds 3% of the mean value under the same irradiance conditions.
