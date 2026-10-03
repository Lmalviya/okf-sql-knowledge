---
type: Calculation
title: Financial Stability Index (FSI)
description: Measures a customer's overall financial stability combining income, savings, and debt factors.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:54+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 6
---

# Definition

FSI = 0.3 × (1 - debincratio) + 0.3 × \frac{liqassets}{mthincome × 6} + 0.2 × \frac{bankaccbal}{mthincome × 3} + 0.2 × \frac{savamount}{mthincome × 12}, \text{where each component is capped at 1.0}

# Columns used

* [employment_and_income](/tables/employment_and_income.md): `mthincome`, `debincratio`
* [expenses_and_assets](/tables/expenses_and_assets.md): `savamount`, `liqassets`, `bankaccbal`

# Depends on

* [Debt-to-Income Ratio (DTI)](/knowledge/debt-to-income-ratio.md)

# Used by

* [Premium Banking Candidate](/knowledge/premium-banking-candidate.md)
