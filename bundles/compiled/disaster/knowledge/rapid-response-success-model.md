---
type: Business Rule
title: Rapid Response Success Model
description: Identifies exemplary rapid deployment operations
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 49
---

# Definition

Operations where RTER > 20 AND OEI > 2.5 AND deliverysuccessrate > 85, representing highly effective and rapidly deployed response operations that can serve as models for future disasters

# Columns used

* [transportation](/tables/transportation.md): `deliverysuccessrate`

# Depends on

* [Operational Efficiency Index (OEI)](/knowledge/operational-efficiency-index.md)
* [Response Time Effectiveness Ratio (RTER)](/knowledge/response-time-effectiveness-ratio.md)
