---
type: Business Rule
title: Churn Candidate
description: Identifies fans at immediate risk of platform abandonment
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 23
---

# Definition

A fan with RRF > 3.5, lastlogdt more than 20 days in the past, and engrate < 0.2, requiring immediate retention efforts.

# Columns used

* [preferencesandsettings](/tables/preferencesandsettings.md): `lastlogdt`
* [engagement](/tables/engagement.md): `engrate`

# Depends on

* [engagement.engrate](/knowledge/engagement-engrate.md)
* [Retention Risk Factor (RRF)](/knowledge/retention-risk-factor.md)
