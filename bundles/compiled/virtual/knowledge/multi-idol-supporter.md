---
type: Business Rule
title: Multi-Idol Supporter
description: Identifies fans who support multiple virtual idols on the platform
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 29
---

# Definition

A fan who has interacted (interactfanpivot appears multiple times with different interactidolpivot values) with at least 2 different idols, with engrate > 0.4 for each. These fans spread their support across the platform ecosystem rather than focusing on a single idol.

# Columns used

* [interactions](/tables/interactions.md): `interactfanpivot`, `interactidolpivot`
* [engagement](/tables/engagement.md): `engrate`

# Depends on

* [engagement.engrate](/knowledge/engagement-engrate.md)
