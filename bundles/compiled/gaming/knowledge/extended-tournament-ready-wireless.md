---
type: Business Rule
title: Extended Tournament Ready Wireless
description: Defines wireless devices suitable for full-day tournament use without connectivity or battery concerns.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 45
---

# Definition

A wireless device with WPE > 8.5, BER > 7.0, BattLifeH > 40, and LatMs < 2.5, providing reliable, tournament-grade performance throughout extended competition days without requiring recharging or experiencing degraded responsiveness.

# Columns used

* [testsessions](/tables/testsessions.md): `battlifeh`, `latms`

# Depends on

* [Wireless Performance Efficiency (WPE)](/knowledge/wireless-performance-efficiency.md)
* [Battery Efficiency Ratio (BER)](/knowledge/battery-efficiency-ratio.md)
