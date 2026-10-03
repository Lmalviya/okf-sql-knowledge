---
type: Calculation
title: Aggressive Trading Intensity (ATI)
description: Measures intensity by combining high turnover, leverage, and order modification frequency.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 36
---

# Definition

ATI = \text{DTR} \times \text{TLE} \times \text{OMI}.

# Depends on

* [Daily Turnover Rate (DTR)](/knowledge/daily-turnover-rate.md)
* [Order Modification Intensity (OMI)](/knowledge/order-modification-intensity.md)
* [Trader Leverage Exposure (TLE)](/knowledge/trader-leverage-exposure.md)

# Used by

* [Problematic Compliance History](/knowledge/problematic-compliance-history.md)
* [Aggressive Suspicion Score (ASS)](/knowledge/aggressive-suspicion-score.md)
