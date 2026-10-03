---
type: Business Rule
title: Content Creator Classification
description: Categorizes fans based on their content creation quality, volume, and reach
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 50
---

# Definition

Fans are classified into three categories based on content metrics: 'High-Value Content Creator' identifies fans with exceptional content quality (contqualrate > 8.5), significant reach (follcount > 1000), and substantial content volume (ugcval > 20); 'Content Creator' identifies fans who produce good quality content (contqualrate > 7.0) with substantial volume (ugcval > 20); 'Regular Fan' applies to all others who don't meet content creator thresholds, representing the standard user base who primarily consume rather than create content.

# Depends on

* [socialcommunity.community_engagement.content_creation.contqualrate](/knowledge/socialcommunity-community-engagement-content-creation-contqualrate.md)
* [Content Creator](/knowledge/content-creator.md)
* [High-Value Content Creator](/knowledge/high-value-content-creator.md)
