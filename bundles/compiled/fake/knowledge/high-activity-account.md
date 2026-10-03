---
type: Business Rule
title: High-Activity Account
description: Identifies accounts with elevated engagement levels based on the number of sessions or total posting frequency.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:01+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 74
---

# Definition

An account with session_count > 1000 or total_post_frequency > 50.
