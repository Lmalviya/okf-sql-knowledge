---
type: Business Rule
title: Financially Vulnerable
description: Identifies customers who may be financially stressed or at risk.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 11
---

# Definition

A customer with debincratio > 0.5, liqassets < mthincome × 3, and at least one of: delinqcount > 0, latepaycount > 1, or ovrfreq of 'Frequent'.

# Columns used

* [employment_and_income](/tables/employment_and_income.md): `mthincome`, `debincratio`
* [expenses_and_assets](/tables/expenses_and_assets.md): `liqassets`
* [bank_and_transactions](/tables/bank_and_transactions.md): `ovrfreq`
* [credit_and_compliance](/tables/credit_and_compliance.md): `delinqcount`, `latepaycount`

# Depends on

* [Debt-to-Income Ratio (DTI)](/knowledge/debt-to-income-ratio.md)
