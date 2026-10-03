---
type: Business Rule
title: High-Value Content Creator
description: Identifies fans who produce exceptional quality content with significant reach
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 40
---

# Definition

A fan who produces content with contqualrate > 8.5, has follcount > 1000, and maintains ugcval > 20, representing the elite tier of community content producers.

# Depends on

* [socialcommunity.community_engagement.content_creation.contqualrate](/knowledge/socialcommunity-community-engagement-content-creation-contqualrate.md)
* [Content Creator](/knowledge/content-creator.md)

# Used by

* [Content Creator Classification](/knowledge/content-creator-classification.md)
