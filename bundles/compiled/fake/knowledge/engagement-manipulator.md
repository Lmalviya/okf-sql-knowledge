---
type: Business Rule
title: Engagement Manipulator
description: Identifies artificial engagement patterns.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 17
---

# Definition

An account where engauth < 0.3 and tempinteractpat = 'Automated'
