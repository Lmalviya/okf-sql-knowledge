---
type: Calculation
title: Margin Utilization
description: Calculates the percentage of margin being utilized.
tags:
- crypto
generated:
  by: okf_compiler/0.1
  at: '2026-10-03T00:26:57+05:30'
sources:
- id: kb
  resource: https://huggingface.co/datasets/birdsql/livesqlbench-base-lite/blob/main/crypto/crypto_kb.jsonl
  title: crypto business rules (LiveSQLBench), rule 7
---

# Definition

Margin Utilization = \frac{inithold}{margsum} \times 100, \text{where } inithold \text{ is the initial margin required and } margsum \text{ is the margin account balance.}

# Columns used

* [accountbalances](/tables/accountbalances.md): `margsum`

# Used by

* [Margin Call Risk](/knowledge/margin-call-risk.md)
