---
type: Business Rule
title: Transport Safety Alert
description: Identifies unsafe transport conditions.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 47
---

# Definition

A condition where TSR < 0.5 and RRF > 0.7

# Depends on

* [Transport Safety Rating (TSR)](/knowledge/transport-safety-rating.md)
* [Route Risk Factor (RRF)](/knowledge/route-risk-factor.md)
