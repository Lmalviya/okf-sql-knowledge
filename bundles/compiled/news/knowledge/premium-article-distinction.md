---
type: Business Rule
title: Premium Article Distinction (PAD)
description: Classifies articles as premium based on quality and content policy adherence.
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 41
---

# Definition

An article qualifies as premium when it surpasses the Article Quality Index threshold and complies with the Premium Content Rule.

# Depends on

* [Article Quality Index (AQI)](/knowledge/article-quality-index.md)
* [Premium Content Rule (PCR)](/knowledge/premium-content-rule.md)
