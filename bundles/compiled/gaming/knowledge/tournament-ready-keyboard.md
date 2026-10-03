---
type: Business Rule
title: Tournament-Ready Keyboard
description: Defines what constitutes a keyboard suitable for competitive tournament play based on response time and switch quality.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 11
---

# Definition

A keyboard with IRS > 8.5, ClkLat < 1.0ms, PollRateHz ≥ 1000, and SPR > 8.0, ensuring minimal input latency and consistent actuation during high-pressure competitive scenarios.

# Columns used

* [testsessions](/tables/testsessions.md): `pollratehz`
* [performance](/tables/performance.md): `clklat`

# Depends on

* [Input Responsiveness Score (IRS)](/knowledge/input-responsiveness-score.md)
* [Switch Performance Rating (SPR)](/knowledge/switch-performance-rating.md)
