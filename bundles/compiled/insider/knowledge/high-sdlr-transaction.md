---
type: Business Rule
title: High SDLR Transaction
description: Identifies transactions deemed high-risk based on their Sentiment-Driven Leakage Risk score exceeding a specific threshold.
tags:
- insider
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:03+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/insider/insider_kb.jsonl
  title: insider business rules (LiveSQLBench), rule 70
---

# Definition

A transaction where the calculated Sentiment-Driven Leakage Risk (SDLR) > 1000.

# Depends on

* [Sentiment-Driven Leakage Risk (SDLR)](/knowledge/sentiment-driven-leakage-risk.md)
