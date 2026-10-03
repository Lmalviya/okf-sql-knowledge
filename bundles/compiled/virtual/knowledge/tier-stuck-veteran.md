---
type: Business Rule
title: Tier-Stuck Veteran
description: Identifies long-term fans who have stalled in tier progression
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 48
---

# Definition

A fan with membdays > 365, engrate > 0.4, but TAF < 0.5, representing users who remain engaged but are advancing through tier levels more slowly than expected.

# Columns used

* [membershipandspending](/tables/membershipandspending.md): `membdays`
* [engagement](/tables/engagement.md): `engrate`

# Depends on

* [fans.tierstep](/knowledge/fans-tierstep.md)
* [engagement.engrate](/knowledge/engagement-engrate.md)
* [Tier Acceleration Factor (TAF)](/knowledge/tier-acceleration-factor.md)
