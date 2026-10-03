---
type: Calculation
title: Network Influence Centrality (NIC)
description: Quantifies account's position and influence in interaction network.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 51
---

# Definition

NIC = 0.4 \times \text{connqualscore} + 0.3 \times \text{netinflscore} + 0.3 \times \text{interactdiv}

# Columns used

* [moderationaction](/tables/moderationaction.md): `netinflscore`

# Used by

* [Content Amplification Effect (CAE)](/knowledge/content-amplification-effect.md)
* [Network Influence Hub](/knowledge/network-influence-hub.md)
* [influence ranking by NIC](/knowledge/influence-ranking-by-nic.md)
