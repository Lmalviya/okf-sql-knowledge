---
type: Calculation
title: Resource Utilization Ratio (RUR)
description: Measures how effectively hub capacity is being used relative to available resources.
tags: [disaster, logistics]
generated: { by: human:your-name, at: 2026-10-02T17:00:00+05:30 }
sources:
  - id: kb
    resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/disaster/disaster_kb.jsonl
    title: disaster business rules (LiveSQLBench), rule 10
---

# Definition

RUR = (hubutilpct / 100) × (storecapm3 / (storeavailm3 + 1))

# Columns used

All three columns are in [distributionhubs](/tables/distributionhubs.md): `hubutilpct`, `storecapm3` and `storeavailm3`.

# Used by

* [Resource Utilization Classification](/knowledge/resource-utilization-classification.md)