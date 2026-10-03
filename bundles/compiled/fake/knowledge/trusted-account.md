---
type: Business Rule
title: Trusted Account
description: Identifies highly trustworthy accounts.
tags:
- fake
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:00+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/fake/fake_kb.jsonl
  title: fake business rules (LiveSQLBench), rule 12
---

# Definition

An account with PCI > 0.8 and no security detections in the past 180 days

# Depends on

* [Profile Credibility Index (PCI)](/knowledge/profile-credibility-index.md)

# Used by

* [Behavioral Pattern Anomaly](/knowledge/behavioral-pattern-anomaly.md)
* [review priority](/knowledge/review-priority.md)
