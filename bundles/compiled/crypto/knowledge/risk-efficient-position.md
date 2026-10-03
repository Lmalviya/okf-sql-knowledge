---
type: Business Rule
title: Risk-Efficient Position
description: Identifies positions with favorable risk-adjusted characteristics.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 45
---

# Definition

A position where the Risk-Adjusted Return exceeds 1.5 and the Risk-to-Reward Ratio is less than 0.5, indicating strong returns relative to risk exposure and favorable potential profit compared to potential loss.

# Depends on

* [Risk-Adjusted Return](/knowledge/risk-adjusted-return.md)
* [Risk-to-Reward Ratio](/knowledge/risk-to-reward-ratio.md)
