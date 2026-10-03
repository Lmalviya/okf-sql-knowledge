---
type: Business Rule
title: Unsafe Vaccine Condition
description: Identifies potentially compromised vaccines.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 44
---

# Definition

A condition where VSI < 0.4 and CES < 0.5

# Depends on

* [Vaccine Safety Index (VSI)](/knowledge/vaccine-safety-index.md)
* [Container Efficiency Score (CES)](/knowledge/container-efficiency-score.md)
