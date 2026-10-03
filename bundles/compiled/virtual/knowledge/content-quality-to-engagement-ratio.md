---
type: Calculation
title: Content Quality to Engagement Ratio (CQER)
description: Measures how a fan's content quality relates to their overall engagement
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 31
---

# Definition

CQER = \frac{contqualrate}{engrate \times 10}, \text{ where values above 1.0 indicate fans producing content of quality higher than their general engagement level would predict.}

# Columns used

* [engagement](/tables/engagement.md): `engrate`

# Depends on

* [engagement.engrate](/knowledge/engagement-engrate.md)
* [socialcommunity.community_engagement.content_creation.contqualrate](/knowledge/socialcommunity-community-engagement-content-creation-contqualrate.md)
