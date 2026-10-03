---
type: Business Rule
title: High-Risk Trader Profile
description: Identifies traders exhibiting characteristics associated with high-risk trading strategies.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 10
---

# Definition

A trader is considered High-Risk if their TLE > 5.0 AND their `trading_performance.risklevel.risklevel` is 'Aggressive' OR their DTR > 0.5.

# Columns used

* [trader](/tables/trader.md): `trading_performance`

# Depends on

* [Daily Turnover Rate (DTR)](/knowledge/daily-turnover-rate.md)
* [Trader Leverage Exposure (TLE)](/knowledge/trader-leverage-exposure.md)

# Used by

* [High-Frequency High-Risk Trader](/knowledge/high-frequency-high-risk-trader.md)
* [High-Risk Collusion Group Member](/knowledge/high-risk-collusion-group-member.md)
* [High-Risk Manipulator Candidate](/knowledge/high-risk-manipulator-candidate.md)
