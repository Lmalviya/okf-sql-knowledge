---
type: Business Rule
title: Cross-Sell Priority
description: Identifies customers who should be prioritized for cross-selling efforts.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 49
---

# Definition

A customer with strong CES (Customer Engagement Score > 0.7), positive CQI (Credit Quality Index > 0.7), and unrealized product potential (crossratio > 0.5 but produsescore < 0.5).

# Columns used

* [core_record](/tables/core_record.md): `crossratio`
* [credit_accounts_and_history](/tables/credit_accounts_and_history.md): `produsescore`

# Depends on

* [Customer Engagement Score (CES)](/knowledge/customer-engagement-score.md)
* [Credit Quality Index (CQI)](/knowledge/credit-quality-index.md)
