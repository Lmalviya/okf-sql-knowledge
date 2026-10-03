---
type: Calculation
title: Total Debt Service Ratio (TDSR)
description: Extended debt ratio that accounts for all financial obligations including housing costs.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 30
---

# Definition

TDSR = DTI + \frac{\text{Housing Costs}}{\text{Monthly Income}}, \text{where Housing Costs are determined by propfinancialdata and DTI is the Debt-to-Income Ratio}

# Columns used

* [expenses_and_assets](/tables/expenses_and_assets.md): `propfinancialdata`

# Depends on

* [Debt-to-Income Ratio (DTI)](/knowledge/debt-to-income-ratio.md)
