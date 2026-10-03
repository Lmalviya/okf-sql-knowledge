---
type: Business Rule
title: Synchronized Behavior Cluster
description: Identifies groups with highly synchronized activities.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:01+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 66
---

# Definition

A cluster where NSI > 0.9 and all accounts have similar BCS patterns

# Depends on

* [Network Synchronization Index (NSI)](/knowledge/network-synchronization-index.md)
* [Behavioral Consistency Score (BCS)](/knowledge/behavioral-consistency-score.md)

# Used by

* [Multi-Platform Threat Network](/knowledge/multi-platform-threat-network.md)
