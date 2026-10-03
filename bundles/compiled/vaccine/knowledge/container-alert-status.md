---
type: Business Rule
title: Container Alert Status
description: Identifies containers requiring urgent attention.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 48
---

# Definition

A status where CES < 0.4 and TRS > 0.7

# Depends on

* [Container Efficiency Score (CES)](/knowledge/container-efficiency-score.md)
* [Total Risk Score (TRS)](/knowledge/total-risk-score.md)
