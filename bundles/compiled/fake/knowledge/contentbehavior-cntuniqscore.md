---
type: Value Illustration
title: contentbehavior.cntuniqscore
description: Illustrates content uniqueness scoring.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 23
---

# Definition

Ranges from 0 to 1. Scores above 0.8 indicate highly unique content, while scores below 0.3 suggest duplicate or templated content.

# Columns used

* [contentbehavior](/tables/contentbehavior.md): `cntuniqscore`
