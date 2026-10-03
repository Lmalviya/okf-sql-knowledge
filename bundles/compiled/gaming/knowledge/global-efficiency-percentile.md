---
type: Calculation
title: Global Efficiency Percentile (GEP)
description: Ranks a device’s Battery Efficiency Ratio (BER) relative to all other wireless gaming devices.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 53
---

# Definition

GEP = \text{PERCENT\_RANK}()_{BER} \times 100, where PERCENT\_RANK() is computed over all devices sorted by BER; 0\% corresponds to the lowest BER and 100\% to the highest.

# Depends on

* [Battery Efficiency Ratio (BER)](/knowledge/battery-efficiency-ratio.md)
