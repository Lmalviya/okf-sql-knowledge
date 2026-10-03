---
type: Calculation
title: Cohort Percentage
description: Calculates the proportional representation of each test group within monthly registration cohorts
tags:
- news
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:27:07+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/news/news_kb.jsonl
  title: news business rules (LiveSQLBench), rule 55
---

# Definition

(Group registrations / Total monthly registrations) * 100

# Depends on

* [AB Testing Cohort Analysis (ABTCA)](/knowledge/ab-testing-cohort-analysis.md)
