---
type: Business Rule
title: Tournament Standard Device
description: Defines the minimum requirements for devices used in formal esports tournaments and professional competitions.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 40
---

# Definition

A device that meets the CGPI > 8.0, LatMs < 2.0, PollRateHz ≥ 1000, and WlLatVar < 1.0 if wireless, supporting the precision and reliability demands of tournament play with consistent performance across extended match durations.

# Columns used

* [testsessions](/tables/testsessions.md): `latms`, `pollratehz`
* [deviceidentity](/tables/deviceidentity.md): `wllatvar`

# Depends on

* [Competitive Gaming Performance Index (CGPI)](/knowledge/competitive-gaming-performance-index.md)
