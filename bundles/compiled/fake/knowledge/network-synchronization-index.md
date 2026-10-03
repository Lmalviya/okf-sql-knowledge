---
type: Calculation
title: Network Synchronization Index (NSI)
description: Quantifies synchronized activities across account clusters.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 56
---

# Definition

NSI = \frac{\sum_{i=1}^{n} \sum_{j=i+1}^{n} \text{sync}(i,j)}{\text{clustsize}} \times MACI

# Columns used

* [moderationaction](/tables/moderationaction.md): `clustsize`

# Depends on

* [Multi-Account Correlation Index (MACI)](/knowledge/multi-account-correlation-index.md)
* [Network Manipulation Index (NMI)](/knowledge/network-manipulation-index.md)

# Used by

* [Coordinated Influence Operation](/knowledge/coordinated-influence-operation.md)
* [Synchronized Behavior Cluster](/knowledge/synchronized-behavior-cluster.md)
* [Advanced Influence Campaign](/knowledge/advanced-influence-campaign.md)
