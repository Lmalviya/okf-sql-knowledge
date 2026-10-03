---
type: Business Rule
title: Logger Critical State
description: Identifies critically failing loggers.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 45
---

# Definition

A logger where LRS < 0.3 and CMR > 0.8

# Depends on

* [Logger Reliability Score (LRS)](/knowledge/logger-reliability-score.md)
* [Combined Maintenance Risk (CMR)](/knowledge/combined-maintenance-risk.md)
