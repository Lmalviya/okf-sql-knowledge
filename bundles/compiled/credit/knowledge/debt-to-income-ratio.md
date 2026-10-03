---
type: Calculation
title: Debt-to-Income Ratio (DTI)
description: Calculates the proportion of a customer's monthly income that goes toward debt payments.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:54+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 0
---

# Definition

DTI = \frac{\text{Total Monthly Debt Payments}}{\text{Monthly Income}} = debincratio

# Columns used

* [employment_and_income](/tables/employment_and_income.md): `debincratio`

# Used by

* [Financial Stability Index (FSI)](/knowledge/financial-stability-index.md)
* [Financially Vulnerable](/knowledge/financially-vulnerable.md)
* [Over-Extended](/knowledge/over-extended.md)
* [Debt-to-Income Ratio Interpretation](/knowledge/debt-to-income-ratio-interpretation.md)
* [Total Debt Service Ratio (TDSR)](/knowledge/total-debt-service-ratio.md)
* [Financial Vulnerability Score (FVS)](/knowledge/financial-vulnerability-score.md)
* [Declining Credit Health](/knowledge/declining-credit-health.md)
