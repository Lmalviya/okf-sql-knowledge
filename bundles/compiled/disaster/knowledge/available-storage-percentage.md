---
type: Calculation
title: available storage percentage
description: Calculates what proportion of total storage capacity is currently available
tags:
- disaster
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:59+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
  title: disaster business rules (LiveSQLBench), rule 53
---

# Definition

The percentage calculated by dividing available storage (storeavailm3) by total storage capacity (storecapm3) and multiplying by 100

# Columns used

* [distributionhubs](/tables/distributionhubs.md): `storecapm3`, `storeavailm3`
