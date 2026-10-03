---
type: Calculation
title: Risk-Adjusted Win Rate (RAWR)
description: Calculates the trader's historical win percentage adjusted for their leverage exposure.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 59
---

# Definition

RAWR = \frac{\text{trading_performance.winpct}}{\text{Max}(1, \text{TLE})}

# Columns used

* [trader](/tables/trader.md): `trading_performance`

# Depends on

* [Trader Leverage Exposure (TLE)](/knowledge/trader-leverage-exposure.md)
