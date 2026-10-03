---
type: Business Rule
title: Critical Route Status
description: Identifies routes with critical risk levels.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 43
---

# Definition

A route where RRF > 0.8 and TSR < 0.3

# Depends on

* [Route Risk Factor (RRF)](/knowledge/route-risk-factor.md)
* [Transport Safety Rating (TSR)](/knowledge/transport-safety-rating.md)
