---
type: Business Rule
title: Flash Transaction Cluster
description: Identifies unusually rapid transaction sequences potentially indicating coordinated activity
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 44
---

# Definition

A group of transactions with TVM > 50 from related sources, using privacy-focused cryptocurrencies (paymethod = 'Crypto_B') as defined in the payment method classification, completed within a short timeframe (MAX(eventstamp) - MIN(eventstamp) < 24 hours), and involving minimal escrow time (escrowhrs < 12). Such clusters often indicate coordinated market manipulation or 'smurfing' behavior.

# Columns used

* [transactions](/tables/transactions.md): `eventstamp`, `paymethod`, `escrowhrs`

# Depends on

* [cybermarket|transactions|paymethod](/knowledge/cybermarket-transactions-paymethod.md)
* [Transaction Velocity Metric (TVM)](/knowledge/transaction-velocity-metric.md)
