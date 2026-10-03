---
type: Calculation
title: Trader Leverage Exposure (TLE)
description: Extracts the leverage ratio from the trader's performance data.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 2
---

# Definition

TLE = \text{trading_performance.risklevel.levratio}

# Columns used

* [trader](/tables/trader.md): `trading_performance`

# Used by

* [High-Risk Trader Profile](/knowledge/high-risk-trader-profile.md)
* [Risk-Adjusted Turnover (RAT)](/knowledge/risk-adjusted-turnover.md)
* [Aggressive Trading Intensity (ATI)](/knowledge/aggressive-trading-intensity.md)
* [Risk-Adjusted Win Rate (RAWR)](/knowledge/risk-adjusted-win-rate.md)
