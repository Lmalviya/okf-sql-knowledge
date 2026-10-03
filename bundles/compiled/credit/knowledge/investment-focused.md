---
type: Business Rule
title: Investment Focused
description: Identifies customers with significant investment activity and sophistication.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 15
---

# Definition

A customer with chaninvdatablock.invcluster.investport of 'Moderate' or 'Aggressive', chaninvdatablock.invcluster.investexp of 'Extensive', and investamt > 0.3 × totassets.

# Columns used

* [expenses_and_assets](/tables/expenses_and_assets.md): `investamt`, `totassets`
* [bank_and_transactions](/tables/bank_and_transactions.md): `chaninvdatablock`
