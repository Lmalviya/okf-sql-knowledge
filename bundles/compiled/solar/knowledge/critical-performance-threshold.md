---
type: Business Rule
title: Critical Performance Threshold
description: Defines when a panel's performance has degraded to a level requiring attention.
tags:
- solar
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:11+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/solar/solar_kb.jsonl
  title: solar business rules (LiveSQLBench), rule 10
---

# Definition

A solar panel is considered below critical performance threshold when its Panel Performance Ratio (PPR) falls below 80% of the expected value for its age, accounting for normal degradation.

# Depends on

* [Panel Performance Ratio (PPR)](/knowledge/panel-performance-ratio.md)

# Used by

* [Advanced Performance Degradation Alert](/knowledge/advanced-performance-degradation-alert.md)
