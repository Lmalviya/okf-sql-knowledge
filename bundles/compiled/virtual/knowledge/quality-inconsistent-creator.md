---
type: Business Rule
title: Quality Inconsistent Creator
description: Identifies fans who produce occasional high-quality content but lack consistency
tags:
- virtual
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:13+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/virtual/virtual_kb.jsonl
  title: virtual business rules (LiveSQLBench), rule 43
---

# Definition

A fan who has created at least one content piece with contqualrate > 8.5 but maintains an overall CQC < 5, indicating talent but inconsistent output.

# Depends on

* [socialcommunity.community_engagement.content_creation.contqualrate](/knowledge/socialcommunity-community-engagement-content-creation-contqualrate.md)
* [Content Quality Consistency (CQC)](/knowledge/content-quality-consistency.md)
