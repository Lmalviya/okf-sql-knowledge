---
type: Business Rule
title: Session Drop-off Risk (SDR)
description: Determines the likelihood of a session ending abruptly.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 46
---

# Definition

A session is at high drop-off risk when low Real-Time Session Efficiency coincides with an elevated Adjusted Bounce Ratio.

# Depends on

* [Real-Time Session Efficiency (RTSE)](/knowledge/real-time-session-efficiency.md)
* [Adjusted Bounce Ratio (ABR)](/knowledge/adjusted-bounce-ratio.md)
