---
type: Business Rule
title: Property Risk Exposure
description: Assesses risk related to a customer's property investment.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 17
---

# Definition

A customer with propfinancialdata.propown of 'Own', LTV > 0.8, and propfinancialdata.mortgagebits.mortpayhist of 'Fair' or 'Poor'.

# Columns used

* [expenses_and_assets](/tables/expenses_and_assets.md): `propfinancialdata`

# Depends on

* [Loan-to-Value Ratio (LTV)](/knowledge/loan-to-value-ratio.md)
