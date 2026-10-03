---
type: Calculation
title: Customer Lifetime Value (CLV)
description: Measures the total worth of a customer to the financial institution over the entire relationship.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:54+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 3
---

# Definition

CLV = custlifeval, which factors in product usage, tenure, profitability, and expected future transactions.

# Columns used

* [credit_accounts_and_history](/tables/credit_accounts_and_history.md): `custlifeval`
