---
type: Calculation
title: Tier Acceleration Factor (TAF)
description: Measures how quickly a fan is advancing through tier levels relative to platform norms
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 33
---

# Definition

TAF = \frac{tierstep}{\sqrt{membdays}} \times \frac{10}{\sqrt{365}}, \text{ normalized to annual scale for consistent comparison across fans with different membership durations.}

# Columns used

* [fans](/tables/fans.md): `tierstep`
* [membershipandspending](/tables/membershipandspending.md): `membdays`

# Depends on

* [fans.tierstep](/knowledge/fans-tierstep.md)

# Used by

* [Rapidly Ascending Fan](/knowledge/rapidly-ascending-fan.md)
* [Tier-Stuck Veteran](/knowledge/tier-stuck-veteran.md)
