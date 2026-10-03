---
type: Business Rule
title: Complex Money Laundering Operation
description: Identifies sophisticated financial obfuscation schemes
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 49
---

# Definition

A transaction network with MFC > 90, displaying Money Laundering Indicator characteristics, high TCR scores (TCR > 180), and 'High' money laundering risk classification as defined in the money laundering risk system. These operations represent the most sophisticated financial obfuscation attempts requiring specialized financial investigation approaches.

# Depends on

* [cybermarket|riskanalysis|moneyrisk](/knowledge/cybermarket-riskanalysis-moneyrisk.md)
* [Transaction Chain Risk (TCR)](/knowledge/transaction-chain-risk.md)
* [Money Flow Complexity (MFC)](/knowledge/money-flow-complexity.md)
