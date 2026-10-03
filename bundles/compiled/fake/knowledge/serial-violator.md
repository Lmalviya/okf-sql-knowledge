---
type: Business Rule
title: Serial Violator
description: Identifies repeat policy violators.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 18
---

# Definition

An account with susphist > 2 and warnnum > 5

# Columns used

* [moderationaction](/tables/moderationaction.md): `susphist`, `warnnum`
