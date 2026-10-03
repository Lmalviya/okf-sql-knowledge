---
type: Business Rule
title: Social Amplifier
description: Identifies fans who significantly extend idol content reach
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 22
---

# Definition

A fan with follcount > 500, SIM > 2.0, and viralcont ≥ 1, representing users who effectively spread idol content through their substantial social networks.

# Columns used

* [retentionandinfluence](/tables/retentionandinfluence.md): `viralcont`

# Depends on

* [Social Influence Multiplier (SIM)](/knowledge/social-influence-multiplier.md)
