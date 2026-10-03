---
type: Business Rule
title: Investment Services Target
description: Identifies customers who are good candidates for investment services.
tags:
- credit
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:55+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/credit/credit_kb.jsonl
  title: credit business rules (LiveSQLBench), rule 46
---

# Definition

A customer with high ALR (Asset Liquidity Ratio > 0.3) and strong income (mthincome > $5,000).

# Columns used

* [employment_and_income](/tables/employment_and_income.md): `mthincome`

# Depends on

* [Asset Liquidity Ratio (ALR)](/knowledge/asset-liquidity-ratio.md)
