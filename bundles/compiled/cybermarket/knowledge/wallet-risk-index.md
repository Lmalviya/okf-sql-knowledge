---
type: Calculation
title: Wallet Risk Index (WRI)
description: Assesses the risk level of cryptocurrency wallets
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 14
---

# Definition

WRI = (fraudprob \times 100) + (wallrisksc \times 0.5) - \frac{wallage}{30} + (wallturnrt \times 10) + \frac{txvel}{10}, \text{where higher scores indicate potentially suspicious wallet activity.}

# Columns used

* [riskanalysis](/tables/riskanalysis.md): `fraudprob`, `wallrisksc`, `wallage`, `wallturnrt`, `txvel`

# Used by

* [Cross-Platform Risk Amplification (CPRA)](/knowledge/cross-platform-risk-amplification.md)
* [Multi-Platform Threat Entity](/knowledge/multi-platform-threat-entity.md)
