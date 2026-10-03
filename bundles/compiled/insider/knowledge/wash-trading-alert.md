---
type: Business Rule
title: Wash Trading Alert
description: Flags transactions highly suspicious for wash trading.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 16
---

# Definition

A transaction triggers a Wash Trading Alert if `risk_indicators.washsus` is 'High'.

# Columns used

* [transactionrecord](/tables/transactionrecord.md): `risk_indicators`

# Depends on

* [Risk-Adjusted Turnover (RAT)](/knowledge/risk-adjusted-turnover.md)

# Used by

* [High-Volume Wash Trading Concern](/knowledge/high-volume-wash-trading-concern.md)
