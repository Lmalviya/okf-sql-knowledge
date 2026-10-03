---
type: Business Rule
title: Revolving Credit Dependent
description: Identifies customers who heavily rely on revolving credit.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 16
---

# Definition

A customer with credutil > 0.7, cardcount > 2, and cardpayhist of 'Fair' or 'Poor'.

# Columns used

* [credit_accounts_and_history](/tables/credit_accounts_and_history.md): `cardcount`, `credutil`, `cardpayhist`

# Depends on

* [Credit Utilization Ratio (CUR)](/knowledge/credit-utilization-ratio.md)
