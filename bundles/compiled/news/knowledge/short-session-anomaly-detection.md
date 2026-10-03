---
type: Business Rule
title: Short Session Anomaly Detection (SSAD)
description: Identifies sessions with unusually short durations that may signal disengagement or testing anomalies.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 18
---

# Definition

Sessions with a duration significantly below the average, accompanied by low engagement and minimal page views, are flagged as anomalies.

# Depends on

* [Session Bounce Rate Adjustment (SBRA)](/knowledge/session-bounce-rate-adjustment.md)

# Used by

* [User Churn Predictor (UCP)](/knowledge/user-churn-predictor.md)
