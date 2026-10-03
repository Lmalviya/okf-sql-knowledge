---
type: Business Rule
title: Premium Gaming Mouse
description: Defines the criteria for a high-end gaming mouse based on sensor performance and ergonomics.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 10
---

# Definition

A mouse with SPI > 7.5, DpiRes ≥ 16000, PollRateHz ≥ 1000, and CI > 8.0, offering exceptional precision and comfort for competitive gaming scenarios.

# Columns used

* [testsessions](/tables/testsessions.md): `pollratehz`
* [deviceidentity](/tables/deviceidentity.md): `dpires`

# Depends on

* [Sensor Performance Index (SPI)](/knowledge/sensor-performance-index.md)
* [Comfort Index (CI)](/knowledge/comfort-index.md)
