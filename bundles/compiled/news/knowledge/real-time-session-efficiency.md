---
type: Calculation
title: Real-Time Session Efficiency (RTSE)
description: Evaluates session efficiency by balancing interaction outcomes against bounce adjustments.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 31
---

# Definition

RTSE = \frac{CIE}{SBRA}, where CIE denotes the Content Interaction Efficiency and SBRA is the Session Bounce Rate Adjustment.

# Depends on

* [Session Bounce Rate Adjustment (SBRA)](/knowledge/session-bounce-rate-adjustment.md)
* [Content Interaction Efficiency (CIE)](/knowledge/content-interaction-efficiency.md)

# Used by

* [Adjusted Bounce Ratio (ABR)](/knowledge/adjusted-bounce-ratio.md)
* [Session Drop-off Risk (SDR)](/knowledge/session-drop-off-risk.md)
