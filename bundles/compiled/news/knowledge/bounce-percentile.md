---
type: Calculation
title: Bounce Percentile
description: Ranks sessions by their adjusted bounce rate relative to all other sessions.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 52
---

# Definition

A percentile ranking computed using PERCENT_RANK() over all sessions ordered by adjusted_bounce_rate.

# Depends on

* [Session Bounce Rate Adjustment (SBRA)](/knowledge/session-bounce-rate-adjustment.md)

# Used by

* [Performance Segment](/knowledge/performance-segment.md)
