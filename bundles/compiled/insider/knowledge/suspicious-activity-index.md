---
type: Calculation
title: Suspicious Activity Index (SAI)
description: A composite index attempting to quantify overall suspicious trading behavior based on risk indicators.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 3
---

# Definition

SAI = (w_1 \times \text{SpoofProbNorm}) + (w_2 \times \text{FrontScoreNorm}) + (w_3 \times \text{QStuffNorm}) + (w_4 \times \text{WashSusNorm}) + (w_5 \times \text{LayerIndNorm}) \\ \text{where } \text{SpoofProbNorm} = \frac{\text{risk_indicators.spoofprob}}{100} \\ \text{FrontScoreNorm} = \frac{\text{risk_indicators.frontscore}}{100} \text{ (assuming max score is 100)} \\ \text{QStuffNorm} = \text{MinMaxScale}(\text{risk_indicators.qstuffindex}) \\ \text{WashSusNorm} = \text{MapToNumeric}(\text{risk_indicators.washsus}, {'Low': 0.1, 'Medium': 0.5, 'High': 1.0}) \\ \text{LayerIndNorm} = \text{MapToNumeric}(\text{risk_indicators.layerind}, {'None': 0.0, 'Suspected': 0.5, 'Confirmed': 1.0}) \\ w_i \text{ are weights assigned based on importance, summing to 1.}

# Columns used

* [transactionrecord](/tables/transactionrecord.md): `risk_indicators`

# Used by

* [Combined Manipulation Indicator (CMI)](/knowledge/combined-manipulation-indicator.md)
* [Suspicion-Weighted Turnover (SWT)](/knowledge/suspicion-weighted-turnover.md)
* [Aggressive Suspicion Score (ASS)](/knowledge/aggressive-suspicion-score.md)
* [Market-Agnostic Suspicion Index (MASI)](/knowledge/market-agnostic-suspicion-index.md)
* [High Velocity Suspicion Trader](/knowledge/high-velocity-suspicion-trader.md)
