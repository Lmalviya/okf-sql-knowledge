---
type: Business Rule
title: Credit Building Opportunity
description: Identifies customers who would benefit from credit-building products.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 45
---

# Definition

A customer with limited credit history (credageyrs < 2), low CQI (Credit Quality Index < 0.6), but positive banking behavior (bouncecount = 0 and bankrelscore > 0.6).

# Columns used

* [bank_and_transactions](/tables/bank_and_transactions.md): `bankrelscore`, `bouncecount`
* [credit_and_compliance](/tables/credit_and_compliance.md): `credageyrs`

# Depends on

* [Credit Quality Index (CQI)](/knowledge/credit-quality-index.md)
