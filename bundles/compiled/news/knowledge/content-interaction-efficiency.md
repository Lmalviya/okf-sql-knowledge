---
type: Calculation
title: Content Interaction Efficiency (CIE)
description: Measures how efficiently a user interacts with content inside a session by looking at the average relative order in which events occur (their sequence values)
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 9
---

# Definition

CIE = AVG(seqval)

Here `seqval` is the event’s sequence/position within a session (e.g., 1, 2, 3…).  Average it across all interactions in a session.

# Columns used

* [interactions](/tables/interactions.md): `seqval`

# Used by

* [User Behavior Paradigm (UBP)](/knowledge/user-behavior-paradigm.md)
* [Interaction Timeliness Indicator (ITI)](/knowledge/interaction-timeliness-indicator.md)
* [Real-Time Session Efficiency (RTSE)](/knowledge/real-time-session-efficiency.md)
* [Interactive Content Amplifier (ICA)](/knowledge/interactive-content-amplifier.md)
* [High Engagement Indicator (HEI)](/knowledge/high-engagement-indicator.md)
