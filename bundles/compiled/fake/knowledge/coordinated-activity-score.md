---
type: Calculation
title: Coordinated Activity Score (CAS)
description: Measures likelihood of coordinated behavior across accounts.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 6
---

# Definition

CAS = 0.5 \times \text{coordscore} + 0.3 \times \text{netinflscore} + 0.2 \times \frac{\text{clustsize}}{100}

# Columns used

* [moderationaction](/tables/moderationaction.md): `clustsize`, `netinflscore`, `coordscore`

# Used by

* [Sockpuppet Network](/knowledge/sockpuppet-network.md)
* [Network Manipulation Index (NMI)](/knowledge/network-manipulation-index.md)
* [Coordinated Bot Risk (CBR)](/knowledge/coordinated-bot-risk.md)
