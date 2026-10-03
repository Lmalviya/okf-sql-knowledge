---
type: Business Rule
title: Readability Segmentation
description: Classifies articles into readability categories based on calculated readability scores.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 57
---

# Definition

Low readability: ARS < 50, Medium readability: 50 ≤ ARS ≤ 100, High readability: ARS > 100.

# Depends on

* [Article Readability Score (ARS)](/knowledge/article-readability-score.md)
