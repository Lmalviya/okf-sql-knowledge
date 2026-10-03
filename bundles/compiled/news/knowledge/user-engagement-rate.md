---
type: Calculation
title: User Engagement Rate (UER)
description: Calculates the engagement rate of a user during a session by combining engagement score, page views, and session duration.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 0
---

# Definition

UER = \frac{\text{seshviews} \times \text{engscore}}{\text{seshdur}}, \text{ where seshviews is the number of articles viewed and seshdur is the duration in seconds.}

# Columns used

* [sessions](/tables/sessions.md): `seshdur`, `seshviews`, `engscore`

# Used by

* [Engagement Consistency Principle (ECP)](/knowledge/engagement-consistency-principle.md)
* [User Behavior Paradigm (UBP)](/knowledge/user-behavior-paradigm.md)
* [Adjusted Read Time Estimator (ARTE)](/knowledge/adjusted-read-time-estimator.md)
* [Conversion Impact Factor (CIF)](/knowledge/conversion-impact-factor.md)
* [High Engagement Indicator (HEI)](/knowledge/high-engagement-indicator.md)
* [Content Consumption Consistency (CCC)](/knowledge/content-consumption-consistency.md)
* [Composite User Activity Score (CUAS)](/knowledge/composite-user-activity-score.md)
