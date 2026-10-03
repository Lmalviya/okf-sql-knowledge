---
type: Business Rule
title: Logistics Breakdown
description: Identifies severe disruptions in the supply chain
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 29
---

# Definition

Situations where LPM < 30 AND lastmilestatus is 'Suspended' AND vehiclebreakrate > 15, indicating critical failures in the logistics system requiring immediate intervention

# Columns used

* [transportation](/tables/transportation.md): `lastmilestatus`, `vehiclebreakrate`

# Depends on

* [lastmilestatus](/knowledge/lastmilestatus.md)
* [Logistics Performance Metric (LPM)](/knowledge/logistics-performance-metric.md)

# Used by

* [Logistics System Collapse Risk](/knowledge/logistics-system-collapse-risk.md)
