---
type: Calculation
title: Bot Behavior Index (BBI)
description: Combines multiple bot-detection metrics into a single score.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 3
---

# Definition

BBI = 0.4 \times \text{botlikscore} + 0.3 \times \text{autobehavscore} + 0.3 \times (1 - \text{convnatval})

# Columns used

* [messaginganalysis](/tables/messaginganalysis.md): `convnatval`

# Used by

* [Bot Network](/knowledge/bot-network.md)
* [Dormant Bot](/knowledge/dormant-bot.md)
* [Network Manipulation Index (NMI)](/knowledge/network-manipulation-index.md)
* [Coordinated Bot Risk (CBR)](/knowledge/coordinated-bot-risk.md)
* [Automated Behavior Score (ABS)](/knowledge/automated-behavior-score.md)
* [Behavioral Anomaly Score (BAS)](/knowledge/behavioral-anomaly-score.md)
