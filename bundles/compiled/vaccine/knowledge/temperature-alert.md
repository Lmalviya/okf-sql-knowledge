---
type: Business Rule
title: Temperature Alert
description: Identifies critical temperature conditions.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 16
---

# Definition

A condition where TBS > 2.0 and TempDevCount > 5

# Columns used

* [sensordata](/tables/sensordata.md): `tempdevcount`

# Depends on

* [Temperature Breach Severity (TBS)](/knowledge/temperature-breach-severity.md)
