---
type: Business Rule
title: Credit Builder
description: Identifies customers actively working to establish or improve credit.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 13
---

# Definition

A customer with credageyrs < 3, credinq > 2 in the past year, and recentbeh of 'Improving'.

# Columns used

* [credit_and_compliance](/tables/credit_and_compliance.md): `credinq`, `credageyrs`
* [credit_accounts_and_history](/tables/credit_accounts_and_history.md): `recentbeh`
