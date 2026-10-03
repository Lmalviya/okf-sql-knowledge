---
type: Calculation
title: Network Manipulation Index (NMI)
description: Measures the extent of network manipulation considering bot behavior and coordination.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 31
---

# Definition

NMI = 0.6 \times BBI + 0.4 \times CAS

# Depends on

* [Bot Behavior Index (BBI)](/knowledge/bot-behavior-index.md)
* [Coordinated Activity Score (CAS)](/knowledge/coordinated-activity-score.md)

# Used by

* [Advanced Persistent Threat](/knowledge/advanced-persistent-threat.md)
* [Multi-Account Correlation Index (MACI)](/knowledge/multi-account-correlation-index.md)
* [Network Synchronization Index (NSI)](/knowledge/network-synchronization-index.md)
