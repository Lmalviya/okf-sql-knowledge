---
type: Calculation
title: Wireless Performance Efficiency (WPE)
description: Evaluates the efficiency of wireless performance relative to battery consumption for untethered gaming devices.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 35
---

# Definition

WPE = WPR \times \sqrt{\frac{BER}{5}} \times \left(1 - \frac{WlLatVar}{3}\right) \times 2

# Columns used

* [deviceidentity](/tables/deviceidentity.md): `wllatvar`

# Depends on

* [Wireless Performance Rating (WPR)](/knowledge/wireless-performance-rating.md)
* [Battery Efficiency Ratio (BER)](/knowledge/battery-efficiency-ratio.md)

# Used by

* [Extended Tournament Ready Wireless](/knowledge/extended-tournament-ready-wireless.md)
