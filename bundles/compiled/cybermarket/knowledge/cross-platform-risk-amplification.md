---
type: Calculation
title: Cross-Platform Risk Amplification (CPRA)
description: Measures how risk increases when an entity operates across multiple platforms
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 38
---

# Definition

CPRA = (keymatchcount \times 3) + (COUNT(DISTINCT mktref) \times 10) + (WRI \times 0.2) + (\frac{mktspan}{365} \times 5) - (\frac{compliancescore}{20}), \text{where WRI is defined by the Wallet Risk Index, platformcount is the count of distinct markets an entity operates on, and higher values indicate greater cross-platform risk.}

# Columns used

* [markets](/tables/markets.md): `mktspan`
* [vendors](/tables/vendors.md): `mktref`
* [investigation](/tables/investigation.md): `compliancescore`
* [buyers](/tables/buyers.md): `mktref`
* [transactions](/tables/transactions.md): `mktref`
* [communication](/tables/communication.md): `keymatchcount`

# Depends on

* [Wallet Risk Index (WRI)](/knowledge/wallet-risk-index.md)

# Used by

* [Multi-Platform Threat Entity](/knowledge/multi-platform-threat-entity.md)
