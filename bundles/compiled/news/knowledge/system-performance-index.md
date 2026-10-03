---
type: Calculation
title: System Performance Index (SPI)
description: Measures overall system performance by considering response time, load, and performance scores.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 4
---

# Definition

SPI = \frac{(perfscore - loadscore) \times 100}{resptime}, \text{ where resptime is measured in milliseconds.}

# Columns used

* [systemperformance](/tables/systemperformance.md): `resptime`, `loadscore`, `perfscore`

# Used by

* [Content Recommendation Strategy (CRS)](/knowledge/content-recommendation-strategy.md)
* [Optimized Recommendation Score (ORS)](/knowledge/optimized-recommendation-score.md)
* [Composite System Stability (CSS)](/knowledge/composite-system-stability.md)
* [System Resilience Factor (SRF)](/knowledge/system-resilience-factor.md)
