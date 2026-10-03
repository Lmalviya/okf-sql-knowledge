---
type: Business Rule
title: High Lunar Interference Events
description: Observations with significant lunar interference.
tags:
- alien
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:52+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/alien/alien_kb.jsonl
  title: alien business rules (LiveSQLBench), rule 53
---

# Definition

Events where the calculated LIF is greater than 0.5, indicating strong lunar contamination in the data.

# Depends on

* [Lunar Interference Factor (LIF)](/knowledge/lunar-interference-factor.md)
