---
type: Business Rule
title: High Engagement Criteria
description: Defines customers with a high level of engagement with bank products and services.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 50
---

# Definition

A Customer Engagement Score (CES) greater than 0.7.

# Depends on

* [Customer Engagement Score (CES)](/knowledge/customer-engagement-score.md)
