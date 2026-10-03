---
type: Calculation
title: Behavioral Consistency Score (BCS)
description: Measures consistency of account behavior patterns.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 55
---

# Definition

BCS = (1 - TPDS) \times (1 - RVI) \times (1 - \frac{\text{patterndev}}{100})

# Depends on

* [Temporal Pattern Deviation Score (TPDS)](/knowledge/temporal-pattern-deviation-score.md)
* [Reputation Volatility Index (RVI)](/knowledge/reputation-volatility-index.md)

# Used by

* [Authentication Pattern Score (APS)](/knowledge/authentication-pattern-score.md)
* [Behavioral Pattern Anomaly](/knowledge/behavioral-pattern-anomaly.md)
* [Synchronized Behavior Cluster](/knowledge/synchronized-behavior-cluster.md)
