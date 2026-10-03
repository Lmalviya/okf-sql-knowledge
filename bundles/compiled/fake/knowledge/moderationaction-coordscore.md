---
type: Value Illustration
title: moderationaction.coordscore
description: Illustrates coordination score meaning.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 21
---

# Definition

Ranges from 0 to 1. Scores above 0.7 strongly indicate coordinated behavior, while scores below 0.2 suggest independent actions.

# Columns used

* [moderationaction](/tables/moderationaction.md): `coordscore`
