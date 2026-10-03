---
type: Calculation
title: Session Bounce Rate Adjustment (SBRA)
description: Adjusts the raw session bounce rate by factoring in the click-through rate to better understand session quality.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 3
---

# Definition

SBRA = bncrate \times \left(1 - \frac{ctrval}{100}\right), \text{ where bncrate is the bounce rate and ctrval is the click-through rate percentage.}

# Columns used

* [sessions](/tables/sessions.md): `bncrate`, `ctrval`

# Used by

* [Short Session Anomaly Detection (SSAD)](/knowledge/short-session-anomaly-detection.md)
* [Real-Time Session Efficiency (RTSE)](/knowledge/real-time-session-efficiency.md)
* [Adjusted Bounce Ratio (ABR)](/knowledge/adjusted-bounce-ratio.md)
* [Bounce Percentile](/knowledge/bounce-percentile.md)
