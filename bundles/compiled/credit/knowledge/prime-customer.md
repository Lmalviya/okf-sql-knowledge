---
type: Business Rule
title: Prime Customer
description: Identifies customers with excellent creditworthiness and financial stability.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 10
---

# Definition

A customer with credscore > 720, defhist of 'Excellent' or 'Good', and risklev of 'Low'.

# Columns used

* [credit_and_compliance](/tables/credit_and_compliance.md): `credscore`, `risklev`, `defhist`
