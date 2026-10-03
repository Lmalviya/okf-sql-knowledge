---
type: Value Illustration
title: genderFactor
description: A weighting value used to balance gender representation in demographic scoring.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 7
---

# Definition

Assigned as 1.0 for Male, Female, and 0.8 otherwise. It standardizes the gender effect on demographic impact.

# Used by

* [User Demographic Score (UDS)](/knowledge/user-demographic-score.md)
