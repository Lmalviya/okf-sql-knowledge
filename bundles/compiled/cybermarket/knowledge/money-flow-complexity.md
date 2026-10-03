---
type: Calculation
title: Money Flow Complexity (MFC)
description: Quantifies the complexity of money flows in transaction chains
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 39
---

# Definition

MFC = (txchainlen \times 5) + (linkedtxcount \times 3) + (moneyrisk_numeric \times 15) + (TCR \times 0.2) - (profilecomplete \times 10), \text{where moneyrisk_numeric maps Low=1, Medium=2, High=3, Unknown=2 according to the money laundering risk classification, and higher scores indicate more complex money flows.}

# Columns used

* [riskanalysis](/tables/riskanalysis.md): `linkedtxcount`, `txchainlen`, `profilecomplete`

# Depends on

* [cybermarket|riskanalysis|moneyrisk](/knowledge/cybermarket-riskanalysis-moneyrisk.md)
* [Transaction Chain Risk (TCR)](/knowledge/transaction-chain-risk.md)

# Used by

* [Complex Money Laundering Operation](/knowledge/complex-money-laundering-operation.md)
