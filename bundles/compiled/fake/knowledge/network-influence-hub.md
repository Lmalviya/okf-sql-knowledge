---
type: Business Rule
title: Network Influence Hub
description: Identifies accounts with unusual influence patterns.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:01+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 64
---

# Definition

An account with NIC > 0.8 and CAE > 0.7 that is part of a Coordinated Influence Operation

# Depends on

* [Network Influence Centrality (NIC)](/knowledge/network-influence-centrality.md)
* [Content Amplification Effect (CAE)](/knowledge/content-amplification-effect.md)
* [Coordinated Influence Operation](/knowledge/coordinated-influence-operation.md)

# Used by

* [Advanced Influence Campaign](/knowledge/advanced-influence-campaign.md)
