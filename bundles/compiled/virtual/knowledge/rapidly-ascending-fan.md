---
type: Business Rule
title: Rapidly Ascending Fan
description: Identifies fans who are progressing through membership tiers at an accelerated rate
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 42
---

# Definition

A fan with TAF > 1.5 and LPR > 20, demonstrating exceptional speed in advancing through tier levels and accumulating loyalty points.

# Depends on

* [fans.tierstep](/knowledge/fans-tierstep.md)
* [Loyalty Progression Rate (LPR)](/knowledge/loyalty-progression-rate.md)
* [Tier Acceleration Factor (TAF)](/knowledge/tier-acceleration-factor.md)
