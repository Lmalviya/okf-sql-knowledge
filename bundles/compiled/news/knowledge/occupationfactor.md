---
type: Value Illustration
title: occupationFactor
description: A multiplier that reflects how user occupation contributes to their demographic value.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 8
---

# Definition

'Professional' = 1.5, 'Retired' = 1.2, 'Student' = 0.7, 'Other' = 1.0. These values are based on segmentation assumptions or business rules.

# Used by

* [User Demographic Score (UDS)](/knowledge/user-demographic-score.md)
