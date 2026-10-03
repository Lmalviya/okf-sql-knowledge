---
type: Business Rule
title: Silent Supporter
description: Identifies financially supportive fans with low social visibility
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 24
---

# Definition

A fan with MV > 100, engrate < 0.3, and chatmsg/sesscount ratio < 0.5, representing valuable economic contributors who prefer to observe rather than actively participate in community activities.

# Columns used

* [preferencesandsettings](/tables/preferencesandsettings.md): `sesscount`
* [engagement](/tables/engagement.md): `engrate`

# Depends on

* [engagement.engrate](/knowledge/engagement-engrate.md)
* [Monetization Value (MV)](/knowledge/monetization-value.md)
