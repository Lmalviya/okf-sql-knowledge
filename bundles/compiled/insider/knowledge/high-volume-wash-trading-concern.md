---
type: Business Rule
title: High-Volume Wash Trading Concern
description: Flags traders with wash trading alerts who also trade significant volume.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 45
---

# Definition

A trader triggering a Wash Trading Alert  AND whose voldaily exceeds 1000000.

# Columns used

* [trader](/tables/trader.md): `voldaily`

# Depends on

* [Wash Trading Alert](/knowledge/wash-trading-alert.md)

# Used by

* [High-Scrutiny Wash Trading Case](/knowledge/high-scrutiny-wash-trading-case.md)
