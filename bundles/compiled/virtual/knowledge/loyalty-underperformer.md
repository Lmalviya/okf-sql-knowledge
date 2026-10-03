---
type: Business Rule
title: Loyalty Underperformer
description: Identifies fans with unusually low loyalty points relative to their spending
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 45
---

# Definition

A fan with LVR < 0.5 and MV > 150, indicating a lower than expected loyalty point accumulation compared to their economic contribution.

# Depends on

* [Monetization Value (MV)](/knowledge/monetization-value.md)
* [Loyalty Value Ratio (LVR)](/knowledge/loyalty-value-ratio.md)
