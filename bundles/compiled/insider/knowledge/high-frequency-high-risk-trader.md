---
type: Business Rule
title: High-Frequency High-Risk Trader
description: Identifies traders classified as High-Risk who also operate at high frequency.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 40
---

# Definition

A trader matching the High-Risk Trader Profile  AND whose freqscope is 'High'.

# Columns used

* [trader](/tables/trader.md): `freqscope`

# Depends on

* [High-Risk Trader Profile](/knowledge/high-risk-trader-profile.md)

# Used by

* [Costly High-Frequency Risk Enforcement](/knowledge/costly-high-frequency-risk-enforcement.md)
