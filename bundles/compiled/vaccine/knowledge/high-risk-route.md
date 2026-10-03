---
type: Business Rule
title: High-Risk Route
description: Identifies high-risk transportation routes.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 12
---

# Definition

A route where RCP < 50% and CRI > 0.4

# Depends on

* [Container Risk Index (CRI)](/knowledge/container-risk-index.md)
* [Route Completion Percentage (RCP)](/knowledge/route-completion-percentage.md)
