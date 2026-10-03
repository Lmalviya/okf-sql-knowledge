---
type: Business Rule
title: Liquidation Cascade Risk
description: Identifies market conditions prone to cascading liquidations.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 47
---

# Definition

Market conditions where more than 15% of open positions are classified as Liquidation Risk Level 'High Risk' and the Order Book Imbalance Ratio exceeds 0.3 in absolute value, indicating concentrated risk and imbalanced liquidity.

# Depends on

* [Liquidation Risk Level](/knowledge/liquidation-risk-level.md)
* [Order Book Imbalance Ratio](/knowledge/order-book-imbalance-ratio.md)

# Used by

* [Flash Crash Vulnerability](/knowledge/flash-crash-vulnerability.md)
