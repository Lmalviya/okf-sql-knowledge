---
type: Business Rule
title: Content Creator
description: Identifies fans who actively produce and share idol-related content
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 21
---

# Definition

A fan with ugcval > 20, contqualrate > 7.0, and at least one of: artsubs > 3, ficsubs > 2, or coverperfcnt > 0. These fans contribute significantly to community content ecosystem.

# Depends on

* [socialcommunity.community_engagement.content_creation.contqualrate](/knowledge/socialcommunity-community-engagement-content-creation-contqualrate.md)

# Used by

* [High-Value Content Creator](/knowledge/high-value-content-creator.md)
* [Content Creator Classification](/knowledge/content-creator-classification.md)
