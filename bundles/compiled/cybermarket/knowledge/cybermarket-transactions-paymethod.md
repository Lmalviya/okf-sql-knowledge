---
type: Value Illustration
title: cybermarket|transactions|paymethod
description: Explains the significance of different payment methods
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 2
---

# Definition

Payment methods represent varying degrees of anonymity and traceability: 'Crypto_A' typically refers to Bitcoin, offering pseudonymous transactions with public ledgers; 'Crypto_B' often indicates Monero or similar privacy coins with enhanced transaction obfuscation; 'Crypto_C' represents emerging or niche cryptocurrencies; 'Token' indicates platform-specific value exchange systems that operate outside traditional blockchain networks.

# Columns used

* [transactions](/tables/transactions.md): `paymethod`

# Used by

* [Suspicious Transaction Pattern](/knowledge/suspicious-transaction-pattern.md)
* [Transaction Velocity Metric (TVM)](/knowledge/transaction-velocity-metric.md)
* [High-Exposure Product](/knowledge/high-exposure-product.md)
* [Flash Transaction Cluster](/knowledge/flash-transaction-cluster.md)
