---
type: Business Rule
title: Suspicious Transaction Pattern
description: Identifies transactions with characteristics suggesting potential illegal activity
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 22
---

# Definition

A transaction with TAS > 75, payment in privacy-focused cryptocurrencies (Crypto_B), escrow disabled or minimized (escrowused = 'No' or escrowhrs < 24), and unusual routing complexity (routecomplexity = 'Complex'). These transactions often represent high-risk activities requiring further investigation.

# Columns used

* [transactions](/tables/transactions.md): `escrowused`, `escrowhrs`, `routecomplexity`

# Depends on

* [cybermarket|transactions|paymethod](/knowledge/cybermarket-transactions-paymethod.md)
* [Transaction Anomaly Score (TAS)](/knowledge/transaction-anomaly-score.md)

# Used by

* [Priority Investigation Target](/knowledge/priority-investigation-target.md)
