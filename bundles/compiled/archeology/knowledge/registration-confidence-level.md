---
type: Business Rule
title: Registration Confidence Level
description: Classification system for registration confidence based on multiple factors and error propagation analysis.
tags:
- archeology
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:53+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/archeology/archeology_kb.jsonl
  title: archeology business rules (LiveSQLBench), rule 44
---

# Definition

A classification where 'High Confidence' registrations have RAR > 1.5 and LogMethod containing 'Target', where RAR is Registration Accuracy Ratio, 'Medium Confidence' have RAR between 1.0-1.5, and 'Low Confidence' have RAR < 1.0, determining appropriate use cases for spatial analysis and interpretive visualization.

# Columns used

* [scanregistration](/tables/scanregistration.md): `logmethod`

# Depends on

* [Registration Accuracy Ratio (RAR)](/knowledge/registration-accuracy-ratio.md)
