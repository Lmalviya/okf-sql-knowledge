---
type: Business Rule
title: Bot Network
description: Identifies coordinated bot activity.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 11
---

# Definition

A cluster where clustsize > 10 and average BBI > 0.7 for all accounts in cluster

# Columns used

* [moderationaction](/tables/moderationaction.md): `clustsize`

# Depends on

* [Bot Behavior Index (BBI)](/knowledge/bot-behavior-index.md)

# Used by

* [Network Security Threat](/knowledge/network-security-threat.md)
* [Automated Spam Network](/knowledge/automated-spam-network.md)
* [Behavioral Anomaly Cluster](/knowledge/behavioral-anomaly-cluster.md)
* [Cross-Platform Bot Network](/knowledge/cross-platform-bot-network.md)
