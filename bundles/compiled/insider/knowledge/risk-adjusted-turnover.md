---
type: Calculation
title: Risk-Adjusted Turnover (RAT)
description: Calculates trader turnover scaled by their leverage exposure.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 30
---

# Definition

RAT = \text{DTR} \times \text{TLE} \\ \text{where DTR is Daily Turnover Rate  and TLE is Trader Leverage Exposure .}

# Depends on

* [Daily Turnover Rate (DTR)](/knowledge/daily-turnover-rate.md)
* [Trader Leverage Exposure (TLE)](/knowledge/trader-leverage-exposure.md)

# Used by

* [Wash Trading Alert](/knowledge/wash-trading-alert.md)
* [High Velocity Suspicion Trader](/knowledge/high-velocity-suspicion-trader.md)
