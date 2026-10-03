---
type: Business Rule
title: High-Value Customer
description: Identifies customers with significant value to the institution.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 12
---

# Definition

A customer with custlifeval in the top quartile, tenureyrs > 5, and crossratio > 0.5.

# Columns used

* [core_record](/tables/core_record.md): `tenureyrs`, `crossratio`
* [credit_accounts_and_history](/tables/credit_accounts_and_history.md): `custlifeval`
