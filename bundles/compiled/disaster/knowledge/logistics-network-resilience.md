---
type: Calculation
title: Logistics Network Resilience (LNR)
description: Quantifies the ability of the logistics network to withstand disruption
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 36
---

# Definition

LNR = LPM \times \frac{vehiclecount}{20} \times lastmile\_factor, \text{ where lastmile\_factor is 1.0 for On Track, 0.7 for Delayed, 0.4 for Suspended lastmilestatus, 0 for else}

# Columns used

* [transportation](/tables/transportation.md): `vehiclecount`, `lastmilestatus`

# Depends on

* [Logistics Performance Metric (LPM)](/knowledge/logistics-performance-metric.md)

# Used by

* [Logistics System Collapse Risk](/knowledge/logistics-system-collapse-risk.md)
