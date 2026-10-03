---
type: Business Rule
title: Reputation Manipulation Ring
description: Identifies coordinated reputation manipulation.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:01+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 65
---

# Definition

A Content Manipulation Ring where all accounts have RVI > 0.7 and similar CDPS patterns

# Depends on

* [Content Manipulation Ring](/knowledge/content-manipulation-ring.md)
* [Reputation Volatility Index (RVI)](/knowledge/reputation-volatility-index.md)
* [Content Distribution Pattern Score (CDPS)](/knowledge/content-distribution-pattern-score.md)
