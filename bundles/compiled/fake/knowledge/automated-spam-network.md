---
type: Business Rule
title: Automated Spam Network
description: Identifies automated spam distribution networks.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 45
---

# Definition

A Bot Network where average ABS > 0.8 and all accounts are Content Farms

# Depends on

* [Bot Network](/knowledge/bot-network.md)
* [Automated Behavior Score (ABS)](/knowledge/automated-behavior-score.md)
* [Content Farm](/knowledge/content-farm.md)
