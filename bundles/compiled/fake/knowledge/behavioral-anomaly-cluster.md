---
type: Business Rule
title: Behavioral Anomaly Cluster
description: Identifies groups showing unusual behavior patterns.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 47
---

# Definition

A cluster where average BAS > 0.8 and contains at least one Bot Network

# Depends on

* [Behavioral Anomaly Score (BAS)](/knowledge/behavioral-anomaly-score.md)
* [Bot Network](/knowledge/bot-network.md)
