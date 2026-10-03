---
type: Business Rule
title: Cross-Platform Bot Network
description: Identifies coordinated bot activity across platforms.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:01+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 62
---

# Definition

A Bot Network where CPCS > 0.8 and all accounts have similar MACI patterns

# Depends on

* [Bot Network](/knowledge/bot-network.md)
* [Cross-Platform Correlation Score (CPCS)](/knowledge/cross-platform-correlation-score.md)
* [Multi-Account Correlation Index (MACI)](/knowledge/multi-account-correlation-index.md)
