---
type: Business Rule
title: ReadingInterval
description: Time denominator used for calculating rate of temperature change
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 60
---

# Definition

Time interval in minutes between successive temperature readings, used to normalize temperature differences into rates of change. Standard value is 15 minutes with acceptable range 5-60 minutes depending on monitoring requirements

# Used by

* [Thermal Stability Coefficient (TSC)](/knowledge/thermal-stability-coefficient.md)
