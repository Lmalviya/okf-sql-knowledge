---
type: Business Rule
title: Quality Alert Status
description: Identifies severe quality issues.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 46
---

# Definition

A status where QMI < 0.3 and VSI < 0.5

# Depends on

* [Quality Maintenance Index (QMI)](/knowledge/quality-maintenance-index.md)
* [Vaccine Safety Index (VSI)](/knowledge/vaccine-safety-index.md)
