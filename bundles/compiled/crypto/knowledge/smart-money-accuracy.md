---
type: Calculation
title: Smart Money Accuracy
description: Measures the success rate of smart money flow in predicting the 4-hour price movement direction.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 51
---

# Definition

The proportion of times the Smart Money Flow direction matches the 4-hour price movement direction, calculated as: $$ \frac{\text{COUNT(CASE WHEN (smartforce > retailflow AND smartforce > instflow AND next\_price\_4h > mid\_price) OR (smartforce < retailflow AND smartforce < instflow AND next\_price\_4h < mid\_price) THEN 1 ELSE 0 END)}}{\text{COUNT(*)}} $$

# Depends on

* [Smart Money Flow](/knowledge/smart-money-flow.md)
