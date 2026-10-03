---
type: Business Rule
title: User Churn Predictor (UCP)
description: Identifies users at risk of churning through behavior pattern analysis.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 43
---

# Definition

Churn risk is flagged when inconsistent engagement per the Engagement Consistency Principle combines with anomalies detected by Short Session Anomaly Detection.

# Depends on

* [Engagement Consistency Principle (ECP)](/knowledge/engagement-consistency-principle.md)
* [Short Session Anomaly Detection (SSAD)](/knowledge/short-session-anomaly-detection.md)
