---
type: Business Rule
title: Ultra-Responsive Gaming Device
description: Defines the elite tier of input devices with exceptional response characteristics for reaction-critical competitive games.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 43
---

# Definition

A device with IRS > 9.0, RAI > 8.5, LatMs < 1.0, and ClkLat < 0.5, delivering near-instantaneous input recognition essential for competitive gaming at the highest levels where milliseconds determine outcomes.

# Columns used

* [testsessions](/tables/testsessions.md): `latms`
* [performance](/tables/performance.md): `clklat`

# Depends on

* [Input Responsiveness Score (IRS)](/knowledge/input-responsiveness-score.md)
* [Response Accuracy Index (RAI)](/knowledge/response-accuracy-index.md)
