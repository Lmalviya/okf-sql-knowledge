---
type: Business Rule
title: Credit Utilization Alert
description: Identifies customers with problematic credit utilization patterns.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 41
---

# Definition

A customer with CUR (Credit Utilization Ratio) > 0.8, an increasing trend in utilization, and limited available credit (totcredlimit < mthincome × 2).

# Columns used

* [employment_and_income](/tables/employment_and_income.md): `mthincome`
* [credit_accounts_and_history](/tables/credit_accounts_and_history.md): `totcredlimit`

# Depends on

* [Credit Utilization Ratio (CUR)](/knowledge/credit-utilization-ratio.md)
