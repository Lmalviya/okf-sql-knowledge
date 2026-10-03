---
type: Calculation
title: Composite System Stability (CSS)
description: Combines system and device performance to yield an overall stability measure.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 38
---

# Definition

CSS = \sqrt{SPI \times DPM}, where SPI is the System Performance Index and DPM is the Device Performance Metric.

# Depends on

* [System Performance Index (SPI)](/knowledge/system-performance-index.md)
* [statusWeight](/knowledge/statusweight.md)

# Used by

* [System Resilience Factor (SRF)](/knowledge/system-resilience-factor.md)
