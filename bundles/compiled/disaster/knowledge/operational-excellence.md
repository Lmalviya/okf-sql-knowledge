---
type: Business Rule
title: Operational Excellence
description: Identifies disaster response operations demonstrating superior performance
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 24
---

# Definition

Operations with deliverysuccessrate > 90 AND invaccpct > 95 AND OEI > 3, representing highly effective logistics and resource management

# Columns used

* [distributionhubs](/tables/distributionhubs.md): `invaccpct`
* [transportation](/tables/transportation.md): `deliverysuccessrate`

# Depends on

* [Operational Efficiency Index (OEI)](/knowledge/operational-efficiency-index.md)

# Used by

* [Sustainable Operation Excellence](/knowledge/sustainable-operation-excellence.md)
