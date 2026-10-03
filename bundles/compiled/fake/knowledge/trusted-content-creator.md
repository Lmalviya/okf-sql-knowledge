---
type: Business Rule
title: Trusted Content Creator
description: Identifies reliable content creators.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 41
---

# Definition

An account with ETS > 0.8 and CIS < 0.2

# Depends on

* [Enhanced Trust Score (ETS)](/knowledge/enhanced-trust-score.md)
* [Content Impact Score (CIS)](/knowledge/content-impact-score.md)
