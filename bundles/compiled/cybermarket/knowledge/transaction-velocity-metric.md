---
type: Calculation
title: Transaction Velocity Metric (TVM)
description: Measures the rapidity and volume of transactions from a single source
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 34
---

# Definition

TVM = \frac{COUNT(txregistry)}{(MAX(eventstamp) - MIN(eventstamp))} \times \frac{payamtusd}{500} \times (1 + (paymethod\_weight \times 0.1)), \text{where paymethod\_weight assigns Crypto\_A=1, Crypto\_B=3, Crypto\_C=2, Token=2 based on the payment method classifications defined in cybermarket|transactions|paymethod, and higher values indicate potentially suspicious transaction velocity.}

# Columns used

* [transactions](/tables/transactions.md): `txregistry`, `eventstamp`, `paymethod`, `payamtusd`

# Depends on

* [cybermarket|transactions|paymethod](/knowledge/cybermarket-transactions-paymethod.md)

# Used by

* [Flash Transaction Cluster](/knowledge/flash-transaction-cluster.md)
