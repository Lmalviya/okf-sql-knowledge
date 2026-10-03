---
type: Business Rule
title: Mass Manipulation Campaign
description: Identifies large-scale manipulation efforts.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 48
---

# Definition

A Content Manipulation Ring where CIS > 0.8 for all accounts

# Depends on

* [Content Manipulation Ring](/knowledge/content-manipulation-ring.md)
* [Content Impact Score (CIS)](/knowledge/content-impact-score.md)

# Used by

* [Advanced Influence Campaign](/knowledge/advanced-influence-campaign.md)
