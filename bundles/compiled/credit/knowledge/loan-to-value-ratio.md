---
type: Calculation
title: Loan-to-Value Ratio (LTV)
description: Calculates the ratio of loan amount to the value of the asset securing the loan.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:54+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 2
---

# Definition

LTV = \frac{\text{Mortgage Balance}}{\text{Property Value}} = \frac{\text{propfinancialdata.mortgagebits.mortbalance}}{\text{propfinancialdata.propvalue}}

# Columns used

* [expenses_and_assets](/tables/expenses_and_assets.md): `propfinancialdata`

# Used by

* [Property Risk Exposure](/knowledge/property-risk-exposure.md)
* [Loan-to-Value Ratio Significance](/knowledge/loan-to-value-ratio-significance.md)
* [Housing Affordability Ratio (HAR)](/knowledge/housing-affordability-ratio.md)
* [Mortgage Risk Profile](/knowledge/mortgage-risk-profile.md)
