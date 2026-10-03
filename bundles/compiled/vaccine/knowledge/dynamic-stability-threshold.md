---
type: Business Rule
title: Dynamic Stability Threshold
description: Evaluates stability under varying conditions.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 57
---

# Definition

A condition where average TSC over last 5 readings < 0.7 AND MPRA > 0.6

# Depends on

* [Thermal Stability Coefficient (TSC)](/knowledge/thermal-stability-coefficient.md)
* [Multi-Parameter Risk Assessment (MPRA)](/knowledge/multi-parameter-risk-assessment.md)
