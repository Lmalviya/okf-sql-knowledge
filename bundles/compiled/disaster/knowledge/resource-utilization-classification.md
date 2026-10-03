---
type: Business Rule
title: Resource Utilization Classification
description: Categorizes distribution hubs based on their Resource Utilization Ratio (RUR) values
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 50
---

# Definition

High Utilization (RUR > 5) indicates potentially overloaded hubs that may need resource expansion; Moderate Utilization (2 ≤ RUR ≤ 5) represents optimal resource usage balance; Low Utilization (RUR < 2) indicates underutilized hubs with potential efficiency gains through resource reallocation

# Depends on

* [Resource Utilization Ratio (RUR)](/knowledge/resource-utilization-ratio.md)
