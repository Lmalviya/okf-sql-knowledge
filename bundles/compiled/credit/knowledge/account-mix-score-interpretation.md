---
type: Value Illustration
title: Account Mix Score Interpretation
description: Illustrates what different account mix scores represent.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 28
---

# Definition

Account mix score (accmixscore) ranges from 0-1. Higher scores indicate a healthy diversity of account types (revolving, installment, mortgage, etc.), which positively impacts credit scores and indicates financial sophistication.

# Columns used

* [credit_accounts_and_history](/tables/credit_accounts_and_history.md): `accmixscore`
