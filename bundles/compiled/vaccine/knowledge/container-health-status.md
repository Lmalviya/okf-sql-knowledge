---
type: Business Rule
title: Container Health Status
description: Classifies containers based on overall risk and temperature stability to prioritize immediate action and monitor operational trends.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 10
---

# Definition

Four-level classification based on CRI, TSS, and TBS:
- Critical: CRI > 0.6 OR current TSS < 0.4
- Unstable: Average TSS < 0.4 OR maximum TBS > 1.5 over the past 1 year, and not Critical
- Moderate: Average TSS >= 0.4 AND maximum TBS <= 1.5 over the past 1 year, and not Critical
- Stable: Average TSS >= 0.7 AND maximum TBS <= 1.0 over the past 1 year, and not Critical

# Depends on

* [Temperature Stability Score (TSS)](/knowledge/temperature-stability-score.md)
* [Container Risk Index (CRI)](/knowledge/container-risk-index.md)
* [Temperature Breach Severity (TBS)](/knowledge/temperature-breach-severity.md)
