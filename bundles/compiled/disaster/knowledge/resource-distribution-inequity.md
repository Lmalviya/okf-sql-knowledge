---
type: Business Rule
title: Resource Distribution Inequity
description: Identifies operations with significant disparities in resource allocation
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 48
---

# Definition

Operations where RDE < 0.4 AND distequityidx < 0.5 AND distributionpoints < 5, indicating serious inequities in how resources reach affected populations

# Columns used

* [beneficiariesandassessments](/tables/beneficiariesandassessments.md): `distequityidx`
* [transportation](/tables/transportation.md): `distributionpoints`

# Depends on

* [Resource Distribution Equity (RDE)](/knowledge/resource-distribution-equity.md)
