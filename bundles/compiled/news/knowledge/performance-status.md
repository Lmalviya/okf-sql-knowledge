---
type: Business Rule
title: Performance Status
description: Categorizes system records based on response time into Critical, Warning, or Normal bands.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 51
---

# Definition

A CASE-based classification where resptime > 200 is 'Critical', >150 is 'Warning', and others are 'Normal'.

# Columns used

* [systemperformance](/tables/systemperformance.md): `resptime`
