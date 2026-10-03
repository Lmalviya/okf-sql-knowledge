---
type: Calculation
title: Transaction Chain Risk (TCR)
description: Evaluates the risk level of a transaction chain
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 16
---

# Definition

TCR = (txchainlen \times 10) + (linkedtxcount \times 5) + (fraudprob \times 100) - (profilecomplete \times 0.5) - (idverifyscore \times 0.5), \text{where higher scores indicate higher risk transaction chains.}

# Columns used

* [riskanalysis](/tables/riskanalysis.md): `fraudprob`, `linkedtxcount`, `txchainlen`, `profilecomplete`, `idverifyscore`

# Used by

* [Money Laundering Indicator](/knowledge/money-laundering-indicator.md)
* [Money Flow Complexity (MFC)](/knowledge/money-flow-complexity.md)
* [Complex Money Laundering Operation](/knowledge/complex-money-laundering-operation.md)
