---
type: Business Rule
title: Coolant Critical
description: Identifies critical coolant conditions.
tags:
- vaccine
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:12+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/vaccine/vaccine_kb.jsonl
  title: vaccine business rules (LiveSQLBench), rule 17
---

# Definition

A condition where CDR > 1 and CoolRemainPct < 30

# Columns used

* [container](/tables/container.md): `coolremainpct`

# Depends on

* [Coolant Depletion Rate (CDR)](/knowledge/coolant-depletion-rate.md)
