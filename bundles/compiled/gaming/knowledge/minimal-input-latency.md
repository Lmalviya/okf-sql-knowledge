---
type: Business Rule
title: Minimal Input Latency
description: Identifies devices with exceptionally low input latency suitable for reaction-critical games.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 17
---

# Definition

A device with InpLagMs < 1.0, PollRateHz ≥ 1000, LatMs < 2.0, and ClkLat < 0.8, providing almost instantaneous input recognition critical for competitive FPS and fighting games.

# Columns used

* [testsessions](/tables/testsessions.md): `latms`, `inplagms`, `pollratehz`
* [performance](/tables/performance.md): `clklat`
