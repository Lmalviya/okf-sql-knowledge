---
type: Business Rule
title: Resource Optimization Opportunity
description: Identifies situations where resource allocation could be optimized
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 22
---

# Definition

A scenario where hubutilpct < 30 while simultaneously having distributionpoints > 20, suggesting potential for redistribution of resources to maximize efficiency

# Columns used

* [distributionhubs](/tables/distributionhubs.md): `hubutilpct`
* [transportation](/tables/transportation.md): `distributionpoints`
