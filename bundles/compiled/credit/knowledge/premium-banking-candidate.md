---
type: Business Rule
title: Premium Banking Candidate
description: Identifies customers who are good candidates for premium banking services.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 43
---

# Definition

A customer with high CQI (Credit Quality Index > 0.8), strong FSI (Financial Stability Index > 0.7), and significant assets (totassets > $250,000).

# Columns used

* [expenses_and_assets](/tables/expenses_and_assets.md): `totassets`

# Depends on

* [Financial Stability Index (FSI)](/knowledge/financial-stability-index.md)
* [Credit Quality Index (CQI)](/knowledge/credit-quality-index.md)
