---
type: Calculation
title: Logistics Performance Metric (LPM)
description: Measures the overall performance of logistics operations
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 15
---

# Definition

LPM = \frac{totaldeliverytons}{hubcaptons} \times deliverysuccessrate \times \left(1 - \frac{vehiclebreakrate}{100}\right) \times 100

# Columns used

* [distributionhubs](/tables/distributionhubs.md): `hubcaptons`
* [transportation](/tables/transportation.md): `totaldeliverytons`, `deliverysuccessrate`, `vehiclebreakrate`

# Used by

* [Logistics Breakdown](/knowledge/logistics-breakdown.md)
* [Logistics Network Resilience (LNR)](/knowledge/logistics-network-resilience.md)
