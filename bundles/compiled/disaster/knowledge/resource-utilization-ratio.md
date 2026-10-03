---
type: Calculation
title: Resource Utilization Ratio (RUR)
description: Measures how effectively hub capacity is being used relative to available resources
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 10
---

# Definition

RUR = \frac{hubutilpct}{100} \times \frac{storecapm3}{storeavailm3 + 1}

# Columns used

* [distributionhubs](/tables/distributionhubs.md): `hubutilpct`, `storecapm3`, `storeavailm3`

# Used by

* [Financial Vulnerability Zone](/knowledge/financial-vulnerability-zone.md)
* [Resource Utilization Classification](/knowledge/resource-utilization-classification.md)
