---
type: Business Rule
title: Potential Ambassador
description: Identifies fans with high potential to represent the idol brand
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 26
---

# Definition

A fan with inflscore > 75, trustval > 8.5, FEI > 0.6, and contqualrate > 8.0, representing candidates for official ambassador programs who can authentically promote the idol.

# Columns used

* [loyaltyandachievements](/tables/loyaltyandachievements.md): `inflscore`, `trustval`

# Depends on

* [socialcommunity.community_engagement.content_creation.contqualrate](/knowledge/socialcommunity-community-engagement-content-creation-contqualrate.md)
* [Fan Engagement Index (FEI)](/knowledge/fan-engagement-index.md)
