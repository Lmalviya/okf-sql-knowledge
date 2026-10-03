---
type: Business Rule
title: Logistics System Collapse Risk
description: Identifies operations at imminent risk of complete logistics failure
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 45
---

# Definition

Operations experiencing Logistics Breakdown where LNR < 20 AND vehiclebreakrate > 25, indicating a logistics system on the verge of complete collapse requiring immediate external support

# Columns used

* [transportation](/tables/transportation.md): `vehiclebreakrate`

# Depends on

* [Logistics Breakdown](/knowledge/logistics-breakdown.md)
* [Logistics Network Resilience (LNR)](/knowledge/logistics-network-resilience.md)
