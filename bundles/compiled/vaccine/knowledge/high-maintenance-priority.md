---
type: Business Rule
title: High Maintenance Priority
description: Identifies equipment requiring urgent maintenance.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 42
---

# Definition

Equipment where CMR > 0.7 and QMI < 0.4

# Depends on

* [Combined Maintenance Risk (CMR)](/knowledge/combined-maintenance-risk.md)
* [Quality Maintenance Index (QMI)](/knowledge/quality-maintenance-index.md)
