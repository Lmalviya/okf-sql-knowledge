---
type: Calculation
title: Risk-Adjusted Return (RAR)
description: Measures the profitability of a customer relationship adjusted for credit risk.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:54+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 8
---

# Definition

RAR = profitscore × (1 - \frac{risklev}{4}), \text{where risklev is converted to a numeric scale: Low=1, Medium=2, High=3, Very High=4}

# Columns used

* [core_record](/tables/core_record.md): `profitscore`
* [credit_and_compliance](/tables/credit_and_compliance.md): `risklev`

# Used by

* [Investment Portfolio Quality (IPQ)](/knowledge/investment-portfolio-quality.md)
