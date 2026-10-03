---
type: Calculation
title: Risk-to-Reward Ratio
description: Calculates the ratio of potential risk to potential reward for a position.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 38
---

# Definition

Risk-to-Reward Ratio = \frac{|entryquote - (posedge == 'Long' ? stopquote : trigquote)|}{|entryquote - (posedge == 'Long' ? trigquote : stopquote)|}, \text{where } entryquote \text{ is the entry price, } stopquote \text{ is the stop price, } trigquote \text{ is the advanced trigger price, and } posedge \text{ determines position direction (Long or Short).}

# Depends on

* [Market Efficiency Ratio (MER)](/knowledge/market-efficiency-ratio.md)
* [posedge](/knowledge/posedge.md)

# Used by

* [Risk-Efficient Position](/knowledge/risk-efficient-position.md)
