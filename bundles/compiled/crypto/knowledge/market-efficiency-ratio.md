---
type: Calculation
title: Market Efficiency Ratio (MER)
description: Measures how efficiently orders are executed compared to expected slippage.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 9
---

# Definition

MER = \frac{Slippage Impact}{slipratio}, \text{where } Slippage Impact \text{ is the calculated expected slippage and } slipratio \text{ is the average slippage measure.}

# Columns used

* [systemmonitoring](/tables/systemmonitoring.md): `slipratio`

# Depends on

* [Slippage Impact](/knowledge/slippage-impact.md)

# Used by

* [Risk-to-Reward Ratio](/knowledge/risk-to-reward-ratio.md)
* [High-Quality Arbitrage Opportunity](/knowledge/high-quality-arbitrage-opportunity.md)
