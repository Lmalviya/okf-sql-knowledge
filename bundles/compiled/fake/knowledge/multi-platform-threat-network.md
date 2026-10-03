---
type: Business Rule
title: Multi-Platform Threat Network
description: Identifies sophisticated cross-platform threats.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:01+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 67
---

# Definition

A Cross-Platform Threat where CPCS > 0.8 and all accounts are part of a Synchronized Behavior Cluster

# Depends on

* [Cross-Platform Threat](/knowledge/cross-platform-threat.md)
* [Cross-Platform Correlation Score (CPCS)](/knowledge/cross-platform-correlation-score.md)
* [Synchronized Behavior Cluster](/knowledge/synchronized-behavior-cluster.md)
