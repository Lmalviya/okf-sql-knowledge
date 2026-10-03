---
type: Calculation
title: Adjusted Bounce Ratio (ABR)
description: Modifies the raw bounce metric by integrating real-time efficiency factors.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 37
---

# Definition

ABR = SBRA \times (RTSE \; factor), with SBRA representing the Session Bounce Rate Adjustment and RTSE signifying Real-Time Session Efficiency.

# Depends on

* [Session Bounce Rate Adjustment (SBRA)](/knowledge/session-bounce-rate-adjustment.md)
* [Real-Time Session Efficiency (RTSE)](/knowledge/real-time-session-efficiency.md)

# Used by

* [Session Drop-off Risk (SDR)](/knowledge/session-drop-off-risk.md)
