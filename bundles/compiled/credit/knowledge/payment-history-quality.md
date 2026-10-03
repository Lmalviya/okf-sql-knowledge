---
type: Value Illustration
title: Payment History Quality
description: Illustrates what different payment history classifications indicate.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 26
---

# Definition

Payment history (defhist, mortpayhist, rentpayhist, cardpayhist, loanpayhist) classifications indicate reliability. 'Excellent' indicates no late payments, 'Good' indicates minimal late payments, 'Fair' indicates occasional missed payments, 'Poor' indicates regular missed payments, 'Current' indicates being up to date, and 'Past' indicates historical data.

# Columns used

* [credit_and_compliance](/tables/credit_and_compliance.md): `defhist`
* [credit_accounts_and_history](/tables/credit_accounts_and_history.md): `cardpayhist`, `loanpayhist`
