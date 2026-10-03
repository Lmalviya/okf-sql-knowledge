---
type: Business Rule
title: Readability Weight Mapping
description: Defines difficulty-based weighting for readability calculations.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 56
---

# Definition

Difficulty levels are assigned weights: Basic = 1, Intermediate = 1.5, Advanced = 2, Others = 1.2.
