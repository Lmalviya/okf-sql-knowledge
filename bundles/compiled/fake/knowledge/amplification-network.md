---
type: Business Rule
title: Amplification Network
description: Identifies coordinated content amplification.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 19
---

# Definition

A cluster where clustrole = 'Amplifier' and coordscore > 0.8

# Columns used

* [moderationaction](/tables/moderationaction.md): `clustrole`, `coordscore`

# Used by

* [cluster identifier](/knowledge/cluster-identifier.md)
