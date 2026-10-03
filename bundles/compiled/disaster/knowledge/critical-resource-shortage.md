---
type: Business Rule
title: Critical Resource Shortage
description: Identifies situations where essential resources are dangerously depleted
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 20
---

# Definition

A condition where storeavailm3 is less than 10% of storecapm3 AND supplyflowstate is 'Strained' or 'Disrupted', indicating severe logistical constraints that may compromise disaster response

# Columns used

* [distributionhubs](/tables/distributionhubs.md): `storecapm3`, `storeavailm3`
* [operations](/tables/operations.md): `supplyflowstate`

# Used by

* [Critical Resource Prioritization Need](/knowledge/critical-resource-prioritization-need.md)
