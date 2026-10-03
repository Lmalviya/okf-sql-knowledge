---
type: Business Rule
title: Digital First Customer
description: Identifies customers who primarily engage through digital channels.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 14
---

# Definition

A customer with chaninvdatablock.onlineuse of 'High' or chaninvdatablock.mobileuse of 'High', and chaninvdatablock.autopay of 'Yes'.

# Columns used

* [bank_and_transactions](/tables/bank_and_transactions.md): `chaninvdatablock`
