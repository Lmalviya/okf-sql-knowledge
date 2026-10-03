---
type: Calculation
title: Transaction Anomaly Score (TAS)
description: Detects unusual transactions based on multiple variables
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 12
---

# Definition

TAS = \frac{payamtusd}{1000} \times \frac{txfinishhrs}{24} \times \left(1 + \frac{escrowhrs}{100}\right) \times \left(1 - \frac{esccomprate}{100}\right), \text{where esccomprate is from the associated market, and higher scores indicate more suspicious transactions.}

# Columns used

* [markets](/tables/markets.md): `esccomprate`
* [transactions](/tables/transactions.md): `payamtusd`, `escrowhrs`, `txfinishhrs`

# Used by

* [Suspicious Transaction Pattern](/knowledge/suspicious-transaction-pattern.md)
