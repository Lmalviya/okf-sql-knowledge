---
type: Value Illustration
title: fans.tierstep
description: Explains the practical significance of fan tier levels
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 1
---

# Definition

Fan tiers (tierstep) start at 1 and increase progressively, representing different loyalty levels and privileges: Tiers 1-3 are 'Entry-level' fans (newly joined), tiers 4-7 represent 'Mid-level' fans (stable supporters), tiers 8-10 are 'High-level fans (long-term loyal followers), and tiers above 10 are 'Core' fans (foundational idol supporters). Any accounts with missing or invalid tier values are classified as 'Undefined' and require administrative review. Each tier level grants new privileges and increases platform visibility.

# Columns used

* [fans](/tables/fans.md): `tierstep`

# Used by

* [Superfan](/knowledge/superfan.md)
* [Tier Acceleration Factor (TAF)](/knowledge/tier-acceleration-factor.md)
* [Rapidly Ascending Fan](/knowledge/rapidly-ascending-fan.md)
* [Tier-Stuck Veteran](/knowledge/tier-stuck-veteran.md)
