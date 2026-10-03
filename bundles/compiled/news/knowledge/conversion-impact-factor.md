---
type: Calculation
title: Conversion Impact Factor (CIF)
description: Assesses the potential impact on conversions by linking engagement with prompt interaction.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 36
---

# Definition

CIF = \frac{UER}{ITI}, where UER indicates user engagement and ITI measures the Interaction Timeliness Indicator.

# Depends on

* [User Engagement Rate (UER)](/knowledge/user-engagement-rate.md)
* [Interaction Timeliness Indicator (ITI)](/knowledge/interaction-timeliness-indicator.md)

# Used by

* [Conversion Potential Indicator (CPI)](/knowledge/conversion-potential-indicator.md)
