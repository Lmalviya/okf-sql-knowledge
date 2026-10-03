---
type: Business Rule
title: Coordinated Influence Operation
description: Identifies sophisticated influence campaigns.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:01+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 60
---

# Definition

A network where NSI > 0.8 and CAE > 0.7 and contains at least one Content Manipulation Ring

# Depends on

* [Network Synchronization Index (NSI)](/knowledge/network-synchronization-index.md)
* [Content Amplification Effect (CAE)](/knowledge/content-amplification-effect.md)
* [Content Manipulation Ring](/knowledge/content-manipulation-ring.md)

# Used by

* [Network Influence Hub](/knowledge/network-influence-hub.md)
