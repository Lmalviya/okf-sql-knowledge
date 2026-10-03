---
type: Business Rule
title: Multi-Platform Threat Entity
description: Identifies high-risk entities operating across multiple cybermarket platforms
tags:
- cybermarket
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:58+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/cybermarket/cybermarket_kb.jsonl
  title: cybermarket business rules (LiveSQLBench), rule 48
---

# Definition

An entity with CPRA > 80, displaying Cross-Platform Operator characteristics, with high Wallet Risk Index scores (WRI > 70), and consistently employing the same operational security tactics across platforms. These entities represent priority targets for coordinated investigation efforts due to their expanded reach.

# Depends on

* [Wallet Risk Index (WRI)](/knowledge/wallet-risk-index.md)
* [Cross-Platform Operator](/knowledge/cross-platform-operator.md)
* [Cross-Platform Risk Amplification (CPRA)](/knowledge/cross-platform-risk-amplification.md)
