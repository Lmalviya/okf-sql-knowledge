---
type: Calculation
title: Housing Affordability Ratio (HAR)
description: Measures the affordability of housing costs relative to income.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 32
---

# Definition

HAR = \frac{\text{Monthly Housing Payment}}{\text{Monthly Income}} × 100\%, \text{where Monthly Housing Payment is derived from propfinancialdata and LTV calculations}

# Columns used

* [expenses_and_assets](/tables/expenses_and_assets.md): `propfinancialdata`

# Depends on

* [Loan-to-Value Ratio (LTV)](/knowledge/loan-to-value-ratio.md)
