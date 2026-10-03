---
type: Calculation
title: Daily Turnover Rate (DTR)
description: Calculates the ratio of a trader's daily trading volume to their account balance, indicating capital velocity.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 0
---

# Definition

DTR = \frac{\text{voldaily}}{\text{acctbal}}

# Columns used

* [trader](/tables/trader.md): `acctbal`, `voldaily`

# Used by

* [High-Risk Trader Profile](/knowledge/high-risk-trader-profile.md)
* [Risk-Adjusted Turnover (RAT)](/knowledge/risk-adjusted-turnover.md)
* [Aggressive Trading Intensity (ATI)](/knowledge/aggressive-trading-intensity.md)
* [Suspicion-Weighted Turnover (SWT)](/knowledge/suspicion-weighted-turnover.md)
