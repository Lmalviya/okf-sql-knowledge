---
type: Calculation
title: Authentication Pattern Score (APS)
description: Evaluates consistency of authentication behaviors.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 58
---

# Definition

APS = (1 - TEI) \times BCS \times (1 - \frac{\text{authanom}}{100})

# Depends on

* [Technical Evasion Index (TEI)](/knowledge/technical-evasion-index.md)
* [Behavioral Consistency Score (BCS)](/knowledge/behavioral-consistency-score.md)

# Used by

* [Authentication Anomaly Cluster](/knowledge/authentication-anomaly-cluster.md)
