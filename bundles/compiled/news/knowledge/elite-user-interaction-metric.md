---
type: Calculation
title: Elite User Interaction Metric (EUIM)
description: A newly defined metric to identify elite user interactions by combining session clicks, views, and engagement score.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 59
---

# Definition

EUIM = (seshclicks + seshviews) * (engscore / 100), where a higher value indicates more elite or intense user interaction.

# Columns used

* [sessions](/tables/sessions.md): `seshviews`, `engscore`, `seshclicks`
