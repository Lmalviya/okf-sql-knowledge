---
type: Business Rule
title: Money Laundering Indicator
description: Identifies transaction patterns consistent with money laundering
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 23
---

# Definition

A transaction chain with TCR > 150, involving wallets less than 30 days old (wallage < 30), high turnover rates (wallturnrt > 5), and at least 3 linked transactions (linkedtxcount >= 3). These patterns often indicate attempts to obscure the source or destination of funds.

# Columns used

* [riskanalysis](/tables/riskanalysis.md): `linkedtxcount`, `wallage`, `wallturnrt`

# Depends on

* [Transaction Chain Risk (TCR)](/knowledge/transaction-chain-risk.md)
