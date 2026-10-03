---
type: Calculation
title: Coordinated Bot Risk (CBR)
description: Assesses risk from coordinated bot networks.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 33
---

# Definition

CBR = BBI \times CAS \times \frac{\text{clustsize}}{100}

# Columns used

* [moderationaction](/tables/moderationaction.md): `clustsize`

# Depends on

* [Bot Behavior Index (BBI)](/knowledge/bot-behavior-index.md)
* [Coordinated Activity Score (CAS)](/knowledge/coordinated-activity-score.md)

# Used by

* [Network Trust Score (NTS)](/knowledge/network-trust-score.md)
* [High-Risk Bot Network](/knowledge/high-risk-bot-network.md)
