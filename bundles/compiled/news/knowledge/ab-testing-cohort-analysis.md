---
type: Business Rule
title: AB Testing Cohort Analysis (ABTCA)
description: Defines segmentation criteria for splitting users into cohorts for A/B testing experiments.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 12
---

# Definition

Users are assigned to predetermined groups to facilitate controlled comparisons of experimental feature performance across cohorts.

# Used by

* [Cohort Percentage](/knowledge/cohort-percentage.md)
