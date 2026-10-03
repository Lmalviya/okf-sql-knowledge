---
type: Value Illustration
title: Income Stability Score
description: Illustrates the meaning of income stability scores.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 21
---

# Definition

Income stability (incstabscore) ranges from 0-10. Scores below 3 indicate highly variable income, 3-6 indicates moderate stability, and above 6 indicates highly stable income sources.

# Columns used

* [employment_and_income](/tables/employment_and_income.md): `incstabscore`
