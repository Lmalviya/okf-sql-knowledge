---
type: Value Illustration
title: Debt-to-Income Ratio Interpretation
description: Illustrates what different debt-to-income ratios mean for lending decisions.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 22
---

# Definition

Debt-to-Income ratio (debincratio) ranges from 0-1 (or above). Below 0.36 is typically considered excellent, 0.36-0.43 is good, 0.43-0.50 is concerning, and above 0.50 is risky for new credit approval.

# Columns used

* [employment_and_income](/tables/employment_and_income.md): `debincratio`

# Depends on

* [Debt-to-Income Ratio (DTI)](/knowledge/debt-to-income-ratio.md)
