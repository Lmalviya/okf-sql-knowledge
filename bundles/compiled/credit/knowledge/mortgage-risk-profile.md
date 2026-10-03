---
type: Business Rule
title: Mortgage Risk Profile
description: Identifies customers with elevated mortgage-related risk factors.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 40
---

# Definition

A customer with high LTV (Loan-to-Value Ratio > 0.9), negative equity risk (LTV > 1.0), or payment stress (propfinancialdata.mortgagebits.mortpayhist of 'Fair' or 'Poor').

# Columns used

* [expenses_and_assets](/tables/expenses_and_assets.md): `propfinancialdata`

# Depends on

* [Loan-to-Value Ratio (LTV)](/knowledge/loan-to-value-ratio.md)
