---
type: Business Rule
title: High-Quality Arbitrage Opportunity
description: Identifies particularly favorable arbitrage opportunities with minimal execution risk.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 41
---

# Definition

An Arbitrage Window where the Arbitrage ROI exceeds 0.5% and the Market Efficiency Ratio is less than 1.2, indicating high potential return with low execution risk.

# Depends on

* [Arbitrage Window](/knowledge/arbitrage-window.md)
* [Arbitrage ROI](/knowledge/arbitrage-roi.md)
* [Market Efficiency Ratio (MER)](/knowledge/market-efficiency-ratio.md)
