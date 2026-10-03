---
type: Business Rule
title: Sockpuppet Network
description: Identifies related accounts used for manipulation.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 14
---

# Definition

A group of accounts where linkacctnum > 5 and CAS > 0.8

# Columns used

* [moderationaction](/tables/moderationaction.md): `linkacctnum`

# Depends on

* [Coordinated Activity Score (CAS)](/knowledge/coordinated-activity-score.md)

# Used by

* [Content Manipulation Ring](/knowledge/content-manipulation-ring.md)
* [Cross-Platform Threat](/knowledge/cross-platform-threat.md)
