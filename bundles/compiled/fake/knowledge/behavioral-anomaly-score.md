---
type: Calculation
title: Behavioral Anomaly Score (BAS)
description: Quantifies unusual behavior patterns.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 39
---

# Definition

BAS = 0.4 \times BBI + 0.4 \times AAF + 0.2 \times NGV

# Depends on

* [Bot Behavior Index (BBI)](/knowledge/bot-behavior-index.md)
* [Account Activity Frequency (AAF)](/knowledge/account-activity-frequency.md)
* [Network Growth Velocity (NGV)](/knowledge/network-growth-velocity.md)

# Used by

* [Behavioral Anomaly Cluster](/knowledge/behavioral-anomaly-cluster.md)
* [Temporal Pattern Deviation Score (TPDS)](/knowledge/temporal-pattern-deviation-score.md)
