---
type: Value Illustration
title: cybermarket|riskanalysis|moneyrisk
description: Explains the significance of money laundering risk classification
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 8
---

# Definition

'Low' indicates minimal risk patterns with transparent transaction flows and consistent monetary behavior; 'Medium' suggests some unusual patterns warranting monitoring but insufficient evidence for immediate action; 'High' represents significant red flags such as rapid fund transfers, unusual transaction chains, or known high-risk wallet associations; 'Unknown' indicates insufficient data to properly assess risk, itself often considered a risk indicator due to potential deliberate obfuscation.

# Columns used

* [riskanalysis](/tables/riskanalysis.md): `moneyrisk`

# Used by

* [Money Flow Complexity (MFC)](/knowledge/money-flow-complexity.md)
* [Complex Money Laundering Operation](/knowledge/complex-money-laundering-operation.md)
