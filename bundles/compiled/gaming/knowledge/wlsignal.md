---
type: Value Illustration
title: WlSignal (Wireless Signal Strength)
description: Illustrates the importance of wireless signal strength measurements for stable connectivity.
tags:
- gaming
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:02+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/gaming/gaming_kb.jsonl
  title: gaming business rules (LiveSQLBench), rule 25
---

# Definition

Typically measured in dBm, with values ranging from -30 (excellent) to -90 (poor). Signal strength above -50dBm indicates optimal performance with minimal interference, -50 to -70dBm represents good connectivity suitable for most gaming, while below -70dBm may experience occasional disconnections or increased latency in challenging environments.

# Columns used

* [testsessions](/tables/testsessions.md): `wlsignal`
