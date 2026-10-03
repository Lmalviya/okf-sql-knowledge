---
type: Business Rule
title: Frequent Credit Seeker
description: Identifies customers frequently seeking new credit.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 18
---

# Definition

A customer with hardinq > 3 in the past six months, seekbeh of 'High', and newaccage < 1.

# Columns used

* [credit_and_compliance](/tables/credit_and_compliance.md): `hardinq`
* [credit_accounts_and_history](/tables/credit_accounts_and_history.md): `newaccage`, `seekbeh`
