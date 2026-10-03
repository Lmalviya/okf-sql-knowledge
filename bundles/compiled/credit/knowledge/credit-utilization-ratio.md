---
type: Calculation
title: Credit Utilization Ratio (CUR)
description: Measures how much of available credit a customer is currently using.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:54+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 1
---

# Definition

CUR = \frac{\text{Total Credit Used}}{\text{Total Credit Limit}} = credutil

# Columns used

* [credit_accounts_and_history](/tables/credit_accounts_and_history.md): `credutil`

# Used by

* [Revolving Credit Dependent](/knowledge/revolving-credit-dependent.md)
* [Over-Extended](/knowledge/over-extended.md)
* [Credit Utilization Impact](/knowledge/credit-utilization-impact.md)
* [Credit Quality Index (CQI)](/knowledge/credit-quality-index.md)
* [Credit Utilization Alert](/knowledge/credit-utilization-alert.md)
