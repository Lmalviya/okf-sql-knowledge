---
type: Calculation
title: Content Amplification Effect (CAE)
description: Measures the cascade effect of content sharing.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 57
---

# Definition

CAE = \text{CIS} \times NIC \times \log(1 + \text{resharecount})

# Depends on

* [Content Impact Score (CIS)](/knowledge/content-impact-score.md)
* [Network Influence Centrality (NIC)](/knowledge/network-influence-centrality.md)

# Used by

* [Coordinated Influence Operation](/knowledge/coordinated-influence-operation.md)
* [Network Influence Hub](/knowledge/network-influence-hub.md)
