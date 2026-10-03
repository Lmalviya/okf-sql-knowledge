---
type: Calculation
title: Account Health Index (AHI)
description: Composite measure of account quality considering age, mix, and payment history.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:54+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 9
---

# Definition

AHI = 0.4 × \frac{avgaccage}{10} + 0.3 × accmixscore + 0.3 × payconsist, \text{where each component is capped at 1.0}

# Columns used

* [credit_accounts_and_history](/tables/credit_accounts_and_history.md): `avgaccage`, `accmixscore`, `payconsist`

# Used by

* [Credit Risk Intensity (CRI)](/knowledge/credit-risk-intensity.md)
