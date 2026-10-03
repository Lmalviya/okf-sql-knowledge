---
type: Calculation
title: Wireless Performance Rating (WPR)
description: Rates the quality of wireless connectivity based on range, latency, and interference handling.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 8
---

# Definition

WPR = \frac{WlRangeM}{10} \times \left(1 - \frac{WlLatVar}{5}\right) \times \left(1 + \frac{WlChanHop}{2}\right) \times \frac{WlSignal + 100}{100}, \text{ where higher values indicate more reliable wireless performance with better range and stability.}

# Columns used

* [testsessions](/tables/testsessions.md): `wlsignal`
* [deviceidentity](/tables/deviceidentity.md): `wlrangem`, `wlchanhop`, `wllatvar`

# Used by

* [Premium Wireless Solution](/knowledge/premium-wireless-solution.md)
* [Wireless Performance Efficiency (WPE)](/knowledge/wireless-performance-efficiency.md)
