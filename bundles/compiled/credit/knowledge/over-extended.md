---
type: Business Rule
title: Over-Extended
description: Identifies customers who are financially over-extended.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 19
---

# Definition

A customer with DTI > 0.43, CUR > 0.8, and at least one of: ovrfreq of 'Frequent', bouncecount > 0 in the past three months.

# Columns used

* [bank_and_transactions](/tables/bank_and_transactions.md): `ovrfreq`, `bouncecount`

# Depends on

* [Debt-to-Income Ratio (DTI)](/knowledge/debt-to-income-ratio.md)
* [Credit Utilization Ratio (CUR)](/knowledge/credit-utilization-ratio.md)
